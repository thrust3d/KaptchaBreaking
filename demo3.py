import os
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from collections import Counter

import tensorflow as tf
from tensorflow import keras

# Path to the data directory
data_dir = Path("./captcha_images_v2/")

# Get list of all the images
images = sorted(list(map(str, list(data_dir.glob("*.png")))))
print(images)
labels = [img.split(os.path.sep)[-1].split(".png")[0] for img in images]
print(labels)
characters = set(char for label in labels for char in label)
characters = sorted(list(characters))
print(characters)