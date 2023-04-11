from GUI import GUI
from HAL import HAL
import cv2


while True:
    img = HAL.getImage()
    GUI.showImage(img)
  
    HAL.setW(0.2)
    
    laser_data = HAL.getLaserData()
    print(laser_data)
    print("Laser len: " + str(len(laser_data)))
    
    bounding_boxes =  HAL.getBoundingBoxes(img)
  
    for bbox in bounding_boxes:
        name = bbox.class_id
        score = bbox.score
        xmin = bbox.xmin
        ymin = bbox.ymin
        xmax = bbox.xmax
        ymax = bbox.ymax
        
        if name == "person" and score > 0.3:
          color = (23, 230, 210)
          thickness = 2
          cv2.rectangle(img, (int(xmin), int(ymin)), (int(xmax), int(ymax)), color, thickness)
    
