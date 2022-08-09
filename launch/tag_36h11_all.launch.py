import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

# detect all 36h11 tags
cfg_tag36h11 = {
    "image_transport": "raw",
    "family": "36h11",
    "size": 0.06,
    "max_hamming": 0,
    "z_up": True,
    "decimate" : 1.5, 
    "blur" : 0.5, 
    "refine-edges" : 2,
    "decode_sharpening":10.0,
    "debug": 1,
}

def generate_launch_description():
    composable_node = ComposableNode(
        name='apriltag',
        package='apriltag_ros', plugin='AprilTagNode',
        remappings=[("/apriltag/image", "/camera/image"), ("/apriltag/camera_info", "/camera/camera_info")],
        parameters=[cfg_tag36h11])

    # viz_composable_node = ComposableNode(
	# 	name='viz', 
	# 	package='apriltag_ros', plugin='AprilVizNode',
	# 	remappings=[("/apriltag/image", "/camera/image"), # input
	# 			],
	# 	)
    container = ComposableNodeContainer(
        name='tag_container',
        namespace='apriltag',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[composable_node],
        output='screen'
    )

    return launch.LaunchDescription([container])
