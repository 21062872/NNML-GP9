# -*- coding: utf-8 -*-
"""MLAss.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zUy1NkqL6wrJmbsQQJuoSp_8iBSOUCTo
"""

# Commented out IPython magic to ensure Python compatibility.


# Machine Learning Assignment
# Group Submission
# Group 9
     

# mounting google drive
import pandas as pd
import os
from google.colab import drive
drive.mount('/content/drive')

os.environ['MLDS'] ='/content/drive/MyDrive/MLNN DS'

# upload Group_Project_Data 2.zip 
# %cd /content/drive/MyDrive/MLNN DS
     
Mounted at /content/drive
/content/drive/MyDrive/MLNN DS

# unzip input file 
# This will execute only the first time
!unzip \*.zip && rm *.zip
     
Archive:  Group_Project_Data 2.zip
replace __MACOSX/._Group_Project_Data? [y]es, [n]o, [A]ll, [N]one, [r]ename: 

#view a sample image
import cv2
from google.colab.patches import cv2_imshow
img = "/content/drive/MyDrive/MLNN DS/Group_Project_Data/Train/Real/img_1.png"
image = cv2.imread(img)
cv2_imshow(image)
     


import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

image_size = 224
labels = ('Real', 'Fake')
def get_data(data_dir):
    data = []
    for label in labels:
        path = os.path.join(data_dir, label)
        class_num = labels.index(label)
        for img in os.listdir(path):
            try:
                img_arr = cv2.imread(os.path.join(path, img))[..., ::-1]
                resized_arr = cv2.resize(img_arr, (image_size, image_size))
                data.append([resized_arr, class_num])
            except Exception as e:
                print(e)

    return np.array(data, dtype='object')
     

import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf

train = tf.keras.utils.image_dataset_from_directory("/content/drive/MyDrive/MLNN DS/Group_Project_Data/Train/")
valid = tf.keras.utils.image_dataset_from_directory("/content/drive/MyDrive/MLNN DS/Group_Project_Data/Valid/")
     
Found 6000 files belonging to 2 classes.
Found 2000 files belonging to 2 classes.

train_iterator = train.as_numpy_iterator()
     

valid_iterator = valid.as_numpy_iterator()
     

train_batch = train_iterator.next()
     

valid_batch = valid_iterator.next()
     

fig, ax = plt.subplots(ncols=10, figsize=(20,20))
for idx, img in enumerate(train_batch[0][10:20]):
    ax[idx].imshow(img.astype(int))
    ax[idx].title.set_text(train_batch[1][idx])
     


fig, ax = plt.subplots(ncols=10, figsize=(20,20))
for idx, img in enumerate(valid_batch[0][10:20]):
    ax[idx].imshow(img.astype(int))
    ax[idx].title.set_text(valid_batch[1][idx])
     


# Class 0 = Fake images
# Class 1 = Real images


     

train = train.map(lambda x,y: (x/255, y))
valid = valid.map(lambda x,y: (x/255, y))
     

train.as_numpy_iterator().next()
     
(array([[[[0.06666667, 0.06666667, 0.06666667],
          [0.06666667, 0.06666667, 0.06666667],
          [0.06715687, 0.06715687, 0.06715687],
          ...,
          [0.0627451 , 0.0627451 , 0.0627451 ],
          [0.0627451 , 0.0627451 , 0.0627451 ],
          [0.0627451 , 0.0627451 , 0.0627451 ]],
 
         [[0.06666667, 0.06666667, 0.06666667],
          [0.06666667, 0.06666667, 0.06666667],
          [0.06715687, 0.06715687, 0.06715687],
          ...,
          [0.0627451 , 0.0627451 , 0.0627451 ],
          [0.0627451 , 0.0627451 , 0.0627451 ],
          [0.0627451 , 0.0627451 , 0.0627451 ]],
 
         [[0.06911765, 0.06911765, 0.06911765],
          [0.06911765, 0.06911765, 0.06911765],
          [0.0692402 , 0.0692402 , 0.0692402 ],
          ...,
          [0.06194853, 0.06194853, 0.06194853],
          [0.06176471, 0.06176471, 0.06176471],
          [0.06176471, 0.06176471, 0.06176471]],
 
         ...,
 
         [[0.0877451 , 0.0877451 , 0.0877451 ],
          [0.0877451 , 0.0877451 , 0.0877451 ],
          [0.08547794, 0.08547794, 0.08547794],
          ...,
          [0.04589461, 0.04589461, 0.04589461],
          [0.04607843, 0.04607843, 0.04607843],
          [0.04607843, 0.04607843, 0.04607843]],
 
         [[0.09019608, 0.09019608, 0.09019608],
          [0.09019608, 0.09019608, 0.09019608],
          [0.0877451 , 0.0877451 , 0.0877451 ],
          ...,
          [0.04313726, 0.04313726, 0.04313726],
          [0.04313726, 0.04313726, 0.04313726],
          [0.04313726, 0.04313726, 0.04313726]],
 
         [[0.09019608, 0.09019608, 0.09019608],
          [0.09019608, 0.09019608, 0.09019608],
          [0.0877451 , 0.0877451 , 0.0877451 ],
          ...,
          [0.04313726, 0.04313726, 0.04313726],
          [0.04313726, 0.04313726, 0.04313726],
          [0.04313726, 0.04313726, 0.04313726]]],
 
 
        [[[0.01960784, 0.01960784, 0.01960784],
          [0.01960784, 0.01960784, 0.01960784],
          [0.02009804, 0.02009804, 0.02009804],
          ...,
          [0.00735294, 0.00735294, 0.00735294],
          [0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314]],
 
         [[0.01960784, 0.01960784, 0.01960784],
          [0.01960784, 0.01960784, 0.01960784],
          [0.02009804, 0.02009804, 0.02009804],
          ...,
          [0.00735294, 0.00735294, 0.00735294],
          [0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314]],
 
         [[0.02058824, 0.02058824, 0.02058824],
          [0.02058824, 0.02058824, 0.02058824],
          [0.02089461, 0.02089461, 0.02089461],
          ...,
          [0.00796569, 0.00796569, 0.00796569],
          [0.00833333, 0.00833333, 0.00833333],
          [0.00833333, 0.00833333, 0.00833333]],
 
         ...,
 
         [[0.01029412, 0.01029412, 0.01029412],
          [0.01029412, 0.01029412, 0.01029412],
          [0.00949755, 0.00949755, 0.00949755],
          ...,
          [0.00618873, 0.00618873, 0.00618873],
          [0.00539216, 0.00539216, 0.00539216],
          [0.00539216, 0.00539216, 0.00539216]],
 
         [[0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          [0.00735294, 0.00735294, 0.00735294],
          ...,
          [0.00490196, 0.00490196, 0.00490196],
          [0.00392157, 0.00392157, 0.00392157],
          [0.00392157, 0.00392157, 0.00392157]],
 
         [[0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          [0.00735294, 0.00735294, 0.00735294],
          ...,
          [0.00490196, 0.00490196, 0.00490196],
          [0.00392157, 0.00392157, 0.00392157],
          [0.00392157, 0.00392157, 0.00392157]]],
 
 
        [[[0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          ...,
          [0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        ]],
 
         [[0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          ...,
          [0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        ]],
 
         [[0.00735294, 0.00735294, 0.00735294],
          [0.00735294, 0.00735294, 0.00735294],
          [0.00735294, 0.00735294, 0.00735294],
          ...,
          [0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        ]],
 
         ...,
 
         [[0.00343137, 0.00343137, 0.00343137],
          [0.00343137, 0.00343137, 0.00343137],
          [0.00661765, 0.00661765, 0.00661765],
          ...,
          [0.0278799 , 0.0278799 , 0.0278799 ],
          [0.02794118, 0.02794118, 0.02794118],
          [0.02794118, 0.02794118, 0.02794118]],
 
         [[0.00392157, 0.00392157, 0.00392157],
          [0.00392157, 0.00392157, 0.00392157],
          [0.00735294, 0.00735294, 0.00735294],
          ...,
          [0.02745098, 0.02745098, 0.02745098],
          [0.02745098, 0.02745098, 0.02745098],
          [0.02745098, 0.02745098, 0.02745098]],
 
         [[0.00392157, 0.00392157, 0.00392157],
          [0.00392157, 0.00392157, 0.00392157],
          [0.00735294, 0.00735294, 0.00735294],
          ...,
          [0.02745098, 0.02745098, 0.02745098],
          [0.02745098, 0.02745098, 0.02745098],
          [0.02745098, 0.02745098, 0.02745098]]],
 
 
        ...,
 
 
        [[[0.01960784, 0.01960784, 0.01960784],
          [0.01960784, 0.01960784, 0.01960784],
          [0.01911765, 0.01911765, 0.01911765],
          ...,
          [0.02303922, 0.02303922, 0.02303922],
          [0.02352941, 0.02352941, 0.02352941],
          [0.02352941, 0.02352941, 0.02352941]],
 
         [[0.01960784, 0.01960784, 0.01960784],
          [0.01960784, 0.01960784, 0.01960784],
          [0.01911765, 0.01911765, 0.01911765],
          ...,
          [0.02303922, 0.02303922, 0.02303922],
          [0.02352941, 0.02352941, 0.02352941],
          [0.02352941, 0.02352941, 0.02352941]],
 
         [[0.01911765, 0.01911765, 0.01911765],
          [0.01911765, 0.01911765, 0.01911765],
          [0.01868873, 0.01868873, 0.01868873],
          ...,
          [0.02254902, 0.02254902, 0.02254902],
          [0.02303922, 0.02303922, 0.02303922],
          [0.02303922, 0.02303922, 0.02303922]],
 
         ...,
 
         [[0.0504902 , 0.0504902 , 0.0504902 ],
          [0.0504902 , 0.0504902 , 0.0504902 ],
          [0.05      , 0.05      , 0.05      ],
          ...,
          [0.01960784, 0.01960784, 0.01960784],
          [0.01960784, 0.01960784, 0.01960784],
          [0.01960784, 0.01960784, 0.01960784]],
 
         [[0.05098039, 0.05098039, 0.05098039],
          [0.05098039, 0.05098039, 0.05098039],
          [0.0504902 , 0.0504902 , 0.0504902 ],
          ...,
          [0.01960784, 0.01960784, 0.01960784],
          [0.01960784, 0.01960784, 0.01960784],
          [0.01960784, 0.01960784, 0.01960784]],
 
         [[0.05098039, 0.05098039, 0.05098039],
          [0.05098039, 0.05098039, 0.05098039],
          [0.0504902 , 0.0504902 , 0.0504902 ],
          ...,
          [0.01960784, 0.01960784, 0.01960784],
          [0.01960784, 0.01960784, 0.01960784],
          [0.01960784, 0.01960784, 0.01960784]]],
 
 
        [[[0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          ...,
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471]],
 
         [[0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          ...,
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471]],
 
         [[0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          ...,
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471]],
 
         ...,
 
         [[0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01133578, 0.01133578, 0.01133578],
          ...,
          [0.0122549 , 0.0122549 , 0.0122549 ],
          [0.0122549 , 0.0122549 , 0.0122549 ],
          [0.0122549 , 0.0122549 , 0.0122549 ]],
 
         [[0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01127451, 0.01127451, 0.01127451],
          ...,
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471]],
 
         [[0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01127451, 0.01127451, 0.01127451],
          ...,
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471]]],
 
 
        [[[0.03529412, 0.03529412, 0.03529412],
          [0.03529412, 0.03529412, 0.03529412],
          [0.03431373, 0.03431373, 0.03431373],
          ...,
          [0.0495098 , 0.0495098 , 0.0495098 ],
          [0.04705882, 0.04705882, 0.04705882],
          [0.04705882, 0.04705882, 0.04705882]],
 
         [[0.03529412, 0.03529412, 0.03529412],
          [0.03529412, 0.03529412, 0.03529412],
          [0.03431373, 0.03431373, 0.03431373],
          ...,
          [0.0495098 , 0.0495098 , 0.0495098 ],
          [0.04705882, 0.04705882, 0.04705882],
          [0.04705882, 0.04705882, 0.04705882]],
 
         [[0.03529412, 0.03529412, 0.03529412],
          [0.03529412, 0.03529412, 0.03529412],
          [0.03425245, 0.03425245, 0.03425245],
          ...,
          [0.04803922, 0.04803922, 0.04803922],
          [0.04558824, 0.04558824, 0.04558824],
          [0.04558824, 0.04558824, 0.04558824]],
 
         ...,
 
         [[0.00735294, 0.00735294, 0.00735294],
          [0.00735294, 0.00735294, 0.00735294],
          [0.00827206, 0.00827206, 0.00827206],
          ...,
          [0.01397059, 0.01397059, 0.01397059],
          [0.01568628, 0.01568628, 0.01568628],
          [0.01568628, 0.01568628, 0.01568628]],
 
         [[0.00392157, 0.00392157, 0.00392157],
          [0.00392157, 0.00392157, 0.00392157],
          [0.00490196, 0.00490196, 0.00490196],
          ...,
          [0.01029412, 0.01029412, 0.01029412],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471]],
 
         [[0.00392157, 0.00392157, 0.00392157],
          [0.00392157, 0.00392157, 0.00392157],
          [0.00490196, 0.00490196, 0.00490196],
          ...,
          [0.01029412, 0.01029412, 0.01029412],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471]]]], dtype=float32),
 array([1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1,
        1, 1, 0, 0, 0, 0, 1, 0, 0, 1], dtype=int32))

valid.as_numpy_iterator().next()
     
(array([[[[0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471],
          ...,
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471]],
 
         [[0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471],
          ...,
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471]],
 
         [[0.01127451, 0.01127451, 0.01127451],
          [0.01127451, 0.01127451, 0.01127451],
          [0.01127451, 0.01127451, 0.01127451],
          ...,
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471]],
 
         ...,
 
         [[0.01568628, 0.01568628, 0.01568628],
          [0.01568628, 0.01568628, 0.01568628],
          [0.01519608, 0.01519608, 0.01519608],
          ...,
          [0.01176471, 0.01176471, 0.01176471],
          [0.0122549 , 0.0122549 , 0.0122549 ],
          [0.0122549 , 0.0122549 , 0.0122549 ]],
 
         [[0.01568628, 0.01568628, 0.01568628],
          [0.01568628, 0.01568628, 0.01568628],
          [0.01519608, 0.01519608, 0.01519608],
          ...,
          [0.01127451, 0.01127451, 0.01127451],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471]],
 
         [[0.01568628, 0.01568628, 0.01568628],
          [0.01568628, 0.01568628, 0.01568628],
          [0.01519608, 0.01519608, 0.01519608],
          ...,
          [0.01127451, 0.01127451, 0.01127451],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471]]],
 
 
        [[[0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          ...,
          [0.03480392, 0.03480392, 0.03480392],
          [0.03529412, 0.03529412, 0.03529412],
          [0.03529412, 0.03529412, 0.03529412]],
 
         [[0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          ...,
          [0.03480392, 0.03480392, 0.03480392],
          [0.03529412, 0.03529412, 0.03529412],
          [0.03529412, 0.03529412, 0.03529412]],
 
         [[0.00882353, 0.00882353, 0.00882353],
          [0.00882353, 0.00882353, 0.00882353],
          [0.00894608, 0.00894608, 0.00894608],
          ...,
          [0.03351716, 0.03351716, 0.03351716],
          [0.03382353, 0.03382353, 0.03382353],
          [0.03382353, 0.03382353, 0.03382353]],
 
         ...,
 
         [[0.03480392, 0.03480392, 0.03480392],
          [0.03480392, 0.03480392, 0.03480392],
          [0.03425245, 0.03425245, 0.03425245],
          ...,
          [0.03400735, 0.03400735, 0.03400735],
          [0.03137255, 0.03137255, 0.03137255],
          [0.03137255, 0.03137255, 0.03137255]],
 
         [[0.03529412, 0.03529412, 0.03529412],
          [0.03529412, 0.03529412, 0.03529412],
          [0.03480392, 0.03480392, 0.03480392],
          ...,
          [0.03382353, 0.03382353, 0.03382353],
          [0.03137255, 0.03137255, 0.03137255],
          [0.03137255, 0.03137255, 0.03137255]],
 
         [[0.03529412, 0.03529412, 0.03529412],
          [0.03529412, 0.03529412, 0.03529412],
          [0.03480392, 0.03480392, 0.03480392],
          ...,
          [0.03382353, 0.03382353, 0.03382353],
          [0.03137255, 0.03137255, 0.03137255],
          [0.03137255, 0.03137255, 0.03137255]]],
 
 
        [[[0.02352941, 0.02352941, 0.02352941],
          [0.02352941, 0.02352941, 0.02352941],
          [0.02352941, 0.02352941, 0.02352941],
          ...,
          [0.01960784, 0.01960784, 0.01960784],
          [0.01960784, 0.01960784, 0.01960784],
          [0.01960784, 0.01960784, 0.01960784]],
 
         [[0.02352941, 0.02352941, 0.02352941],
          [0.02352941, 0.02352941, 0.02352941],
          [0.02352941, 0.02352941, 0.02352941],
          ...,
          [0.01960784, 0.01960784, 0.01960784],
          [0.01960784, 0.01960784, 0.01960784],
          [0.01960784, 0.01960784, 0.01960784]],
 
         [[0.02352941, 0.02352941, 0.02352941],
          [0.02352941, 0.02352941, 0.02352941],
          [0.02352941, 0.02352941, 0.02352941],
          ...,
          [0.01954657, 0.01954657, 0.01954657],
          [0.01960784, 0.01960784, 0.01960784],
          [0.01960784, 0.01960784, 0.01960784]],
 
         ...,
 
         [[0.04607843, 0.04607843, 0.04607843],
          [0.04607843, 0.04607843, 0.04607843],
          [0.04607843, 0.04607843, 0.04607843],
          ...,
          [0.02395833, 0.02395833, 0.02395833],
          [0.02401961, 0.02401961, 0.02401961],
          [0.02401961, 0.02401961, 0.02401961]],
 
         [[0.04705882, 0.04705882, 0.04705882],
          [0.04705882, 0.04705882, 0.04705882],
          [0.04705882, 0.04705882, 0.04705882],
          ...,
          [0.02352941, 0.02352941, 0.02352941],
          [0.02352941, 0.02352941, 0.02352941],
          [0.02352941, 0.02352941, 0.02352941]],
 
         [[0.04705882, 0.04705882, 0.04705882],
          [0.04705882, 0.04705882, 0.04705882],
          [0.04705882, 0.04705882, 0.04705882],
          ...,
          [0.02352941, 0.02352941, 0.02352941],
          [0.02352941, 0.02352941, 0.02352941],
          [0.02352941, 0.02352941, 0.02352941]]],
 
 
        ...,
 
 
        [[[0.02352941, 0.02352941, 0.02352941],
          [0.02352941, 0.02352941, 0.02352941],
          [0.02352941, 0.02352941, 0.02352941],
          ...,
          [0.01568628, 0.01568628, 0.01568628],
          [0.01568628, 0.01568628, 0.01568628],
          [0.01568628, 0.01568628, 0.01568628]],
 
         [[0.02352941, 0.02352941, 0.02352941],
          [0.02352941, 0.02352941, 0.02352941],
          [0.02352941, 0.02352941, 0.02352941],
          ...,
          [0.01568628, 0.01568628, 0.01568628],
          [0.01568628, 0.01568628, 0.01568628],
          [0.01568628, 0.01568628, 0.01568628]],
 
         [[0.02303922, 0.02303922, 0.02303922],
          [0.02303922, 0.02303922, 0.02303922],
          [0.02297794, 0.02297794, 0.02297794],
          ...,
          [0.01519608, 0.01519608, 0.01519608],
          [0.01519608, 0.01519608, 0.01519608],
          [0.01519608, 0.01519608, 0.01519608]],
 
         ...,
 
         [[0.01519608, 0.01519608, 0.01519608],
          [0.01519608, 0.01519608, 0.01519608],
          [0.01476716, 0.01476716, 0.01476716],
          ...,
          [0.01525735, 0.01525735, 0.01525735],
          [0.01568628, 0.01568628, 0.01568628],
          [0.01568628, 0.01568628, 0.01568628]],
 
         [[0.01568628, 0.01568628, 0.01568628],
          [0.01568628, 0.01568628, 0.01568628],
          [0.01519608, 0.01519608, 0.01519608],
          ...,
          [0.01519608, 0.01519608, 0.01519608],
          [0.01568628, 0.01568628, 0.01568628],
          [0.01568628, 0.01568628, 0.01568628]],
 
         [[0.01568628, 0.01568628, 0.01568628],
          [0.01568628, 0.01568628, 0.01568628],
          [0.01519608, 0.01519608, 0.01519608],
          ...,
          [0.01519608, 0.01519608, 0.01519608],
          [0.01568628, 0.01568628, 0.01568628],
          [0.01568628, 0.01568628, 0.01568628]]],
 
 
        [[[0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          [0.01127451, 0.01127451, 0.01127451],
          ...,
          [0.02598039, 0.02598039, 0.02598039],
          [0.02745098, 0.02745098, 0.02745098],
          [0.02745098, 0.02745098, 0.02745098]],
 
         [[0.00784314, 0.00784314, 0.00784314],
          [0.00784314, 0.00784314, 0.00784314],
          [0.01127451, 0.01127451, 0.01127451],
          ...,
          [0.02598039, 0.02598039, 0.02598039],
          [0.02745098, 0.02745098, 0.02745098],
          [0.02745098, 0.02745098, 0.02745098]],
 
         [[0.00735294, 0.00735294, 0.00735294],
          [0.00735294, 0.00735294, 0.00735294],
          [0.01047794, 0.01047794, 0.01047794],
          ...,
          [0.02346814, 0.02346814, 0.02346814],
          [0.0245098 , 0.0245098 , 0.0245098 ],
          [0.0245098 , 0.0245098 , 0.0245098 ]],
 
         ...,
 
         [[0.02843137, 0.02843137, 0.02843137],
          [0.02843137, 0.02843137, 0.02843137],
          [0.02904412, 0.02904412, 0.02904412],
          ...,
          [0.01170343, 0.01170343, 0.01170343],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471]],
 
         [[0.03137255, 0.03137255, 0.03137255],
          [0.03137255, 0.03137255, 0.03137255],
          [0.03186275, 0.03186275, 0.03186275],
          ...,
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471]],
 
         [[0.03137255, 0.03137255, 0.03137255],
          [0.03137255, 0.03137255, 0.03137255],
          [0.03186275, 0.03186275, 0.03186275],
          ...,
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471],
          [0.01176471, 0.01176471, 0.01176471]]],
 
 
        [[[0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        ],
          ...,
          [0.0004902 , 0.0004902 , 0.0004902 ],
          [0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        ]],
 
         [[0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        ],
          ...,
          [0.0004902 , 0.0004902 , 0.0004902 ],
          [0.        , 0.        , 0.        ],
          [0.        , 0.        , 0.        ]],
 
         [[0.00147059, 0.00147059, 0.00147059],
          [0.00147059, 0.00147059, 0.00147059],
          [0.00128676, 0.00128676, 0.00128676],
          ...,
          [0.00104167, 0.00104167, 0.00104167],
          [0.0004902 , 0.0004902 , 0.0004902 ],
          [0.0004902 , 0.0004902 , 0.0004902 ]],
 
         ...,
 
         [[0.06568628, 0.06568628, 0.06568628],
          [0.06568628, 0.06568628, 0.06568628],
          [0.06121324, 0.06121324, 0.06121324],
          ...,
          [0.00441176, 0.00441176, 0.00441176],
          [0.00392157, 0.00392157, 0.00392157],
          [0.00392157, 0.00392157, 0.00392157]],
 
         [[0.06666667, 0.06666667, 0.06666667],
          [0.06666667, 0.06666667, 0.06666667],
          [0.0622549 , 0.0622549 , 0.0622549 ],
          ...,
          [0.00441176, 0.00441176, 0.00441176],
          [0.00392157, 0.00392157, 0.00392157],
          [0.00392157, 0.00392157, 0.00392157]],
 
         [[0.06666667, 0.06666667, 0.06666667],
          [0.06666667, 0.06666667, 0.06666667],
          [0.0622549 , 0.0622549 , 0.0622549 ],
          ...,
          [0.00441176, 0.00441176, 0.00441176],
          [0.00392157, 0.00392157, 0.00392157],
          [0.00392157, 0.00392157, 0.00392157]]]], dtype=float32),
 array([0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
        0, 1, 0, 0, 1, 1, 0, 0, 1, 1], dtype=int32))

len(data)
     
250

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
     

model = Sequential()
     

model.add(Conv2D(16, (3,3), 1, activation='relu', input_shape=(256,256,3)))
model.add(MaxPooling2D())
model.add(Conv2D(32, (3,3), 1, activation='relu'))
model.add(MaxPooling2D())
model.add(Conv2D(16, (3,3), 1, activation='relu'))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
     

model.compile('adam', loss=tf.losses.BinaryCrossentropy(), metrics=['accuracy'])
     

model.summary()
     
Model: "sequential_2"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d_6 (Conv2D)           (None, 254, 254, 16)      448       
                                                                 
 max_pooling2d_6 (MaxPooling  (None, 127, 127, 16)     0         
 2D)                                                             
                                                                 
 conv2d_7 (Conv2D)           (None, 125, 125, 32)      4640      
                                                                 
 max_pooling2d_7 (MaxPooling  (None, 62, 62, 32)       0         
 2D)                                                             
                                                                 
 conv2d_8 (Conv2D)           (None, 60, 60, 16)        4624      
                                                                 
 max_pooling2d_8 (MaxPooling  (None, 30, 30, 16)       0         
 2D)                                                             
                                                                 
 flatten_2 (Flatten)         (None, 14400)             0         
                                                                 
 dense_4 (Dense)             (None, 256)               3686656   
                                                                 
 dense_5 (Dense)             (None, 1)                 257       
                                                                 
=================================================================
Total params: 3,696,625
Trainable params: 3,696,625
Non-trainable params: 0
_________________________________________________________________

logdir='logs'
     

tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir)
     

hist = model.fit(train, epochs=20, validation_data=valid, callbacks=[tensorboard_callback])
     
Epoch 1/20
188/188 [==============================] - 35s 108ms/step - loss: 0.1093 - accuracy: 0.9460 - val_loss: 0.0161 - val_accuracy: 0.9975
Epoch 2/20
188/188 [==============================] - 19s 97ms/step - loss: 0.0099 - accuracy: 0.9967 - val_loss: 0.0127 - val_accuracy: 0.9970
Epoch 3/20
188/188 [==============================] - 20s 103ms/step - loss: 0.0094 - accuracy: 0.9975 - val_loss: 0.0186 - val_accuracy: 0.9975
Epoch 4/20
188/188 [==============================] - 18s 96ms/step - loss: 0.0026 - accuracy: 0.9995 - val_loss: 0.0035 - val_accuracy: 0.9980
Epoch 5/20
188/188 [==============================] - 22s 113ms/step - loss: 0.0354 - accuracy: 0.9912 - val_loss: 0.0098 - val_accuracy: 0.9970
Epoch 6/20
188/188 [==============================] - 21s 107ms/step - loss: 0.0045 - accuracy: 0.9987 - val_loss: 0.0055 - val_accuracy: 0.9985
Epoch 7/20
188/188 [==============================] - 20s 104ms/step - loss: 0.0049 - accuracy: 0.9987 - val_loss: 0.0094 - val_accuracy: 0.9975
Epoch 8/20
188/188 [==============================] - 21s 107ms/step - loss: 0.0017 - accuracy: 0.9993 - val_loss: 0.0060 - val_accuracy: 0.9985
Epoch 9/20
188/188 [==============================] - 18s 95ms/step - loss: 1.8142e-04 - accuracy: 1.0000 - val_loss: 0.0049 - val_accuracy: 0.9980
Epoch 10/20
188/188 [==============================] - 20s 105ms/step - loss: 7.3784e-04 - accuracy: 0.9997 - val_loss: 0.0011 - val_accuracy: 0.9995
Epoch 11/20
188/188 [==============================] - 18s 95ms/step - loss: 4.7034e-06 - accuracy: 1.0000 - val_loss: 8.4411e-04 - val_accuracy: 0.9995
Epoch 12/20
188/188 [==============================] - 20s 103ms/step - loss: 3.4927e-06 - accuracy: 1.0000 - val_loss: 7.5987e-04 - val_accuracy: 0.9995
Epoch 13/20
188/188 [==============================] - 21s 108ms/step - loss: 2.9844e-06 - accuracy: 1.0000 - val_loss: 7.2558e-04 - val_accuracy: 0.9995
Epoch 14/20
188/188 [==============================] - 18s 94ms/step - loss: 2.6624e-06 - accuracy: 1.0000 - val_loss: 7.0095e-04 - val_accuracy: 0.9995
Epoch 15/20
188/188 [==============================] - 20s 102ms/step - loss: 2.4173e-06 - accuracy: 1.0000 - val_loss: 7.0414e-04 - val_accuracy: 0.9995
Epoch 16/20
188/188 [==============================] - 20s 104ms/step - loss: 2.1754e-06 - accuracy: 1.0000 - val_loss: 6.8876e-04 - val_accuracy: 0.9995
Epoch 17/20
188/188 [==============================] - 19s 99ms/step - loss: 2.0333e-06 - accuracy: 1.0000 - val_loss: 6.9512e-04 - val_accuracy: 0.9995
Epoch 18/20
188/188 [==============================] - 20s 103ms/step - loss: 1.8747e-06 - accuracy: 1.0000 - val_loss: 7.0647e-04 - val_accuracy: 0.9995
Epoch 19/20
188/188 [==============================] - 20s 104ms/step - loss: 1.7211e-06 - accuracy: 1.0000 - val_loss: 7.1061e-04 - val_accuracy: 0.9995
Epoch 20/20
188/188 [==============================] - 20s 104ms/step - loss: 1.6000e-06 - accuracy: 1.0000 - val_loss: 7.1740e-04 - val_accuracy: 0.9995

fig = plt.figure()
plt.plot(hist.history['loss'], color='teal', label='loss')
plt.plot(hist.history['val_loss'], color='orange', label='val_loss')
fig.suptitle('Loss', fontsize=20)
plt.legend(loc="upper left")
plt.show()
     


fig = plt.figure()
plt.plot(hist.history['accuracy'], color='teal', label='accuracy')
plt.plot(hist.history['val_accuracy'], color='orange', label='val_accuracy')
fig.suptitle('Accuracy', fontsize=20)
plt.legend(loc="upper left")
plt.show()
     


import cv2
img = cv2.imread("/content/drive/MyDrive/MLNN DS/Group_Project_Data/Train/Fake/img_1.png")
plt.imshow(img)
plt.show()


     


resize = tf.image.resize(img, (256,256))
plt.imshow(resize.numpy().astype(int))
plt.show()
     


yhat = model.predict(np.expand_dims(resize/255, 0))
yhat
     
1/1 [==============================] - 0s 21ms/step
array([[2.2797321e-06]], dtype=float32)

if yhat > 0.5: 
    print(f'Predicted class is Real')
else:
    print(f'Predicted class is Fake')
     
Predicted class is Fake