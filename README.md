# ROS 2 Week 3 Assignment – Question 2.2

## ✅ Description

This package contains two ROS 2 Python nodes for controlling two traffic signals (S1 and S2) based on a timing relationship:

- `s1_publisher` publishes the color **green** for 10 seconds, then **red** for 10 seconds, on the topic `/s1`, and repeats.
- `s2_controller` subscribes to `/s1` and publishes:
  - **red** on `/s2` when `/s1` is **green**
  - **green** on `/s2` when `/s1` is **red**

This simulates alternating signal logic for a simple traffic system.

---

## 📁 Files

| File Name         | Description |
|------------------|-------------|
| `s1_publisher.py` | Publishes `"green"` and `"red"` alternately every 10 seconds on topic `/s1`. |
| `s2_controller.py`| Subscribes to `/s1`, and publishes the opposite color to `/s2`. |

---

## 🚀 How to Run

### 1. Build the package

```bash
cd ~/ros2_ws
colcon build --packages-select kratos_manav
source install/setup.bash
