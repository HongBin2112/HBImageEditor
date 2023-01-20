import sys
import os

from PySide6.QtWidgets import QApplication
from HBMainWindow import HBMainWindow

def convert_ui_files(files):
    for ui_file in files:
        ui_name = ui_file[:-3]
        result_file_name = f'./{ui_name}/{ui_name}Ui.py'
        os.system(f"pyside6-uic {ui_file} > {result_file_name}")


ui_files = [
    "HBMainWindow.ui",
    "HBDialogLoad.ui"
]


if __name__ == "__main__":

    convert_ui_files(ui_files)

    app = QApplication(sys.argv)
    HBIP_window = HBMainWindow()
    HBIP_window.show()
    app.exec()

