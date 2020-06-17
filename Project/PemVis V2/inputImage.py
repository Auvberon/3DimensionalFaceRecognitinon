# Untuk masukkin csv ke Database
import face_alignment
from skimage import io
import pandas
import numpy

fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._3D, device='cpu', flip_input=True)

input_img = io.imread('DatabaseFoto/rizkyDepan.jpg') #anggep dari kamera
preds = fa.get_landmarks(input_img)[-1]
prediction = pandas.DataFrame(preds)
csv_hasil = prediction.to_csv('rizky.csv', index = False)