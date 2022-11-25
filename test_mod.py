from PIL import Image
import os
import cv2
import numpy as np
from detecto import core, utils, visualize


# assign directory

# iterate over files i
        # checking if it is a file
        #if os.path.isfile(f):
ilo =0 

for filename in os.listdir("D:\\Edhitha 2023\\new_seg\\totest"):

            f=os.path.join("D:\\Edhitha 2023\\new_seg\\totest",filename)
            image = utils.read_image(f)
            predictions =  core.Model.load('model_weights.pth', ['Target']).predict(image)
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
            ilo = ilo +1 
       


