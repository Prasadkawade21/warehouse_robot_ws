from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

import os
import xacro


def generate_launch_description():

    # Warehouse robot package
    pkg_path = get_package_share_directory(
        "warehouse_robot_description"
    )

    # Gazebo package
    ros_gz_sim = get_package_share_directory(
        "ros_gz_sim"
    )

    # Robot Xacro
    xacro_file = os.path.join(
        pkg_path,
        "urdf",
        "warehouse_robot.urdf.xacro"
    )

    robot_description = {
        "robot_description": xacro.process_file(
            xacro_file
        ).toxml()
    }

    return LaunchDescription([

        # Start Gazebo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(
                    ros_gz_sim,
                    "launch",
                    "gz_sim.launch.py"
                )
            ),
            launch_arguments={
                "gz_args": "-r empty.sdf"
            }.items()
        ),

        # Publish robot state
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[robot_description],
            output="screen"
        ),
        Node(
             package="ros_gz_sim",
            executable="create",
            arguments=[
                "-topic",
                "robot_description",
                "-name",
                "warehouse_robot"
            ],
            output="screen"
        ),

    ])