# WEEK 7 MOBILE ROBOTICS LAB
This lab session builds upon Lab Manual 5 by enabling students to perform autonomous navigation using a pre-built map, the Nav2 navigation stack, and the TurtleBot3 platform in a Gazebo simulation. It will load a previously saved map, localize the robot using AMCL, and plan multi-waypoint missions using both the Nav2 command-line interface and a custom
Python node.

# Prerequisites
* Basic knowledge of Linux commands
* Familiarity with ROS 2 concepts (nodes, topics, services)
* ROS 2 Humble installed on the system
* TurtleBot3 packages installed
* Gazebo Simulation and Rviz Nav2
* Rqt graphical representation

# Procedures
* First, install the Turtlebot3 and Gazebo packages via command "sudo apt install ros-humble-turtlebot3* ros-humble-gazebo-ros-pkgs".
* Open terminal and set the Turtlebot3 model by exporting waffle or burger.
* Then, source ROS2 workspace and launch the Gazebo simulator using the command "ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py".
* Again open new terminal and generate the RViz software using the following command:
  "ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=true \ map:=$HOME/maps/my_map.yaml".
* Now initialize the pose of the robot using the 2D estimate pose and then provided a navigation point via nav2 goal.
* Manually built a python node having the provided waypoints in order to move accordingly.
* Open a new terminal and source the rqt graph to show the its velocities.
* During the navigation behavior, the robot moved backup when the obstacle is inserted within the environment.
* By comparing between SLAM and Navigation, SLAM is good for creating an accurate map of an unknown environment while Navigation proceeds to move the robot from Point A to Point B safely using the provided built-in map.
