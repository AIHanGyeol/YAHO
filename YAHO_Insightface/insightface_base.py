import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

def insightface_detec(img):
    app = FaceAnalysis(providers=[ 'CPUExecutionProvider']) #'CUDAExecutionProvider',
    app.prepare(ctx_id=0, det_size=(640, 640))

    # img = ins_get_image('t1')
    img = cv2.resize(img , (640,640))
    faces = app.get(img , max_num=1)
    rimg = app.draw_on(img, faces)
    cv2.imwrite("./t1_output.jpg", rimg)