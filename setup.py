from glob import glob
import os

from setuptools import setup


package_name = 'mbari_wec_ctrl-learn_py'

setup(
    name=package_name,
    version='3.12', #Check that this is correct
    packages=[f'{package_name}'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='eagan',
    maintainer_email='ajeagan@uw.org',
    description='MBARI Power Buoy Learning Controller (python)',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            f'Learner = {package_name}.controller:main',
        ],
    },
)
