import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    urdf_file = os.path.join(get_package_share_directory('my_rover_py'), 'urdf', 'rover_joint.urdf')

    return LaunchDescription([
        # Includi il lancio di Gazebo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
        ),
        
        # Spawna il modello su Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'simple_rover', '-file', urdf_file, '-x', '0', '-y', '0', '-z', '0'],
            output='screen'
        ),

        # Avvia robot_state_publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}]
        ),

        # Nodo per il movimento circolare
        Node(
            package='my_rover_py',
            executable='move_circle',
            name='move_circle',
            output='screen',
        ),

        # Nodo per l'odometria manuale
        Node(
            package='my_rover_py',
            executable='manual_odometry',
            name='manual_odometry',
            output='screen',
        ),
    ])
