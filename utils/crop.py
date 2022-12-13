# Plotting utils

import glob
import math
import os
import random
from copy import copy
from pathlib import Path

import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from PIL import Image, ImageDraw, ImageFont
from scipy.signal import butter, filtfilt

from utils.general import xywh2xyxy, xyxy2xywh
from utils.metrics import fitness

def crop_one_box(x, img):
    crop_img = img[ int(x[1]) : int(x[3]), int(x[0]): int(x[2])]
    return crop_img