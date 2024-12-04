# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:04:04 2024

@author: net_g
"""


import scipy.io as sio  # for loading matlab files\n",
import numpy as np
import matplotlib.pyplot as plt

data = sio.loadmat('umist_cropped.mat')

data['facedat']