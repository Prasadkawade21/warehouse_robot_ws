from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

import os
import xacro


def generate_launch_description():

    # Package paths
    pkg_path = get_package_share_directory(
        "warehouse_robot_description"
    )

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

    # Bridge configuration
    bridge_config = os.path.join(
        pkg_path,
        "config",
        "bridge.yaml"
    )

    # Custom Gazebo world
    world_file = os.path.join(
        pkg_path,
        "worlds",
        "warehouse.world"
    )

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
                "gz_args": f"-r {world_file}"
            }.items()
        ),

        # Robot State Publisher
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[robot_description],
            output="screen"
        ),

        # Spawn Robot
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

        # ROS ↔ Gazebo Bridge
        Node(
            package="ros_gz_bridge",
            executable="parameter_bridge",
            parameters=[
                {
                    "config_file": bridge_config,
                }
            ],
            output="screen"
        ),

    ])