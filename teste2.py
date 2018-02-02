import dicom
import numpy
import cv2

def bgr2hsv(B, G, R):
    array = [0,0,0]

    H = 0
    S = 0
    V = 0

    Cmax = max(R,G,B)
    Cmin = min(R,G,B)

    V = float(Cmax)/float(255)

    delta = Cmax - Cmin
    if Cmax == Cmin:
        H=0
    elif Cmax == G:
        H = (60 * ((float(B)-float(R))/float(delta)) + float(120))
    elif Cmax == B:
        H = (60 * ((float(R)-float(G))/float(delta)) + float(240))
    elif Cmax == R:
        H = (60 * ((float(G)-float(B))/float(delta)) + float(360))
    if(Cmax ==0):
        S = 0
    else:
        S = float(delta)/float(Cmax)

    array[0] = H
    array[1] = S
    array[2] = V

    return array


def convert(value, maximo):
    porcentagem = value/maximo
    normalizado = 255*porcentagem
    return int(normalizado)

numpy.set_printoptions(threshold=numpy.nan)

ds=dicom.read_file("./data/2.dcm")

linhas = ds.Rows

colunas = ds.Columns

print(colunas)

print(linhas)

#print(ds)

array = ds.pixel_array

array2 = numpy.zeros((linhas,colunas), numpy.uint8)

maximo = max(array.flatten())

print(maximo)

for i in range(linhas):
    for j in range(colunas):
        array2[i][j] = int(convert(array[i][j],maximo))

#numpy.savetxt('testando', array, delimiter=',',fmt='%d')


array3 = cv2.cvtColor(array2, cv2.COLOR_GRAY2BGR)

array4 = numpy.copy(array3)

array5 = numpy.copy(array3)

for i in range(linhas):
    for j in range(colunas):
        aux = bgr2hsv(array4[i][j][0], array4[i][j][1], array4[i][j][2])
        if(array4[i][j][0]>10 and array4[i][j][1]>10 and array4[i][j][2]>10):
            array4[i][j][0] = int(aux[0]/2)
            array4[i][j][1] = int(aux[1]*255)
            array4[i][j][2] = int(aux[2]*255)

        array5[i][j][0] = int((359 * (float(array4[i][j][2])/255)))
        array5[i][j][1] = int(255)
        array5[i][j][2] = int(255)


array6 = cv2.cvtColor(array5, cv2.COLOR_HSV2BGR_FULL)

cv2.imshow("eoq", array3)
cv2.imshow("eoq2", array4)
cv2.imshow("eoq3", array5)
cv2.imshow("eoq4", array6)

cv2.waitKey(0)