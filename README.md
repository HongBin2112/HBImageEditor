# HBImageEditor

---  

---  
Change Log:

> ### Version 1.2  
> - Add Fuction : Undo/Redo :  
> Don't need to worry about making mistakes. This function is implemented in HBImageBox.
> 
> - Add Fuction : Zoom in/out  
> Use "Ctrl + mouse wheel" on image to zoom in/out .
> 
> - Refactor HBImageBox :  
> Separate HBImageBox from HBMainWindow. Now HBImageBox is an individual widget.  
> HBImageBox need to import "HBImage". 
> 
> - About HBImageBox :  
> Inherited from "PySide6.QtWidgets.QWidget".  
> HBImageBox takes care of all image editing functions (cropping, flipping, rotating...).  
> HBImageBox just like a HBImageEditor, but can only load and edit a single image at the same time.  
> In other words, HBImageEditor is HBImageBox with a beautiful appearance and can load multiple images at the same time.
> 

  


  

---  
  
### Publish Steps:
(assume "pipenv" is installed)

if Pipfile is exist:  

```pipenv```  
  
else:  
  
```
pipenv --python (your python version) 
ex.$ pipenv --python 3.8

#install packages
pipenv install Pillow
pipenv install PySide6
pipenv install pyinstaller
```

```
#pyinstaller
pipenv shell
pyinstaller main_publish.py -F -w -i icon.ico --upx-dir "../upx-4.0.1-amd64_linux"

```

---  
