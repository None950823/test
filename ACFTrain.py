import sys
sys.path.append("../bbGt")
from bbGt import getFiles
from ACF import InitializeOpts
from config import acf_conf
import numpy as np
import time
import datetime
import os
import cv2

opts = acf_conf.get_trainParams()


is_training = 1  # 1:traing 0:test

def train_adaboost(opts):
    detector = {"opts":opts,"clf":[],"info":[]}
    for stage in range(len(opts["nWeak"])):
        print("="* 200)
        print("=" *50 + "》》》" + "Training stage {}".format(stage + 1))
        startTime = datetime.datetime.now()

        if(stage == 1):
            pass
def sampleWins(detector,stage,positive):
    opts = detector["opts"]
    startTime = datetime.datetime.now()

    if(positive == 1):#对正样本进行采样
        n = opts["nPos"]
    else:
        n = opts["nNeg"]

    if(positive == 1):
        crDir = opts["posWinDir"]
    else:
        crDir = opts["negWinDir"]

    if(os.path.exists(crDir) and stage == 0):
        ##如果已经保存了采样
        raise  Exception("还没实现！")

    else:###如果没保存下来
        hasGt = positive or len(opts["negImgDir"])
        fs = [opts["negImgDir"]]
        if(hasGt):
            fs = [opts["posImgDir"],opts["posGtDir"]]

        ##取每张图片和标签的地址
        trainData_dict = getFiles.getfiles(fs)

        num_of_images = len(trainData_dict)
        #print(num_of_images)
        #print(num_of_annotations)
        #assert num_of_images == num_of_annotations and num_of_images > 0 and num_of_annotations > 0,Exception("输入图片的地址不正确，个数不符合！")

        print("="*50 + "Sampling Windows......")
        i = 0
        for image_dir in trainData_dict.keys():
            i += 1

            I = cv2.imread(image_dir.replace("\\","/"))








detector = {"opts":opts,"clf":[],"info":[]}
train_adaboost(opts)
sampleWins(detector,0,1)