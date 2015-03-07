# USAGE
# python index.py --dir image

from imagesearch.colordescriptor import ColorDescriptor
import argparse
import glob
import cv2
import sqlite3

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", required = True,
    help = "Path to the dir that contains the images to be indexed")
args = vars(ap.parse_args())

cd = ColorDescriptor((8, 12, 3))

con = sqlite3.connect(".\\index.db")
cu = con.cursor()
cu.execute("CREATE TABLE imageindex(filename text primary key,features text)")
con.commit()

for imagePath in glob.glob(args["dir"] + "\\*.png"):
    imageID = imagePath[imagePath.rfind("\\") + 1:]
    image = cv2.imread(imagePath)
    features = cd.describe(image)
    data = (imageID, str(features))
    cu.execute("INSERT INTO imageindex(filename, features) values (?, ?)", data)

con.commit()
con.close()
