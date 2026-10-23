# ROS 2 TurtleBot3 Autonomous Navigation

Autonomous navigation of a TurtleBot3 Burger in Gazebo simulation using ROS 2 Humble: SLAM mapping, AMCL localization and Nav2 waypoint navigation.

## Pipeline
1. Build a map of the Gazebo world with SLAM and save it
2. Localize the robot on the saved map with AMCL
3. Send goals and waypoints through Nav2

## Environment
- ROS 2 Humble, Ubuntu 22.04 (WSL2)
- Gazebo, RViz2, Nav2, TurtleBot3 packages

## Notes
- If the robot fails to spawn in Gazebo, make sure `GAZEBO_PLUGIN_PATH` includes `/opt/ros/humble/lib`.
- The Nav2 goal tool needs the Nav2 RViz config, not plain `rviz2`.

## Author
Aditya Deo
