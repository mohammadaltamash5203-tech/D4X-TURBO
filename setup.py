import sys
from setuptools import setup, find_packages

# Check if it's Termux or Android
is_mobile = "android" in sys.platform.lower() or "termux" in sys.executable

reqs = ['ujson', 'aiohttp']
if not is_mobile:
    reqs.append('uvloop') # VPS par uvloop install hoga, Termux par skip

setup(
    name="d4x-turbo",
    version="1.5", # Version hamesha increment karein
    packages=find_packages(),
    install_requires=reqs,
    author="D4X", # Apna asli naam ya username likhein
    description="Ultra fast bot engine booster for Python bots",
    long_description="D4X-TURBO optimizes your bot using ujson and advanced memory management for both Termux and VPS.",
    long_description_content_type="text/markdown",
    url="https://github.com/aapka-username/d4x-turbo", # Apni repo ka link
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
