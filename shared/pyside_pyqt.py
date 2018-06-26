# try:
#     from PySide2.QtCore import *
#     from PySide2.QtGui import *
#     from PySide2.QtWidgets import *
#
#     QTLIBRARY = 'PySide2'
#
# except:
if True:
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
    import platform

    # if platform.release() == 'XP':
    if True:
        from PyQt5 import QtWebKit, QtWebKitWidgets

        webView = QtWebKitWidgets.QWebView
        QWebEnginePage_Back = QtWebKitWidgets.QWebPage.Back
        QWebEnginePage_Forward = QtWebKitWidgets.QWebPage.Forward

    # else:
    #     from PyQt5 import QtWebEngineWidgets
    #
    #     webView = QtWebEngineWidgets.QWebEngineView
    #     QWebEnginePage_Back = QtWebEngineWidgets.QWebEnginePage.Back
    #     QWebEnginePage_Forward = QtWebEngineWidgets.QWebEnginePage.Forward

    QTLIBRARY = 'PyQt5'

    Signal = pyqtSignal
    Slot = pyqtSlot
