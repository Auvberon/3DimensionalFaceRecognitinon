import face_alignment
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skimage import io
import pandas
import numpy

fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._3D, device='cpu', flip_input=True)

input_img = io.imread('dataset\Jason\jasonInput2.jpg')
input_img2 = io.imread('dataset\Jason\jasonInput.jpg')

test1 = fa.get_landmarks(input_img)[-1]
test2 = fa.get_landmarks(input_img2)[-1]

hasil1 = pandas.DataFrame(test1)
hasil2 = pandas.DataFrame(test2)

numpy_Hasil1 = hasil1.to_numpy()
numpy_Hasil2 = hasil2.to_numpy()

sq_dist = numpy.sum((numpy_Hasil1-numpy_Hasil2)**2, axis=0)
dist = numpy.sqrt(sq_dist)
print(dist)