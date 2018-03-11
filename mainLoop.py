# coding: utf-8

from ScreenShot import screenshot
from ImageProcessing import imageprocessing

if __name__ == '__main__':
    ss = screenshot.ScreenShot()
    ss.take_screen_shot()
    ip = imageprocessing.ImageProcessing('screenshot.png', 820, 820, (200, 100, 1020, 920), (200, 1000, 1020, 1820))
    im1, im2 = ip.load_image()
    diff_img = ip.cmr_img(im1, im2)
    diff_img = ip.post_processing(diff_img)
    ip.make_black()
    ip.show_img(diff_img)
