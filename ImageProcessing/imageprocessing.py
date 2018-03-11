# coding: utf-8

from PIL import Image
from PIL import ImageFilter
from pylab import *
import numpy as np


class ImageProcessing:
    def __init__(self, image_path, width, height, img1_pos, img2_pos):
        self.image_path = image_path
        self.image = Image.open("".join(("./", self.image_path)))
        self.width = width
        self.height = height
        self.img1_pos = img1_pos
        self.img2_pos = img2_pos
        self.img1 = Image
        self.img2 = Image
        self.diff_img = Image
        self.fix_img = Image

    def load_image(self):
        region1 = self.image.crop(self.img1_pos)
        region2 = self.image.crop(self.img2_pos)
        im1 = array(region1)
        im2 = array(region2)
        self.img1 = Image.fromarray(im1)
        self.img2 = Image.fromarray(im2)
        return im1, im2

    def cmr_img(self, im1, im2):
        diff_mat = np.sum(np.abs(im1 - im2) > 3, 2)
        diff_mat[diff_mat > 0] = 1
        self.diff_img = diff_mat
        return Image.fromarray(diff_mat * 255)

    @staticmethod
    def post_processing(img):
        return img.filter(ImageFilter.MinFilter(3))

    def make_black(self):
        raw_array = array(self.img1)
        self.fix_img = raw_array[self.diff_img == 1] * [1, 1, 1, 0]
        print(self.fix_img)
        print(np.shape(self.fix_img))
        self.fix_img = Image.fromarray(self.fix_img)

    def show_img(self, img):
        f = figure()
        f.set_size_inches(60, 10)
        subplot(221)
        imshow(self.fix_img)
        subplot(222)
        imshow(img)
        subplot(223)
        imshow(self.img1)
        subplot(224)
        imshow(self.img2)
        show()
