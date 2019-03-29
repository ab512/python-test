#!usr/bin/env python3
# -*- coding:utf-8 -*-


from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self,cap):
        super(LastUpdatedOrderedDict,self).__init__()
        self.cap=cap

    def __setitem__(self,key,value):
        com