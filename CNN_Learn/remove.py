import os

dir_name = "/home/ash/Desktop/project/dataset/train_set_cat/"
test = os.listdir(dir_name)
i=0
for item in test:
    if item.endswith(".cat"):
        i+=1
        #print(os.path.join(dir_name, item))
        os.remove(os.path.join(dir_name, item))

print("Total"+" "+str(i)+" "+"Deleted Files ")
