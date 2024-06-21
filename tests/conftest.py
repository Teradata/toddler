# tests/conftest.py
import sys
import os

# Get the root directory of the project
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the my_python_library directory to the system path
sys.path.insert(0, os.path.join(root_path, 'toddler'))
