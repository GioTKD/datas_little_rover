import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MoveRobot(Node):

    def __init__(self):
        super().__init__('move_robot')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move_robot)  # Timer per eseguire ogni 0.1 secondi

    def move_robot(self):
        msg = Twist()
        msg.linear.x = 0.5  # Velocità lineare costante
        msg.angular.z = 0.5  # Velocità angolare costante per il movimento circolare
        self.publisher_.publish(msg)
        self.get_logger().info(f"Moving in circle: linear.x = {msg.linear.x}, angular.z = {msg.angular.z}")

def main(args=None):
    rclpy.init(args=args)
    node = MoveRobot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
