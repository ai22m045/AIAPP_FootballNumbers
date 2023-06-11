from ultralytics import YOLO

model = YOLO("NOGS/train/weights/best.pt")
model.predict("test5.mp4", show=True, save=True, save_txt=True, show_labels=True)
