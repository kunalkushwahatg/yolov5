import cv2
import torch
import numpy as np
import os 
'''
small = yolov5s
large = yolov5l
extralarge = yolov5x
'''
model = torch.hub.load('ultralytics/yolov5', 'yolov5x',verbose=False)
print("model loaded")
with open('coco.txt', 'r') as f:
    class_labels = f.read().strip().split('\n')


def predict(model,class_labels,img):
    labels_to_detect = ['car', 'bicycle', 'bus', 'truck','motorbike']
    total_counts = {label: 0 for label in labels_to_detect}
    results = model(img)
    for label in labels_to_detect:
        class_index = class_labels.index(label)
        for obj in results.pred[0]:
            if obj[-1] == class_index:
                total_counts[label] += 1
                bbox = obj[:4].cpu().numpy().astype(int)
                cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
                cv2.putText(img, label, (bbox[0], bbox[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return img , total_counts

for i in os.listdir("images"):
    image_path = 'images/'+i
    img = cv2.imread(image_path)
    img ,total_counts = predict(model,class_labels,img)

    for label, count in total_counts.items():
        print(f"Total {label}s: {count}")

    cv2.imshow('Detection Results', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

