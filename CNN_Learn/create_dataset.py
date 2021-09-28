import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from scipy import ndimage
from os import walk
def readImg(roots = "",label = 1):
    print(roots)
    for (root, dirs, files) in walk(roots):
        print()
        images = []
        print(files)
        for image in files:
            fname = root + "/" +image
            #fname="/home/ash/Desktop/project/dataset/"  + root + "/"
            image = np.array(ndimage.imread(fname,flatten = False))
            image = scipy.misc.imresize(image,size=(64,64))
            images.append(image)
        images = np.array(images)
        labels = (np.zeros((1,images.shape[0]))+label)
        #labels = (np.zeros((33,)+label)
        labels = labels.astype(int)
        #print(images,type(images))

    return images,labels


#np.set_printoptions(threshold=np.nan)
#print("images_test_cat: " + str(images_test_cat))
#print(images_test_cat.shape)
#print(labels_test_cat)


images_train_cat,labels_train_cat=readImg("train_set_cat", label = 1)
images_train_nocat,labels_train_nocat=readImg("train_set_nocat",label = 0)

images = np.vstack((images_train_cat,images_train_nocat))
labels = np.hstack((labels_train_cat,labels_train_nocat))

#print(images)
# print(images.shape)
# print(labels)


'''images_test_cat,labels_test_cat=readImg("test_set_cat", label = 1)
images_test_nocat,labels_test_nocat=readImg("test_set_nocat", label = 0)
test_images = np.vstack((images_test_cat,images_test_nocat)) #纵向合并
test_labels = np.hstack((labels_test_cat,labels_test_nocat))#横向合并
classes =['nocat','cat']
'''#print(test_images.shape)
#print(test_labels)

#写入数据库
def write_train_dataset(dbname,images,labels):
    try:
        f = h5py.File(dbname,"w")
        f.create_dataset("train_set_x",data = images)
        f.create_dataset("train_set_y", data=labels)
    finally:
        f.close()




def write_test_dataset(dbname,images,labels,list):
    try:
        f = h5py.File(dbname,"w")
        f.create_dataset("test_set_x",data = images)
        f.create_dataset("test_set_y", data=labels)
        f.create_dataset("list_classes",data=list)
    finally:
        f.close()


write_train_dataset('train_catvnoncat.h5',images,labels)
#write_test_dataset('test_catvnoncat.h5',test_images,test_labels,classes)





#def read_dataset(dbname,xName,yName):
#    try:
#        f = h5py.File(dbname,"r")
#        X = f[xName][:]
#        Y = f[yName][:]
#    finally:
#        f.close()
#    return X,Y

##############################
