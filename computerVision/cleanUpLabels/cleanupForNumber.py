from os import listdir
from os.path import isfile, join

# Purpose of this class is to extract the Number labels from shared project, so players are not included anymore

folders = ["../../American-Football-Number/test/labels"
          ,"../../American-Football-Number/valid/labels",
           "../../American-Football-Number/train/labels"
           ]

for folder in folders:
    newFiles = []
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    for fileName in onlyfiles:
        newLines = []
        with open(file=folder+'/'+fileName, encoding='utf8') as f:
            for line in f:
                parts = line.split(" ")
                if parts[0] == "0" or parts[0] == "1" or parts[0] == "2" or parts[0] == "3" or parts[0] == "4":
                    newLines.append(line)
        f = open(folder+'/'+fileName, "r+")
        f.truncate(0)
        for newLine in newLines:
            f.write(newLine)
        with open(folder+'/'+fileName) as f_input:
            data = f_input.read().rstrip('\n')
        with open(folder+'/'+fileName, 'w') as f_output:
            f_output.write(data)
        f.close()
            # newFiles.append(newLines)
    # print(newFiles)



