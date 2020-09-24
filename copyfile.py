#!/usr/bin/env python3
import sys
if len(sys.argv) < 3:
    print("Wrong parameter")
    print("./copyfile.py file1 file2")
    sys.exit(1)
with open(sys.argv[1]) as f1:
    s = f1.read()
f1.close()
with open(sys.argv[2]) as f2:
    f2.write(s)
f2.close()