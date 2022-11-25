
from PIL import Image
import os
import cv2
import numpy as np
from detecto import core, utils, visualize


# assign directory

# iterate over files i
        # checking if it is a file
        #if os.path.isfile(f):



'''ilo =0 
for filename in os.listdir("C:\\Users\\spoor\\Desktop"):

            f=os.path.join("C:\\Users\\spoor\\Desktop\\totest",filename)
            image = utils.read_image(f)
            predictions =  core.Model.load('model_weights.pth', ['human']).predict(image)
                #print(predictions)
            labels, boxes, scores = predictions
                #print(boxes)
                #show_labeled_image(image, boxes, labels)
            thresh=0.3
            filtered_indices=np.where(scores>thresh)
            filtered_scores=scores[filtered_indices]  
            filtered_boxes=boxes[filtered_indices]
            x = filtered_boxes.tolist()
            print(x)
            num_list = filtered_indices[0].tolist()
            filtered_labels = [labels[ilo] for ilo in num_list]
                #show_labeled_image(image, filtered_boxes, filtered_labels)
            img = Image.open(f)
                # print(x[0][0])
            area = (x[0][0], x[0][1], x[0][2], x[0][3])
            cropped_img = img.crop(area)
            cropped_img 
            cropped_img.save("D:\\Edhitha 2023\\new_seg\\results\\result_img{}.jpg".format(ilo))
            ilo = ilo +1 '''

image = utils.read_image('C:\\Users\\spoor\\Desktop\\cam_1_2_and_helf_mins_00000063.jpg')
model=core.Model.load("C:\\Users\\spoor\\Desktop\\model_weights.pth",["human"])
predictions = model.predict(image)
print(predictions)
labels, boxes, scores = predictions
print(boxes)
show_labeled_image(image, boxes, labels)
       
thresh=0.55
filtered_indices=np.where(scores>thresh)
filtered_scores=scores[filtered_indices]
filtered_boxes=boxes[filtered_indices]
x = filtered_boxes.tolist()
count = 0
while(len(x)!=0):
  print(x)
  print(x[0])
  num_list = filtered_indices[0].tolist()
  filtered_labels = [labels[i] for i in num_list]
  show_labeled_image(image, filtered_boxes, filtered_labels)
  break

# Given information
img = Image.open("C:\\Users\\spoor\\Desktop\\cam_1_2_and_helf_mins_00000063.jpg")
#width, height = 440, 190
#x, y = 100, 20
 
# Select area to crop
area = (x[0][0], x[0][1], x[0][2], x[0][3])
x_cp = (x[0][0] + x[0][2])/2
y_cp = (x[0][1] + x[0][3])/2
print(x_cp,",",y_cp)
 
# Crop, show, and save image
cropped_img = img.crop(area)
#img.show(cropped_img)
cropped_img.save("C:\\Users\\spoor\\Desktop\\out\\cropped_image.jpg")
im=image.open("C:\\Users\\spoor\\Desktop\\out\\cropped_image.jpg")
im.show()
