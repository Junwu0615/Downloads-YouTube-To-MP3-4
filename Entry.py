# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-11-24
"""
from package.YTube import YTube
from package.ArgumentParser import AP

class Entry:
    def __init__(self):
        self.type = None
        self.path = None
        self.url = None

    def main(self):
        ap = AP(self)
        ap.config_once()
        yt = YTube(self)
        yt.main()

if __name__ == '__main__':
    entry = Entry()
    entry.main()