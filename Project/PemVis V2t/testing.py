import face_alignment
from skimage import io
import pandas
import numpy
import os
import sys


fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._3D, device='cpu', flip_input=True)
input_img = io.imread('lfw\Aaron_Eckhart\Aaron_Eckhart_0001.jpg')

inp = fa.get_landmarks(input_img)[-1]

for filename in os.listdir("."):
    if filename.endswith(".csv"):
        db = pandas.read_csv(filename)
        db_numpy = db.to_numpy()
        sq_dist = numpy.sum((db_numpy-inp)**2, axis=0)
        dist = numpy.sqrt(sq_dist)

        if(dist[0] < 1000 and dist[1] < 1000 and dist[2] < 1000):
            print("true")