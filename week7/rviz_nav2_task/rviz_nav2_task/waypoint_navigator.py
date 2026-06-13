import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import FollowWaypoints
from geometry_msgs.msg import PoseStamped
import math                                         

class WaypointNavigator(Node):
    def __init__(self):                             
        super().__init__('waypoint_navigator')
        self._client = ActionClient(self, FollowWaypoints, 'follow_waypoints')

    def send_waypoints(self, waypoints):            
        self.get_logger().info('Waiting for FollowWaypoints action server...')  
        self._client.wait_for_server()

        goal_msg = FollowWaypoints.Goal()
        goal_msg.poses = waypoints

        self.get_logger().info(f'Sending {len(waypoints)} waypoints...')  
        send_goal_future = self._client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, send_goal_future)

        goal_handle = send_goal_future.result()
        if not goal_handle.accepted:
            self.get_logger().error('Goal rejected by server!')
            return

        self.get_logger().info('Goal accepted. Navigating...')
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        self.get_logger().info('All waypoints reached!')

    def make_pose(self, x, y, yaw):              
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.get_clock().now().to_msg()  
        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = 0.0
        pose.pose.orientation.z = math.sin(yaw / 2.0)  
        pose.pose.orientation.w = math.cos(yaw / 2.0)  
        return pose


def main(args=None):
    rclpy.init(args=args)
    navigator = WaypointNavigator()

    waypoints = [
        navigator.make_pose(2.2783, -1.2187, 0.3071),  # Waypoint 1
        navigator.make_pose(0.3280, -0.6765, 0.5187),  # Waypoint 2
        navigator.make_pose(0.3098,  0.9125, 0.9810),  # Waypoint 3
        navigator.make_pose(1.5161,  0.7361, 0.6903),  # Waypoint 4
        navigator.make_pose(1.5444, -0.4722, 0.9589),  # Waypoint 5
    ]

    navigator.send_waypoints(waypoints)
    navigator.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()