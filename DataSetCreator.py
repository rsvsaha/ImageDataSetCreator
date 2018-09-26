# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 01:30:07 2018

@author: Rishav
"""

from Cleaner_and_Resizer import resizer
from sklearn.externals import joblib
import os
from sklearn.preprocessing import LabelBinarizer
import argparse
import numpy as np
def DatasetCreator(ParentDirectory,width,height,createbinarizer=False):
    labels=[]
    DATASET=[]
    for Directories in os.listdir(ParentDirectory):
        print(Directories)
        fulldir=ParentDirectory+os.sep+Directories
        smaller_images=resizer(fulldir,width,height,save=False)
        
        DATASET.append(smaller_images)
        for i in range(smaller_images.shape[0]):
            labels.append(Directories)
    labels=np.array(labels)
    DATASET=np.concatenate(tuple(DATASET),axis=0)
    #if createbinarizer:
     #   lb=LabelBinarizer()
      #  labels=lb.fit_transform(labels)
    return (DATASET,labels)
if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("-p","--parentdirectory",required=True,help="Parent Directory Containing the Image Folders")
    ap.add_argument("-c","--createbinarizer",required=True,help="Create Binarized Labels?")
    ap.add_argument("-o","--output",required=True,help="Location of Ouput Dataset")
    ap.add_argument("-x","--width",required=True,help="width of the image")
    ap.add_argument("-y","--height",required=True,help="height cof the image")
    args=vars(ap.parse_args())
    Dataset=DatasetCreator(args["parentdirectory"],int(args["width"]),int(args["height"]),bool(args["createbinarizer"]))
    print("Dimensions of DataSet: insatances={} height={} width={} channels={} ".format(Dataset[0].shape[0],Dataset[0].shape[1],Dataset[0].shape[2],Dataset[0].shape[3]))
    print("Shape of DataSet is:{}".format(Dataset[0].shape))
    joblib.dump(Dataset,args["output"]+os.sep+"DataSet.pkl")
    