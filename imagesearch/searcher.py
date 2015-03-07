import numpy
import sqlite3

class Searcher:
    def __init__(self):
        x = 1

    def search(self, queryFeatures, limit = 10):
        results = {}
        con = sqlite3.connect(".\\index.db")
        cu = con.cursor()
        cu.execute("select filename,features from imageindex")
        table = cu.fetchall()

        for data in table:
            features = eval(data[1])
            filename = str(data[0])
            results[filename] = self.chi2_distance(features, queryFeatures)
        results = sorted([(v, k) for (k, v) in results.items()])

        return results[:limit]

    def chi2_distance(self, histA, histB, eps = 1e-10):
        d = 0.5 * numpy.sum([((a - b) ** 2) / (a + b + eps)
            for (a, b) in zip(histA, histB)])
        return d
