import cv2
import numpy as np
dim=(1024,768)

left=cv2.imread(r"C:\Users\Siddhesh Patil\OneDrive\Desktop\left.jpg",cv2.IMREAD_COLOR)
left=cv2.resize(left, dim, interpolation = cv2.INTER_AREA)    #ReSize to (1024,768)

mid=cv2.imread(r"C:\Users\Siddhesh Patil\OneDrive\Desktop\mid.jpg",cv2.IMREAD_COLOR)
mid=cv2.resize(mid, dim, interpolation = cv2.INTER_AREA)  #ReSize to (1024,768)

right=cv2.imread(r"C:\Users\Siddhesh Patil\OneDrive\Desktop\right.jpg",cv2.IMREAD_COLOR)
right=cv2.resize(right, dim, interpolation = cv2.INTER_AREA)



images=[]
images.append(left)
images.append(mid)
images.append(right)


 # stitcher = cv2.createStitcher()

stitcher = cv2. Stitcher.create()
ret, pano = stitcher.stitch(images)

if ret==cv2.STITCHER_OK:
    cv2.imshow('Panorama', pano)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("Error during Stitching")