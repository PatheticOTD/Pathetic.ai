import numpy as np

def rgb2gray(rgb):
    c = rgb[...,:3]
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

class LBPtransform():


    def _get_pixel(self, center, x, y): 
        new_value = 0

        try: 
            if self.img[x][y] >= center: 
                new_value = 1

        except: 
            # срабатывает у границ
            pass
        
        return new_value 

    # калькулирует LBP пикселя
    def _lbp_calculate_pixel(self, x, y): 
        
        center = self.img[x][y] 
        val_ar = [] 
        val = 0
        
        val_ar.append(self._get_pixel( center, x-1, y-1))        #верхний левый 
        val_ar.append(self._get_pixel( center, x-1, y))          #верхний
        val_ar.append(self._get_pixel( center, x-1, y + 1))      #верхний правый
        val_ar.append(self._get_pixel( center, x, y + 1))        #справа
        val_ar.append(self._get_pixel( center, x + 1, y + 1))    #нижний правый
        val_ar.append(self._get_pixel( center, x + 1, y))        #нижний
        val_ar.append(self._get_pixel( center, x + 1, y-1))      #нижний правый
        val_ar.append(self._get_pixel( center, x, y-1))          #слева
        
        power_val = [1, 2, 4, 8, 16, 32, 64, 128] 

        for i in range(len(val_ar)): 
            val += val_ar[i] * power_val[i] 
        return val 
    
    def get(self, img):
        self.img = img
        height = self.img.shape[0]
        width = self.img.shape[1]
        
        lbp_img = np.zeros((height, width), np.uint8) 
        
        for i in range(height):
            for j in range(width):
                lbp_img[i,j] = self._lbp_calculate_pixel(i, j)
        
        return lbp_img
