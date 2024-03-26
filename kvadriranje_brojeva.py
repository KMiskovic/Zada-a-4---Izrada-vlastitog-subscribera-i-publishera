
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class KvadriranjeBrojeva(Node):
    def __init__(self):
        super().__init__('kvadriranje_brojeva')
        self.subscription_ = self.create_subscription(
            Int32, '/broj', self.receive_number, 10)
        self.publisher_ = self.create_publisher(Int32, '/kvadrat_broja', 10)

    def receive_number(self, msg):
        received_number = msg.data
        squared_number = received_number ** 2
        self.get_logger().info(f"data:{squared_number}")

        result_msg = Int32()
        result_msg.data = squared_number
        self.publisher_.publish(result_msg)

def main(args=None):
    rclpy.init(args=args)
    node = KvadriranjeBrojeva()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
