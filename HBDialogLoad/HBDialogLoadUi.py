# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HBDialogLoad.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_HBDialogLoad(object):
    def setupUi(self, HBDialogLoad):
        if not HBDialogLoad.objectName():
            HBDialogLoad.setObjectName(u"HBDialogLoad")
        HBDialogLoad.resize(600, 200)
        HBDialogLoad.setMinimumSize(QSize(600, 180))
        HBDialogLoad.setMaximumSize(QSize(1440, 840))
        icon = QIcon()
        icon.addFile(u"assets/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        HBDialogLoad.setWindowIcon(icon)
        HBDialogLoad.setStyleSheet(u"*{\n"
"font-family:\"Roboto\";\n"
"font-size:12;\n"
"font-weight: 600;\n"
"}\n"
"\n"
"#widgetMain{\n"
"background-color: rgba(123, 197, 174, 0.95);\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"#textFilePath{\n"
"  background-color:rgba(209, 237, 225, 0.95);\n"
"  border-radius: 6px;\n"
"}\n"
"\n"
"#widgetMain .QPushButton {\n"
"color: #FFFFFF;\n"
"background-color: #028C6A;\n"
"border-radius: 5px;\n"
"\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #028C6A;\n"
"/*text-align:left;*/\n"
"padding:0px 8px;\n"
"}\n"
"\n"
"#widgetMain .QPushButton:hover {\n"
"color: #003E19 ;\n"
"background-color: #7BC5AE;\n"
"border-width: 3px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(HBDialogLoad)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widgetMain = QWidget(HBDialogLoad)
        self.widgetMain.setObjectName(u"widgetMain")
        self.widgetMain.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.verticalLayout = QVBoxLayout(self.widgetMain)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(28, 8, 28, -1)
        self.lineTop = QFrame(self.widgetMain)
        self.lineTop.setObjectName(u"lineTop")
        self.lineTop.setMinimumSize(QSize(0, 36))
        self.lineTop.setMaximumSize(QSize(1440, 36))
        self.lineTop.setCursor(QCursor(Qt.ArrowCursor))
        self.lineTop.setFrameShape(QFrame.HLine)
        self.lineTop.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.lineTop)

        self.textFilePath = QPlainTextEdit(self.widgetMain)
        self.textFilePath.setObjectName(u"textFilePath")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textFilePath.sizePolicy().hasHeightForWidth())
        self.textFilePath.setSizePolicy(sizePolicy)
        self.textFilePath.setMaximumSize(QSize(1440, 32))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(True)
        self.textFilePath.setFont(font)
        self.textFilePath.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textFilePath.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.textFilePath)

        self.widgetBtns = QWidget(self.widgetMain)
        self.widgetBtns.setObjectName(u"widgetBtns")
        self.widgetBtns.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.widgetBtns)
        self.horizontalLayout.setSpacing(14)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 12, 0, 4)
        self.btnLoad = QPushButton(self.widgetBtns)
        self.btnLoad.setObjectName(u"btnLoad")
        self.btnLoad.setMaximumSize(QSize(120, 36))
        self.btnLoad.setFont(font)
        self.btnLoad.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnLoad)

        self.btnSelect = QPushButton(self.widgetBtns)
        self.btnSelect.setObjectName(u"btnSelect")
        self.btnSelect.setMaximumSize(QSize(120, 36))
        self.btnSelect.setFont(font)
        self.btnSelect.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnSelect)

        self.btnCancel = QPushButton(self.widgetBtns)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMaximumSize(QSize(120, 36))
        self.btnCancel.setFont(font)
        self.btnCancel.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnCancel)


        self.verticalLayout.addWidget(self.widgetBtns)

        self.verticalSpacer = QSpacerItem(1440, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.widgetMain)


        self.retranslateUi(HBDialogLoad)

        QMetaObject.connectSlotsByName(HBDialogLoad)
    # setupUi

    def retranslateUi(self, HBDialogLoad):
        HBDialogLoad.setWindowTitle(QCoreApplication.translate("HBDialogLoad", u"Load", None))
        self.textFilePath.setPlaceholderText(QCoreApplication.translate("HBDialogLoad", u"Enter File Path...", None))
        self.btnLoad.setText(QCoreApplication.translate("HBDialogLoad", u"Load", None))
        self.btnSelect.setText(QCoreApplication.translate("HBDialogLoad", u"Select File", None))
        self.btnCancel.setText(QCoreApplication.translate("HBDialogLoad", u"Cancel", None))
    # retranslateUi

