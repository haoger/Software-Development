# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 08:33:32 2016

@author: zerloy
"""

import os
os.mkdir('G:/黄智豪/python/awesome-python3-webapp/')
list1 = ['backup/', 'conf/', 'dist/', 'www/', 'ios/', 'LICENSE/']
for i in range(len(list1)):
    os.mkdir('G:/黄智豪/python/awesome-python3-webapp/'+list1[i])
os.mkdir('G:/黄智豪/python/awesome-python3-webapp/www/static/')
os.mkdir('G:/黄智豪/python/awesome-python3-webapp/www/templates/')


