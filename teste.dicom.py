import dicom
import os
import numpy

numpy.set_printoptions(threshold=numpy.nan)

ds=dicom.read_file("./data/2.dcm")

print(ds)
