import cv2
from skimage.feature import hog
import numpy as np
from config import acf_conf
import math
import matlab
import matlab.engine
eng = matlab.engine.start_matlab()
'''
函数说明：获取原图像的相应十幅特征图
输入：原图像
输出：特征图像 [m*n*10]
'''
def FaceDetectionImage(RGBOriginalImage):

    #获取HSV特征
    HSVoriginalImag = cv2.cvtColor(RGBOriginalImage,cv2.COLOR_RGB2HSV)

    #先灰度化
    GRAYIMAGE = cv2.cvtColor(RGBOriginalImage, cv2.COLOR_RGB2GRAY)

    #获取梯度特征
    sobelx = cv2.Sobel(GRAYIMAGE, cv2.CV_64F, dx=1, dy=0)
    sobelx = cv2.convertScaleAbs(sobelx)
    sobely = cv2.Sobel(GRAYIMAGE, cv2.CV_64F, dx=0, dy=1)
    sobely = cv2.convertScaleAbs(sobely)
    SobelyFeature = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    ##计算HOG特征
    fd, hog_img_2 = hog(GRAYIMAGE, orientations=2, block_norm="L2-Hys", pixels_per_cell=(8, 8), cells_per_block=(8, 8),visualize=True)
    fd, hog_img_4 = hog(GRAYIMAGE, orientations=4, block_norm="L2-Hys", pixels_per_cell=(8, 8), cells_per_block=(8, 8),visualize=True)
    fd, hog_img_5 = hog(GRAYIMAGE, orientations=5, block_norm="L2-Hys", pixels_per_cell=(8, 8), cells_per_block=(8, 8),visualize=True)
    fd, hog_img_6 = hog(GRAYIMAGE, orientations=6, block_norm="L2-Hys", pixels_per_cell=(8, 8), cells_per_block=(8, 8),visualize=True)
    fd, hog_img_7 = hog(GRAYIMAGE, orientations=7, block_norm="L2-Hys", pixels_per_cell=(8, 8), cells_per_block=(8, 8),visualize=True)
    fd, hog_img_9 = hog(GRAYIMAGE, orientations=9, block_norm="L2-Hys", pixels_per_cell=(8, 8), cells_per_block=(8, 8),visualize=True)
    return HSVoriginalImag,SobelyFeature,hog_img_2,hog_img_4,hog_img_5,hog_img_6,hog_img_7,hog_img_9
    '''
    #初始化
    img = eng.imread(img_path)
    img_height,img_width = np.array(img).shape[0],np.array(img).shape[1]
    featureImag = np.zeros((img_height,img_width,10))

    #原始RGB图像
    RGBoriginalImag = eng.im2single(img)

    #RGB转HSV
    HSVoriginalImag = eng.rgb2hsv(RGBoriginalImag )
    featureImag[:,:,0] = np.array(HSVoriginalImag)[:,:,0]
    featureImag[:, :, 1] = np.array(HSVoriginalImag)[:, :, 1]
    featureImag[:, :, 2] = np.array(HSVoriginalImag)[:, :, 2]

    M,O = eng.gradientMag(RGBoriginalImag ,[], [], [], [],nargout=2)
    print(M)
    featureImag[:, :, 3] = np.array(M)

    #HOG特征
    M,O = eng.gradientMag(RGBoriginalImag,3,nargout=2)
    featureImag[:, :, 4:9] = np.array(eng.gradientHist(M,O,8,8))[:,:,0:5]
    print(featureImag.shape)
    return featureImag
    '''

def getDetectionVector(featureImg,ii,jj):
    '''

    :param featureImg:特征图：m*n*10
    :param ii:起始位置（ii,jj）
    :param jj:
    :return:特征图对应的特征向量
    '''
    hight,weidth = featureImg.shape
    #将特征图归一化为长宽均为20的倍数



def faceDectionTest(img,winSize,divideStep):
    #将图片归一化到合适的尺寸，是的滑窗大小为20 * 20
    #scale是归一尺度
    scale =  20 /winSize

    #图像归一化
    originalImage = cv2.resize(img,(np.array(img).shape[0] * scale,np.array(img).shape[1] * scale), cv2.INTER_NEAREST)
    #originalImage = cv2.resize(img, (np.array(img).shape[0] * scale, np.array(img).shape[1] * scale), cv2.INTER_LINEAR)

    detectionImage = FaceDetectionImage(originalImage)

    imgRow,imgCol = detectionImage.shape[0],detectionImage.shape[1]

    step = math.ceil(winSize / acf_conf.divideStep)








if __name__ == "__main__":
    img = cv2.imread("../square dataset frame/frames/2583.jpg")
    cv2.imshow("org", img)
    HSVoriginalImag, SobelyFeature, hog_img_2, hog_img_4, hog_img_5, hog_img_6, hog_img_7, hog_img_9 = FaceDetectionImage(img)

    cv2.imshow("hsv0", HSVoriginalImag[:, :, 0])
    cv2.imshow("hsv1", HSVoriginalImag[:, :, 1])
    cv2.imshow("hsv2", HSVoriginalImag[:, :, 2])
    #cv2.imshow("SobelyFeature", SobelyFeature)
    cv2.imshow("hog_img_2", hog_img_2)
    cv2.imshow("hog_img_4", hog_img_4)
    cv2.imshow("hog_img_5", hog_img_5)
    cv2.imshow("hog_img_6", hog_img_6)
    cv2.imshow("hog_img_7", hog_img_7)
    cv2.imshow("hog_img_9", hog_img_9)
    cv2.waitKey(0)
