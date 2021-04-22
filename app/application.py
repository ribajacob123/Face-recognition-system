import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtWidgets import QListWidget, QLabel, QLineEdit

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Application"
        self.width = 800
        self.height = 600
        self.initialize()

    def initialize(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)

        button_upload = QPushButton("New Case", self)
        button_upload.move(470, 100)

        button_refresh_model = QPushButton("Refresh", self)
        button_refresh_model.move(470, 150)
        
        button_match = QPushButton("Match", self)
        button_match.move(470, 200)
        
        confirmedButton = QPushButton("Confirmed", self)
        confirmedButton.move(470, 250)
        
        self.show()
    
app = QApplication(sys.argv)
style = """
        QWidget{
            background: #262D37;
        }
        QLabel{
            color: #fff;
        }
        QLabel#round_count_label, QLabel#highscore_count_label{
            border: 1px solid #fff;
            border-radius: 8px;
            padding: 2px;
        }
        QPushButton
        {
            color: white;
            background: #0577a8;
            border: 1px #DADADA solid;
            padding: 5px 10px;
            border-radius: 2px;
            font-weight: bold;
            font-size: 9pt;
            outline: none;
        }
        QPushButton:hover{
            border: 1px #C6C6C6 solid;
            color: #fff;
            background: #0892D0;
        }
        QLineEdit {
            padding: 1px;
            color: #fff;
            border-style: solid;
            border: 2px solid #fff;
            border-radius: 8px;
        }
    """
app.setStyleSheet(style)
w = AppWindow()
sys.exit(app.exec())