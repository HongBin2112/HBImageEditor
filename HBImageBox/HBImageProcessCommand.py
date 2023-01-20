from PySide6.QtGui import QUndoCommand

from HBImage import HBImage


class CommandImageProcess(QUndoCommand):
    def __init__(self, _hb_image_box, process: str):
        super().__init__("Image Process")
        self.image_box = _hb_image_box
        #This store ROI when undo called. 
        #Then this ROI will imply when redo called.
        #(only "redo" action called)
        self.undo_ROI = None

    def redo(self):
        if self.undo_ROI:
            self.image_box._image.ROI = self.undo_ROI
            self.undo_ROI = None
        ...

    def undo(self):
        # implement undo logic here
        ...
        if self.undo_ROI is None:
            self.undo_ROI = self.image_box._image.ROI


class CommandCropImage(QUndoCommand):
    def __init__(self, _hb_image_box):
        super().__init__("Crop")

        self.pre_image:'HBImage' = _hb_image_box.image
        self.pre_zoom_scale = _hb_image_box.zoom_scale
        self.image_box = _hb_image_box

        self.undo_ROI = None 

        
    def redo(self):
        if self.undo_ROI:
            self.image_box._image.ROI = self.undo_ROI
            self.undo_ROI = None

        self.image_box._image = self.pre_image.crop()
        
        if self.image_box.display_mode=="zoom":
            self.image_box._scale_label_size(self.image_box.image.size, self.image_box.zoom_scale)

        self.image_box.update_image_box()
        self.image_box.hide_rubber_band()

    def undo(self):
        self.image_box._image = self.pre_image
        if self.image_box.display_mode=="zoom":
            self.image_box._scale_label_size(self.image_box.image.size, self.pre_zoom_scale)
        self.image_box.update_image_box()
        self.image_box.show_ROI()

        if self.undo_ROI is None:
            self.undo_ROI = self.image_box._image.ROI
    

class CommandFlipImage(QUndoCommand):
    def __init__(self, _hb_image_box, direction:str):
        super().__init__(f"Flip {direction}")
        self.image_box = _hb_image_box
        self.pre_ROI = _hb_image_box.image.ROI
        self.undo_ROI = None 
        #direction's value is "H" or "V"
        if direction!="H" and direction!="V":
            raise ValueError(f"direction's value should be 'H' or 'V', not {direction}")
        self.direction = direction
        
        
    
    def redo(self):
        if self.undo_ROI:
            self.image_box._image.ROI = self.undo_ROI
            self.undo_ROI = None

        if self.direction=="H":
            self.image_box._image = self.image_box.image.filp_horizontal()
        elif self.direction=="V":
            self.image_box._image = self.image_box.image.filp_vertical()
        self.image_box.update_image_box()

        
    def undo(self):
        self.image_box._image.ROI = self.pre_ROI

        if self.direction=="H":
            self.image_box._image = self.image_box.image.filp_horizontal()
        elif self.direction=="V":
            self.image_box._image = self.image_box.image.filp_vertical()

        self.image_box.update_image_box()

        if self.undo_ROI is None:
            self.undo_ROI = self.image_box._image.ROI



class CommandColorImage(QUndoCommand):
    def __init__(self, _hb_image_box, color_process:str):
        super().__init__(f"Color {color_process}")

        self.pre_image:'HBImage' = _hb_image_box.image
        self.image_box = _hb_image_box
        self.undo_ROI = None
        if color_process!="Gray" and color_process!="Invert":
            raise ValueError(f"direction's value should be 'Gray' or 'Invert', not {color_process}")
        self.color_process = color_process
        
    def redo(self):
        if self.undo_ROI:
            self.image_box._image.ROI = self.undo_ROI
            self.undo_ROI = None

        if self.color_process=="Gray":
            self.image_box._image = self.pre_image.to_gray()
        elif self.color_process=="Invert":
            self.image_box._image = self.pre_image.color_invert()

        self.image_box.update_image_box()


    def undo(self):
        self.image_box._image = self.pre_image
        self.image_box.update_image_box()
        if self.undo_ROI is None:
            self.undo_ROI = self.image_box._image.ROI





class CommandRotateImage(QUndoCommand):
    def __init__(self, _hb_image_box, angle:int):
        super().__init__(f"Rotate {angle}")
        self.image_box = _hb_image_box
        self.angle = angle
        
    def _set_rotated_image(self):
        self.image_box._scale_label_size(self.image_box.image.size, self.image_box.zoom_scale)
        self.image_box.hide_rubber_band()
        self.image_box.update_image_box()   

    def redo(self):
        self.image_box._image = self.image_box.image.rotate(self.angle)
        self._set_rotated_image()

    def undo(self):
        self.image_box._image = self.image_box.image.rotate(360-self.angle)
        self._set_rotated_image()



