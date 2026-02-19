from setuptools import setup, find_packages

setup(
    name="d4x_turbo",
    version="1.0",
    packages=find_packages(),
    install_requires=['ujson', 'uvloop; platform_system != "Windows"'],
)
