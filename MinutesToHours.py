import os
import sys
def Hours(mm):
    if mm < 0:
        raise ValueError("Input number cannot be negative")
    else:
        h, m = divmod(mm, 60)
        print("{} H, {} M".format(h, m))    
    
def main(argv):
    try:
        Hours(int(argv))
    except:
        print("Parameter Error")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))     
    else:
        sys.exit(-1)
    sys.exit(0)