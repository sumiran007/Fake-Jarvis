import os
import sys
format = input("What should I name the files as?")
filetype = input("What is the file type?")
for i in range(1, len(sys.argv)):
    os.rename(f"{format}{i}.{filetype}")
