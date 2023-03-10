import cv2
import turtle
import numpy as np
from matplotlib import pyplot as plt

def find_closest(p):
    if len(positions) > 0: 
        nodes = np.array(positions)
        distances = np.sum((nodes - p)**2, axis=1) 
        i_min = np.argmin(distances)
        return positions[i_min] 
    else:
        return None

def outline():
    src_image = cv2.imread(image,0)
    blurred = cv2.GaussianBlur(src_image, (7, 7), 0)
    th3 = cv2.adaptiveThreshold(blurred, maxValue = 255, adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType = cv2.THRESH_BINARY, blockSize = 9, C = 2)
    return th3
    
image = 'shiva.jpg'  
im = cv2.imread(image,0)
th3 = outline()

plt.imshow(th3)
plt.axis('off')
plt.tight_layout()
plt.show()
W = im.shape[1]
H = im.shape[0]
print(W,H)
CUTOFF_LEN = ((W+H)/2)/60 
iH, iW = np.where(th3 == [0])
iW = iW - W/2
iH = -1*(iH - H/2)
positions = [list(iwh) for iwh in zip(iW, iH)]

t = turtle.Turtle()
t.color("brown")
t.shapesize(1.4)
t.pencolor("gray70")

t.speed(0)

t.penup()
t.goto(positions[0])
t.pendown()

p = positions[0]
while (p):
    p = find_closest(p)
    if p:    
        current_pos = np.asarray(t.pos())
        new_pos = np.asarray(p)
        length = np.linalg.norm(new_pos - current_pos)
        if length < CUTOFF_LEN:
            t.goto(p)  
        else:
            t.penup()
            t.goto(p) 
            t.pendown()         
        positions.remove(p) 
    else:     
        p = None