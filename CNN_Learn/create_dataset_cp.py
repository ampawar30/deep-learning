# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from scipy import ndimage
from os import walk
images=np.array([])
labels=np.array([])
#从外存中读取图片
def readImg(roots = "",label = 1):
   #roots表示的是目录路径，可以直接将图片放在一个文件夹A，文件夹A与此模块在同一个目录下便可以直接访问到。
    print(roots)
    for (root, dirs, files) in walk(roots):
        print()
        images = [] #定义一下变量
        print(files)
        for image in files:
            fname = root + "/" +image
            #fname="/home/ash/Desktop/project/dataset/"  + root + "/"
            image = np.array(ndimage.imread(fname,flatten = False))
            image = scipy.misc.imresize(image,size=(64,64))
            images.append(image)
    try:
        images = np.array(images)
        labels = (np.zeros((1,images.shape[0]))+label)
        labels = labels.astype(int)
        #print(images,type(images))
    except:
        images=np.array([])
        labels=np.array([])
        pass


    return images,labels


#np.set_printoptions(threshold=np.nan) #nan是无穷大量意思，如果threshold阈值设定为某一整数，输出长度大于该数就会显示省略号问题
#print("images_test_cat: " + str(images_test_cat))
#print(images_test_cat.shape) #1张图（1个3为向量）长64 宽64 3个通道 （1,64,64,3）
#print(labels_test_cat)


#整合训练数据
images_train_cat,labels_train_cat=readImg("train_set_cat", label = 1)
images_train_nocat,labels_train_nocat=readImg("train_set_nocat",label = 0)

images = np.vstack((images_train_cat,images_train_nocat)) #纵向合并
labels = np.hstack((labels_train_cat,labels_train_nocat))#横向合并

#print(images) #1张图（1个3为向量）长64 宽64 3个通道 （1,64,64,3）
# print(images.shape)
# print(labels)

#整合测试数据
images_test_cat,labels_test_cat=readImg("test_set_cat", label = 1)
images_test_nocat,labels_test_nocat=readImg("test_set_nocat", label = 0)
test_images = np.vstack((images_test_cat,images_test_nocat)) #纵向合并
test_labels = np.hstack((labels_test_cat,labels_test_nocat))#横向合并
classes =['nocat','cat']
#print(test_images.shape)
#print(test_labels)

#写入数据库
def write_train_dataset(dbname,images,labels):
    try:
        f = h5py.File(dbname,"w")
        f.create_dataset("train_set_x",data = images) #第一个参数是数据集的名字
        f.create_dataset("train_set_y", data=labels)
    finally:
        f.close()




def write_test_dataset(dbname,images,labels,list):
    try:
        f = h5py.File(dbname,"w")
        f.create_dataset("test_set_x",data = images) #第一个参数是数据集的名字
        f.create_dataset("test_set_y", data=labels)
        f.create_dataset("list_classes",data=list)
    finally:
        f.close()


write_train_dataset('train_catvnoncat.h5',images,labels) #制作训练集
write_test_dataset('test_catvnoncat.h5',test_images,test_labels,classes)




#读取数据库
#def read_dataset(dbname,xName,yName):
#    try:
#        f = h5py.File(dbname,"r")
#        X = f[xName][:]
#        Y = f[yName][:]
#    finally:
#        f.close()
#    return X,Y

#########################第二部分，读取数据集模块#######
