import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class OdomSubscriber(Node):
    def __init__(self):
        super().__init__('odom_subscriber')
        # Subscribe to /odom using the identified nav_msgs/Odometry type
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

    def odom_callback(self, msg):
        # Extract position and orientation data from the incoming message
        position = msg.pose.pose.position
        orientation = msg.pose.pose.orientation
        
        self.get_logger().info(
            f"Position -> X: {position.x:.2f}, Y: {position.y:.2f} | "
            f"Orientation -> Z-Quat: {orientation.z:.2f}"
        )

def main(args=None):
    rclpy.init(args=args)
    node = OdomSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()