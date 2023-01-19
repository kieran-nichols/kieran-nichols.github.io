title: TADA Software Architecture
Date: 2023-01-16 14:00
category: Posts

My PhD project involves developing a real-time controller for the Two Axis aDaptable Ankle (TADA).
The software can be summariezed as follows:
## Architecture Summary
### [Raspberry pi](https://github.com/kieran-nichols/catkin_ws_tadaros)
_Linux_

* Brain
* Motors
* IMU
* Europa
### [Remote computer](https://github.com/kieran-nichols/catkin_ws_remote) 
_Windows_

* Data processing 
* Xsens
* GUI
### Remote bridge: 
_ROS over Wi-Fi_