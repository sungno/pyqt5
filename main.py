from moduls import *
import apps


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('pyat5_test.ui')
form_class = uic.loadUiType(form)[0]


# form_class = uic.loadUiType("test.ui")[0]


class MyWindow(QtWidgets.QMainWindow, QMessageBox, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.start_button)


    def start_button(self):
        qqq = threading.Thread(target=apps.go_run, args=(model,))
        qqq.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = MyWindow()
    model.show()
    app.exec_()
    sys.exit(app.exec_())
