# ImageDataSetCreator
This project is aimed for creating a Image Data Set using Web Scraping of Google Images

How to use:

1. Run the SeleniumSearching.py with command line argument -s="SEARCH WORD".
It will automatically browse the web and will scroll to the bottom of the google images web page for that search word.


2. Open the developer console of that browser and run the commands written in "JS Query.txt"
It will download a "myFile.txt" which contains the urls of the images on the google image search for that particular SEARCH WORD.

3. Do steps 1 and 2 for all the classes of images you need and rename the myFile.txt according to the class names.

4. Next Create a directory named "DataSet" and under that directories of the classes of images you want. It will be like


|-DataSet
    |-Class1
    |-Class2
    |-Class3
     .....
5. Run the "Downloader.py" with command line argument -u="LOCATION OF THAT PARTICULAR CLASS myFILE.txt" -o="DataSet\PARTICULAR CLASS PATH" -n="NUMBER OF IMAGES YOU WANT TO DOWNLOAD FOR THAT CLASS"
NOTE:If the number of images on the google image search is less than the number of images you want it will download only tha available images.
Continue Step 5 for all the classes this will fill the Class folders with images downloaded from the web.

6.Next Run DataSetCreator.py with CLI -p=DataSet -o="OUTPUT PATH OF THE DATA SET" -x="width of image" -y="height of the image"

This will create a "DataSet.pkl" file at the directory given by -o.

Tip: If you want to resize the images permanently then just run Cleaner_and_Resizer.py with CLI -c="Location of directory whose Images are to be resized" -x=Width of the image -y=height of the image -s=True.


This repo is highly inspired from pyimagesearch tutorial on how to build deep learning datasets using GOOGLE Images.
