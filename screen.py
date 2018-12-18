#!usr/bin/env python3
# -*- coding:utf-8 -*-


class Screen(object):
    _height = 0
    _width = 0

    def __init__(self, height=0, width=0):
        self._height = height
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def resolution(self):
        return self._height*self._width


def printScreen(screen):
    print(screen.height)
    print(screen.width)
    print(screen.resolution)


screen = Screen(1024,768)
printScreen(screen)
screen.height = 1080
screen.width = 1920
printScreen(screen)
