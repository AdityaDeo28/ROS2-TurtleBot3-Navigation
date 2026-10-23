# ROS 2 TurtleBot3 Autonomous Navigation

Autonomous navigation of a TurtleBot3 Burger in Gazebo simulation using ROS 2 Humble: SLAM mapping with Cartographer, AMCL localization and Nav2 waypoint navigation.

## Environment
- ROS 2 Humble, Ubuntu 22.04 (WSL2)
- Gazebo, RViz2, Nav2, Cartographer, TurtleBot3 packages

## Run (each command in its own terminal, after `source /opt/ros/humble/setup.bash`)

Simulation:
```bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py
```

1. Build a map (SLAM), drive with the keyboard, then save it:
```bash
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
ros2 run turtlebot3_teleop teleop_keyboard
ros2 run nav2_map_server map_saver_cli -f ~/deo_house_map
```

2. Localize with AMCL and navigate with Nav2 using the saved map (included in `maps/`):
```bash
ros2 launch turtlebot3_navigation2 navigation2.launch.py map:=$HOME/ros2_ws/src/turtlebot3_nav_project/maps/deo_house_map.yaml use_sim_time:=True
```

3. Set the initial pose and send goals with the Nav2 tools in RViz.

## Waypoint mission
`mission_executor` is a ROS 2 Python node that sends a list of waypoints to Nav2 using `BasicNavigator`.
```bash
cd ~/ros2_ws && colcon build --packages-select mission_executor && source install/setup.bash
ros2 run mission_executor mission_executor
```

## Notes
- If the robot fails to spawn in Gazebo, make sure `GAZEBO_PLUGIN_PATH` includes `/opt/ros/humble/lib`.
- The Nav2 goal tool needs the Nav2 RViz config, not plain `rviz2`.

## Author
Aditya Deo
