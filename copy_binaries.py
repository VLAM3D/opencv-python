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
    
    if sys.version_info[0] == 2:
        assert_copy(os.path.join(opencvbuildpath, 'lib', 'Release', 'cv2.pyd'), os.path.join(dst_folder, 'cv2.pyd'))
    else:
        assert_copy(os.path.join(opencvbuildpath, 'lib', 'python3', 'Release', 'cv2.cp35-win_amd64.pyd'), os.path.join(dst_folder, 'cv2.pyd'))
      
    dlls = glob.glob(os.path.join(opencvbuildpath, 'bin', 'Release', 'opencv_*.dll'))
    
    for file in dlls:
        assert_copy(file, os.path.join(dst_folder, os.path.basename(file)))

    cuda_bin_path = r'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.2\bin'
    cuda_files = [  'cudart64_92.dll', 
                    'nppc64_92.dll', 
                    'nppif64_92.dll',
                    'nppim64_92.dll',
                    'npps64_92.dll', 
                    'nppial64_92.dll', 
                    'nppicc64_92.dll', 
                    'nppidei64_92.dll', 
                    'nppist64_92.dll',
                    'nppitc64_92.dll', 
                    'nppig64_92.dll',
                    'cublas64_92.dll',
                    'cufft64_92.dll']

    for file in cuda_files:
        assert_copy(os.path.join(cuda_bin_path,file), os.path.join(dst_folder, file))
        
if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='Copy the binaries from the OpenCV build path.')
    parser.add_argument('opencvbuildpath', type=str, help='Full path of the OpenCV build path e.g. folder containing CMakeCache.txt')
    
    args = parser.parse_args()

    copy_binaries_main(args.opencvbuildpath)
