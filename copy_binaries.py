from __future__ import print_function
import sys
import os
import argparse
import glob
from shutil import copyfile

this_file_dir = os.path.dirname(os.path.realpath(__file__))

def assert_copy(src, dst):    
    assert(os.path.exists(src))
    print('Copying %s to %s' % (src,dst))
    copyfile(src, dst)
   
def copy_binaries_main(opencvbuildpath):
    
    dst_folder = os.path.join(this_file_dir, 'cv2')        
    if not os.path.exists(dst_folder):
        raise RuntimeError('cv2 subfolder not found - you may have moved this script to the wrong folder')
    
    assert_copy(os.path.join(opencvbuildpath, 'lib', 'Release', 'cv2.pyd'), os.path.join(dst_folder, 'cv2.pyd'))
      
    dlls = glob.glob(os.path.join(opencvbuildpath, 'bin', 'Release', 'opencv_*.dll'))
    
    for file in dlls:
        assert_copy(file, os.path.join(dst_folder, os.path.basename(file)))
        
if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='Copy the binaries from the OpenCV build path.')
    parser.add_argument('opencvbuildpath', type=str, help='Full path of the OpenCV build path e.g. folder containing CMakeCache.txt')
    
    args = parser.parse_args()

    copy_binaries_main(args.opencvbuildpath)
