from setuptools import find_packages, setup

package_name = 'mission_executor'

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
    maintainer='aditya',
    maintainer_email='adityadeo2003@gmail.com',
    description='ROS 2 node that sends waypoint missions to Nav2 using BasicNavigator',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
		'mission_executor = mission_executor.mission_executor:main',
        ],
    },
)
