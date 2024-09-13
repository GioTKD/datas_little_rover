from setuptools import setup
import os
from glob import glob

package_name = 'my_rover_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='giovanni',
    maintainer_email='giovanni@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
entry_points={
    'console_scripts': [
        'talker = my_rover_py.talker:main',
        'move_circle = my_rover_py.move_circle:main',
        'listener = my_rover_py.listener:main',
        'manual_odometry = my_rover_py.manual_odometry:main',
        'move_robot = my_rover_py.move_robot:main',
    ],
},

)
