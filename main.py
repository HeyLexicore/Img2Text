import cv2

im = cv2.imread("img.png")

im = cv2.resize(im,(100,100))

string = str(im.shape[0])+":"+str(im.shape[1])+":"
print(string)

for j in range(im.shape[0]):
    for k in range(im.shape[1]):
        #rgb = ((im[j,k,2])*256*256)+((im[j,k,1])*256)+im[k,j,0]
        rgb = ((im[k, j, 2]) * 256 * 256) + ((im[k, j, 1]) * 256) + im[k, j, 0]
        string += str(rgb)+":"

print(string[:-1]+"#")
open("texture.txt","w").write(string[:-1]+"#")

