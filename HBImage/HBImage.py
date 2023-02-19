from os import path
from urllib.request import urlopen,Request

from PIL import (
    Image,
    ImageGrab,
    ImageQt,
    ImageDraw,
    ImageChops
)

from . import HBCommon



#Decorator define
def image_process(image_process_function):
    """Decorator.\n
    If ROI is set, the function only modified this region.

    Args:
        image_process_function (function): Decorated
    """
    def do_process(self:'HBImage'):
        
        if self.is_ROI_empty:
            return image_process_function(self)
        else:
            process_image = self.crop()
            process_image = image_process_function(process_image)
            return self.paste(process_image)

    return do_process









class HBImage:

    def __init__(self, source,**kwargs):
        self._is_empty = True
        self._image = None
        self._roi = (0, 0, 0, 0)
        self._information = dict.fromkeys([
            "filename","filepath","format","size"
        ])

        """The fit_ratio and fix_offset parameters are used to adjust the difference
        in coordinates between the container and the image size."""
        self._fit_ratio:float = 1.0
        self._fit_offset:tuple = (0, 0)

        self.load(source,**kwargs)


    def __str__(self):
        return self.information

    def __delete__(self, instance):
        self._is_empty = True
        self._image.close()
        self._information = None
        del self._image

    def _repr_png_(self):
        """
        This function let you can show image directly in Notebook output with only typing "your_hb_image".
        """
        return display(self._image)


    @property
    def filename(self):
        return self.information.get("filename","untitled")

    @filename.setter
    def filename(self, filename:str):
        self.information = {"filename":filename}

    @property
    def format(self):
        _format = self.information.get("format")
        if _format:
            return _format
        
        try:
            return self._image.format.lower()
        except Exception:
            return "png"

    @property
    def size(self):
        return self._image.size

    @property
    def image(self):
        return self._image

    @property
    def information(self):
        if self._is_empty:
            return None

        self._information["size"] = (self._image.width, self._image.height)

        return self._information

    @information.setter
    def information(self, infos:dict):
        if infos:
            HBCommon.update_dict_only_existing_keys(self._information, infos)

    @property
    def is_empty(self):
        return self._is_empty

    @property
    def is_ROI_empty(self):
        return self.ROI == (0,0,0,0)

    @property
    def ROI(self):
        """ROI represented as a tuple of four int values: (x0, y0, x1, y1).
        If the ROI extends beyond the boundaries of the image,
        the ROI is adjusted to fit within the image.
        """
        #x0, y0, x1, y1 = self._roi
        return self._limit_box(self._roi)


    @ROI.setter
    def ROI(self, _roi):
        """ROI will turn into (int) if Passing variable is (float), 
        
        Args:
            ROI (tuple(int,int,int,int))
        """

        x0, y0, x1, y1 = _roi
        if x0 > x1:
            x0, x1 = x1, x0
        if y0 > y1:
            y0, y1 = y1, y0
        
        if x0==x1 or y0==y1:
            self._roi = (0,0,0,0)
        else:
            self._roi = (int(x0), int(y0), int(x1), int(y1))


    @property
    def fit_offset(self):
        """fit_offset is used for correcting the coordinates 
        between the image and the GUI widget.

        Returns:
            self._fit_offset: tuple(int,int)
        """
        return self._fit_offset

    @fit_offset.setter
    def fit_offset(self, offset:tuple):
        x_offset, y_offset = offset
        self._fit_offset = (int(x_offset), int(y_offset))
        


    #-----------------staticmethod-------------------------------

    @staticmethod
    def load_from_clipboard():
        """
        can get the image from the clipboard. As of PIL version 9.1.0 (April 2022),
        it is available only for Windows and macOS.
        """
        clipboard_img = ImageGrab.grabclipboard()
        if clipboard_img:
            infos = {
                "filename":"untitle",
                "filepath":"from clipboard",
                "format":"png"
            }
            return HBImage(clipboard_img, **infos)
        else:
            raise AttributeError("Load Nothing Or Cannot Load Image From Clipboard.")


    @staticmethod
    def load_from_qimage(source, **image_infos):
        """load image from pyside/pyqt QImage."""
        hb_qt_img = HBImage(ImageQt.fromqimage(source), **image_infos)
            

        return hb_qt_img



    #--------------private fuctions------------------------------

    def _limit_box(self, _box):
        """this function limit the box coordinates between [0, image.size).

        Args:
            _box (tuple(int,int,int,int))

        Returns:
            tuple(int,int,int,int): new box after limited.
        """
        img_W, img_H = self.size
        x0, y0, x1, y1 = _box
        x0 = HBCommon.limit_number(x0, 0, img_W-1)
        y0 = HBCommon.limit_number(y0, 0, img_H-1)
        x1 = HBCommon.limit_number(x1, 0, img_W-1)
        y1 = HBCommon.limit_number(y1, 0, img_H-1)

        return (x0, y0, x1, y1)



    #------------------------------------------------

    def load(self, source,**kwargs):
        """
        According to the type of the passed-in parameter, use a different load method:
        If the passed-in parameter type is...
        - String, then it is determined to be an image file path.
        - HBImage, then its image is copied to self.image.
        - PIL.Image.Image or its subclass, then it is copied to self.image.
        """
        if isinstance(source, str):
            if HBCommon.is_url(source):
                headers = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
                }
                req = Request(source, headers=headers)
                self._image = Image.open(urlopen(req))  
            else: 
                self._image = Image.open(source)

            self.information = {
                "filename":HBCommon.get_file_basename(source),
                "filepath":source,
                "format":self._image.format.lower()
            }
        elif isinstance(source, HBImage):
            self._image = source.image.copy()
            self._roi = source.ROI
            self.information = source.information

        elif isinstance(source, Image.Image):
            self._image = source.copy()
            self.information = kwargs

        else:
            raise TypeError(f"Cannot Load {type(source)}.")

        self._is_empty = False



    def save(self, filepath, format = None, **kwargs):
        if format is None:
            self._image.save(filepath)
            return None
        
        name, name_format = HBCommon.get_file_name_and_format(filepath)
        new_filename = f"{name}.{format}"
        self._image.save(new_filename, format, kwargs)

        

    def copy(self):
        """return HBImage(self)"""
        return HBImage(self)

    def crop(self, box=None):
        """Returns a rectangular region from this image.\n
        If ROI is set, then crop ROI. 
        If box parameter and ROI both set, crop box region.
        Else both are None, return hbimage self.

        Args:
            box (tuple(int,int,int,int), optional): The crop rectangle, 
            as a (left, upper, right, lower)-tuple. Defaults to None.

        Returns:
            HBImage: _description_
        """
        if box:
            return HBImage(self._image.crop(self._limit_box(box)), **self.information)
        if self.is_ROI_empty:
            return self

        return HBImage(self._image.crop(self.ROI), **self.information)


    def draw_rect(self, rect=None, fill_color=None, outline_color="blue", outline_width=1):
        if rect is None:
            rect = self.ROI
        if self.is_ROI_empty:
            return None
        draw = ImageDraw.Draw(self.image)
        draw.rectangle(rect, fill_color, outline_color, outline_width)


    def paste(self, other_hbimage):
        """Pastes another image into this image.

        Args:
            other_hbimage (HBImage)
        Returns:
            HBImage
        """
        hb_image = self.copy()
        hb_image._image.paste(other_hbimage.image,self.ROI)
        return hb_image
        

    def split(self, pos:int, axis:str) -> list:
        """Split an image into two images along a line

        This function splits an image into two separate images, based on the line
        defined by `axis=pos`.\n
        For example, if `pos=300` and `axis="x"`, the
        image will be split along the line `x=300` and the two resulting images
        will be `image0=self.crop((0,0,pos,h))` and `image1=self.crop((pos,0,w,h))`.

        Args:
            pos (int): The index at which to split the image.
            axis (str): Either "x" or "y". Specifies the axis along which to split the image.

        Returns:
            List[HBimage, HBimage]: A list containing the two resulting images.

        Raises:
            ValueError: If `axis` is not "x" or "y".
        """

        w,h = self.size
        if axis == 'y':
            box0 = (0,0,w,pos)
            box1 = (0,pos,w,h)
        elif axis == 'x':
            box0 = (0,0,pos,h)
            box1 = (pos,0,w,h)
        else:
            raise ValueError('axis must be either "x" or "y"')
        
        hbimage0 = self.crop(box0)
        hbimage1 = self.crop(box1)
            
        return [hbimage0, hbimage1]

    def to_qt(self):
        """
        This will return a HBImage object.\n
        with the image that is converted to PIL.ImageQt.ImageQt class.
        """
        qt_hb_img = self.copy()
        qt_hb_img._image = ImageQt.ImageQt(qt_hb_img.image)
        return qt_hb_img



    def to_fit_container(self, container_size: tuple):
        """
        Enlarge image until it width or height is the same as container_size.
        """
        original_width, original_height = self.size
        container_width, container_height = container_size

        x_ratio = container_width / original_width
        y_ratio = container_height / original_height

        self._fit_ratio = x_ratio if (x_ratio < y_ratio) else y_ratio

        new_width = round(original_width * self._fit_ratio, 2)
        new_height = round(original_height * self._fit_ratio, 2)
        new_size = (int(new_width), int(new_height))

        new_width = container_width if (new_width >= container_width) else new_width
        new_height = container_height if (new_height >= container_height) else new_height

        if x_ratio < y_ratio:
            self._fit_offset = (0, (container_height-new_height)//2)
        else:
            self._fit_offset = ((container_width-new_width)//2, 0)

        return HBImage(self._image.resize(new_size, Image.BICUBIC))


    def box_fit_resized_image(self, box):
        x0, y0, x1, y1 = box
        
        x_offset, y_offset = self._fit_offset
        x0 = (x0-x_offset) // self._fit_ratio
        x1 = (x1-x_offset) // self._fit_ratio
        y0 = (y0-y_offset) // self._fit_ratio
        y1 = (y1-y_offset) // self._fit_ratio
        
        return (x0, y0, x1, y1)
    
    
    def point_fit_resized_image(self, point):
        x0,y0 = point
        x_offset, y_offset = self._fit_offset 
        x0 = (x0-x_offset) // self._fit_ratio 
        y0 = (y0-y_offset) // self._fit_ratio
        return (x0,y0)

    def ROI_fit_resized_image(self):
        self.ROI = self.box_fit_resized_image(self._roi)



    def ROI_clear(self):
        """
        This method clears ROI by setting the ROI to (0, 0, 0, 0).
        """
        self._roi = (0, 0, 0, 0)






    #---------------image process---------------------
    def rotate(self, angle):
        rotate_img = self.image.rotate(angle, expand=True)
        return HBImage(rotate_img, **self.information)


    @image_process
    def filp_horizontal(self):
        flip_img = self.image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        return HBImage(flip_img, **self.information)

    @image_process
    def filp_vertical(self):
        flip_img = self.image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        return HBImage(flip_img, **self.information)


    @image_process
    def to_gray(self):
        gray_img = self.image.convert('L')
        return HBImage(gray_img, **self.information)

    @image_process
    def color_invert(self):
        inverted_img = ImageChops.invert(self.image)
        return HBImage(inverted_img, **self.information)


