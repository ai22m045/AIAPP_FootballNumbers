from roboflow import Roboflow
rf = Roboflow(api_key="u3VM1jMlTP08c5ogG5GZ")
project = rf.workspace("fh-technikum-wien-m15r2").project("american-football-player-detection")
dataset = project.version(3).download("yolov8")


rf = Roboflow(api_key="u3VM1jMlTP08c5ogG5GZ")
project = rf.workspace("fh-technikum-wien-m15r2").project("computer-vision-additional-dataset")
dataset = project.version(1).download("yolov8")