import numpy as np
import inspect

def initializeOpts(varargin):
    '''
    initialize opts struct
    :param varargin:
    :return:
    '''
    dfs = {"pPyramid":{},
           "filters":[],
           "modelDs":np.array([100,41]),
           "pNms":{},
           "stride":4,
           "cascThr":-1,
           "cascCal":0.005,
           "nWeak":128,
           "pBoost":{},
           "seed":0,
           "name":" ",
           "posGtDir":" ",
           "posImgDir":" ",
           "negImgDir":" ",
           "posWinDir":" ",
           "negWinDir":" ",
           "imreaddp":{},
           "pLoad":{},
           "nPos":float("inf"),
           "nNeg":5000,
           "nPerNeg":25,
           "nAccNeg":10000,
           "pJitter":{},
           "winSave":0}
    opts = getPrmDflt(varargin,dfs,1)

def getPrmDflt(prm = None,dfs = None,checkExtra = None):
    #if (len(dfs) % 2 != 0):
        #raise Exception("odd number of default parameters")

    ###获取输入参数
    nargin = 0
    input_params = [prm,dfs,checkExtra]
    for param in input_params:
        if(param != None):
            nargin += 1
    if nargin <= 2:
        checkExtra = 0


    #######


getPrmDflt(1)
