# YOLOv5 Object Detection

This repository contains a Python script for performing object detection using the YOLOv5 model on images containing cars, bicycles, buses, trucks, and motorbikes. The detected objects are highlighted with bounding boxes and labeled accordingly.

## Overview

The `detect_objects.py` script loads the pre-trained YOLOv5 model and performs object detection on images. It then displays the detection results using OpenCV.

## Usage

1. Clone this repository:
git clone https://github.com/your_username/yolov5-object-detection.git
cd yolov5-object-detection
2.Place your images containing objects you want to detect in the images directory.
3.Run the detect_objects.py script

This script also contains a function for detection that can be used for flask / fastapi / django based webapps.

##Pre-trained Models
This repository includes pre-trained YOLOv5 models of different sizes:

YOLOv5s (Small)
YOLOv5m (Medium)
YOLOv5l (Large)
YOLOv5x (Extra Large)
You can switch between these models by modifying the model initialization line in the detect_objects.py script according to your requirements: 
model = Model('yolov5s.pt', device='cpu')

##Requirements
Python 3.x
PyTorch
OpenCV
NumPy
Install the required dependencies using:
pip install -r requirements.txt

##Acknowledgments
YOLOv5: Ultralytics YOLOv5
COCO dataset: COCO
