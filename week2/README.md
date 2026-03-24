# Mobile Robotics LAB - WEEK 2
The lab session was conducted to familarize with ROS2 command line tools (CLI), understand the baiscs of simulated tool of turtle (turtlesim) and using different ROS2 topics and services.

# Overview
The purpose of this lab is to install turtlesim, simulate its position and orientation using different commands in terminal and via rqt command, assign topics, services and control to assign differnet linear and angular velocity also.

# Procedure
* Open the terminal and install turtlesim by writing "sudo apt install ros-humble-turtlesim".
* Next phase is to launch turtlesim node via "ros2 run turtlesim turtlesim_node".
* To control the orientation of turtlle in turtlesim, simply write the command "ros2 run turtlesim turtle_teleop_key".
* To sending the velocity either linear or angular, just operate it through function "ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"".
* Another way to assign position and velocities is calling a tab where all services, topics and controlling would be done using the command "rqt".
* For service tab:
  * Navigate to the Services tab in rqt.
  * Select the /reset service and call it to reset the simulation.
  * Select the /spawn service to create a new turtle in the simulation:
    * Set the x, y, and theta values for the turtle's position and orientation.
    * Specify the name for the new turtle.
    * Call the service and observe the new turtle appearing in the simulation.
* For controlling the turtle in rqt tab:
  * Identify the topic for controlling the second turtle (e.g., /turtle2/cmd_vel).
  * Use ros2 topic pub or rqt to send velocity commands to the second turtle.
  * Observe how the second turtle behaves independently of the first.
