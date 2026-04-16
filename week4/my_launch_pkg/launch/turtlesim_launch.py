from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
def generate_launch_description():
    return LaunchDescription([
      Node(
          package='turtlesim',
          executable='turtlesim_node',
          name='sim'
      ),
      ExecuteProcess(
            cmd=['ros2', 'service', 'call', '/spawn', 'turtlesim/srv/Spawn', 
                 '{x: 2.0, y: 2.0, theta: 0.0, name: "turtle2"}'],
            output='screen'
      ),
      Node(
            package='my_launch_pkg', # Ensure this matches your package
            executable='follower_node',  # Ensure this matches your setup.py entry point
            name='follower'
      ),
      Node(
         package='turtlesim',
         executable='turtle_teleop_key',
         name='teleop'
         #prefix='xterm -e'
      ),
      Node(
            package='turtlesim',
            executable='mimic',
            name='follower',
            remappings=[
                ('/input/pose', '/turtle1/pose'),
                ('/output/cmd_vel', '/turtle2/cmd_vel'),
            ]
      )
   ])
