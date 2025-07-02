from setuptools import setup

package_name = 'kratos_manav'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Manav Verma',
    maintainer_email='xlr8victusmanav@bits.com',
    description='ROS 2 Week 3 Assignment Package',
    license='MIT',
    entry_points={
        'console_scripts': [
            'q1_pub = kratos_manav.q1_pub:main',
            'q1_sub = kratos_manav.q1_sub:main',
        ],
    },
)

