import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView

from robot import logging

logger = logging.getLogger(__name__)

app = QApplication(sys.argv)
browser = QWebEngineView()


def run():
    browser.load(QUrl("http://localhost:5000/magic"))
    browser.show()
    app.exec_()


def onSay(msg):
    logger.error("success js"+msg)
    browser.page().runJavaScript("talk('" + msg + "');")
