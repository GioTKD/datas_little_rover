import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    urdf = os.path.join(get_package_share_directory('my_rover_py'), 'urdf', 'rover_joint.urdf')

    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'simple_rover', '-file', urdf, '-x', '0', '-y', '0', '-z', '0'],
            output='screen'
        ),
    ])
