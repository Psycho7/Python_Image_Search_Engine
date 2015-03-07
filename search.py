# USAGE
# python search.py --query query/100000.png --result-path image

from imagesearch.colordescriptor import ColorDescriptor
from imagesearch.searcher import Searcher
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True,
    help = "path to the query image")
ap.add_argument("-r", "--result-path", required = True,
    help = "Path to the result path")
args = vars(ap.parse_args())

cd = ColorDescriptor((8, 12, 3))

query = cv2.imread(args["query"])
features = cd.describe(query)

searcher = Searcher()
results = searcher.search(features)

cv2.imshow("Query", query)

for (score, resultID) in results:
    result = cv2.imread(args["result_path"] + "/" + resultID)
    cv2.imshow("Result", result)
    cv2.waitKey(0)
