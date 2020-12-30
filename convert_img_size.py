import cv2
import os

type_of_img = '.jpg'
img_size = (320, 320)
file_path = '/Users/huangqiming/Desktop/Python/jetson-nano-fire-detection/fire/val/img/'
file_name = os.listdir(file_path)



if '.DS_Store' in file_name:
    file_name.remove('.DS_Store')

for i in range(len(file_name)):
    if file_name[i].endswith(type_of_img):
        img = cv2.imread(file_path + file_name[i])
        img = cv2.resize(img, (img_size[0], img_size[1]))
        cv2.imwrite(file_path + file_name[i], img)

print("successfully convert!")
