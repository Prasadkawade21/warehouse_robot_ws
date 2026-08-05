from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution

from launch_ros.substitutions import FindPackageShare

from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():

    nav2_bringup_dir = get_package_share_directory("nav2_bringup")
    navigation_pkg = get_package_share_directory("warehouse_robot_navigation")

    map_file = os.path.join(
        navigation_pkg,
        "maps",
        "warehouse_map.yaml"
    )

    params_file = os.path.join(
        navigation_pkg,
        "config",
        "nav2_params.yaml"
    )

    return LaunchDescription([

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(
                    nav2_bringup_dir,
                    "launch",
                    "bringup_launch.py"
                )
            ),
            launch_arguments={
                "map": map_file,
                "params_file": params_file,
                "use_sim_time": "True",
            }.items(),
        ),

    ])
