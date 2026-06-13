import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class VelocityPublisher(Node):
    def __init__(self):
        super().__init__('velocity_publisher')
        # Create publisher for /cmd_vel topic using Twist message type
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Timer triggers every 2.0 seconds
        self.timer = self.create_timer(2.0, self.timer_callback)
        
        # State variable to alternate behavior
        self.move = True

    def timer_callback(self):
        msg = Twist()
        
        if self.move:
            msg.linear.x = 0.2  # Move forward
            self.get_logger().info('Publishing: Moving Forward')
        else:
            msg.linear.x = 0.0  # Stop
            self.get_logger().info('Publishing: Stopping')
            
        self.publisher_.publish(msg)
        self.move = not self.move  # Toggle state for next callback

def main(args=None):
    rclpy.init(args=args)
    node = VelocityPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()