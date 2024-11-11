# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainiRYJMC.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QFontComboBox,
    QGridLayout, QGroupBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(920, 481)
        MainWindow.setStyleSheet(u"")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.action12px = QAction(MainWindow)
        self.action12px.setObjectName(u"action12px")
        self.action18px = QAction(MainWindow)
        self.action18px.setObjectName(u"action18px")
        self.action24px = QAction(MainWindow)
        self.action24px.setObjectName(u"action24px")
        self.actionShow_Bible = QAction(MainWindow)
        self.actionShow_Bible.setObjectName(u"actionShow_Bible")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.fontSelect = QFontComboBox(self.groupBox)
        self.fontSelect.setObjectName(u"fontSelect")
        self.fontSelect.setEditable(True)

        self.gridLayout_2.addWidget(self.fontSelect, 0, 1, 1, 3)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 4, 1, 2)

        self.testSize = QSpinBox(self.groupBox)
        self.testSize.setObjectName(u"testSize")

        self.gridLayout_2.addWidget(self.testSize, 0, 6, 1, 1)

        self.boldButton = QPushButton(self.groupBox)
        self.boldButton.setObjectName(u"boldButton")
        self.boldButton.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.boldButton, 1, 0, 1, 1)

        self.italicButton = QPushButton(self.groupBox)
        self.italicButton.setObjectName(u"italicButton")
        self.italicButton.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.italicButton, 1, 1, 1, 1)

        self.underlineButton = QPushButton(self.groupBox)
        self.underlineButton.setObjectName(u"underlineButton")
        self.underlineButton.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.underlineButton, 1, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 3, 1, 2)

        self.colorButton = QPushButton(self.groupBox)
        self.colorButton.setObjectName(u"colorButton")
        self.colorButton.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.colorButton, 1, 5, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_3.addWidget(self.textEdit, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 920, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuVeiw = QMenu(self.menubar)
        self.menuVeiw.setObjectName(u"menuVeiw")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_2 = QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.gridLayout = QGridLayout(self.dockWidgetContents_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.dockWidgetContents_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.bibleSelection = QComboBox(self.dockWidgetContents_2)
        self.bibleSelection.addItem("")
        self.bibleSelection.addItem("")
        self.bibleSelection.addItem("")
        self.bibleSelection.setObjectName(u"bibleSelection")

        self.gridLayout.addWidget(self.bibleSelection, 0, 1, 1, 1)

        self.label_4 = QLabel(self.dockWidgetContents_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.bibleSizeUp = QPushButton(self.dockWidgetContents_2)
        self.bibleSizeUp.setObjectName(u"bibleSizeUp")

        self.gridLayout.addWidget(self.bibleSizeUp, 0, 3, 1, 1)

        self.bibleSizeDown = QPushButton(self.dockWidgetContents_2)
        self.bibleSizeDown.setObjectName(u"bibleSizeDown")

        self.gridLayout.addWidget(self.bibleSizeDown, 0, 4, 1, 1)

        self.webEngineView = QWebEngineView(self.dockWidgetContents_2)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.gridLayout.addWidget(self.webEngineView, 1, 0, 1, 5)

        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockWidget_2)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuVeiw.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)
        self.menuVeiw.addAction(self.actionShow_Bible)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.action12px.setText(QCoreApplication.translate("MainWindow", u"12px", None))
        self.action18px.setText(QCoreApplication.translate("MainWindow", u"18px", None))
        self.action24px.setText(QCoreApplication.translate("MainWindow", u"24px", None))
        self.actionShow_Bible.setText(QCoreApplication.translate("MainWindow", u"Show Bible", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Formating", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Font:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Text Size:", None))
        self.boldButton.setText("")
        self.italicButton.setText("")
        self.underlineButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Text Color:", None))
        self.colorButton.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuVeiw.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.dockWidget_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bible", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Version:", None))
        self.bibleSelection.setItemText(0, QCoreApplication.translate("MainWindow", u"King James Version", None))
        self.bibleSelection.setItemText(1, QCoreApplication.translate("MainWindow", u"American Standard Version", None))
        self.bibleSelection.setItemText(2, QCoreApplication.translate("MainWindow", u"Custom HTML...", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Bible Size:", None))
        self.bibleSizeUp.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.bibleSizeDown.setText(QCoreApplication.translate("MainWindow", u"-", None))
    # retranslateUi

