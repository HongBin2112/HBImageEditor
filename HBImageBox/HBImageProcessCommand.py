
from PySide6.QtGui import QUndoCommand

from HBImage import HBImage



class CommandImageProcess(QUndoCommand):
    def __init__(self, _hb_image_box, *args):
        super().__init__(args[0])
        self.image_box = _hb_image_box
        #This store ROI when undo was called. 
        #Then this ROI will imply when redo was called.
        #(only "redo" action called)
        self.undo_ROI = None

    def redo(self):
        if self.undo_ROI:
            self.image_box._image.ROI = self.undo_ROI
            self.undo_ROI = None
            self.image_box.show_ROI()
        # implement undo logic here

    def undo(self):
        # implement undo logic here
        if self.undo_ROI is None:
            self.undo_ROI = self.image_box._image.ROI
            self.image_box.show_ROI()
        # implement undo logic here


#=============================================================================================
class CommandCropImage(CommandImageProcess):
    def __init__(self, _hb_image_box):
        super(CommandCropImage, self).__init__(_hb_image_box, "Crop")

        self.pre_image:'HBImage' = _hb_image_box.image
        self.pre_zoom_scale = _hb_image_box.zoom_scale

    def redo(self):
        super().redo()
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
        super().undo()
    
#=============================================================================================

class CommandFlipImage(CommandImageProcess):
    def __init__(self, _hb_image_box, direction:str):
        super().__init__(_hb_image_box, f"Flip {direction}")

        self.pre_ROI = _hb_image_box.image.ROI

        #direction's value is "H" or "V"
        if direction!="H" and direction!="V":
            raise ValueError(f"direction's value should be 'H' or 'V', not {direction}")
        self.direction = direction

    def redo(self):
        super().redo()

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
        super().undo()



#=============================================================================================

class CommandColorImage(CommandImageProcess):
    def __init__(self, _hb_image_box, color_process:str):
        super().__init__(_hb_image_box, f"Color {color_process}")

        self.pre_image:'HBImage' = _hb_image_box.image

        if color_process!="Gray" and color_process!="Invert":
            raise ValueError(f"direction's value should be 'Gray' or 'Invert', not {color_process}")
        self.color_process = color_process
        
    def redo(self):
        super().redo()
        if self.color_process=="Gray":
            self.image_box._image = self.pre_image.to_gray()
        elif self.color_process=="Invert":
            self.image_box._image = self.pre_image.color_invert()

        self.image_box.update_image_box()


    def undo(self):
        self.image_box._image = self.pre_image
        self.image_box.update_image_box()
        super().undo()



#=============================================================================================

class CommandRotateImage(CommandImageProcess):
    def __init__(self, _hb_image_box, angle:int):
        super().__init__(_hb_image_box, f"Rotate {angle}")
        
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




#=============================================================================================

class CommandDrawImage(CommandImageProcess):
    def __init__(self, _hb_image_box, shape:str, color:tuple):
        super().__init__(_hb_image_box, f"Draw {color} {shape}")
        self.color = color
        self.shape = shape
        self.draw_area = self.image_box._image.ROI
        self.pre_image:'HBImage' = _hb_image_box.image


    def redo(self):
        #super().redo()
        if self.shape == "Rect":
            self.image_box._image = self.image_box.image.copy()
            self.image_box._image.draw_rect(rect=self.draw_area, outline_color=self.color)
            
        self.image_box.update_image_box()

    def undo(self):
        self.image_box._image = self.pre_image
        self.image_box.update_image_box()
        #super().undo()






