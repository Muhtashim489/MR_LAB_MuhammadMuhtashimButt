# Mobile Robotics LAB - WEEK 2
The lab session was conducted to familarize with ROS2 command line tools (CLI), understand the baiscs of simulated tool of turtle (turtlesim) and using different ROS2 topics and services.

# Overview
The purpose of this lab is to install turtlesim, simulate its position and orientation using different commands in terminal and via rqt command, assign topics, services and control to assign differnet linear and angular velocity also.

# Procedure
* Create a package inside the subfolder "my_first_pkg" which is also inside of ros2_ws named as "my_turtle_package".
* Inside it, create or edit a node "simple_node.py" using nano command
* Then go back to its orignal folder and run the "colcon build" command to improve the flow of system.
* Then open the publisher node "setup.py" and give a path file of subscriber node.
* Run the file using command "source install/setup.bash".
* Then run using command "ros2 run my_first_pkg simple_node".
