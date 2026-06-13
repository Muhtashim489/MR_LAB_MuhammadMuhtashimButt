import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # 1. Define the package name (must match your package.xml exactly)
    package_name = 'my_robot_description'
    
    # 2. Locate the installed URDF file path
    pkg_share = get_package_share_directory(package_name)
    urdf_file = os.path.join(pkg_share, 'urdf', 'my_robot.urdf')

    # 3. Read the URDF file contents into memory
    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()
        
    # 4. Node: Robot State Publisher (Publishes your robot geometry to /robot_description)
    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc, 'use_sim_time': True}]
    )

    # 5. Include: The main Gazebo simulator launch file from gazebo_ros package
    gazebo_share = get_package_share_directory('gazebo_ros')
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_share, 'launch', 'gazebo.launch.py')
        )
    )

    # 6. Node: Spawn Entity (Takes the /robot_description topic and spawns it in Gazebo)
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'my_custom_robot'],
        output='screen'
    )

    # 7. Return the LaunchDescription object containing all actions/nodes to execute
    return LaunchDescription([
        rsp_node,
        gazebo,
        spawn_entity
    ])
