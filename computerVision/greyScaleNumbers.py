from os import listdir
from os.path import isfile, join
from PIL import Image

folders = ["../American-Football-Number/train/images"
          #,"../American-Football-Player/valid/images",
           #"../American-Football-Player/train/images"
           ]

for folder in folders:
    onlyfiles = [f for f in listdir(folder) if join(folder, f)]
    for fileName in onlyfiles:
        newLines = []
        img = Image.open(folder+'/'+fileName).convert('L')
        img.save("../American-Football-Number-GS/train/images/"+fileName)