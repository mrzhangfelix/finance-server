#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.requests import get_png

indexlist=['0000001','1399001','1399300','1399006']
base_url = 'http://img1.money.126.net/chart/hs/time/540x360/'

def main(base_url):
    for index in indexlist:
        filename='..\\data\\indexImg\\'+index+'.png'
        url=base_url+index+'.png'
        open(filename, 'wb').write(get_png(url))

if __name__ == '__main__':
    main(base_url)
