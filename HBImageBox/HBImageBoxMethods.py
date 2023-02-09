"""
To avoid too much code in HBImageBox, I separate some functions to this module.\n
This Module defines a class:_HBImageBoxMethods and some the functions that are used in HBImageBox widgets' event.\n
Using inheritance let class "HBImageBoxMethods" functions add to the class "HBImageBox" .\n
"""

from abc import ABC, abstractmethod

from PySide6.QtCore import Signal,QSize,QMimeData,QUrl
from PySide6.QtGui import QPixmap,QImage,QUndoStack,QMovie

from PySide6.QtWidgets import (
    QLabel,
    QMenu,
    QApplication,
    QMenuBar,
    QMessageBox
)

from HBImage import HBImage
from .HBImageBoxLabel import HBImageBoxLabel
from .HBImageProcessCommand import (
    CommandCropImage,
    CommandFlipImage,
    CommandColorImage,
    CommandRotateImage,
    CommandDrawImage
)



"""Decorator : _image_process"""
def _image_process(process_function):
    def do_process(self):
        if self.is_image_exist is False:
            return None

        process_function(self)
        self.update_image_box()

    return do_process



class _HBImageBoxMethods():
    """To avoid too much code in HBImageBox, 
    I separate some functions to this module.
    Using inheritance let class "_HBImageBoxMethods"'s functions add to the class "HBImageBox".
    """
    #signal
    image_removed:Signal = ...
    image_loaded:Signal = ...
    image_processed:Signal = ...
    
    def __init__(self,*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._image:HBImage
        self.image:HBImage
        self.hb_image_box_label:HBImageBoxLabel
        self.menu_processor:QMenu
        self.menu_bar:QMenuBar
        self._image_process_undo_stack:QUndoStack



    @property
    @abstractmethod
    def is_image_exist(self) -> bool:
        ...

    @property
    @abstractmethod
    def display_mode(self) -> str:
        ...

    @property
    @abstractmethod
    def draw_color(self) -> tuple:
        ...

    @abstractmethod
    def update_image_box(self):
        ...

    @abstractmethod
    def update_widgets_enable(self, enable: bool):
        ...

    @abstractmethod
    def show_image(self):
        ...

    @abstractmethod
    def set_image(self, image:'HBImage'):
        ...

    def _show_msg_box(self, title, msg):
        return QMessageBox.information(
            self, title,
            f'{msg}',
            QMessageBox.Ok
        )

    def _show_original_size_image(self, hb_image: 'HBImage', q_label:QLabel):
        """This function will set q_label's size = hb_image's size.
        Then set image on q_label.

        Args:
            hb_image (HBImage)\n
            q_label (QLabel)
        """
        pixmap_image = QPixmap(hb_image.to_qt().image)
        image_original_size = hb_image.size
        self._zoom_scale = 1

        q_label.setPixmap(pixmap_image)
        q_label.setFixedSize(QSize(*image_original_size))
    
    def _show_gif_image(self, hb_image:'HBImage', q_label:QLabel):
        if hb_image.information["format"]!="gif":
            return None

        movie = QMovie(hb_image.information["filepath"])
        q_label.setMovie(movie)
        movie.start()      

    
    def _show_resized_image(self, hb_image: 'HBImage', q_label: QLabel):
        """This function will resized the hb_image(copy) to fit q_label's size.
        Then set image on q_label.

        Args:
            hb_image (HBImage): _description_
            q_label (QLabel): _description_
        """
        label_size = q_label.size().toTuple()
        resized_image = hb_image.to_fit_container(label_size)
        resized_image = QPixmap(resized_image.to_qt().image)
        
        q_label.setPixmap(resized_image)
        



    def _show_information(self):
        if not self.is_image_exist:
            return None
        image_infos = self.image.information
        infos_strs = []
        infos_strs.append("[File Name] : " + image_infos.get("filename", "untitled"))
        infos_strs.append("[File Path] : " + image_infos.get("filepath", "unknown"))
        infos_strs.append("[File Format] : " + image_infos.get("format"))
        infos_strs.append("[Image Size] : " + str(image_infos.get("size")))
        infos_strs.append("[Selected Area] : " + str(self.image.ROI))

        infos_msg = "\n".join(infos_strs)
        self._show_msg_box("Image Infos",infos_msg)


    #----------------for QEvent-------------------
    def _exec_menu_processor(self, event):
        self.menu_processor.exec(self.hb_image_box_label.mapToGlobal(event.position().toPoint()))


    def _remove_image(self):
        if not self.is_image_exist:
            return None
        
        self._image = None
        self.hb_image_box_label.setFixedSize(self.size())
        self.update_image_box()
        self.update_widgets_enable(self.is_image_exist)
        self._image_process_undo_stack.clear()
        self.image_removed.emit()

    def _copy_image_to_clipboard(self):
        if not self.is_image_exist:
            return None
        clipboard = QApplication.clipboard()
        data = QMimeData()
        data.setImageData(QImage(self.image.crop().to_qt().image))
        clipboard.setMimeData(data)


    def _paste(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        is_load_successful = False
        _image_infos = {
                "filename":"untitle",
                "filepath":"from clipboard",
                "format":"png"
        }

        if mimeData.hasImage():
            q_pixmap = QImage(mimeData.imageData())
            clipboard_image = HBImage.load_from_qimage(q_pixmap, **_image_infos)
            is_load_successful = True

        elif mimeData.hasText():
            clipboard_text = QUrl(mimeData.text())

            if not clipboard_text.isValid(): 
                return None
            
            #if clipboard_text is url, then try to load it.
            try:
                clipboard_image = HBImage(clipboard_text.url())
                is_load_successful = True
            except Exception as e:
                self._show_msg_box("Error!",e)
            

        else:
            raise TypeError("Cannot display data")
        
        if is_load_successful:
            self.set_image(clipboard_image)
            self.image_loaded.emit()
        


    def _set_image_ROI(self, _roi):
        if not self.is_image_exist:
            return None
        
        self.image.ROI = _roi
        if self.display_mode == "zoom":
            self.image.ROI_fit_resized_image()


    def _set_image_fit_offset(self):
        if not self.is_image_exist:
            return None

        label_size = self.hb_image_box_label.size().toTuple()
        box_size = self.size().toTuple()

        _x_offset = (box_size[0]-label_size[0])//2
        _y_offset = (box_size[1]-label_size[1])//2
        
        _x_offset = _x_offset if _x_offset>0 else 0
        _y_offset = _y_offset if _y_offset>0 else 0
        
        self.image.fit_offset = (_x_offset,_y_offset)



    def _scale_label_size(self, base_size:tuple, scale):
        """let label and showed image(copy) size = scale*original size.

        Args:
            base_size (tuple(int,int)):  
            scale (float): new label size = scale * original size.
        """
        if not isinstance(base_size[0], int):
            raise TypeError("original size's type should be a tuple with int.")

        new_label_size = (int(scale*base_size[0]), int(scale*base_size[1]))
        self.hb_image_box_label.setFixedSize(QSize(*new_label_size))


    def _zoom(self):
        if not self.is_image_exist:
            raise AttributeError("There is no image.")
        

        self._scale_label_size(self.image.size, self.zoom_scale)
        #self._show_resized_image(self.image, self.hb_image_box_label)
        self.hide_rubber_band()
        self.update_image_box()




    #----------------------image_process--------------------
    
    def _do_image_process(self, command):
        if self.is_image_exist is False:
            return None
        self._image_process_undo_stack.push(command)
        self.image_processed.emit()

    def _crop_image(self):
        self._do_image_process(CommandCropImage(self))

    def _H_flip_image(self):
        self._do_image_process(CommandFlipImage(self,"H"))

    def _V_flip_image(self):
        self._do_image_process(CommandFlipImage(self,"V"))

    def _gray_image(self):
        self._do_image_process(CommandColorImage(self,"Gray"))

    def _color_invert(self):
        self._do_image_process(CommandColorImage(self,"Invert"))

    def _rotate_90_image(self):
        self._do_image_process(CommandRotateImage(self,90))

    def _draw_rect(self):
        self._do_image_process(CommandDrawImage(self,"Rect",self.draw_color))

        
        




