from setuptools import setup, find_packages

setup(
    name="Bluetooth Connect",
    description="Connect Bluetooth Devices",
    version="0.1",
    author="Akhil <akhilgodvsdemon@gmail.com>",
    license="MIT",
    packages=["bluetooth"],
    install_requires=["click==7.1.2"],
    package_data={"bluetooth": ["bluetooth_peripherals/*.json"]},
    entry_points={"console_scripts": ["bluetoothpython = bluetooth.cli:cli"]},
)
