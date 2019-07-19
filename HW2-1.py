import urllib.request as req
import gzip, os, os.path
import numpy as np
import sys
import os
from array import array
import glob

from struct import *
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def download(url):
    savepath = "./mnist"


    files = [
        "train-images-idx3-ubyte.gz",
        "train-labels-idx1-ubyte.gz",
        "t10k-images-idx3-ubyte.gz",
        "t10k-labels-idx1-ubyte.gz"
]

    if not os.path.exists(savepath):
        os.mkdir(savepath)
    for f in files:
        url = baseurl + "/" + f
        loc = savepath + "/" + f
        print("download: ",url)
        if not os.path.exists(loc):
           req.urlretrieve(url,loc)

    for f in files:
        gz_file = savepath+'/'+f
        raw_file = savepath + "/" + f.replace(".gz","")
        print("gzip:",f)
        with gzip.open(gz_file,"rb") as fp:
            body = fp.read()
            with open(raw_file,"wb") as w:
                w.write(body)
    print("ok")

    directory = "C:/Users/한종훈/PycharmProjects/HW2/mnist/"
    for filename in os.listdir(directory):
        if filename.startswith("t10k"):
            path =os.path.join(directory, filename)
            target = os.path.join(directory, filename[:11]+"."+filename[12:])
            os.rename(path, target)
        if filename.startswith("train"):
            path = os.path.join(directory, filename)
            target = os.path.join(directory, filename[:12]+"."+filename[13:])
            os.rename(path, target)

    fp_image = open('./mnist/train-images.idx3-ubyte','rb')
    fp_label = open('./mnist/train-labels.idx1-ubyte','rb')

    img = np.zeros((28,28))
    lbl = [ [],[],[],[],[],[],[],[],[],[] ]
    d = 0
    l = 0
    index=0

    s = fp_image.read(16)
    l = fp_label.read(8)

    k=0
    while True:
        s = fp_image.read(784)
        l = fp_label.read(1)

        if not s:
            break;
        if not l:
            break;

        index = int(l[0])

        img = np.reshape( unpack(len(s)*'B',s), (28,28))
        lbl[index].append(img)
        k=k+1

    plt.imshow(img,cmap = cm.binary)
    plt.show()

    print("read done")

baseurl ="http://yann.lecun.com/exdb/mnist"
download(baseurl)