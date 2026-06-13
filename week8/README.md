# Procedure to create urdf model robtot
• Replaced the default rounded, tiered TurtleBot3 layout with a distinct blue rectangular box-shaped chassis.
• Positioned the two active traction wheels further outward to widen the wheel track separation, and shifted them backward.
• Inserted a spherical caster wheel at the front to act as the third contact point for stability.
• enter-aligned the cylindrical LiDAR sensor directly on the longitudinal centerline to ensure an unobstructed, symmetrical field of view for clean mapping.
• Configured physical properties by dropping the caster wheel's friction coefficients down to eliminate skidding, while keeping active tires at high friction for optimal traction.
• Customized a python launch file that reads the URDF directly into memory to feed the robot_state_publisher, while simultaneously running an automated node to inject your custom robot into a fresh Gazebo environment on startup.
