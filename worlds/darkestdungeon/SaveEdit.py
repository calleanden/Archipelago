import struct

filePath = "C:/Program Files (x86)/Steam/userdata/37721742/262060/remote/profile_0/"

def readFile(fileName):
    with open(filePath + fileName, mode="rb") as file:
        fileContent = file.read()
        r_heading = struct.unpack("iiiii", fileContent[:20])
        r_body = struct.unpack("i" * ((len(fileContent) - 24) // 4), fileContent[20:-4])
        r_footing = struct.unpack("i", fileContent[-4:])
        print(r_heading)
        print(r_body)
        print(r_footing)

readFile("persist.progression.json")