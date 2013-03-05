from inherated_main_window import *
from configeration_dialog import *
from extra_method import _fromUtf8
from configeration_dialog import ConfDialog


 
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = InheratedMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
