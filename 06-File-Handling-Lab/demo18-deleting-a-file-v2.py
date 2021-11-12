# Keep in mind if the file does not exist, an error will be raised
# To avoid getting an error
# Check whether the file exists
# Delete file
import os

file_path = "my_first_file_v3.txt"
if os.path.exists(file_path):
    os.remove(file_path)
