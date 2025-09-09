import sys
from PyQt5.QtWidgets import QApplication
from ui_main import TextDisplayApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextDisplayApp()
    window.show()
    sys.exit(app.exec_())
