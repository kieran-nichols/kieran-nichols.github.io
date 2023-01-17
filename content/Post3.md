title: Windows to Linux ROS Bridge
Date: 2023-01-16 15:00
category: Tutorials

You can find more details to this post in this [tutorial](https://github.com/kieran-nichols/catkin_ws_remote).
## How to set up Remote bridge:
Helpful links: https://husarion.com/tutorials/ros-tutorials/5-running-ros-on-multiple-machines/ 
https://github.com/Brabalawuka/RosOnWindows

### Key instructions for remote windows:

1\. Change ROS_MASTER URI (The rasp pi will be running roscore). You won't need to start roscore but you can if you want to run rostopic or rqt_plot
2\. Create a .txt including following content: (Use your raspi ip address). Save as C:\bashrc.cmd at disk C (or another non-catkin_ws location).
```	
@echo off 
set ROS_MASTER_URI=http://192.168.1.19:11311
set ROS_IP=192.168.1.249
```
3\. (Optional) Following step 2, open regedit: -> Win+R and enter regedit. Find [HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor] and add a string key named Autorun, value is C:\bashrc.cmd"

4\. Run the cmd file in the Developer Command Prompt in VS22 "C:\bashrc.cmd". There were some issues with it autorunning in step 3

5\. Use rosrun to execute the individual programs on remote machine.

### Key instructions for raspi:
1\. On the raspi device open the .bashrc file, then add the lines:
```
export ROS_MASTER_URI=http://192.168.1.19:11311
export ROS_IP=192.168.1.19
```
2\. Start roscore