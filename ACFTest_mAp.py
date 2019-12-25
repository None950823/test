#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import  matlab

import matlab.engine as e
np.set_printoptions(suppress=True)
eng = e.start_matlab()
import os
import sys
#The model dimensions ('modelDs') define the window height and width（定义滑窗的大小）
#The padded dimensions ('modelDsPad') define the extended region around object candidates that are used for classification   填充尺寸（'modelDsPad'）定义了用于分类的对象候选周围的扩展区域,例如，对于100像素高的行人，通常使用128像素高的区域进行决策
#'pNms'控制非最大抑制（请参阅bbNms.m）
# 'stride' controls the window stride

#“ cascThr”和“ cascCal”是用于恒定软级联的阈值和校准,通常，将“ cascThr”设置为-1并调整“ cascCal”，直到达到所需的recall，setting 'cascCal' shifts the final scores output by the detector by the given amount
#指定训练数据的位置和数量：训练数据可以采用多种不同的形式。 可以使用预先裁剪的窗口的目录（'posWinDir'）或完整图像的目录（'posImgDir'）和地面真实标签（'posGtDir'）来指定正值。
#而'imreadp'是imreadf的自定义附加参数。
#从完整图像采样时，“ pLoad”确定如何加载ground truth并将其转换为一组positive bbs（请参见bbGt> bbLoad）。

#'nPos' controls the total number of positives to sample for training (if nPos=inf  the number of positives is limited by the training set).
#“ nNeg”控制要采样的负片总数，“ nPerNeg”限制每个图像的负片数量。
#“ nAccNeg”控制可以在bootstrapping的多个阶段累积的最大负数
#定义“ pJitter”以抖动阳性（请参见jitterImage.m），从而人为地增加阳性训练窗口的数量。
#'winsSave'是真的，裁剪后的窗口将作为mat文件保存到磁盘。
################################4024 pictures in test set##########################################
path = "D:/Paper/piotr_toolbox/toolbox/detector"
os.chdir(path)
print("当前路径为：",os.getcwd())

gt,dt = eng.acfDemoCal(nargout = 2)
print(len(gt))
lossCount = 0
hasMatched = []
notMatched = []
for i in range(len(gt)):
    has = False
    if(len(gt[i]) != 0):
        print("*"*100)
        print(gt[i])
        for j in range(len(dt[i])):
            if(dt[i][j][-1] == -1.0 or dt[i][j][-1] == 1.0):
                has = True
                hasMatched.append(j)
                print("匹配到的框")
                print(dt[i][j])

        if not has:
            print("没有匹配到的框")


    for v in range(len(dt[i])):
                if v in hasMatched:
                    continue
                else:
                    notMatched.append(dt[i][v])
            print(np.array(notMatched,np.float))

        if not has:
            lossCount += 1
print(lossCount)