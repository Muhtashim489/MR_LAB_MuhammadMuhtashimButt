import rclpy
from rclpy.node import Node
import os


class SimpleNode(Node):

    def __init__(self):
        super().__init__('simple_node')

        self.get_logger().info("Welcome to Mobile Robotics")

        # Run counter file
        file_path = "run_counter.txt"

        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                count = int(f.read().strip())
        else:
            count = 0

        count += 1

        with open(file_path, "w") as f:
            f.write(str(count))

        self.get_logger().info(f"Run count: {count}")

        # Parameter
        self.declare_parameter("student_name", "")

        student_name = self.get_parameter("student_name").value

        if student_name:
            self.get_logger().info(f"Student name: {student_name}")
        else:
            self.get_logger().info("student_name not set")


def main(args=None):
    rclpy.init(args=args)

    node = SimpleNode()

    rclpy.spin_once(node, timeout_sec=0.1)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
