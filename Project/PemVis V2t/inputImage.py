# Untuk masukkin csv ke Database
import face_alignment
from skimage import io
import pandas
import numpy
import os
import fnmatch

fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._3D, device='cpu', flip_input=True)

# Code for training
# for dirName, subdirList, filelist in os.walk("lfw"):
#     print(dirName)
#     for fname in filelist:
#         # print(dirName + "/" + fname)
#         input_img = io.imread(dirName + "/" + fname)
#         preds = fa.get_landmarks(input_img)[-1]
#         prediction = pandas.DataFrame(preds)
#         csv_hasil = prediction.to_csv("csvHasil/" + fname + ".csv", index=False)

input_img = io.imread('lfw\Abdel_Nasser_Assidi\Abdel_Nasser_Assidi_0001.jpg') #anggep dari kamera
inp = fa.get_landmarks(input_img)[-1]

true = 0

for filename in os.listdir("csvHasil"):
    if filename.endswith(".csv"):
        db = pandas.read_csv("csvHasil/" + filename)
        db_numpy = db.to_numpy()
        sq_dist = numpy.sum((db_numpy-inp)**2, axis=0)
        dist = numpy.sqrt(sq_dist)

        if(dist[0] < 50 and dist[1] < 50 and dist[2] < 50):
            true = 1 + true

print(true)

# for filename in os.listdir("csvHasil"):
#     if filename.endswith(".csv"):
#         db = pandas.read_csv("csvHasil/" + filename)
#         db_numpy = db.to_numpy()
#         sq_dist = numpy.sum((db_numpy-inp)**2, axis=0)
#         dist = numpy.sqrt(sq_dist)
#         print(dist)