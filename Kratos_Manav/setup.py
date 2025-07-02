from setuptools import find_packages, setup

package_name = 'clock_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='xlr8victusmanav',
    maintainer_email='xlr8victusmanav@gmail.com',
    description='Simple ROS 2 Clock Publisher that publishes time on /hour, /minute, /second, and /clock.',
    license='MIT',  # or update as needed
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'clock_node = clock_publisher.clock_node:main',
        ],
    },
)

