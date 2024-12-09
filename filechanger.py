import os
import sys
format = input("What should I name the files as?")
filetpye = input("What is the file type?")
for i in range(1, len(sys.argv)):
    os.rename(sys.argv[i], f"{format}{i}.{filetpye}")
