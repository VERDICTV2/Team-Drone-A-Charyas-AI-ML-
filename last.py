from PIL import Image
import os
import cv2
import numpy as np
from detecto import core, utils, visualize
from detecto.visualize import show_labeled_image
import torchvision   
import torch 
from torchvision import transforms
                               

cap = cv2.VideoCapture(1)
i=0
model=core.Model.load("C:\\Users\\spoor\\Desktop\\model_weights.pth",["human"])
global x,frame 

def objdet():
    while(True):
        ret, frame = cap.read()
        #frame = cv2.resize(frame,(0,0), fx = 0.5, fy = 0.5)
        if ret==False:
            break
        predictions= model.predict(frame)
        labels, boxes, scores = predictions
        thresh=0.26
        filtered_indices=np.where(scores>thresh)
        filtered_scores=scores[filtered_indices]  
        filtered_boxes=boxes[filtered_indices]
        x= filtered_boxes.tolist()
        num_list = filtered_indices[0].tolist()
        filtered_labels = [labels[ilo] for ilo in num_list]
        #show_labeled_image(frame, filtered_boxes, filtered_labels)
        box = tuple(x)
        print(x)
        try:
            #box = torch(box, dtype=torch.int)
            cv2.rectangle(frame, (int(x[0][0]),int(x[0][1])),(int(x[0][2]), int(x[0][3])), (0,255,0), 2)
            #cv2.putText(frame, "human", (x+2,y+h//8), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0,255,0), 1)
            #img = torchvision.transforms.ToPILImage()(img)
            #img.numpy()
            cv2.imshow('Label',frame)
            cropimg()
        except:
            print("nothing detected")

        if cv2.waitKey(1) & 0xFF == ord('a'):
            break

def cropimg():
    area = (x[0][0], x[0][1], x[0][2], x[0][3]) 
    cropped_img = frame.crop(area)
    frame.show(cropped_img)
    cropped_img.save("C:\Users\spoor\Desktop\cropped\img{i}.jpg".format(i))
    i+=1
    im=Image.open("C:\Users\spoor\Desktop\cropped\img{i}.jpg")
    im.show("C:\Users\spoor\Desktop\cropped\img{i}.jpg")

def centrep():
    x_cp = (x[0][0] + x[0][2])/2
    y_cp = (x[0][1] + x[0][3])/2
    print(x_cp,",",y_cp)
