# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import yaml
import ultralytics
from ultralytics import YOLO
def create_model():
    # Use a breakpoint in the code line below to debug your script.
    # 버전체크
    ultralytics.checks()

    model = YOLO('yolov8n.pt')

    # model.train_epochs10(data=os.getcwd()+"/datasets/data.yaml",epochs=100, project=save_path)
    model.train(data=os.getcwd() + "/datasets/data.yaml", epochs=100, project="./")

    model.export(format='onnx', dynamic=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_model()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
