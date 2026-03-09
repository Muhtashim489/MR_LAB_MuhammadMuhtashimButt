# Mobile Robotics LAB - WEEK 1
The lab session was conducted about the basic commands to gain knowledge of ROS2 operations and learn to create packages as well as the nodes to deploy on workspace.

# Overview
The summary of this lab session is to create a package where it would display to print the welcome gesture of the lab printed as "Welcome to Mobile Robotics" and also show its number of count every time the code was running and also detected the name of the student.

# Procedure
* Create a package inside the subfolder "my_first_pkg" which is also inside of ros2_ws named as "my_first_pkg".
* Inside it, create or edit a node "simple_node.py" using nano command
* Then go back to its orignal folder and run the "colcon build" command to improve the flow of system.
* Then open the publisher node "setup.py" and give a path file of subscriber node.
* Run the file using command "source install/setup.bash".
* Then run using command "ros2 run my_first_pkg simple_node".
