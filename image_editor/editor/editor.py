import cv2 as cv
import numpy as np

class Editor():
    def __init__(self, name, copy_name, data):
        self.name = name
        self.data = data
        self.original = cv.imread('../media/tmp/{}'.format(copy_name))
        self.modified = cv.imread('../media/tmp/{}'.format(name))
        self.modified = self.original.copy()
        