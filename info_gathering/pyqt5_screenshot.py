#!/usr/bin/env python
import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage

class Screenshot(QWebView): 
    def __init__(self):
        self.app = QApplication(sys.argv)
        QWebView.__init__(self)
        self._loaded = False
        self.loadFinished.connect(self._loadFinished)

    def wait_load(self, delay=0):
        while not self._loaded:
            self.app.processEvents()
            time.sleep(delay)
        self._loaded = False
    
    def _loadFinished(self, result):
        self._loaded = True
    
    def get_image(self, url):
        self.load(QUrl(url))
        self.wait_load()
        frame = self.page().mainFrame()
        self.page().setViewportSize(frame.contentsSize())
        image = QImage(self.page().viewportSize(),
                QImage.Format_ARGB32)
        painter = QPainter(image)
        frame.render(painter)
        painter.end()
        return image

if __name__ == '__main__':
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        print('Usage: python pyqt5_scrap.py <target_url>')
        sys.exit(1)
    s = Screenshot()
    image = s.get_image(target)
    image.save(target.replace('/', '_') + '_scrape.png')
