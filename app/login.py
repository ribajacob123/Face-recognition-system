import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QListView, QLabel, QLineEdit

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Login"
        self.width = 800
        self.height = 600

        self.initialize()

    def initialize(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.get_username()
        self.get_password()

        login_bt = QPushButton("Login", self)
        login_bt.move(340, 250)

        self.show()

    def get_username(self):
        username_label = QLabel(self)
        username_label.setText("Username: ")
        username_label.move(310, 170)

        self.username = QLineEdit(self)
        self.username.move(370, 170)
    
    def get_password(self):
        password_label = QLabel(self)
        password_label.setText("Password: ")
        password_label.move(310, 200)

        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.move(370, 200)       


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
w = LoginWindow()
sys.exit(app.exec())
