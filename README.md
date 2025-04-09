# Prerequisite
Make sure you follow instructions for setting up Isaac ROS and the various components necessary.
We recommend using [`agx-indro-docker`](https://github.com/noah-curran/agx-indro-docker) to get started.

This includes successful installation of:
- ROS2 Humble
- RealSense D435i ROS2 driver
- RoboSense LiDAR ROS2 driver
- Fixposition RTK/GPS 2 ROS2 driver
- AgileX Hunter base ROS2 driver

# Installation and Running
To build this package run from the workspace directory:
```bash
cd src && git clone https://github.com/noah-curran/agilex_bringup_ros2
cd .. && colcon build --packages-select agilex_robot_bringup
source install/setup.bash
ros2 launch agilex_robot_bringup agilex.launch.py
```
