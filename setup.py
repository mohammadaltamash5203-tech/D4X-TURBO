import sys
import os
from setuptools import setup, find_packages

# The Ultimate Platform Detector
is_android = 'android' in sys.platform.lower() or 'com.termux' in sys.executable

# 1. Base Dependencies (Jo Termux aur VPS dono par makkhan chalenge)
install_requires = ['ujson>=5.0.0', 'aiohttp>=3.8.0']

# 2. Extreme Dependencies (Sirf VPS/Linux Server ke liye)
if not is_android:
    # uvloop = CPU speed, aiodns = Network/API speed
    install_requires.extend(['uvloop>=0.17.0', 'aiodns>=3.0.0', 'cchardet>=2.1.7'])

long_desc = "The Ultimate Beast Engine for Python Bots (Termux & VPS)"
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as f:
        long_desc = f.read()

setup(
    name="d4x-turbo",
    version="4.0.0",  # The Ultimate Beast Version
    packages=find_packages(),
    install_requires=install_requires,
    author="D4X",
    description="Ultra-Advanced High-Speed Engine for Termux and VPS Bots",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
