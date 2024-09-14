# Little data acquisition from topic on rover
## Goals of the project
The goal of this project is to acquire data from different topics
## Prerequisites
* ROS2 Humble
* Gazebo classic
## Create a folder
```
cd
mkdir ros2_ws
```
## Clone in it the repo
```
cd ros2_ws
git clone https://github.com/GioTKD/datas_little_rover
```
## build
```
cd ros2_ws
colcon build
source install/setup.bash
```
## Run project
```
ros2 launch my_rover_py circle_movement.launch.py
```
