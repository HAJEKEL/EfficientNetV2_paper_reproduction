import torch
from torch import nn #module with classes and functions for different types of layers etc. 
from torch import optim #module with classes and functions for optimization algoritms sgd, adam etc. 
import timm #pytorch image models (collection of state-of-the-art pre-trained models)
import math #importing math module to use mathematical functions and constants
import os #import os module to interact with the operating system: access/manipulate file system, environment variables etc. 

"""
Efficientnetv2: faster training speed and better parameter efficiency
- Training-aware neural architecture search and scaling: optimize for both training speed and parameter efficiency

- 

"""
CONFIGS = {
    #a dictrionary with the different architectures
    "b0": { #b0 varient of the efficientnetv2 architecture
    "widths": [32, 16, 32, 48, 96, 112, 192], # number of channels in each block of the model 
    "depths": [1, 2, 2, 3, 5, 8],
    "strides": [1, 2, 2, 2, 1, 2],
    "convs": [0, 1, 1, 2, 3, 3],
    "output_conv_size": 1280,
    "timm_weights": "tf_efficientnetv2_b0" # pretrained weights
    },
    "b1": {
    "widths": [32, 16, 32, 48, 96, 112, 192],
    "depths": [2, 3, 3, 4, 6, 7],
    "strides": [1, 2, 2, 2, 1, 2],
    "convs": [0, 1, 1, 2, 3, 3],
    "output_conv_size": 1280,
    "timm_weights": "tf_efficientnetv2_b1" # pretrained weights
    },
}


