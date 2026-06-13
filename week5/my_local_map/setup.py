from setuptools import find_packages, setup

package_name = 'my_local_map'

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
    maintainer='muhtashim',
    maintainer_email='muhtashim@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': ['localmap = my_local_map.localmap:main',
                            'vel_publisher = my_local_map.vel_publisher:main',
                            'odom_subscriber = my_local_map.odom_subscriber:main',
        ],
    },
)
