import sys

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QPushButton, QApplication
from PyQt5.QtWidgets import QLabel, QLineEdit


class NewCase(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Register New Case"
        self.name = None
        self.age = None
        self.mob = None
        self.father_name = None
        self.image = None
        self.initialize()

    def initialize(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle(self.title)
        upload_image_bt = QPushButton("Image", self)
        upload_image_bt.move(400, 20)
        upload_image_bt.clicked.connect(self.openFileNameDialog)

        save_bt = QPushButton("Save ", self)
        save_bt.move(400, 350)

        self.get_name()
        self.get_age()
        self.get_fname()
        self.get_mob()
        self.show()

    def get_name(self):
        self.name_label = QLabel(self)
        self.name_label.setText('Name:')
        self.name_label.move(420, 70)

        self.name = QLineEdit(self)
        self.name.move(480, 70)

    def get_age(self):
        self.age_label = QLabel(self)
        self.age_label.setText('Age:')
        self.age_label.move(420, 110)

        self.age = QLineEdit(self)
        self.age.move(480, 110)

    def get_fname(self):
        self.fname_label = QLabel(self)
        self.fname_label.setText('Father\'s\n Name:')
        self.fname_label.move(420, 150)

        self.father_name = QLineEdit(self)
        self.father_name.move(480, 150)

    def get_mob(self):
        self.mob_label = QLabel(self)
        self.mob_label.setText('Mobile:')
        self.mob_label.move(420, 190)

        self.mob = QLineEdit(self)
        self.mob.move(480, 190)


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getOpenFileName(
                    self, "QFileDialog.getOpenFileName()",
                    "", "jpg file (*.jpg)", options=options)


app = QApplication(sys.argv)

style = """
        QWidget{
            background: #262D37;
        }
        QLabel{
            color: #fff;
        }
        QListView
        {
            background: #7e959e;
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
w = NewCase()
sys.exit(app.exec())