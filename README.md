# createSrcSet
Create a set of smaller images to use as srcSet (tool for web development)

This script takes a larger image and a number, and makes smaller copies at an interval determined by the number given. 


# how to use (UNIX)
1. clone repo
3. make sure your version of python has opencv installed (pip3 install opencv-python)
4. add createSrcSet.py to your PATH variable in your respective .zshrc or .bashrc folder
5. run python3 createSrcSet.py <num_copies> <source_file_path>
6. copies should be in a folder called tiny_copies_<source_file_path> in the directory you ran the command in.
