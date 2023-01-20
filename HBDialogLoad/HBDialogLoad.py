from PySide6.QtGui import Qt
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QDialog,
    )

from .HBDialogLoadMethods import _HBDialogLoadMethods
from .HBDialogLoadUi import Ui_HBDialogLoad

class HBDialogLoad(QDialog, _HBDialogLoadMethods):

    signal_load = Signal(list)
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_HBDialogLoad()
        self.ui.setupUi(self)

        self.set_frameless_window()
        self.init_connect_events()

        self._filepaths = []
        

    @property
    def filepath(self):
        return self._filepaths[0]

    @property
    def filepaths(self):
        return self._filepaths

    def set_frameless_window(self):
        self.setWindowFlags(
            self.windowFlags() |
            Qt.FramelessWindowHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)



    def init_connect_events(self):

        self.ui.lineTop.mousePressEvent = self.move_window_mouse_press
        self.ui.lineTop.mouseMoveEvent = self.move_window_mouse_move

        self.ui.btnLoad.clicked.connect(self.btn_load_click_event)
        self.ui.btnSelect.clicked.connect(self.btn_select_files_click_event)
        self.ui.btnCancel.clicked.connect(self.close)


