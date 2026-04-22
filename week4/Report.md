# Mobile Robotics LAB - WEEK 4
The lab session was conducted about the basic commands to gain knowledge of ROS2 operations and learn to create packages as well as the nodes to deploy on workspace.

# Approach
* A Python-based launch file was created within "my_launch_pkg" to simultaneously initialize the turtlesim_node and turtle_teleop_key.
* The setup.py file was configured with data_files to ensure the launch system could locate the .py configurations.
* Ros2 bag was utilized to record the turtle1 cmd_vel topics. This allowed for the persistent storage of trajectory and command data for offline playback.
* The rqt_plot plugin was used to monitor real-time velocity changes on the /turtle1/cmd_vel topic, providing a graphical representation of the teleoperation inputs.
* Follow-the-Leader Logic: To implement the task of a second turtle following the first, a subscriber node was developed to interpret the pose of turtle1 and calculate the necessary twist commands for turtle2.

# Findings
* The launch system significantly reduced manual terminal entry by starting multiple nodes—such as the simulator and the teleop controller—using a single command: ros2 launch my_launch_pkg turtlesim_launch.py.
* Replaying the recorded Rosbag demonstrated that captured pose data accurately reflected the turtle's original movements, proving the tool's effectiveness for debugging and analyzing robot trajectories.
* Through rqt_plot, it was observed that linear and angular velocities fluctuated sharply during keyboard teleoperation, showing the discrete nature of manual input versus the smooth trajectory expected in automated control.

# Observations
* System integration is successfully executed required consistent sourcing of both the global ROS 2 environment and the local workspace (source install/setup.bash) to prevent package-not-found errors.
* There were small errors in setup.py, specifically regarding the path joining for share directories, can prevent colcon build from properly installing launch files.
