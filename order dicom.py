import dicom
import os

PathDicom = "./data/"
lstFilesDCM = []  # create an empty list
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
            lstFilesDCM.append(os.path.join(dirName, filename))


for i in range(len(lstFilesDCM)):
    ds = dicom.read_file(lstFilesDCM[i])
    ds.save_as("./data2/"+str(ds[0x20,0x13].value)+".dcm")