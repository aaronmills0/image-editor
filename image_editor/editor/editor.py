import cv2 as cv
import numpy as np
from django.conf import settings
import os

class Editor():
    def __init__(self, data):
        self.data = data
        self.folder = settings.MEDIA_ROOT + 'tmp'
        self.ref = cv.imread(os.path.join(self.folder, os.listdir(self.folder)[1]))
        self.img = cv.imread(os.path.join(self.folder, os.listdir(self.folder)[0]))
        self.img = self.ref.copy()

    def isGray(self):
        if len(self.img.shape) == 3:
            return False
        return True

    def horizontal_flip(self):
        self.img = cv.flip(self.img, 1)
    
    def vertical_flip(self):
        self.img = cv.flip(self.img, 0)

    def grayscale(self):
        if not self.isGray():
            self.img = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
    
    def sepia(self):
        if not self.isGray():
            kernel = np.array([
                [0.272, 0.534, 0.131],
                [0.349, 0.686, 0.168], 
                [0.393, 0.769, 0.189]
                ], dtype=np.float64)
            self.img = np.array(self.img, dtype=np.float64)
            self.img = cv.transform(self.img, kernel)  
            self.img[np.where(self.img > 255)] = 255
            self.img = np.array(self.img, dtype=np.uint8)
    
    def binarize(self):
        if not self.isGray():
            self.grayscale()
        ret, self.img = cv.threshold(self.img, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

    def histogram_equalize(self):
        if self.isGray():
            self.img = cv.equalizeHist(self.img)
        else:
            self.img = cv.cvtColor(self.img, cv.COLOR_BGR2HSV)
            h, s, v = cv.split(self.img)
            v = cv.equalizeHist(v)
            self.img = cv.merge((h, s, v))
            self.img = cv.cvtColor(self.img, cv.COLOR_HSV2BGR)
    def invert(self):
        self.img = cv.bitwise_not(self.img)

    def smoothness(self, val):
        if val > 0:
            self.img = cv.medianBlur(self.img, 2*val-1)
    
    def sharpness(self, val):
        if val > 0:
            kernel = np.array([
                [0, -val, 0,],
                [-val, 4*val+1, -val],
                [0, -val, 0]])
            self.img = cv.filter2D(self.img, -1, kernel)

    def brightness(self, val):
        self.img = cv.convertScaleAbs(self.img, self.img, alpha=1.0, beta=1.5*val)
        self.img = np.clip(self.img, 0, 255)

    
    def contrast(self, val):
        a = val/10.0
        self.img = cv.convertScaleAbs(self.img, alpha=a, beta=0)
        self.img = np.clip(self.img, 0, 255)

    def gamma_correction(self, val):
        val = val/10.0
        inverse = 1.0/val
        table = np.array([((i/255.0)**inverse)*255
            for i in np.arange(0,256)]).astype("uint8")
        self.img = cv.LUT(self.img, table)

    def saturation(self, val):
        if val != 0 and not self.isGray():
            self.img = cv.cvtColor(self.img, cv.COLOR_BGR2HSV)
            for y in range(self.img.shape[0]):
                for x in range(self.img.shape[1]):
                    self.img[y, x, 1] = np.clip(self.img[y, x, 1] + 20*val, 0, 255)
            self.img = cv.cvtColor(self.img, cv.COLOR_HSV2BGR)
    
    def resize(self, val):
        ratio = 1.0 + 0.1*val
        dim = (int(self.img.shape[1]*ratio), int(self.img.shape[0]*ratio))
        self.img = cv.resize(self.img, dim, interpolation=cv.INTER_AREA)

    def update(self):
        if self.data.get('horizontal_flip') == 1:
            self.horizontal_flip()
        if self.data.get('vertical_flip') == 1:
            self.vertical_flip()
        if self.data.get('grayscale') == 1:
            self.grayscale()
        if self.data.get('sepia') == 1:
            self.sepia()
        if self.data.get('binarize') == 1:
            self.binarize()
        if self.data.get('histogram_equalize') == 1:
            self.histogram_equalize()
        if self.data.get('invert') == 1:
            self.invert()
        self.smoothness(self.data.get('smoothness'))
        self.sharpness(self.data.get('sharpness'))
        self.brightness(self.data.get('brightness'))
        self.contrast(self.data.get('contrast'))
        self.gamma_correction(self.data.get('gamma_correction'))
        self.saturation(self.data.get('saturation'))
        self.resize(self.data.get('resize'))
        print(os.listdir(self.folder)[0])
        #cv.imshow('img', self.img)
        #cv.waitKey(0)
        cv.imwrite(os.path.join(self.folder,os.listdir(self.folder)[0]), self.img) 