import sys

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QPushButton, QApplication
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox


class MobileApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Submit Image"
        self.location = None
        self.name = None
        self.mobile = None
        self.image = None
        self.key_points = None
        self.initialize()

    def initialize(self):
        self.setFixedSize(400, 700)
        self.setWindowTitle(self.title)

        upload_image_bt = QPushButton("Image", self)
        upload_image_bt.move(150, 250)
        upload_image_bt.clicked.connect(self.openFileNameDialog)

        save_bt = QPushButton("Save ", self)
        save_bt.move(150, 640)
        save_bt.clicked.connect(self.save)

        self.get_name()
        self.get_mobile_num()
        self.get_location()
        self.show()

    def get_name(self):
        self.name_label = QLabel(self)
        self.name_label.setText('Your Name:')
        self.name_label.move(170, 20)

        self.name = QLineEdit(self)
        self.name.move(150, 50)

    def get_mobile_num(self):
        self.mobile_label = QLabel(self)
        self.mobile_label.setText('Mobile:')
        self.mobile_label.move(170, 90)

        self.mobile = QLineEdit(self)
        self.mobile.move(150, 120)

    def get_location(self):
        self.location_label = QLabel(self)
        self.location_label.setText('Location:')
        self.location_label.move(150, 160)

        self.location = QLineEdit(self)
        self.location.move(150, 190)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getOpenFileName(
                    self, "QFileDialog.getOpenFileName()",
                    "", "jpg file (*.jpg)", options=options)

    def get_entries(self):
        entries = {}
        if self.mobile.text() != "" and self.name.text() != "" and self.location.text() != "":
            entries['name'] = self.name.text()
            entries['location'] = self.location.text()
            entries['mobile'] = self.mobile.text()
            return entries
        else:
            return None

    def save(self):
        entries = self.get_entries()
        if entries:
            QMessageBox.about(self, "Excuse", "This part is not done")
        else:
            QMessageBox.about(self, "Error", "Please fill all entries")


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
w = MobileApp()
sys.exit(app.exec())