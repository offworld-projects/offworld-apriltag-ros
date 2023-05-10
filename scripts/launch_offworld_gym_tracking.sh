#!/usr/bin/env bash
# Service manager currently does not support ros2 launch files, so we use this script as an OS_SERVICE to launch the node
ros2 launch apriltag_ros offworld_gym_env_tracking.py