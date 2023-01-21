# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HBMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

from HBImageBox import HBImageBox

class Ui_HBMainWindow(object):
    def setupUi(self, HBMainWindow):
        if not HBMainWindow.objectName():
            HBMainWindow.setObjectName(u"HBMainWindow")
        HBMainWindow.resize(800, 600)
        HBMainWindow.setMaximumSize(QSize(4096, 2048))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setBold(True)
        HBMainWindow.setFont(font)
        HBMainWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u"assets/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        HBMainWindow.setWindowIcon(icon)
        HBMainWindow.setWindowOpacity(1.000000000000000)
        HBMainWindow.setStyleSheet(u"*{\n"
"font-family:\"Roboto\";\n"
"font-weight: 500;\n"
"}\n"
"\n"
".QStatusBar {\n"
"  background-color: rgba(123, 197, 174,1);\n"
"border-bottom-right-radius: 4px;\n"
"border-bottom-left-radius: 4px;\n"
"}\n"
"\n"
"#widgetBanner {\n"
"background-color:#7BC5AE;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"}\n"
"\n"
"\n"
"#hbImageBox {\n"
"background-color: rgba(209, 237, 225, 0.92);\n"
"}\n"
"\n"
"#btnMenu {\n"
" background-color: #7BC5AE;\n"
" border-radius: 5px;\n"
" border-color: #003E19;\n"
" border-width: 2px;\n"
" border-style: solid;\n"
"}\n"
"\n"
"#btnMenu:hover {\n"
" background-color: #028C6A;\n"
" border-color: #003E19;\n"
"}\n"
"\n"
"#widgetMenu {\n"
"background-color: #028C6A;\n"
"}\n"
"\n"
"#widgetMenu .QPushButton {\n"
"color: #FFFFFF;\n"
"border-radius: 5px;\n"
"text-align:left;\n"
"padding:0px 8px;\n"
"}\n"
"\n"
"#widgetMenu .QPushButton:hover {\n"
"color: #003E19 ;\n"
"background-color: #7BC5AE;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#widgetMenu .QLabel {\n"
"color:"
                        " #FFFFFF;\n"
"padding:0px 4px;\n"
"}\n"
"#widgetImageInfos .QLabel {\n"
"color: #FFFFFF;\n"
"padding:0px 0px;\n"
"}\n"
"#labelPage:hover {\n"
"color: #003E19 ;\n"
"background-color: #7BC5AE;\n"
"border-radius: 1px;\n"
"}\n"
"#widgetMenu .QLineEdit{\n"
"color: #FFFFFF;\n"
"background-color: #028C6A;\n"
"border-width: 0px;\n"
" border-style: none;\n"
"padding:0px 4px;\n"
"}\n"
"#widgetMenu .QLineEdit:hover {\n"
"color: #003E19 ;\n"
"background-color: #7BC5AE;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"#widgetIndexBtns .QPushButton{\n"
"text-align:center;\n"
"}\n"
"\n"
"#widgetWindowControl .QPushButton {\n"
" background-color:#7BC5AE;\n"
" border-radius: 3px;\n"
"}\n"
"#widgetWindowControl .QPushButton:hover {\n"
" background-color:#D1EDE1;\n"
"}")
        self.centralwidget = QWidget(HBMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAcceptDrops(True)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widgetBanner = QWidget(self.centralwidget)
        self.widgetBanner.setObjectName(u"widgetBanner")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetBanner.sizePolicy().hasHeightForWidth())
        self.widgetBanner.setSizePolicy(sizePolicy)
        self.widgetBanner.setMinimumSize(QSize(0, 70))
        self.widgetBanner.setMaximumSize(QSize(16777215, 65))
        self.horizontalLayout = QHBoxLayout(self.widgetBanner)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(14, 8, 6, 8)
        self.btnMenu = QPushButton(self.widgetBanner)
        self.btnMenu.setObjectName(u"btnMenu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnMenu.sizePolicy().hasHeightForWidth())
        self.btnMenu.setSizePolicy(sizePolicy1)
        self.btnMenu.setMinimumSize(QSize(70, 40))
        self.btnMenu.setMaximumSize(QSize(150, 40))
        self.btnMenu.setBaseSize(QSize(70, 40))
        self.btnMenu.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"assets/list32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMenu.setIcon(icon1)
        self.btnMenu.setIconSize(QSize(32, 32))
        self.btnMenu.setFlat(False)

        self.horizontalLayout.addWidget(self.btnMenu)

        self.widgetWindowMove = QWidget(self.widgetBanner)
        self.widgetWindowMove.setObjectName(u"widgetWindowMove")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widgetWindowMove.sizePolicy().hasHeightForWidth())
        self.widgetWindowMove.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.widgetWindowMove)

        self.widgetWindowControl = QWidget(self.widgetBanner)
        self.widgetWindowControl.setObjectName(u"widgetWindowControl")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widgetWindowControl.sizePolicy().hasHeightForWidth())
        self.widgetWindowControl.setSizePolicy(sizePolicy3)
        self.widgetWindowControl.setMinimumSize(QSize(100, 0))
        self.widgetWindowControl.setMaximumSize(QSize(100, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.widgetWindowControl)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnMinWindow = QPushButton(self.widgetWindowControl)
        self.btnMinWindow.setObjectName(u"btnMinWindow")
        self.btnMinWindow.setMinimumSize(QSize(24, 24))
        self.btnMinWindow.setMaximumSize(QSize(24, 24))
        self.btnMinWindow.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"assets/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMinWindow.setIcon(icon2)
        self.btnMinWindow.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.btnMinWindow)

        self.btnMaxWindow = QPushButton(self.widgetWindowControl)
        self.btnMaxWindow.setObjectName(u"btnMaxWindow")
        self.btnMaxWindow.setMinimumSize(QSize(24, 24))
        self.btnMaxWindow.setMaximumSize(QSize(24, 24))
        self.btnMaxWindow.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"assets/maximize24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMaxWindow.setIcon(icon3)
        self.btnMaxWindow.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.btnMaxWindow)

        self.btnClose = QPushButton(self.widgetWindowControl)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(24, 24))
        self.btnClose.setMaximumSize(QSize(24, 24))
        self.btnClose.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"assets/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnClose.setIcon(icon4)
        self.btnClose.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.btnClose)


        self.horizontalLayout.addWidget(self.widgetWindowControl)

        self.widgetWindowMove.raise_()
        self.btnMenu.raise_()
        self.widgetWindowControl.raise_()

        self.gridLayout.addWidget(self.widgetBanner, 0, 0, 1, 1)

        self.layoutMiddle = QHBoxLayout()
        self.layoutMiddle.setSpacing(0)
        self.layoutMiddle.setObjectName(u"layoutMiddle")
        self.widgetMenu = QWidget(self.centralwidget)
        self.widgetMenu.setObjectName(u"widgetMenu")
        self.widgetMenu.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.widgetMenu.sizePolicy().hasHeightForWidth())
        self.widgetMenu.setSizePolicy(sizePolicy1)
        self.widgetMenu.setMinimumSize(QSize(200, 300))
        self.widgetMenu.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.widgetMenu.setFont(font1)
        self.verticalLayout = QVBoxLayout(self.widgetMenu)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 12, 10, 8)
        self.btnImageInfos = QPushButton(self.widgetMenu)
        self.btnImageInfos.setObjectName(u"btnImageInfos")
        self.btnImageInfos.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.btnImageInfos.sizePolicy().hasHeightForWidth())
        self.btnImageInfos.setSizePolicy(sizePolicy1)
        self.btnImageInfos.setMinimumSize(QSize(0, 40))
        self.btnImageInfos.setMaximumSize(QSize(200, 60))
        self.btnImageInfos.setFont(font1)
        self.btnImageInfos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnImageInfos.setLayoutDirection(Qt.RightToLeft)
        icon5 = QIcon()
        icon5.addFile(u"assets/picture.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnImageInfos.setIcon(icon5)
        self.btnImageInfos.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btnImageInfos)

        self.widgetImageInfos = QWidget(self.widgetMenu)
        self.widgetImageInfos.setObjectName(u"widgetImageInfos")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widgetImageInfos.sizePolicy().hasHeightForWidth())
        self.widgetImageInfos.setSizePolicy(sizePolicy4)
        self.widgetImageInfos.setMinimumSize(QSize(0, 150))
        self.widgetImageInfos.setMaximumSize(QSize(200, 600))
        self.verticalLayout_2 = QVBoxLayout(self.widgetImageInfos)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEditName = QLineEdit(self.widgetImageInfos)
        self.lineEditName.setObjectName(u"lineEditName")
        sizePolicy1.setHeightForWidth(self.lineEditName.sizePolicy().hasHeightForWidth())
        self.lineEditName.setSizePolicy(sizePolicy1)
        self.lineEditName.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_2.addWidget(self.lineEditName)

        self.widgetWidth = QWidget(self.widgetImageInfos)
        self.widgetWidth.setObjectName(u"widgetWidth")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widgetWidth.sizePolicy().hasHeightForWidth())
        self.widgetWidth.setSizePolicy(sizePolicy5)
        self.widgetWidth.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_4 = QHBoxLayout(self.widgetWidth)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.labelWidth = QLabel(self.widgetWidth)
        self.labelWidth.setObjectName(u"labelWidth")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.labelWidth.sizePolicy().hasHeightForWidth())
        self.labelWidth.setSizePolicy(sizePolicy6)
        self.labelWidth.setMinimumSize(QSize(0, 0))
        self.labelWidth.setMaximumSize(QSize(60, 36))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.labelWidth.setFont(font2)
        self.labelWidth.setCursor(QCursor(Qt.ArrowCursor))
        self.labelWidth.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelWidth)

        self.lineEditWidth = QLineEdit(self.widgetWidth)
        self.lineEditWidth.setObjectName(u"lineEditWidth")
        self.lineEditWidth.setMaximumSize(QSize(100, 16777215))
        self.lineEditWidth.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEditWidth)


        self.verticalLayout_2.addWidget(self.widgetWidth)

        self.widgetHeight = QWidget(self.widgetImageInfos)
        self.widgetHeight.setObjectName(u"widgetHeight")
        sizePolicy5.setHeightForWidth(self.widgetHeight.sizePolicy().hasHeightForWidth())
        self.widgetHeight.setSizePolicy(sizePolicy5)
        self.widgetHeight.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_5 = QHBoxLayout(self.widgetHeight)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.labelHeight = QLabel(self.widgetHeight)
        self.labelHeight.setObjectName(u"labelHeight")
        sizePolicy6.setHeightForWidth(self.labelHeight.sizePolicy().hasHeightForWidth())
        self.labelHeight.setSizePolicy(sizePolicy6)
        self.labelHeight.setMinimumSize(QSize(0, 0))
        self.labelHeight.setMaximumSize(QSize(60, 36))
        self.labelHeight.setFont(font2)
        self.labelHeight.setCursor(QCursor(Qt.ArrowCursor))
        self.labelHeight.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.labelHeight)

        self.lineEditHeight = QLineEdit(self.widgetHeight)
        self.lineEditHeight.setObjectName(u"lineEditHeight")
        self.lineEditHeight.setMaximumSize(QSize(100, 16777215))
        self.lineEditHeight.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEditHeight)


        self.verticalLayout_2.addWidget(self.widgetHeight)


        self.verticalLayout.addWidget(self.widgetImageInfos)

        self.widgetIndexBtns = QWidget(self.widgetMenu)
        self.widgetIndexBtns.setObjectName(u"widgetIndexBtns")
        self.widgetIndexBtns.setMinimumSize(QSize(0, 40))
        self.widgetIndexBtns.setMaximumSize(QSize(200, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.widgetIndexBtns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnPrevious = QPushButton(self.widgetIndexBtns)
        self.btnPrevious.setObjectName(u"btnPrevious")
        self.btnPrevious.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.btnPrevious.sizePolicy().hasHeightForWidth())
        self.btnPrevious.setSizePolicy(sizePolicy1)
        self.btnPrevious.setMinimumSize(QSize(0, 40))
        self.btnPrevious.setMaximumSize(QSize(200, 60))
        self.btnPrevious.setFont(font1)
        self.btnPrevious.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnPrevious.setLayoutDirection(Qt.LeftToRight)
        icon6 = QIcon()
        icon6.addFile(u"assets/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPrevious.setIcon(icon6)
        self.btnPrevious.setIconSize(QSize(24, 24))
        self.btnPrevious.setFlat(False)

        self.horizontalLayout_3.addWidget(self.btnPrevious)

        self.lineEditPage = QLineEdit(self.widgetIndexBtns)
        self.lineEditPage.setObjectName(u"lineEditPage")
        sizePolicy1.setHeightForWidth(self.lineEditPage.sizePolicy().hasHeightForWidth())
        self.lineEditPage.setSizePolicy(sizePolicy1)
        self.lineEditPage.setMaximumSize(QSize(40, 16777215))
        self.lineEditPage.setMaxLength(1023)
        self.lineEditPage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lineEditPage)

        self.btnNext = QPushButton(self.widgetIndexBtns)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.btnNext.sizePolicy().hasHeightForWidth())
        self.btnNext.setSizePolicy(sizePolicy1)
        self.btnNext.setMinimumSize(QSize(0, 40))
        self.btnNext.setMaximumSize(QSize(200, 60))
        self.btnNext.setFont(font1)
        self.btnNext.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNext.setLayoutDirection(Qt.LeftToRight)
        icon7 = QIcon()
        icon7.addFile(u"assets/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNext.setIcon(icon7)
        self.btnNext.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.btnNext)


        self.verticalLayout.addWidget(self.widgetIndexBtns)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.line = QFrame(self.widgetMenu)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.btnLoad = QPushButton(self.widgetMenu)
        self.btnLoad.setObjectName(u"btnLoad")
        sizePolicy1.setHeightForWidth(self.btnLoad.sizePolicy().hasHeightForWidth())
        self.btnLoad.setSizePolicy(sizePolicy1)
        self.btnLoad.setMinimumSize(QSize(0, 40))
        self.btnLoad.setMaximumSize(QSize(200, 60))
        self.btnLoad.setFont(font1)
        self.btnLoad.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLoad.setLayoutDirection(Qt.RightToLeft)
        self.btnLoad.setAutoFillBackground(False)
        icon8 = QIcon()
        icon8.addFile(u"assets/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLoad.setIcon(icon8)
        self.btnLoad.setIconSize(QSize(24, 24))
        self.btnLoad.setFlat(False)

        self.verticalLayout.addWidget(self.btnLoad)

        self.btnSave = QPushButton(self.widgetMenu)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy1)
        self.btnSave.setMinimumSize(QSize(0, 40))
        self.btnSave.setMaximumSize(QSize(200, 60))
        self.btnSave.setFont(font1)
        self.btnSave.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSave.setLayoutDirection(Qt.RightToLeft)
        icon9 = QIcon()
        icon9.addFile(u"assets/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSave.setIcon(icon9)
        self.btnSave.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btnSave)

        self.btnSaveAll = QPushButton(self.widgetMenu)
        self.btnSaveAll.setObjectName(u"btnSaveAll")
        self.btnSaveAll.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.btnSaveAll.sizePolicy().hasHeightForWidth())
        self.btnSaveAll.setSizePolicy(sizePolicy1)
        self.btnSaveAll.setMinimumSize(QSize(0, 40))
        self.btnSaveAll.setMaximumSize(QSize(200, 60))
        self.btnSaveAll.setFont(font1)
        self.btnSaveAll.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSaveAll.setLayoutDirection(Qt.RightToLeft)
        self.btnSaveAll.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btnSaveAll)

        self.btnExit = QPushButton(self.widgetMenu)
        self.btnExit.setObjectName(u"btnExit")
        sizePolicy1.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy1)
        self.btnExit.setMinimumSize(QSize(0, 40))
        self.btnExit.setMaximumSize(QSize(200, 60))
        self.btnExit.setFont(font1)
        self.btnExit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnExit.setLayoutDirection(Qt.RightToLeft)
        icon10 = QIcon()
        icon10.addFile(u"assets/powerOff.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnExit.setIcon(icon10)
        self.btnExit.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btnExit)


        self.layoutMiddle.addWidget(self.widgetMenu)

        self.hb_image_box = HBImageBox(self.centralwidget)
        self.hb_image_box.setObjectName(u"hb_image_box")

        self.layoutMiddle.addWidget(self.hb_image_box)


        self.gridLayout.addLayout(self.layoutMiddle, 1, 0, 1, 1)

        HBMainWindow.setCentralWidget(self.centralwidget)
        self.widgetImageProcessor = QMenuBar(HBMainWindow)
        self.widgetImageProcessor.setObjectName(u"widgetImageProcessor")
        self.widgetImageProcessor.setEnabled(True)
        self.widgetImageProcessor.setGeometry(QRect(0, 0, 0, 0))
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widgetImageProcessor.sizePolicy().hasHeightForWidth())
        self.widgetImageProcessor.setSizePolicy(sizePolicy7)
        self.widgetImageProcessor.setMinimumSize(QSize(0, 0))
        self.widgetImageProcessor.setMaximumSize(QSize(0, 0))
        HBMainWindow.setMenuBar(self.widgetImageProcessor)
        self.statusbar = QStatusBar(HBMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setMaximumSize(QSize(16777215, 16))
        HBMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HBMainWindow)

        QMetaObject.connectSlotsByName(HBMainWindow)
    # setupUi

    def retranslateUi(self, HBMainWindow):
        HBMainWindow.setWindowTitle(QCoreApplication.translate("HBMainWindow", u"HB Image Processor", None))
        self.btnMenu.setText("")
#if QT_CONFIG(shortcut)
        self.btnMenu.setShortcut(QCoreApplication.translate("HBMainWindow", u"M", None))
#endif // QT_CONFIG(shortcut)
        self.btnMinWindow.setText("")
        self.btnMaxWindow.setText("")
        self.btnClose.setText("")
        self.btnImageInfos.setText(QCoreApplication.translate("HBMainWindow", u"Image Infos", None))
        self.labelWidth.setText(QCoreApplication.translate("HBMainWindow", u"Width : ", None))
        self.labelHeight.setText(QCoreApplication.translate("HBMainWindow", u"Height :", None))
        self.btnPrevious.setText("")
        self.lineEditPage.setText(QCoreApplication.translate("HBMainWindow", u"-", None))
        self.btnNext.setText("")
#if QT_CONFIG(shortcut)
        self.btnNext.setShortcut(QCoreApplication.translate("HBMainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.btnLoad.setText(QCoreApplication.translate("HBMainWindow", u"Load", None))
#if QT_CONFIG(shortcut)
        self.btnLoad.setShortcut(QCoreApplication.translate("HBMainWindow", u"L", None))
#endif // QT_CONFIG(shortcut)
        self.btnSave.setText(QCoreApplication.translate("HBMainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.btnSave.setShortcut(QCoreApplication.translate("HBMainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.btnSaveAll.setText(QCoreApplication.translate("HBMainWindow", u"Save All", None))
#if QT_CONFIG(shortcut)
        self.btnSaveAll.setShortcut(QCoreApplication.translate("HBMainWindow", u"H", None))
#endif // QT_CONFIG(shortcut)
        self.btnExit.setText(QCoreApplication.translate("HBMainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.btnExit.setShortcut(QCoreApplication.translate("HBMainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

