import cv2
from ultralytics import YOLO


import camera_ctrl
import camera_detect

# Load the exported NCNN model
ncnn_model = YOLO("best_ncnn_model")
picam2 = camera_ctrl.init_camera()

img_path = "./photo/"
filename = 'test_photo'

cnt = 0;
while True:
    if camera_ctrl.take_photo_code(filename+f'{cnt}',picam2):
        
        results = ncnn_model(img_path + filename + f'{cnt}.jpg')
        cnt+=1
        if not results[0].boxes:
            print("No objects detected.")
            continue
        else:
            x1, y1, x2, y2 = [int(coord) for coord in results[0].boxes.xyxy[0]]
            print(x1,y1,x2,y2)
            '''
            cv2.imshow("Camera",results[0].plot())
            if cv2.waitKey(1) == ord("q"):
                break
            '''
        
	
