# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:08:57 2018

@author: Rishav
"""
#%%
from imutils import paths
import argparse
import requests
import cv2
import os
#%%
ap=argparse.ArgumentParser()
ap.add_argument("-u","--urls",required=True,help="path to file containing image URLS")
ap.add_argument("-o","--output",required=True,help="path to output directory of images")
ap.add_argument("-n","--number",required=True,help="number of instances of the image")
args=vars(ap.parse_args())
#%%
rows=open(args["urls"]).read().strip().split("\n")
total=0
req=int(args["number"])
#%%
for url in rows:
    try:
        p=os.path.sep.join([args["output"],"{}.jpg".format(str(total).zfill(8))])
        r=requests.get(url,timeout=60)
        f=open(p,"wb")
        f.write(r.content)
        f.close()
        print("[INFO] downloaded:{}".format(p))
        total+=1
        if total==req:
        	break
    except KeyboardInterrupt:
    	quit()
    except:
        print("[INFO] error downloading{}....skipping".format(p))

