from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QMessageBox
    )

from .HBMainWindowMethods import _HBMainWindowMethods
from .HBMainWindowUi import Ui_HBMainWindow
from HBImage import HBAlbum





class HBMainWindow(QMainWindow, _HBMainWindowMethods):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_HBMainWindow()
        self.ui.setupUi(self)

        self.set_frameless_window()
        self.init_declare_members()
        self.init_appearance()
        self.init_animation()
    
        self.init_connect_events()
        self.ui.widgetMenu.hide()
        



    def init_declare_members(self):
        self.hb_album = HBAlbum()

        self.btns_menu = [
            self.ui.btnImageInfos,
            self.ui.btnLoad,
            self.ui.btnSave,
            self.ui.btnSaveAll,
            self.ui.btnExit,
            self.ui.btnNext,
            self.ui.btnPrevious
        ]
        
        self.need_update_widget = (
            self.ui.btnImageInfos,
            self.ui.btnSave,
            self.ui.btnSaveAll,
            self.ui.btnNext,
            self.ui.btnPrevious,
            self.ui.widgetImageProcessor
        )

    def set_frameless_window(self):
        self.setWindowFlags(
            self.windowFlags() |
            Qt.FramelessWindowHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)


    def init_connect_events(self):
        """
        connect or set qt widgets events,
        and only use in HBMainWindow.__init__().\n
        (Some events use lambda function beacuse some variables in function is fixed.)
        """
        self.ui.hb_image_box.image_removed.connect(self._remove_image)
        self.ui.hb_image_box.image_loaded.connect(self._add_image)

        self.ui.widgetWindowMove.mousePressEvent = self._move_window_mouse_press
        self.ui.widgetWindowMove.mouseMoveEvent = self._move_window_mouse_move

        self.ui.btnClose.clicked.connect(self.close)
        self.ui.btnMaxWindow.clicked.connect(self._max_normal_window)
        self.ui.btnMinWindow.clicked.connect(self.showMinimized)

        self.ui.btnMenu.clicked.connect(self._show_hide_menu)
        self.ui.btnImageInfos.clicked.connect(self.ui.hb_image_box.actionInformation.trigger)
        self.ui.btnLoad.clicked.connect(self.load)
        self.ui.btnSave.clicked.connect(self.ui.hb_image_box.actionSave.trigger)
        self.ui.btnSaveAll.clicked.connect(self.save_all)
        self.ui.btnExit.clicked.connect(self.close)
        
        self.ui.btnNext.clicked.connect(self.next_image)
        self.ui.btnPrevious.clicked.connect(self.previous_image)
        self.ui.lineEditPage.returnPressed.connect(self.change_page)
        self.ui.lineEditName.returnPressed.connect(self.modify_image_name)
        
        




    def init_appearance(self):
        btn_shadow = [2,3,10,(50,50,50,64)]

        _HBMainWindowMethods.add_shadow(self.ui.btnMenu, self, *btn_shadow)
        for btn in self.btns_menu:
            _HBMainWindowMethods.add_shadow(btn, self, *btn_shadow)
 


    def init_animation(self):

        _HBMainWindowMethods.add_animation(
            self.ui.btnMenu,
            name = "show",
            prop = "size",
            duration = 150,
            startValue = self.ui.btnMenu.minimumSize(),
            endValue = self.ui.btnMenu.maximumSize()
        )

        _HBMainWindowMethods.add_animation(
            self.ui.btnMenu,
            name = "hide",
            prop = "size",
            duration = 200,
            startValue = self.ui.btnMenu.maximumSize(),
            endValue = self.ui.btnMenu.minimumSize()
        )
        
        



    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        # This If statement fix the problem that btnMenu will become min size when window resize.
        if not self.ui.widgetMenu.isHidden():
            self.ui.btnMenu.setMinimumWidth(150)

            
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 
            'Message', 
            'Are you sure you want to quit?',
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


        


