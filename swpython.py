import numpy as np
# Install Pillow and not PIL. PIL deprectated, but Pillow uses the same namespace
from PIL import ImageGrab
import cv2
from pymouse import PyMouse

def process_image(image):
    original_image = image
    # Grayscale
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Edge Detection
    processed_image =  cv2.Canny(image, threshold1 = 200, threshold2=300)
    return processed_image

def main() :
    while(True):
        # This grabs the window
        window = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
        new_screen = process_image(window)
        cv2.imshow('window', new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        
# main()

# PyMouse is to programmatically click things
mouse = PyMouse()
x_dim, y_dim = mouse.screen_size()
mouse.click(x_dim/2, y_dim/2, 1)
mouse.click(x_dim/2, y_dim/2, 1)