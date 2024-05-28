import numpy as np
import scipy as sp
import cv2
import matplotlib.pyplot as plt


# image = cv2.imread("01/1 (10).jpg",0)
# gray_filtered = cv2.inRange(image, 165, 255)

def trim(image1, image2):
    nonzerofirst = np.nonzero(image1[:,1])
    mini = nonzerofirst[0][1]
    maxi = nonzerofirst[0][-1]
    cropped = np.zeros((maxi-mini+1, 2048))
    for i in range(mini, maxi+1):
        cropped[i-mini] = image2[i]
    return cropped

def trimadv(image, crackx, cracky):
    cropped = np.zeros((15, np.shape(image)[1]-crackx))
    for i in range(15):
        cropped[i] = image[cracky - 7 + i][crackx: np.shape(image)[1]]
    return cropped


#Must be applied after cropping the background!
def flip(image):
    zeroelelemtsleft = np.where(image[:,0] == 0)
    zeroelelemtsright = np.where(image[:, 2047] == 0)
    if abs(np.mean(zeroelelemtsright) - np.shape(image)[0]/2) < abs(np.mean(zeroelelemtsleft) - np.shape(image)[0]/2):
        image = np.flip(image, axis=1)
    return image

def emptyrow(image):
    x = np.zeros(np.shape(image)[0])
    firstinrow = np.zeros(np.shape(image)[0])
    for i in range(np.size(firstinrow)):
        x[i] = i
        if np.size(np.nonzero(image[i])[0]) != 0:
            firstinrow[i] = np.nonzero(image[i])[0][0]
        else:
            firstinrow[i] = 0
    return firstinrow, x

def crack(image):
    x, y = emptyrow(image)
    maxindex = np.argmax(x)
    crackpos = np.array([x[maxindex], y[maxindex]])
    return crackpos

def iterations(N, gray_filtered, gray_filtered1):
    crackx = np.zeros(N+1)
    cracky = 0
    crackstep = 0
    flipped1 = np.flip(gray_filtered1, axis=1)
    flipped = np.flip(gray_filtered, axis=1)
    #Use if no flipping is needed:
    # flipped = gray_filtered
    # flipped1 = gray_filtered1
    trimmed0 = trim(flipped,flipped1)
    trimmed = trim(flipped, flipped1)

    for i in range(N):
        crackx[i+1] = int(crack(trimmed)[0])
        cracky += int(crack(trimmed)[1])
        if i != 0 and int(crack(trimmed)[1]) != 0: cracky = cracky - 7
        if crackx[i+1] == 0:
            crackx[i+1], ynew = jump(trimmed0, int(sum(crackx)), cracky)
            if ynew != 0: cracky = cracky + ynew - 7
        trimmed = trimadv(trimmed0, int(sum(crackx)), cracky)
        # x, y = emptyrow(trimmed)
        # plt.plot(x, y)
        # plt.show()
    return np.sum(crackx), cracky

def jump(image, crackx, cracky):
    for i in range(1,10):
        crackxh = crackx + i
        trimmed = trimadv(image,crackxh, cracky)
        crackpos = crack(trimmed)
        if crackpos[0] != 0:
            return int(crackpos[0]), int(crackpos[1])
    return [0,0]

def crackdetection(image, gray_filtered, gray_filtered1):
    image = image
    gray_filtered = gray_filtered
    gray_filtered1 = gray_filtered1
    return int(iterations(50, gray_filtered, gray_filtered1)[0]), int(iterations(50, gray_filtered, gray_filtered1)[1])

workbook = xlsxwriter.Workbook('04_4.xlsx')
worksheet = workbook.add_worksheet()
row = 1
col = 1
for file in os.listdir('04'):
    # print(file)
    image = cv2.imread(f"04/{file}", 0)
    name = f"{file}"[3:-5]
    photo_number = int(name)
    gray_filtered = cv2.inRange(image, 185, 255)
    gray_filtered1 = cv2.inRange(image, 185, 255)
    it = crackdetection(image, gray_filtered, gray_filtered1)
    worksheet.write(row, col, photo_number)
    worksheet.write(row, col + 1, it[0])
    row += 1
    print(file, it[0])
    # plt.imshow(trim(np.flip(gray_filtered), np.flip(gray_filtered1)))
    # plt.plot(it[0], it[1], marker='o', color='red', markersize = '1')
    # plt.show()

workbook.close()