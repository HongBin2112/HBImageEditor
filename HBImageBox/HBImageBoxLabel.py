"""
HBImageBoxLabel is custom widget inherited from "PySide6.QtWidgets.QLabel".

Require package:
1. Pyside
2. PIL
3. HBImage
"""


from PySide6.QtCore import (
    QEvent,
    QRect,
    QSize,
    Qt,
    Signal
)

from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QLabel, QRubberBand,QSizePolicy




class HBImageBoxLabel(QLabel):

    #signal
    right_mouse_button_clicked:Signal = Signal(QMouseEvent)
    area_selected:Signal = Signal(tuple)


    def __init__(self, parent=None):
        super().__init__(parent)

        sizePolicy0 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy0.setHorizontalStretch(0)
        sizePolicy0.setVerticalStretch(0)
        self.setSizePolicy(sizePolicy0)

        self._selected_area :tuple(int,int,int,int) = (0,0,0,0)
        self._is_selecting :bool = False
        self._rubber_band = QRubberBand(QRubberBand.Rectangle, self)
        
        self.setText(f"Drag Image Here")
        

    @property
    def selected_area(self) -> tuple:
        """Returns:
            tuple(int,int,int,int): left top point(x0,y0) and right bottom point(x1,y1) coordinates(x0,y0,x1,y1).
        """
        return self._selected_area

    @selected_area.setter
    def selected_area(self, _box:tuple):
        self._selected_area = self.limit_box(_box)




    def limit_box(self, _box):
        """this function limit the box coordinates between [0, HBImageBoxLabel.size).

        Args:
            _box (tuple(int,int,int,int))

        Returns:
            tuple(int,int,int,int): new box after limited.
        """
        img_W, img_H = self.size().toTuple()
        x0, y0, x1, y1 = _box
        x0 = self._limit_number(x0, 0, img_W-1)
        y0 = self._limit_number(y0, 0, img_H-1)
        x1 = self._limit_number(x1, 0, img_W-1)
        y1 = self._limit_number(y1, 0, img_H-1)

        return (x0, y0, x1, y1)



    def hide_rubber_band(self):
        if not self._is_selecting:
            self._rubber_band.hide()

    def show_rubber_band(self, box:tuple=None):
        """
        Args:
            box (tuple(int,int,int,int), optional): 
            If box is given, use rubber_band to show the given area.
        """
        if box is None:
            if not self._is_selecting:
                self._rubber_band.show()
            return None
        
        x0,y0,x1,y1 = box
        width = abs(x1-x0)
        height = abs(y1-y0)
        self._rubber_band.setGeometry(QRect(x0,y0,width,height))
        self._rubber_band.show()        
        




    #------------------QEvent--------------------------------

    def mousePressEvent(self, event:QMouseEvent):
        super().mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self._image_box_select_area_press(event)
            self._is_selecting = True
        elif event.button() == Qt.RightButton:
            self.right_mouse_button_clicked.emit(event)


    def mouseMoveEvent(self, event:QMouseEvent):
        super().mouseMoveEvent(event)
        if self._is_selecting:
            self._image_box_select_area_move(event)


    def mouseReleaseEvent(self, event:QMouseEvent):
        super().mouseReleaseEvent(event)
        if not self._is_selecting:
            return None
        self._image_box_select_area_release(event)
        self._is_selecting = False
        self.area_selected.emit(self.selected_area)
        #print(self.selected_area)





    #-----------------private function-------------------------------

    def _image_box_select_area_press(self, event:QEvent):
        self._select_start_point = event.position().toPoint()
        self._rubber_band.setGeometry(QRect(self._select_start_point, QSize()))
        self._rubber_band.show()


    def _image_box_select_area_move(self, event:QEvent):
        self._rubber_band.setGeometry(
            QRect(
                self._select_start_point, #start point
                event.position().toPoint() #end point
            ).normalized() #normalized() to let QRect's coords x0<x1, y0<y1. 
        )


    def _image_box_select_area_release(self, event:QEvent):
        rubber_band_area = self._rubber_band.geometry()
        
        if not rubber_band_area.isValid():
            self.selected_area = (0,0,0,0)
            return None
        self.selected_area = self._rubber_band.geometry().getCoords()
        #self.setText(f"selected_area:{self.selected_area}")

    def _limit_number(self, x, lower, upper):
        return max(lower, min(x, upper))