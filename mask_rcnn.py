import cv2
import numpy as np
from detecto import core

                               

cap = cv2.VideoCapture(0)

model=core.Model.load("/home/satz/model_weights.pth",["human"])
global x,frame 
global i 
i=0

def objdet():
    ret, frame = cap.read()
    #frame = cv2.resize(frame,(0,0), fx = 0.5, fy = 0.5)
    predictions= model.predict(frame)
    labels, boxes, scores = predictions
    thresh=0.20
    filtered_indices=np.where(scores>thresh)
    filtered_scores=scores[filtered_indices]  
    filtered_boxes=boxes[filtered_indices]
    x= filtered_boxes.tolist()
    num_list = filtered_indices[0].tolist()
    #filtered_labels = [labels[ilo] for ilo in num_list]
    #show_labeled_image(frame, filtered_boxes, filtered_labels)
    #box = tuple(x)
    #print(x)
    
    #box = torch(box, dtype=torch.int)
    try:
        cv2.rectangle(frame, (int(x[0][0]),int(x[0][1])),(int(x[0][2]), int(x[0][3])), (0,255,0), 2)
        #cv2.putText(frame, "human", (x+2,y+h//8), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0,255,0), 1)
        #img = torchvision.transforms.ToPILImage()(img)
        #img.numpy()
        cv2.imshow('Label',frame)
        print("So far so good")
        #cropimg()
        x_cp = (x[0][0] + x[0][2])/2
        y_cp = (x[0][1] + x[0][3])/2
        center_tup = (x_cp, y_cp)
        #area = (x[0][0], x[0][1], x[0][2], x[0][3]) 
        '''cropped_img = frame[int(x[0][0]):int(x[0][2]), int(x[0][1]):int(x[0][3])]
        cv2.imshow('Cropped', cropped_img)
        cv2.imwrite("C:\\Users\\Nihal J\\Desktop\\cropped\\img{i}.jpg".format(i))'''
        #i += 1
        return(center_tup)

    except:
        print("Nothing foundd")
        return (-1,-1)
        

        







