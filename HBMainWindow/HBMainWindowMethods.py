"""
To avoid too much code in HBImageBox, I separate some functions to this module.\n
This Module defines a class:_HBMainWindowMethods and some the functions that are used in HBMainWindow widgets' event.\n
Using inheritance let class "_HBMainWindowMethods" functions add to the class "HBMainWindow" .\n
"""


from PySide6.QtCore import QPropertyAnimation

from PySide6.QtGui import (
    QMouseEvent,
    QColor
)

from PySide6.QtWidgets import (
    QWidget,
    QGraphicsDropShadowEffect,
    QFileDialog
)


from HBImageBox import HBImageBox
from HBImage import HBImage, HBAlbum
from HBDialogLoad import HBDialogLoad




class _HBMainWindowMethods:
    
    def __init__(self) -> None:
        
        self.ui.hb_image_box:HBImageBox
        self.ui.hb_image_box.is_image_exist:bool
        self.hb_album:HBAlbum
        self.need_update_widget:tuple
        ...
    
    



    #----------------------staticmethod-----------------------------------

    @staticmethod
    def add_animation(self:QWidget, name:str, prop:str, duration:int, startValue, endValue):
        anim = QPropertyAnimation(self, prop.encode())
        anim.setDuration(duration)
        anim.setStartValue(startValue)
        anim.setEndValue(endValue)
        
        try:
            self.animations[name] = anim
        except(AttributeError):
            setattr(self, "animations", {name:anim})

    @staticmethod
    def add_shadow(self:QWidget, parent , Xoffset:int, Yoffset:int, BlurRadius:int, Color:tuple):
        """
        Add shadow effect to QWidget.\n
        This will also add a QGraphicsDropShadowEffect object.
        You can get that by YOUR_WIDGET.shadow.
        """

        self.shadow = QGraphicsDropShadowEffect(parent)
        self.shadow.setXOffset(Xoffset)
        self.shadow.setYOffset(Yoffset)
        self.shadow.setBlurRadius(BlurRadius)
        self.shadow.setColor(QColor(*Color))

        self.setGraphicsEffect(self.shadow)
    
    #------------------------------------------------------------


    def _max_normal_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
        self.ui.hb_image_box.update_image_box()


    def _move_window_mouse_press(self:QWidget, event:QMouseEvent):
        self.old_pos = event.globalPos()

    def _move_window_mouse_move(self:QWidget, event:QMouseEvent):
        delta_x = int(event.globalPos().x()) - self.old_pos.x()
        delta_y = int(event.globalPos().y()) - self.old_pos.y()
        self.move(self.x() + delta_x, self.y() + delta_y)
        self.old_pos = event.globalPos()


    #--------------------_update------------------------------------

    def _update(self, widgets_enable):
        if self.hb_album.is_empty is False:
            self.ui.hb_image_box.set_image(self.hb_album.marked_image)

        self._update_widgets_enable(widgets_enable)
        self._update_label_image_info()


    def _update_widgets_enable(self, enable):
        if not self.ui.hb_image_box.is_image_exist:
            return None
        for widget in self.need_update_widget:
            widget.setEnabled(enable)
            
        #set btnNext and btnPrevious enable when no image shown after click.
        is_no_next_image = (self.hb_album.bookmark==len(self.hb_album)-1)
        is_no_previous_image = self.hb_album.bookmark==0
        self.ui.btnNext.setEnabled(not is_no_next_image)
        self.ui.btnPrevious.setEnabled(not is_no_previous_image)


    def _update_label_image_info(self):
        if not self.ui.hb_image_box.is_image_exist:
            self.ui.lineEditName.setText("")
            self.ui.lineEditWidth.setText("")
            self.ui.lineEditHeight.setText("")
            self.ui.lineEditPage.setText("-")
            return None

        image_infos = self.ui.hb_image_box.image.information
        filename = image_infos.get("filename","")
        width, height = image_infos.get("size", ("",""))
        
        self.ui.lineEditName.setText(f"{filename}")
        self.ui.lineEditWidth.setText(f"{width}")
        self.ui.lineEditHeight.setText(f"{height}")
        self.ui.lineEditPage.setText(f"{self.hb_album.bookmark+1}")
        


    #------------------------------------------------------------


    def _load_images(self, filepaths):
        """Load multiple images.\n
        Args:
            filepaths (list[str]): image files' path or url.
        """
        try:
            if self.hb_album.is_empty:
                self.hb_album.load(filepaths)
                self.hb_album.bookmark=0
            else:
                temp_album = HBAlbum(filepaths)
                self.hb_album.merge(temp_album)
            self._update(True)
        except Exception as e:
            self.ui.hb_image_box._show_msg_box('Error!', e)


    def _add_image(self):
        """This funciton is called when image was load by these functions:\n
        "hb_image_box._paste", "hb_image_box.load_image"
        """
        self.hb_album.append(self.ui.hb_image_box.image)
        self.hb_album.bookmark = len(self.hb_album)-1
        self._update(True)
        

    def _remove_image(self):
        if self.hb_album.is_empty:
            raise FileNotFoundError("Try to remove nothing.")
        
        self.hb_album.delete(self.hb_album.bookmark)
        

        self._update(widgets_enable=(not self.hb_album.is_empty))


    #--------------------Menu related------------------------
    
    def _show_hide_menu(self):
        Menu = self.ui.widgetMenu
        btnMenu = self.ui.btnMenu

        if Menu.isHidden():
            Menu.show()
            btnMenu.animations["show"].start()
        else:
            Menu.hide()
            btnMenu.animations["hide"].start()
            btnMenu.setMinimumWidth(70)

    def load(self):
        self.dialog_load = HBDialogLoad()
        self.dialog_load.signal_load.connect(self._load_images)
        self.dialog_load.exec() #會堵住
        #self.dialog_load.show() #沒有堵住



    def save_all(self):
        if not self.ui.hb_image_box.is_image_exist:
            return None

        folder_path = QFileDialog.getExistingDirectory(
            self,
            "Choose Image Save Folder",
            "./" #initial path 
        )
        if folder_path != "":
            self.hb_album.save(folder_path)
            
    def next_image(self):
        self.hb_album.bookmark += 1
        self._update(True)
    
    def previous_image(self):
        self.hb_album.bookmark -= 1
        self._update(True)
    
    def change_page(self):
        new_value = self.ui.lineEditPage.text()
        try:
            new_value = int(new_value)
        except Exception:
            self.hb_album.bookmark = len(self.hb_album)-1
            self._update(True)
            return None

        self.hb_album.bookmark = new_value-1
        self._update(True)
        
    def modify_image_name(self):
        new_value = self.ui.lineEditName.text()
        if (not self.ui.hb_image_box.is_image_exist) or (new_value==""):
            self._update(True)
            return None


        self.ui.hb_image_box.image.information = {"filename":new_value}
        self._update(True)
















