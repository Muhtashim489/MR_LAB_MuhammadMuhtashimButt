1- * Node is a singular module to communicate or transimit and receive the data with other nodes.
   * Topic acts as a bus to exchange the messages between nodes.
   * Package is acted like a container to organize the data decently.
   * Workspace is a directory containing the packages of ROS2.

2- Sourcing help out to able the access of ROS2 commands and also the packages. Without a source, you would not use ROS2.

3- Colcon build command improves the workflow of software packages inside ROS2. And it builds log, install and build folder.

4- It transmits the data from one type to other variable that runs directly from the console.

5- -----------------------              --------------------
   |                     |    Topic     |                  |
   |   Publisher Node A  |+------------>|  Publisher Node B|
   |                     |              |                  |
   -----------------------              --------------------
