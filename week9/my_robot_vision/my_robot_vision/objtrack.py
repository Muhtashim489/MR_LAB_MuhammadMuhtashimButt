import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

class CameraFollower(Node):
    def __init__(self):
        super().__init__('camera_follower')
        
        # Topic Configurations
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10
        )
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.bridge = CvBridge()
        
        # --- COLOR SEGMENTATION THRESHOLDS ---
        self.lower_hsv = np.array([130, 30, 30])
        self.upper_hsv = np.array([175, 255, 255])
        
        # --- TUNED STABILIZATION PARAMETERS ---
        self.kp_angular = 0.045        # Proportional tracking gain
        self.min_angular_speed = 0.05   # Bypasses simulation wheel friction
        self.max_angular_speed = 0.3    # Caps aggressive rotational jerk
        self.center_threshold = 3       # Sane alignment threshold in pixels
        
        # --- LINEAR PROGRESSION TUNING ---
        self.kp_linear = 0.0000035      
        self.max_linear_speed = 0.12    
        self.target_stop_area = 425000  # FIXED: Lowered from 425000 to represent a real physical stopping threshold
        
        self.search_spin_speed = 0.20  
        
        self.get_logger().info("Target Approach Controller Fixed Node Online.")

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv_image, self.lower_hsv, self.upper_hsv)
            
            kernel = np.ones((5, 5), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            
            segmented_output = cv2.bitwise_and(cv_image, cv_image, mask=mask)
            
            height, width, _ = cv_image.shape
            frame_center_x = width // 2
            
            twist = Twist()
            
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            if contours:
                largest_contour = max(contours, key=cv2.contourArea)
                current_area = cv2.contourArea(largest_contour)
                
                if current_area > 700:
                    M = cv2.moments(largest_contour)
                    if M["m00"] != 0:
                        cx = int(M["m10"] / M["m00"])
                        cy = int(M["m01"] / M["m00"])
                        
                        error_x = cx - frame_center_x
                        
                        # --- 1. ANGULAR SYSTEM (Track and Align Heading) ---
                        if abs(error_x) > self.center_threshold:
                            raw_speed = -float(self.kp_angular * error_x)
                            
                            if abs(raw_speed) > self.max_angular_speed:
                                twist.angular.z = self.max_angular_speed if raw_speed > 0 else -self.max_angular_speed
                            elif abs(raw_speed) < self.min_angular_speed:
                                twist.angular.z = self.min_angular_speed if raw_speed > 0 else -self.min_angular_speed
                            else:
                                twist.angular.z = raw_speed
                        else:
                            twist.angular.z = 0.0  # Center locked
                        
                        # --- 2. LINEAR SYSTEM (Advance Toward Centroid) ---
                        if current_area < self.target_stop_area:
                            area_error = self.target_stop_area - current_area
                            base_linear_speed = float(self.kp_linear * area_error)
                            
                            # Alignment factor interlock to prevent swinging outward
                            alignment_factor = max(0.1, 1.0 - (abs(error_x) / 80.0))
                            twist.linear.x = min(base_linear_speed, self.max_linear_speed) * alignment_factor
                        else:
                            twist.linear.x = 0.0  # Goal range satisfied
                            twist.angular.z = 0.0 # Absolute pose kill
                        
                        self.get_logger().info(f"Tracking: Err={error_x}px | Area={current_area:.0f}/{self.target_stop_area} | Lin={twist.linear.x:.3f}")
                        
                        if twist.linear.x == 0.0 and twist.angular.z == 0.0:
                            self.get_logger().info("SUCCESS: Robot reached destination close-range centroid.")
                        
                        # UI Annotations
                        cv2.circle(cv_image, (cx, cy), 8, (0, 0, 255), -1)
                        cv2.line(cv_image, (frame_center_x, 0), (frame_center_x, height), (255, 0, 0), 2)
                        cv2.putText(cv_image, f"Error: {error_x}px", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                        x, y, w, h = cv2.boundingRect(largest_contour)
                        cv2.rectangle(cv_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                else:
                    self.execute_initial_search(twist)
            else:
                self.execute_initial_search(twist)

            # Ship to execution hardware
            self.publisher.publish(twist)

            cv2.imshow("1. Original Camera Feed", cv_image)
            cv2.imshow("2. Segmented Binary Mask", mask)
            cv2.imshow("3. Segmented Color Output", segmented_output)
            cv2.waitKey(1)
            
        except CvBridgeError as e:
            self.get_logger().error(f"CvBridge Error: {str(e)}")

    def execute_initial_search(self, twist_msg):
        twist_msg.linear.x = 0.0
        twist_msg.angular.z = self.search_spin_speed
        self.get_logger().warn("Scanning environment for target...")

def main(args=None):
    if not rclpy.ok():
        rclpy.init(args=args)
    node = CameraFollower()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        stop_twist = Twist()
        node.publisher.publish(stop_twist)
        cv2.destroyAllWindows()
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()