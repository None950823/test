import os
import datetime
def getfiles(dirs):
    return_ = {}
    #annotations_return = []
    #image_return = []
    print("making dirs list......")
    #start_time = datetime.datetime.now()
    if len(dirs) == 2:
        images_dir = dirs[0]
        annotations_dir = dirs[1]
        #all_annotations =[v.split(".")[0] for v in os.listdir(annotations_dir)]
        for image in os.listdir(images_dir):
            return_[images_dir + image] = annotations_dir + "/" +image.split(".")[0] + ".txt"
    #end_time = datetime.datetime.now()
    print("make dir list done......")
    return return_

