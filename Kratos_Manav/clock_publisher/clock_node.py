import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class ClockNode(Node):
    def __init__(self):
        super().__init__('clock_node')
        self.second_pub = self.create_publisher(Int32, '/second', 10)
        self.minute_pub = self.create_publisher(Int32, '/minute', 10)
        self.hour_pub = self.create_publisher(Int32, '/hour', 10)
        self.clock_pub = self.create_publisher(String, '/clock', 10)

        self.timer = self.create_timer(1.0, self.timer_callback)  # 1 second timer
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

    def timer_callback(self):
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes >= 60:
            self.minutes = 0
            self.hours += 1
        if self.hours >= 24:
            self.hours = 0

        # Publish individual topics
        sec_msg = Int32()
        min_msg = Int32()
        hr_msg = Int32()

        sec_msg.data = self.seconds
        min_msg.data = self.minutes
        hr_msg.data = self.hours

        self.second_pub.publish(sec_msg)
        self.minute_pub.publish(min_msg)
        self.hour_pub.publish(hr_msg)

        # Publish complete time as HH:MM:SS
        clock_msg = String()
        clock_msg.data = f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
        self.clock_pub.publish(clock_msg)

        self.get_logger().info(f"Time: {clock_msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = ClockNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

