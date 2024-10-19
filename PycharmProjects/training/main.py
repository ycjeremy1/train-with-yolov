from ultralytics import YOLO
model = YOLO("yolov8n.yaml")
# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="my_data2.yaml", epochs=3)

