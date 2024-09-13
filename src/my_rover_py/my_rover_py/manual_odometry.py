import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from tf2_msgs.msg import TFMessage

class ManualOdometry(Node):

    def __init__(self):
        super().__init__('manual_odometry')

        # Open files to save the position and tf data
        self.position_file = open('position_data.txt', 'w')
        self.tf_file = open('tf_data.txt', 'w')
        self.tf_static_file = open('tf_static_data.txt', 'w')

        # Subscribe to /odom topic
        self.sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)

        # Subscriptions for /tf and /tf_static
        self.tf_sub = self.create_subscription(TFMessage, '/tf', self.tf_callback, 10)
        self.tf_static_sub = self.create_subscription(TFMessage, '/tf_static', self.tf_static_callback, 10)

    def odom_callback(self, msg):
        """Callback to handle /odom data"""
        position = msg.pose.pose.position
        self.position_file.write(f"{position.x}, {position.y}\n")
        self.get_logger().info(f"Position: x={position.x}, y={position.y}")

    def tf_callback(self, msg):
        """Callback to save /tf data to a file"""
        for transform in msg.transforms:
            self.tf_file.write(f"{transform.header.stamp.sec}.{transform.header.stamp.nanosec}: {transform.child_frame_id}, {transform.transform.translation}, {transform.transform.rotation}\n")

    def tf_static_callback(self, msg):
        """Callback to save /tf_static data to a file"""
        for transform in msg.transforms:
            self.tf_static_file.write(f"{transform.header.stamp.sec}.{transform.header.stamp.nanosec}: {transform.child_frame_id}, {transform.transform.translation}, {transform.transform.rotation}\n")

    def destroy_node(self):
        # Close the files when the node is destroyed
        self.position_file.close()
        self.tf_file.close()
        self.tf_static_file.close()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = ManualOdometry()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
