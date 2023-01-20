"""
To avoid too much code in HBDialogLoad, I separate functions to this module.\n
This Module defines a class:Events and some the functions that are used in HBDialogLoad widgets' event.\n
Using inheritance let class "Events" functions add to the class "HBDialogLoad" .\n
"""

from PySide6.QtGui import QMouseEvent

from PySide6.QtWidgets import (
    QFileDialog
    )



def load_file_txt(filepath) -> list:
    try:
        with open(filepath) as f:
            return f.read().splitlines()
    except IOError:
        print("\n-CANNOT Load txt content!!!")
        print(">> {} <<".format(filepath))
        print("-No such file or directory!!!\n")
        return None

def get_file_name_and_format(filename:str) -> list:
    from os import path
    file_basename = path.basename(filename)
    file_basename_splited = path.splitext(file_basename)
    file_name = file_basename_splited[0]
    file_format = file_basename_splited[1][1:]
    return [file_name, file_format]




class _HBDialogLoadMethods:


    def move_window_mouse_press(self, event:QMouseEvent):
        self.old_pos = event.globalPos()

    def move_window_mouse_move(self, event:QMouseEvent):
        delta_x = int(event.globalPos().x()) - self.old_pos.x()
        delta_y = int(event.globalPos().y()) - self.old_pos.y()
        self.move(self.x() + delta_x, self.y() + delta_y)
        self.old_pos = event.globalPos()

    def select_file(self) -> str:
        """
        This funciton will open a QFileDialog,
        and return the selected file path.
        """
        file_dialog = QFileDialog(self)
        file_abs_path, file_type = file_dialog.getOpenFileName(
            self,
            "Select Image",
            "./",
            "All Files(*);;Image (*.png *.bmp *.jpg *.jpeg);;Text File (*.txt)"
            )
        
        is_load_txt_file = get_file_name_and_format(files_abs_path)[1]=="txt"
        if is_load_txt_file:
            files_abs_path = load_file_txt(files_abs_path)

        return file_abs_path
    
    def select_files(self) -> list:
        """
        (select mutiple files)This funciton will open a QFileDialog,
        and return the selected file path.
        """
        files_dialog = QFileDialog(self)
        files_abs_path, file_type = files_dialog.getOpenFileNames(
            self,
            "Select Image",
            "./",
            "All Files(*);;Images (*.png *.bmp *.jpg *.jpeg);;Text File (*.txt)"
            )
        if not files_abs_path:
            return None
        
        is_load_txt_file = get_file_name_and_format(files_abs_path[0])[1]=="txt"
        if is_load_txt_file:
            files_abs_path = load_file_txt(files_abs_path[0])

        return files_abs_path


    #------------click_event define--------------
    def btn_select_files_click_event(self):
        select_files_paths = self.select_files()
        if select_files_paths:
            images_path = "\n".join(select_files_paths)
            self.ui.textFilePath.setPlainText(images_path)

    def btn_select_file_click_event(self):
        image_path = self.select_file()
        self.ui.textFilePath.setPlainText(image_path)

    def btn_load_click_event(self):
        text_files_path = self.ui.textFilePath.toPlainText()
        
        if (text_files_path=="") or (text_files_path is None):
            return None
        
        self._filepaths = text_files_path.split("\n")
        self.signal_load.emit(self.filepaths)
        
        self.close()



