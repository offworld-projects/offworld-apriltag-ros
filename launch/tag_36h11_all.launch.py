import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

# detect all 16h5 tags
cfg_36h11= {
    "image_transport": "raw",
    "family": "36h11",
    "size": 0.06,
    "max_hamming": 0,
    "refine_edges": 1, 
    "z_up": True
}

def generate_launch_description():
    composable_node = ComposableNode(
        name='apriltag',
        package='apriltag_ros', plugin='AprilTagNode',
        remappings=[("/apriltag/image", "/camera/image"), ("/apriltag/camera_info", "/camera/camera_info")],
        parameters=[cfg_36h11])
    container = ComposableNodeContainer(
        name='tag_container',
        namespace='apriltag',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[composable_node],
        output='screen'
    )

    return launch.LaunchDescription([container])
