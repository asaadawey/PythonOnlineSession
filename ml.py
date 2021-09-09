# 1- We need to convert our image to number
# 2- We need to add this numbers to our machine learning model
# 3- Test our machine learning model

#Add imports
import cv2;
from skimage import io, color
from skimage.feature import local_binary_pattern
from sklearn import svm
import numpy as np


FAKE_IMAGE_PATH = ""
REAL_IMAGE_PATH = ""
TEST_IMAGE_PATH = ""

# Define our functions
def read_image(image_path):
    return cv2.imread(image_path);

def lbp_histogram(color_image):
    img = color.rgb2gray(color_image)
    patterns = local_binary_pattern(img, 10, 1)
    hist, _ = np.histogram(patterns, bins=np.arange(2**10 + 1), density=True)
    return hist

#1 - Read image
fake_image = read_image(FAKE_IMAGE_PATH);
fake_image_lpb = lbp_histogram(fake_image);
real_image = read_image(REAL_IMAGE_PATH);
real_image_lpb = lbp_histogram(real_image);

data = [fake_image_lpb,real_image_lpb];
labels = ['0','1'];
model = svm.SVC(kernel='linear',C= 1000000 , probability=True , max_iter= -1)
model.fit(data,labels)
result = model.score(data, labels)
print(result)

test_hist = lbp_histogram(read_image(TEST_IMAGE_PATH));
prediction = model.predict(test_hist.reshape(1, -1))
print(prediction);