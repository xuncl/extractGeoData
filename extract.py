# coding: utf-8

fileName = 'RxRec20191102_002.dat'

newName = 'extracted_' + fileName.replace('.dat', '.csv')
mapName = 'map_' + fileName.replace('.dat', '.txt')
mapWAName = 'mapWithAltitude_' + fileName.replace('.dat', '.txt')
newFile = open(newName, 'w')
oldFile = open(fileName, 'r')
mapFile = open(mapName, 'w')
mapWAFile = open(mapWAName, 'w')
for line in oldFile.readlines():
    if '$GPGGA' in line:
        newFile.write(line)
        items = line.split(',')
        if items[2] and items[4]:
            mapFile.write(items[2]+','+items[4]+'\n')
            if items[9]:
                mapWAFile.write(items[2]+','+items[4]+','+items[9]+'\n')

newFile.close()
mapFile.close()
mapWAFile.close()
