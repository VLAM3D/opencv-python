import sys
import os
import subprocess

opencv_version = ""
# dig out the version from OpenCV sources
version_file_path = "/opencv-3.4.0/modules/core/include/opencv2/core/version.hpp"

with open(version_file_path, 'r') as f:
    for line in f:
        words = line.split()

        if "CV_VERSION_MAJOR" in words:
            opencv_version += words[2]
            opencv_version += "."

        if "CV_VERSION_MINOR" in words:
            opencv_version += words[2]
            opencv_version += "."

        if "CV_VERSION_REVISION" in words:
            opencv_version += words[2]
            break

print("Version: ", opencv_version)

with open('cv_version.py', 'w') as f:
    f.write('opencv_version = "{}"'.format(opencv_version))
