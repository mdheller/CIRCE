import os
import sys
import time

def task(onefile, pathin, pathout):

    filelist=[]
    filelist.append(onefile)

    #time.sleep(50)
    num=filelist[0].partition('s')[0]

    with open(os.path.join(pathout, num+'merged_file0.ipsum'),'w') as outfile:
    	for filename in filelist:
            with open(os.path.join(pathin, filename), 'r') as infile:
                for line in infile:
                    outfile.write(line)

    return num+'merged_file0.ipsum'

def main():

    filelist = '1split_0'
    outfile = task(filelist, os.path.dirname(__file__), os.path.dirname(__file__))
    return outfile

if __name__ == '__main__':

    filename = '1split_0'
    task(filename, os.path.dirname(__file__), os.path.dirname(__file__))
