"""
HBImageBoxUi is inherited from "PySide6.QtWidgets.QWidget".\n
This class is used for creating and layout the HBImageBox's UserInterface.

Require package:
1. Pyside
"""


from PySide6.QtCore import QSize,Qt,QCoreApplication
from PySide6.QtGui import QAction,QKeySequence,QShortcut

from PySide6.QtWidgets import (
    QMenu,
    QWidget,
    QScrollArea,
    QVBoxLayout,
    QHBoxLayout,
    QSpacerItem,
    QSizePolicy,
    QMenuBar
)

from .HBImageBoxLabel import HBImageBoxLabel



class _HBImageBoxUi(QWidget):
    """
    
    This class is used for creating and layout the HBImageBox's UserInterface.
    HBImageBoxUi is inherited from "PySide6.QtWidgets.QWidget".\n
    """

    def __init__(self, parent:QWidget=None) -> None:
        super().__init__(parent)
        self.setObjectName(u"HBImageBox")
        self.setAcceptDrops(True)



        self.add_widgets()
        self.add_actions()
        self.set_actions()
        self.set_widgets()
        self.set_menus()



    def add_widgets(self):
        self.main_layout = QVBoxLayout(self)
        self.scroll_area = QScrollArea(self)

        self.scroll_area_contents = QWidget(self.scroll_area)
        self.contents_layout = QHBoxLayout(self.scroll_area_contents)

        self.hb_image_box_spacer0 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.hb_image_box_label = HBImageBoxLabel(self.scroll_area_contents)
        self.hb_image_box_spacer1 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.menu_bar = QMenuBar(None)
        self.menu_processor = QMenu(self)
        self.menu_edit = QMenu(self.menu_processor)
        self.menu_flip = QMenu(self.menu_edit)
        self.menu_color = QMenu(self.menu_edit)
        self.menu_draw = QMenu(self.menu_edit)


    def add_actions(self):
        self.actionCrop = QAction("Crop",self)
        self.actionCrop.setObjectName(u"actionCrop")

        self.actionHorizontal = QAction("Horizontal",self)
        self.actionHorizontal.setObjectName(u"actionHorizontal")

        self.actionVertical = QAction("Vertical",self)
        self.actionVertical.setObjectName(u"actionVertical")

        self.actionRotate_90 = QAction("Rotate 90'",self)
        self.actionRotate_90.setObjectName(u"actionRotate_90")

        self.actionGray = QAction("Gray",self)
        self.actionGray.setObjectName(u"actionGray")

        self.actionInvert = QAction("Invert",self)
        self.actionInvert.setObjectName(u"actionInvert")

        self.actionCopy = QAction("Copy",self)
        self.actionCopy.setObjectName(u"actionCopy")

        self.actionPaste = QAction("Paste",self)
        self.actionPaste.setObjectName(u"actionPaste")

        self.actionRemove = QAction("Remove",self)
        self.actionRemove.setObjectName(u"actionRemove")
        self.actionRemove.setEnabled(False)
        
        self.actionInformation = QAction("Information",self)
        self.actionInformation.setObjectName(u"actionInformation")     
        
        self.actionUndo = QAction("Undo", self)
        self.actionUndo.setObjectName(u"actionUndo")

        self.actionRedo = QAction("Redo", self)
        self.actionRedo.setObjectName(u"actionRedo")

        self.actionLoad = QAction("Load", self)
        self.actionLoad.setObjectName(u"actionLoad")
        
        self.actionSave = QAction("Save", self)
        self.actionSave.setObjectName(u"actionSave")
        
        self.actionDrawRect = QAction("Rect", self)
        self.actionDrawRect.setObjectName(u"actionDrawRect")        


    def set_actions(self):
        
        self._add_action_shortcut(self.actionCrop, "C")
        self._add_action_shortcut(self.actionHorizontal, "F")
        self._add_action_shortcut(self.actionVertical, QKeySequence(Qt.SHIFT | Qt.Key_F))
        self._add_action_shortcut(self.actionRotate_90, "O")
        self._add_action_shortcut(self.actionGray, "G")
        self._add_action_shortcut(self.actionUndo, QKeySequence.Undo)
        self._add_action_shortcut(self.actionRedo, QKeySequence.Redo)

        self._add_action_shortcut(self.actionCopy, QKeySequence.Copy)
        self._add_action_shortcut(self.actionPaste, QKeySequence.Paste)
        self._add_action_shortcut(self.actionRemove, QKeySequence.Delete)
        self._add_action_shortcut(self.actionSave, QKeySequence.Save)
        
        self.actionCopy.setEnabled(False)
        self.actionSave.setEnabled(False)
        self.actionRemove.setEnabled(False)
        self.actionInformation.setEnabled(False)
        self.actionUndo.setEnabled(False)
        self.actionRedo.setEnabled(False)



    def set_widgets(self):
        self.main_layout.setObjectName(u"mainLayout")
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.scroll_area)


        self.scroll_area.setObjectName(u"scrollArea")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_area_contents)

        self.scroll_area_contents.setObjectName(u"scrollAreaContents")
 
        self.contents_layout.setObjectName(u"scrollAreaLayout")
        self.contents_layout.setSpacing(0)
        self.contents_layout.setContentsMargins(0, 0, 0, 0)

        self.contents_layout.addItem(self.hb_image_box_spacer0)
        self.contents_layout.addWidget(self.hb_image_box_label, 0, Qt.AlignCenter)
        self.contents_layout.addItem(self.hb_image_box_spacer1)

        self.hb_image_box_label.setObjectName(u"HBImageBoxLabel")
        self.hb_image_box_label.setMinimumSize(QSize(300, 120))
        self.hb_image_box_label.setAlignment(Qt.AlignCenter)
        
    def set_menus(self):
        self.menu_flip.setObjectName(u"menuFlip")
        self.menu_flip.addAction(self.actionHorizontal)
        self.menu_flip.addAction(self.actionVertical)
        
        self.menu_color.setObjectName(u"menuColor")
        self.menu_color.addAction(self.actionGray)
        self.menu_color.addAction(self.actionInvert)
        
        self.menu_draw.setObjectName(u"menuDraw")
        self.menu_draw.addAction(self.actionDrawRect)
        

        self.menu_edit.setObjectName(u"menuEdit")
        self.menu_edit.setEnabled(False)
        
        self.menu_edit.addActions([
            self.actionCrop,
            self.actionRotate_90,
            self.menu_color.menuAction(),
            self.menu_draw.menuAction(),
            self.menu_flip.menuAction()
        ])
        self.menu_edit.addSeparator()
        self.menu_edit.addActions([
            self.actionUndo,
            self.actionRedo
        ])
        



        self.menu_processor.setObjectName(u"menuProcessor")
        self.menu_processor.setEnabled(True)

        self.menu_processor.addActions([
            self.menu_edit.menuAction(),
            self.actionCopy,
            self.actionPaste,
            self.actionRemove
        ])
        self.menu_processor.addSeparator()
        self.menu_processor.addActions([
            self.actionLoad,
            self.actionSave,
            self.actionInformation
        ])

        self.menu_bar.addMenu(self.menu_processor)
        
        self.menu_processor.setTitle(u"Processor")
        self.menu_edit.setTitle(u"Edit")
        self.menu_flip.setTitle("Flip")
        self.menu_color.setTitle("Color")
        self.menu_draw.setTitle("Draw")
        



    def _add_action_shortcut(self, widget:QAction, shortcut):
        if isinstance(shortcut,str):
            widget.setShortcut(shortcut)
            shortcut = QShortcut(QKeySequence(shortcut), self)
        elif isinstance(shortcut, QKeySequence):
            widget.setShortcut(shortcut)
            shortcut = QShortcut(shortcut, self)
        else:
            try:
                widget.setShortcut(shortcut)
                shortcut = QShortcut(shortcut, self)
            except:
                raise TypeError("var:shortcut only accept 'str' and 'QKeySequence' type.")

        shortcut.activated.connect(widget.trigger)