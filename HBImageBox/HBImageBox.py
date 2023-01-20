"""
HBImageBox is custom widget inherited from "PySide6.QtWidgets.QWidget".

Require package:
1. Pyside
2. PIL
3. HBImage
"""


from PySide6.QtCore import Signal,Qt
from PySide6.QtGui import (
    QDropEvent,
    QDragEnterEvent,
    QWheelEvent,
    QUndoStack
)

from PySide6.QtWidgets import QWidget,QScrollArea,QFileDialog


from HBImage import HBImage
from .HBImageBoxUi import _HBImageBoxUi
from .HBImageBoxMethods import _HBImageBoxMethods



class HBImageBox(_HBImageBoxUi, _HBImageBoxMethods):
    """HBImageBox is custom widget inherited from "PySide6.QtWidgets.QWidget".
    """
    
    #signal
    image_removed:Signal = Signal()
    image_loaded:Signal = Signal()

    def __init__(self, parent:QWidget=None) -> None:
        super().__init__(parent)

        self._image:HBImage = None
        #display_mode:["original_size", "gif", "zoom"]
        self._display_mode = "original_size"
        self._zoom_scale = 1
        self._image_process_undo_stack = QUndoStack()
        self._image_process_undo_stack.setUndoLimit(10)
        #print(self._image_process_undo_stack.canUndo())
        self.set_events()



    @property
    def is_image_exist(self) -> bool:
        return not (self.image is None)

    @property
    def display_mode(self) -> str:
        return self._display_mode

    @property
    def zoom_scale(self) -> float:
        return self._zoom_scale

    @property
    def image(self) -> 'HBImage':
        return self._image

    @image.setter
    def image(self, value):
        raise PermissionError("Use function \"set_image(image)\" to set image instead.")



    def set_events(self):
        self.scroll_area.wheelEvent = self._scroll_zoom
        
        self.hb_image_box_label.right_mouse_button_clicked.connect(self._exec_menu_processor)
        self.hb_image_box_label.area_selected.connect(self._set_image_ROI)

        self.actionLoad.triggered.connect(self.load_image)
        self.actionSave.triggered.connect(self.save_image)
        self.actionCopy.triggered.connect(self._copy_image_to_clipboard)
        self.actionPaste.triggered.connect(self._paste)
        self.actionRemove.triggered.connect(self._remove_image)
        self.actionInformation.triggered.connect(self._show_information)

        self.actionCrop.triggered.connect(self._crop_image)
        self.actionHorizontal.triggered.connect(self._H_flip_image)
        self.actionVertical.triggered.connect(self._V_flip_image)
        self.actionGray.triggered.connect(self._gray_image)
        self.actionInvert.triggered.connect(self._color_invert)
        self.actionRotate_90.triggered.connect(self._rotate_90_image)

        self.actionUndo.triggered.connect(self._image_process_undo_stack.undo)
        self.actionRedo.triggered.connect(self._image_process_undo_stack.redo)
        self._image_process_undo_stack.canUndoChanged.connect(self.actionUndo.setEnabled)
        self._image_process_undo_stack.canRedoChanged.connect(self.actionRedo.setEnabled)

    def set_image(self, image:'HBImage'):
        if not isinstance(image, HBImage):
            return None
        self._image = image
        self._display_mode = "original_size"
        self._zoom_scale = 1

        self.update_image_box()
        self.update_widgets_enable(self.is_image_exist)
        self.hb_image_box_label.hide_rubber_band()
        

    def update_widgets_enable(self, enable):
        self.menu_edit.setEnabled(enable)
        self.actionCopy.setEnabled(enable)
        self.actionSave.setEnabled(enable)
        self.actionRemove.setEnabled(enable)
        self.actionInformation.setEnabled(enable)

    def update_image_box(self):
        self.show_image()
        if self.display_mode=="zoom":
            pass
            #self.hb_image_box_label.hide_rubber_band()
        #print("self.display_mode:",self.display_mode)

    def show_image(self):
        if not self.is_image_exist:
            self.hb_image_box_label.setText("Drag Image Here")
            return None

        if self.display_mode=="original_size":
            self._show_original_size_image(self.image, self.hb_image_box_label)
        elif self.display_mode=="zoom":
            self._show_resized_image(self.image, self.hb_image_box_label)

    def hide_rubber_band(self):
        self.hb_image_box_label.hide_rubber_band()
        
    def show_ROI(self):
        if self.image.is_ROI_empty:
            return None
        
        roi = self.image.ROI
        if self.display_mode=="zoom":
            roi = [p*self.zoom_scale for p in roi]
        self.hb_image_box_label.show_rubber_band(roi)


    def load_image(self) -> bool:
        """This funciton will open a QFileDialog,
        and then set image to widget.

        Returns:
            bool: If successfully load return True, else False.
        """
        file_dialog = QFileDialog(self)
        file_abs_path, file_type = file_dialog.getOpenFileName(
            self,
            "Select Image",
            "./",
            "All Files(*);;Image (*.png *.bmp *.jpg *.jpeg);;Text File (*.txt)"
        )
        if file_abs_path=="":
            return None
        try:
            self._image = HBImage(file_abs_path)
            self.set_image(self.image)
        except Exception as e:
            self._show_msg_box('Error!', e)
            return False

        self.image_loaded.emit()
        return True


    def save_image(self):
        if not self.is_image_exist:
            return None

        img_infos = self.image.information
        filename, format = img_infos["filename"], img_infos["format"]

        filepath, filetype = QFileDialog.getSaveFileName(
            self,
            "Save Image",  
            f"./{filename}", #initial path 
            "All Files (*);;Images (*.png *.bmp *.jpg *.jpeg)"
        )
        if filepath != "":
            self.image.save(filepath) 


    def _scroll_zoom(self, event:QWheelEvent):
        """change showed image size.
        This function set on the widget : "self.scroll_area" 's WheelEvent.

        Args:
            event (QWheelEvent): _description_
        """
        
        if event.modifiers() == Qt.ControlModifier: #if "ctrl" is pressed.
            wheel_angle = event.angleDelta().y()
            self._display_mode = "zoom"
            
            if wheel_angle>0:
                self._zoom_scale += 0.1
            elif wheel_angle<0:
                self._zoom_scale = 0.1 if (self._zoom_scale<=0.2) else (self._zoom_scale - 0.1)
                
            self._scale_label_size(self.image.size, self.zoom_scale)
            self.hide_rubber_band()
            self.update_image_box()

        else:
            super(QScrollArea,self.scroll_area).wheelEvent(event)


    #------------QEvent--------------

    def dragEnterEvent(self, event:QDragEnterEvent):
        super().dragEnterEvent(event)
        self.activateWindow()
        if event.mimeData().hasUrls():
            event.acceptProposedAction()


    def dropEvent(self, event:QDropEvent):
        super().dropEvent(event)

        if not event.mimeData().hasUrls():
            return False

        filepath = event.mimeData().urls()[0] 
        filepath = filepath.toLocalFile()
        
        self.set_image(HBImage(filepath))
        self.image_loaded.emit()
    
    
    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self._set_image_fit_offset()
        self.hide_rubber_band()
        return None



    




