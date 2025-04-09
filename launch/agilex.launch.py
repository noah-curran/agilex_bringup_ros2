from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import AnyLaunchDescriptionSource
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    return LaunchDescription([
        # LiDAR
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('rslidar_sdk'),
                    'launch',
                    'start.py'
                ])
            ]),
            launch_arguments={

            }.items()
        ),
        
        # GPS/RTK
        IncludeLaunchDescription(
            AnyLaunchDescriptionSource(
                os.path.join(
                    get_package_share_directory('fixposition_driver_ros2'),
                    'launch',
                    'node.launch'
                )
            ),
            launch_arguments={
                
            }.items()
        ),
        
        # Depth Camera
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('realsense2_camera'),
                    'launch',
                    'rs_launch.py'
                ])
            ]),
            launch_arguments={
                
            }.items()
        ),
        
        # AgileX Servo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('hunter_base'),
                    'launch',
                    'hunter_base.launch.py'
                ])
            ]),
            launch_arguments={
                
            }.items()
        )
    ])
