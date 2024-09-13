import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class MoveCircle(Node):

    def __init__(self):
        super().__init__('move_circle')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.odom_subscriber = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.timer = self.create_timer(0.1, self.move_robot)
        self.get_logger().info("Starting circular movement.")
    
    def move_robot(self):
        msg = Twist()
        msg.linear.x = 0.5  # Velocità lineare costante
        msg.angular.z = 0.5  # Velocità angolare costante per il movimento circolare
        self.publisher_.publish(msg)
    
    def odom_callback(self, msg):
        # Log the robot's position
        position = msg.pose.pose.position
        self.get_logger().info(f"Position -> x: {position.x}, y: {position.y}, z: {position.z}")

def main(args=None):
    rclpy.init(args=args)
    node = MoveCircle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
