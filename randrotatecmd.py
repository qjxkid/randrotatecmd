#!/usr/bin/env python2
import random
import math
import sys
import getopt
import os
class ImgRotate:
    def __init__(self,exefile,inimgpath,outdir,outnum):
        self.__exefile = exefile
        self.__inimgpath = inimgpath
        self.__outdir = outdir
        self.__outnum = outnum
        logfile = open(self.__outdir+"log",'w')
        logfile.close()

    def log(self,logstr):
        logfile = open(self.__outdir+"log",'a+w')
        logfile.write(logstr)
        logfile.write('\n')
        logfile.close()

    def imgCreate(self):
        filename = self.__inimgpath.strip().split('/')[-1]
        for i in xrange(self.__outnum):
            a = random.uniform(0, 2*math.pi)
            sina = math.sin(a)
            cosa = math.cos(a)
            outpath = self.__outdir + str(i) + "_" + filename
            cmd = "./" + self.__exefile + " " + self.__inimgpath + " " + str(cosa) + " " + str(sina) + " " + str(-sina) + " " + str(cosa) + " " + outpath
            os.popen(cmd)
            logstr = str(i) + " : " + "a=" + str(a) + "  abcd :" + " " + str(cosa) + " " + str(sina) + " " + str(-sina) + " " + str(cosa)
            self.log(logstr)

def usage():
    print sys.argv[0], "-e <exe_file> -i <input_image> -o <output_dir> -n <output_image_num=100>"

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "e:i:o:n:h")
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)

    exefile = None
    inimgpath = None
    outdir = None
    outnum = 100

    for (o, a) in opts:
        if o == "-i":
            inimgpath = a
        elif o == "-o":
            outdir = a
        elif o == "-e":
            exefile = a
        elif o == "-n":
            outnum = int(a)
        elif o == "-h":
            usage()

    if not exefile or not inimgpath or not outdir:
        usage()
        sys.exit(2)
    
    imrotate = ImgRotate(exefile,inimgpath,outdir,outnum)
    imrotate.imgCreate()

if __name__=="__main__":
    main()
