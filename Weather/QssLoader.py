# -*- coding: utf-8 -*-

class QssLoader:
    def __init__(self):
        pass
    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()
