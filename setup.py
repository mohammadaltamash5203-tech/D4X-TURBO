import sys
from setuptools import setup, find_packages

# Check if it's Termux or Android
is_mobile = "android" in sys.platform.lower() or "termux" in sys.executable

reqs = ['ujson', 'aiohttp']
if not is_mobile:
    reqs.append('uvloop') # VPS par uvloop install hoga, Termux par skip

setup(
    name="d4x-turbo",
    version="1.3",
    packages=find_packages(),
    install_requires=reqs,
    # Baaki info...
)
