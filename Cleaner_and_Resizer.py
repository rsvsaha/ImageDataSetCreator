# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 20:09:16 2018

@author: Rishav
"""
import argparse
from imutils import paths
import cv2
import os
import numpy as np
def resizer(directory,width,height,save=False): 
    IMAGE=[]
    ctr=0
    #print("height={}".format(height))
    #print("width={}".format(width))
    
    for imagePath in paths.list_images(directory):
        #print(imagePath)
        delete=False
        try:
            image=cv2.imread(imagePath)
            if image is None:
                delete=True
            else:
                small=cv2.resize(image,(width,height))
                ctr+=1
                print("[INFO]Done Resizing Image{image}".format(image=imagePath))
                IMAGE.append(small)
                if save:
                	cv2.imwrite(imagePath,small)
        except:
            print("Exception in {}".format(imagePath))
            delete=True
        if delete:
            print("[INFO] deleting {}".format(imagePath))
            os.remove(imagePath)
    IMAGE=np.array(IMAGE)
    print("\n [INFO] Processed {no} images in {directory}".format(no=ctr,directory=directory))
    return IMAGE
if __name__=="__main__":
    ag=argparse.ArgumentParser()
    ag.add_argument("-c","--cleaning",required=True,help="path to directory being cleaned and Resized")
    ag.add_argument("-x","--width",required=True,help="width of the image")
    ag.add_argument("-y","--height",required=True,help="height of the image")
    ag.add_argument("-s","--save",required=True,help="save the modified image or not")
    args=vars(ag.parse_args())
    save=bool(args["save"])
    resizer(args["cleaning"],int(args["width"]),int(args["height"]),save)