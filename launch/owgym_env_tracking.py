#!/usr/bin/env python3
# Copyright offworld.ai 2023

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument

from bot_settings import Settings


def generate_launch_description():
    camera_name = DeclareLaunchArgument(
        'camera_name',
        default_value='env_camera'
    )

    image_topic = DeclareLaunchArgument(
        'image_topic',
        default_value='image_raw'
    )

    apriltag_params = Settings.get("apriltag_params_path")

    return LaunchDescription([
        camera_name,
        image_topic,
        Node(
            package='apriltag_ros',
            namespace='env_camera',
            executable='apriltag_ros_continuous_detector_node',
            name='apriltag_detector',
            parameters=[apriltag_params],
            remappings=[
                ('~/image_rect', '/env_camera/image_raw'),
                ('~/camera_info', '/env_camera/camera_info'),
            ]
        ),
    ])
