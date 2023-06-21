'''Generic functions and classes that are model-independent.'''

import torch as th
import torch.nn as nn
import xml.dom.minidom as minidom
import numpy as np
import re


def loadECG(file):
    
    data = minidom.parse(file)
    
    'Load ECG data from xml file'
    stripdata = data.getElementsByTagName('StripData')
    a = stripdata[0]
    _dict = {}
    # WaveformData contains the measures of each sensor
    for el in a.getElementsByTagName('WaveformData'):
        lead = el.attributes['lead'].value
        values = el.firstChild.data
        # substitute every \t\n character in the string
        values = np.array(re.sub(r'\s', '', values).split(','), dtype=int)
        _dict[lead] = values

    # The result is a dict like {'I': array, 'II': array, ...}
    # 12 keys are I,II,III,aVR,aVL,aVF,V1,V2,V3,V4,V5,V6
    # Resulting array has shape (12, 5000)
    arr = np.vstack(list(_dict.values()))
    
    ##############################################################
    ##########    Return first key for the moment    #############
    ##########    Temporary (to reduce the time)     #############
    ##########    At the end we will return the hole arr    ######
    ##############################################################
    return arr[0]


def median_filter(data, window_size):
    filtered_data = np.zeros(len(data))
    for i in range(len(data)):
        start = max(0, i - window_size//2)
        end = min(len(data), i + window_size//2 + 1)
        window = data[start:end]
        filtered_data[i] = np.median(window)
    return filtered_data


def common_Ids(list, common_values):

    common_names = []

    for item in list:
        if (re.search(r"\d{5,}", item).group() in common_values):
            common_names.append(item)
            
    return common_names


class NormalizeECG(object):
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std
        
    def __call__(self, ecg):
        return (ecg - self.mean) / self.std
    
    
