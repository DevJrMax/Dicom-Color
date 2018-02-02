import dicom
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
from natsort import natsorted

fig = plt.figure()

dicoms = []

PathDicom = "./data2/"
lstFilesDCM = []
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():
            lstFilesDCM.append(os.path.join(dirName, filename))

lstFilesDCM = natsorted(lstFilesDCM)

print(lstFilesDCM)

for i in range(len(lstFilesDCM)):
    ds = dicom.read_file(lstFilesDCM[i])
    array = ds.pixel_array
    imgplot = plt.imshow(array)
    plt.hsv()
    dicoms.append([imgplot])



ani = animation.ArtistAnimation(fig, dicoms, interval=30, blit=True, repeat_delay=1000)

plt.show()