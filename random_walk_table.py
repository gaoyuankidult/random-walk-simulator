from Ui_random_walk_window import *
class RandomWalkTable(QtGui.QTableWidget):
    def __init__(self, parent=None):
        super(RandomWalkTable, self).__init__(parent)
        self.set_none_header()
    def set_none_header(self):
        self.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch )
        
        self.setColumnCount(5)
        self.setRowCount(0)
        
        start_time_item = QtGui.QTableWidgetItem()
        start_time_item.setText(QtGui.QApplication.translate("MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.setHorizontalHeaderItem(0, start_time_item)
        
        stop_time_item = QtGui.QTableWidgetItem()
        stop_time_item.setText(QtGui.QApplication.translate("MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.setHorizontalHeaderItem(1, stop_time_item)
            
        total_packet = QtGui.QTableWidgetItem()
        total_packet.setText(QtGui.QApplication.translate("MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.setHorizontalHeaderItem(2, total_packet)
                
        lost_frame_item = QtGui.QTableWidgetItem()
        lost_frame_item.setText(QtGui.QApplication.translate("MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.setHorizontalHeaderItem(3, lost_frame_item)
        
        progressbar_item = QtGui.QTableWidgetItem()
        progressbar_item.setText(QtGui.QApplication.translate("MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.setHorizontalHeaderItem(4, progressbar_item)
    def set_horizonal_header(self, list):
        self.setColumnCount(len(list))
        for i, item_name in enumerate(list):
            item = QtGui.QTableWidgetItem()
            item.setText(QtGui.QApplication.translate("MainWindow", "Step"+str(item_name), None, QtGui.QApplication.UnicodeUTF8))
            self.setHorizontalHeaderItem(i, item)
    def set_vertical_header(self, list):
        self.setRowCount(len(list))
        for i, item_name in enumerate(list):
            item = QtGui.QTableWidgetItem()
            item.setText(QtGui.QApplication.translate("MainWindow", "No:"+str(item_name), None, QtGui.QApplication.UnicodeUTF8))
            self.setVerticalHeaderItem(i, item)
    def set_columns(self, list):
        for i, row  in enumerate(list):
            for j, column in enumerate(row):
                item = QtGui.QTableWidgetItem()
                item.setText(QtGui.QApplication.translate("MainWindow", str(column), None, QtGui.QApplication.UnicodeUTF8))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.setItem(i, j, item)
        
        
