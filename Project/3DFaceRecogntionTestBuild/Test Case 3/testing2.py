import face_alignment
from skimage import io
import pandas
import numpy
import os
import sys
import time

fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._3D, device='cpu', flip_input=True)
fa2 = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, device='cpu', flip_input=True)

# for dire in os.listdir("lfw"):
#     print(dire)
#     for filename in os.listdir("lfw/" + dire):
#         print(filename)
#         database = io.imread("lfw/" + dire + "/" + filename)
#         preds = fa.get_landmarks(database)[-1]
#         prediction = pandas.DataFrame(preds)
#         cvs_hasil = prediction.to_csv("csvDatabase/" + filename + ".csv", index=False)

# for dire in os.listdir("lfw"):
#     print(dire)
#     for filename in os.listdir("lfw/" + dire):
#         print(filename)
#         database = io.imread("lfw/" + dire + "/" + filename)
#         preds = fa2.get_landmarks(database)[-1]
#         prediction = pandas.DataFrame(preds)
#         cvs_hasil = prediction.to_csv("csvDatabasetwo/" + filename + ".csv", index=False)

for filename in os.listdir("."):
    ctrTrue = 0
    start_time = time.time()
    if filename.endswith(".jpg"):
        print("now testing " + filename)
        input_img = io.imread(filename)
        inp = fa.get_landmarks(input_img)[-1]
        for csvname in os.listdir("csvDatabase"):
            if csvname.endswith(".csv"):
                db = pandas.read_csv("csvDatabase/" + csvname)
                db_numpy = db.to_numpy()
                sq_dist = numpy.sum((db_numpy-inp)**2, axis=0)
                dist = numpy.sqrt(sq_dist)
                
                if((dist[0] < 120 and dist[1] < 120 and dist[2] < 120 or (dist[0] < 120 and dist[1] < 120) or (dist[1] < 120 and dist[2] < 120) or (dist[0] < 120 and dist[2] < 120))):
                    # print(csvname + " is as same as " + filename)
                    # 
                    ctrTrue = ctrTrue + 1
    print(ctrTrue)
    print("--- %s seconds for 3d ---" % (time.time() - start_time))

for filename in os.listdir("."):
    ctrTrue = 0
    start_time = time.time()
    if filename.endswith(".jpg"):
        print("now testing " + filename)
        input_img = io.imread(filename)
        inp = fa2.get_landmarks(input_img)[-1]
        for csvname in os.listdir("csvDatabasetwo"):
            if csvname.endswith(".csv"):
                db = pandas.read_csv("csvDatabasetwo/" + csvname)
                db_numpy = db.to_numpy()
                sq_dist = numpy.sum((db_numpy-inp)**2, axis=0)
                dist = numpy.sqrt(sq_dist)
                
                if((dist[0] < 120 and dist[1] < 120)):
                    # print(csvname + " is as same as " + filename)
                    ctrTrue = ctrTrue + 1
    print(ctrTrue)
    print("--- %s seconds for 2d ---" % (time.time() - start_time))