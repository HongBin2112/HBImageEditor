# HBImageEditor


### 目錄： 
- 前言  
- 程式簡介  
- 文件編排  
- 環境  

---  
### 前言：
HB Image Editor 是一個我自學、入門python，還有Pyside的一個小小小GUI程式。其中程式的UI界面皆由自己設計。    

程式主要功能圖片查看及圖片編輯，可一次讀取多個圖片。目前程式功能不多，當前有：讀取（本地、網路、剪貼簿、拖曳圖片至視窗）、保存圖片，圖片裁切、翻轉及轉為黑白圖片等等...  

程式界面及操作皆相當直覺：點擊左上角按鈕處可打開資訊菜單，其中可進行讀取、保存、查看圖片資訊、及切換當前處理之圖片等動作。 
圖片編輯（裁剪、翻轉、轉為黑白等）選項的部份，透過對圖片右鍵，便會顯示選項菜單。  

<img src="https://github.com/HongBin2112/HongBin2112/blob/main/figs/HBImageEditor/HBImageEditorAppScreenshot.png?raw=true" alt="HB Image Editor App screenshot" align="middle">

更多內容會在下段：程式簡介中講述。  

---  
### 程式簡介：  
#### 界面概覽及操作：
界面及操作皆相當直覺。這邊放上幾張截圖，再搭上一點小說明：

<!--![HB Image Editor App open menu animation]()-->  
透過左上角按鈕可以打開資訊菜單，進行讀取、保存圖片。也可以透過拖拉圖片至視窗中、和剪貼簿貼上來載入圖片。  
如果讀取一張以上圖片，資訊菜單中 "<", ">" 圖示可用來切換當前處理之圖片。也可以透過直接更改圖片索引（"<"和">"中間顯示的數字），來快速切換圖片。   
   
<img src="https://github.com/HongBin2112/HongBin2112/blob/main/figs/HBImageEditor/HBImageEditorAppLoadDialog.png?raw=true" alt="HB Image Editor App Load dialog" width="600">    
  
點擊Load後會跳出dialog。  
除了透過點擊 "Selecte File" 來選取圖片，也可以於輸入框中直接輸入本地或非本地路徑（http:// 、 https://）。  
另外，也可以選取單一.txt文字檔，一次讀取多個檔案路徑。文字檔案內只能有圖片檔案路徑，使用分行來分隔不同檔案路徑。  
此功能實作上是將.txt中的文字內容讀取並處理後，將其中文字輸入至輸入框中，因此無法於輸入框中直接輸入.txt檔案路徑來做使用，請點擊 "Selecte File" 選項來選取.txt文字檔案。  

<img src="https://github.com/HongBin2112/HongBin2112/blob/main/figs/HBImageEditor/select_area_and_crop.gif?raw=true" alt="HB Image Editor App select area on image" width="450">   

中間為顯示圖片部份，滑鼠在其上點擊拉動可以選取範圍，並用於圖片裁切。  
右鍵圖片部分打開圖片編輯菜單。另外也有鍵盤輸入的快捷鍵，如：複製圖片(ctrl+C)、貼上圖片(ctrl+V)、裁切(C)...等等。


---  
### 文件編排：  

#### 文件引用圖：  
  
大比例尺：   
![HB Image Editor App Files import relation](https://github.com/HongBin2112/HongBin2112/blob/main/figs/HBImageEditor/HBImageEditor_largeSize.png?raw=true)   


  

---  
### 環境：  

### Linux：  
- 作業系統版本：Ubuntu 20.04.5 LTS , 64-bit
- Python版本：3.8.10
- 模組版本：  
 
| Package | Version |
| :----: | :----: |
| Pillow | 9.1.0 |
| PySide6 | 6.2.4 |
| pyinstaller | 5.7.0 |  

<br>

### Windows：  
- 作業系統版本：
- Python版本：
- 模組版本：  
 
| Package | Version |
| :----: | :----: |
| Pillow | 9.1.0 |
| PySide6 | 6.2.4 |
| pyinstaller | 5.7.0 |  









---  

### Change Log:   
  

> ### - Version 1.2  
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
