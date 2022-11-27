#! /usr/bin/env python
import cv2
import numpy as np


class Batman_Falling_Class():
    def __init__(self):
        self.falling = True

    def print(self):
        print(self.falling)


if __name__ == "__main__":
    batman = Batman_Falling_Class()
    batman.print()
