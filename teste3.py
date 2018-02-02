import dicom
import numpy
import cv2


def convert(value, maximo):
    porcentagem = value/maximo
    normalizado = 65535*porcentagem
    return int(normalizado)

numpy.set_printoptions(threshold=numpy.nan)

ds=dicom.read_file("./data/2.dcm")

linhas = ds.Rows

colunas = ds.Columns

print(colunas)

print(linhas)

#print(ds)

array = ds.pixel_array

array2 = numpy.zeros((linhas,colunas), numpy.uint16)

maximo = max(array.flatten())

print(maximo)

for i in range(linhas):
    for j in range(colunas):
        array2[i][j] = int(convert(array[i][j],maximo))

#numpy.savetxt('testando', array, delimiter=',',fmt='%d')
print(array2)
cv2.imshow("eoq", array2)
cv2.waitKey(0)