import rclpy
from rclpy.node import Node
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
import time


class MissionExecutor(Node):

    def __init__(self):
        super().__init__('mission_executor')

        self.navigator = BasicNavigator()
        self.get_logger().info("Mission Executor Started")

        self.navigator.waitUntilNav2Active()

        self.waypoints = [
            self.create_pose(1.0, 2.0),
            self.create_pose(2.0, 1.0),
            self.create_pose(0.5, 0.5)
        ]

        self.execute_mission()

    def create_pose(self, x, y):
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.navigator.get_clock().now().to_msg()

        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.orientation.w = 1.0

        return pose

    def execute_mission(self):
        for i, goal in enumerate(self.waypoints):
            self.get_logger().info(f"Going to waypoint {i+1}")

            self.navigator.goToPose(goal)

            while not self.navigator.isTaskComplete():
                time.sleep(0.5)

            result = self.navigator.getResult()

            if result == self.navigator.SUCCEEDED:
                self.get_logger().info("Success")
            else:
                self.get_logger().warn("Failed, retrying once")
                self.navigator.goToPose(goal)


def main():
    rclpy.init()
    node = MissionExecutor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
