
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Brojcanik(Node):
    def __init__(self):
        super().__init__('brojcanik')
        self.publisher_ = self.create_publisher(Int32, '/broj', 10)
        self.timer_ = self.create_timer(1.0, self.publish_number)
        self.number_ = 0

    def publish_number(self):
        msg = Int32()
        msg.data = self.number_
        self.publisher_.publish(msg)
        self.number_ += 1

def main(args=None):
    rclpy.init(args=args)
    node = Brojcanik()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
