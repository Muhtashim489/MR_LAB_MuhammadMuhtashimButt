# Mobile Robotics LAB - WEEK 5
The lab session was conducted about the usage of Gazebo and how to instegrate it with RViz using the TurtleBot3 platform to simulate the robot in simulated environment.

# Prerequisites
* Basic knowledge of Linux commands
• Familiarity with ROS 2 concepts (nodes, topics, services)
• ROS 2 Humble installed on the system
• TurtleBot3 packages installed

# Procedures
* First, install the Turtlebot3 and Gazebo packages via command "sudo apt install ros-humble-turtlebot3* ros-humble-gazebo-ros-pkgs".
* Open terminal and set the Turtlebot3 model by exporting waffle or burger.
* Then, source ROS2 workspace and launch the Gazebo simulator using the command "ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py".
* Again open new terminal and generate the RViz software using the following command:
  "ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=true".
* Now exploring some features of RViz such as Add button to select plugins i.e, LaserScan, Path, Map, TF, Odemetry etc.
* Adjust the frame settings under "Global Options" to odom or map and set the Fixed Frame to map to align all data with the world frame.
* Open a new terminal and source the ROS 2 workspace if needed.
  1. Run the keyboard teleoperation node: ros2 run turtlebot3_teleop teleop_keyboard
  2. Use the following keys to control the robot:
     o w: Forward      o d: Turn right
     o s: Backward     o q: Increase speed
     o a: Turn left    o z: Decrease speed
     o s: Stop Forcefully
* Use the following command to record all topics: ros2 bag record -a
* When the robot cover the all whole bounded area and localize it in map, then save the map via:
  "cd
   mkdir maps
   ros2 run nav2_map_server map_saver_cli -f maps/my_map"
