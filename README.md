# 🤖 Warehouse Robot Simulation using ROS 2 Jazzy & Gazebo Harmonic

A custom differential drive warehouse robot built from scratch using **ROS 2 Jazzy**, **Gazebo Harmonic**, **RViz2**, and **Xacro**. This project demonstrates robot modeling, simulation, keyboard teleoperation, and serves as the foundation for future autonomous warehouse navigation using **SLAM** and **Navigation2**.

---

## 🚀 Project Overview

This project aims to build a complete Autonomous Mobile Robot (AMR) simulation for warehouse automation.

The robot is designed and simulated completely from scratch using ROS 2 tools and will be extended with:

- LiDAR
- Camera
- SLAM
- Navigation2
- Autonomous obstacle avoidance
- Warehouse environment

---

## 🛠️ Technologies Used

- ROS 2 Jazzy
- Gazebo Harmonic
- RViz2
- URDF
- Xacro
- Python Launch Files
- Robot State Publisher
- Joint State Publisher
- ros_gz_sim
- ros_gz_bridge
- Git & GitHub

---

## 📂 Project Structure

```
warehouse_robot_ws
│
├── src
│   └── warehouse_robot_description
│       ├── launch
│       ├── resource
│       ├── test
│       ├── urdf
│       ├── package.xml
│       ├── setup.py
│       └── setup.cfg
│
├── build
├── install
└── log
```

---

# ✅ Completed Milestones

## ✅ Milestone 1 – Robot Description

- Created ROS 2 workspace
- Built warehouse_robot_description package
- Designed robot using URDF & Xacro
- Added robot visualization in RViz
- Configured Robot State Publisher
- Configured Joint State Publisher

---

## ✅ Milestone 2 – Gazebo Integration

- Spawned robot into Gazebo Harmonic
- Added Gazebo launch file
- Verified complete robot model
- Fixed robot spawning issues

---

## ✅ Milestone 3 – Differential Drive

- Added Gazebo physics
- Configured Differential Drive Plugin
- Integrated ros_gz_bridge
- Connected `/cmd_vel`
- Controlled robot using Keyboard Teleoperation

---

## 📸 Current Simulation

Current robot features:

- ✅ Differential Drive
- ✅ Left Wheel
- ✅ Right Wheel
- ✅ Caster Wheel
- ✅ Robot TF
- ✅ Keyboard Teleoperation
- ✅ Gazebo Simulation
- ✅ RViz Visualization

---

## 🚀 Build

```bash
cd ~/warehouse_robot_ws

colcon build --symlink-install
```

---

## ▶️ Run Simulation

```bash
source /opt/ros/jazzy/setup.bash

source install/setup.bash

ros2 launch warehouse_robot_description gazebo.launch.py
```

---

## 🎮 Keyboard Teleoperation

Open another terminal

```bash
source /opt/ros/jazzy/setup.bash

source install/setup.bash

ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

---

## 🌉 ROS ↔ Gazebo Bridge

Open another terminal

```bash
source /opt/ros/jazzy/setup.bash

source install/setup.bash

ros2 run ros_gz_bridge parameter_bridge \
/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist
```

---

# 🗺️ Roadmap

- ✅ Robot Description
- ✅ Gazebo Simulation
- ✅ Keyboard Teleoperation
- ⏳ LiDAR Integration
- ⏳ Camera Integration
- ⏳ SLAM Mapping
- ⏳ Navigation2
- ⏳ Warehouse Environment
- ⏳ Autonomous Navigation
- ⏳ Pick & Place Integration

---

# 📚 Learning Objectives

This project demonstrates practical experience with:

- Robot Modeling
- ROS 2 Nodes
- TF Tree
- Gazebo Simulation
- Differential Drive Kinematics
- Robot State Publisher
- ROS ↔ Gazebo Communication
- Robot Teleoperation
- Xacro
- Git Version Control

---

# 👨‍💻 Author

**Prasad Kawade**

Automation & Robotics Engineer

GitHub: https://github.com/Prasadkawade21

---

## ⭐ Future Work

The next milestone is integrating a **LiDAR sensor** and building a complete autonomous warehouse robot capable of mapping and navigating using **SLAM** and **Navigation2**.