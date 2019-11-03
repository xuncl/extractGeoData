# coding: utf-8

fileName = 'RxRec20191102_002.dat'


def add_file_to(the_file_name, file2):
    the_file = open(the_file_name, 'r')
    for the_line in the_file.readlines():
        file2.write(the_line)


def degree_to_float(d):
    nums = d.split('.')
    num1 = float(nums[0])
    num2 = float('0.'+nums[1])*100/60
    return str(num1+num2)


newName = 'extracted_' + fileName.replace('.dat', '.csv')
mapName = 'map_' + fileName.replace('.dat', '.kml')
mapWAName = 'mapWithAltitude_' + fileName.replace('.dat', '.kml')
newFile = open(newName, 'w')
oldFile = open(fileName, 'r')
mapFile = open(mapName, 'w')
mapWAFile = open(mapWAName, 'w')
add_file_to('header.out', mapFile)
add_file_to('header.out', mapWAFile)
mapWAFile.write('          ')
for line in oldFile.readlines():
    if '$GPGGA' in line:
        newFile.write(line)
        items = line.split(',')
        if items[2] and items[4]:
            latitude = degree_to_float(str(float(items[2])/100))
            longitude = degree_to_float(str(float(items[4])/100))
            mapFile.write(str(longitude)+','+str(latitude)+',0 ')

            if items[9]:
                mapWAFile.write(str(longitude)+','+str(latitude)+','+items[9]+' ')

add_file_to('footer.out', mapFile)
add_file_to('footer.out', mapWAFile)
newFile.close()
mapFile.close()
mapWAFile.close()
