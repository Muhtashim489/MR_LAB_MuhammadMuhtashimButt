# WEEK 9 Mobile Robotics Lab
This lab introduces	image-based	perception and control using the onboard camera. In this session, simulation would be done by vision and detect the object.

# Techniques
* use Waffle to see the object in Gazebo
* Insert objects to segment the colors and masking their images
* Maintain the distance with obstacle and reduce the error of centroid

# Procedures
* Mastered the integration of real-time computer vision with ROS 2 by utilizing the CvBridge library to seamlessly convert incoming simulated camera images into NumPy arrays compatible with OpenCV.
* Developed hands-on experience with color space segmentation by translating raw image feeds into the HSV domain and applying static color masking.
* Learned to extract spatial properties from pixel data using contour analysis and structural moments to accurately calculate the target's centroid and bounding box dimensions in real time.
* Gain practical knowledge in closed-loop robot control by designing a proportional tracking algorithm that maps spatial pixel errors directly to angular and linear velocities.
* Faced and overcame real-world simulation physics challenges—such as wheel friction and inertial jerk—by implementing saturation limits and dead-bands to ensure smooth, stable tracking behavior without oscilation.
* Learned to manage robot state machines by writing fallback routines that automatically command an angular spin to scan and recover the target whenever visual tracking is broken.
