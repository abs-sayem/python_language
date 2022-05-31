# Write a Python program to get the Python version you are using.

# Using system module
import sys
print("Pyhton Version:", sys.version)
print("Python Version Info:", sys.version_info)

# Using platform module
import platform
print("Python Version:", platform.python_version)
print("Python Version:", platform.python_version_tuple())
print("Python Version:", type(platform.python_version_tuple()))