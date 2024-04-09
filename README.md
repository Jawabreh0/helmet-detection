# Helmet Detection Algorithm

Helmet detection experiment, designed using YOLOv7 object detection model, with bicycle and motorbike helmets training data

## Dataset
The dataset used for training the model is not included in this repository. You can use your own dataset or download a helmet detection dataset from https://www.kaggle.com/datasets/andrewmvd/helmet-detection

## Setup
To set up the environment for running the algorithm, follow these steps:

1. Clone this repository: ```
git clone git@github.com:Jawabreh0/helmet-detection.git```

2. Navigate to the cloned repository: cd Helmet-Detection.

3. Download the YOLOv7 weights: wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt.

4. Download the YOLOv7x weights: wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt.

5. Install the required packages: pip install -r requirements.txt.

## Training
To train the algorithm, run the following command:

```python
python train.py --data data.yaml --cfg models/custom_yolov7.yaml --weights yolov7.pt
```

You can adjust the batch size, number of epochs, and other parameters by modifying the command above.

## Inference
To detect helmets in an image, run the following command:

```python
python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.4 --source path/to/image.jpg
```

This will output an image with bounding boxes around the detected helmets.

## Results
The trained model achieved an average precision of 0.85 on the test set.


## License
This project is licensed under the MIT License
