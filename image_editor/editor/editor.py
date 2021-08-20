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

    def smoothness(self, val):
        if val > 0:
            self.img = cv.medianBlur(self.img, 2*val-1)
    
    def sharpness(self, val):
        if val > 0:
            kernel = np.add(np.array([
                [0, 0, 0,],
                [0, 1, 0],
                [0, 0, 0]]),
                np.array([
                [-1, -1, -1],
                [-1, 4, -1],
                [-1, -1, -1]
                ])*(1))
            self.img = cv.filter2D(self.img, -1, kernel)
    
    def brightness(self, val):
        if val != 0 and not self.isGray():
            for y in range(self.img.shape[0]):
                for x in range(self.img.shape[1]):
                    for c in range(self.img.shape[2]):
                        self.img[y, x, c] = np.clip(self.img[y, x, c] + 20*val, 0, 255)
    
    def contrast(self, val):
        if val != 0 and not self.isGray():
            for y in range(self.img.shape[0]):
                for x in range(self.img.shape[1]):
                    for c in range(self.img.shape[2]):
                        self.img[y, x, c] = np.clip((1.0 + val*0.2)*self.img[y, x, c], 0, 255)
    
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
        self.smoothness(self.data.get('smoothness'))
        self.sharpness(self.data.get('sharpness'))
        self.brightness(self.data.get('brightness'))
        self.contrast(self.data.get('contrast'))
        self.saturation(self.data.get('saturation'))
        self.resize(self.data.get('resize'))
        print(os.listdir(self.folder)[0])
        #cv.imshow('img', self.img)
        #cv.waitKey(0)
        cv.imwrite(os.path.join(self.folder,os.listdir(self.folder)[0]), self.img) 