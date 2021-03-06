import cv2 as cv
import numpy as np
from django.conf import settings
import os

class Editor():
    def __init__(self, data):
        self.data = data
        self.folder = settings.MEDIA_ROOT + 'tmp'
        try:
            self.ref = cv.imread(os.path.join(self.folder, os.listdir(self.folder)[2]))
            self.img = cv.imread(os.path.join(self.folder, os.listdir(self.folder)[1]))
            self.img = self.ref.copy()
        except:
            raise Exception("Failed to upload image")

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
            h, s, v = cv.split(self.img)
            a = val/10.0
            s = cv.convertScaleAbs(s, alpha=a, beta=0)
            s = np.clip(s, 0, 255)
            self.img = cv.merge((h,s,v))
            self.img = cv.cvtColor(self.img, cv.COLOR_HSV2BGR)
    
    def temperature(self, val):
        if val != 0 and not self.isGray():
            self.img = cv.cvtColor(self.img, cv.COLOR_BGR2YUV)
            y, u, v = cv.split(self.img)
            if val > 0:
                a = (1 + val/100.0)
                v = cv.convertScaleAbs(v, alpha=a, beta=0)
                v = np.clip(v, 0, 255)
            else:
                a = (1 - val/100.0)
                u = cv.convertScaleAbs(u, alpha=a, beta=0)
                u = np.clip(u, 0, 255)
            self.img = cv.merge((y,u,v))
            self.img = cv.cvtColor(self.img, cv.COLOR_YUV2BGR)

    def resize(self, val):
        ratio = 1.0 + 0.1*val
        dim = (int(self.img.shape[1]*ratio), int(self.img.shape[0]*ratio))
        self.img = cv.resize(self.img, dim, interpolation=cv.INTER_AREA)

    def toRGB(self, color):
        b_hex = color[-2:]
        g_hex = color[-4:-2]
        r_hex = color[-6:-4]
        
        b = int(b_hex, 16)
        g = int(g_hex, 16)
        r = int(r_hex, 16)

        return (r, g, b)

    def color_pop_color(self, color, encoded, boundary):
        if not self.isGray():
            if len(encoded) == 0:
                r, g, b = self.toRGB(color)
            else:
                data = encoded.split(':')
                x = float(data[0])
                y = float(data[1])
                w = float(data[2])
                h = float(data[3])
                if h < 1 or w < 1:
                    return
                ratio = self.img.shape[0]/h
                x = int(x*ratio)
                y = int(y*ratio)
                b = self.img[y, x, 0]
                g = self.img[y, x, 1]
                r = self.img[y, x, 2]
                h_r = hex(r)[2:]
                h_g = hex(g)[2:]
                h_b = hex(b)[2:]
                if len(h_r) < 2:
                    h_r = "0" + h_r
                if len(h_g) < 2:
                    h_g = "0" + h_g
                if len(h_b) < 2:
                    h_b = "0" + h_b
                h = "#" + h_r + h_g + h_b
                self.data.update({'color_pop_color':h})

            c = np.uint8([[[b, g, r]]])
            hsv_color = cv.cvtColor(c, cv.COLOR_BGR2HSV)
            h = hsv_color[0, 0, 0]

            hsv = cv.cvtColor(self.img, cv.COLOR_BGR2HSV)
            gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)

            s_l_bound = 70
            v_l_bound = 50
            if 180 - h < boundary or h < boundary:
                if 180 - h < boundary:
                    upper1 = np.array([h+boundary - 180, 255, 255])
                    lower1 = np.array([0, s_l_bound, v_l_bound])
                    upper2 = np.array([180, 255, 255])
                    lower2 = np.array([h-boundary, s_l_bound, v_l_bound])
                else:
                    upper1 = np.array([h+boundary, 255, 255])
                    lower1 = np.array([0, s_l_bound, v_l_bound])
                    upper2 = np.array([180, 255, 255])
                    lower2 = np.array([h-boundary + 180, s_l_bound, v_l_bound])
                mask1 = cv.inRange(hsv, lower1, upper1)
                mask2 = cv.inRange(hsv, lower2, upper2)
                mask = cv.bitwise_or(mask1, mask2)
            else:
                upper = np.array([h+boundary, 255, 255])
                lower = np.array([h-boundary, s_l_bound, v_l_bound])
                mask = cv.inRange(hsv, lower, upper)

            mask_inv = cv.bitwise_not(mask)

            color = cv.bitwise_and(self.img, self.img, mask=mask)

            background = cv.bitwise_and(gray, gray, mask=mask_inv)

            background = np.stack((background,)*3, axis=-1)

            self.img = cv.add(color, background)
    
    def crop(self, encoded):
        if len(encoded) > 0:
            crops = encoded.split('^')
            for c in crops:
                data = c.split(':')
                x1 = float(data[0])
                y1 = float(data[1])
                x2 = float(data[2])
                y2 = float(data[3])
                w = float(data[4])
                h = float(data[5])
                if h < 28 or w < 28:
                    return
                ratio = self.img.shape[0]/h
                x1 = int(x1*ratio)
                y1 = int(y1*ratio)
                x2 = int(x2*ratio)
                y2 = int(y2*ratio)
                tx = min(x1, x2)
                ty = min(y1, y2)
                bx = max(x1, x2)
                by = max(y1, y2)
                if by-ty < 28 or bx-tx < 28:
                    return
                if not self.isGray():
                    self.img = self.img[ty:by,tx:bx,:]
                else:
                    self.img = self.img[ty:by,tx:bx]


    def update(self):
        if self.data.get('horizontal_flip') == 1:
            self.horizontal_flip()
        if self.data.get('vertical_flip') == 1:
            self.vertical_flip()
        if self.data.get('crop_bool') == 1:
            self.crop(self.data.get('crop_data'))
        if self.data.get('grayscale') == 1:
            self.grayscale()
        if self.data.get('sepia') == 1:
            self.sepia()
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
        self.temperature(self.data.get('temperature'))
        self.resize(self.data.get('resize'))
        if self.data.get('color_pop_bool') == 1:
            self.color_pop_color(self.data.get('color_pop_color'), self.data.get('color_pop_data'), self.data.get('color_pop_range'))
        if self.data.get('binarize') == 1:
            self.binarize()
        if self.img is not None:
            cv.imwrite(os.path.join(self.folder,os.listdir(self.folder)[1]), self.img) 
        