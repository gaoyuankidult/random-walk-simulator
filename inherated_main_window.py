from Ui_random_walk_window import *
from PyQt4.QtGui import QMessageBox
from conf_info import ConfInfo
from extra_method import _fromUtf8
from configeration_dialog import ConfDialog
from random_walk_graph import StatisticGraph
from scipy import stats
from numpy  import array
#TOUNDERSTAND: 
# if I use 
# from myapp.enviroment import singleton
# then I dont need to specify sengleton as global  in function
# 

class InheratedMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(InheratedMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._add_graph()
        self._add_table_header()
        self.setup_connections()
        self.class_info = ConfInfo()
        self.disable_dimension_selection()
    def disable_dimension_selection(self):
        self.ui.dimension_statistics_box.setEnabled(False)
    def setup_simulation_parameters(self):
        conf_dialog = ConfDialog()
        conf_dialog.show()
        if conf_dialog.exec_() :
            self.class_info.set_info(conf_dialog.get_values())
    def edit_simulation_parameters(self):
        conf_dialog = ConfDialog()
        conf_dialog.show()
        conf_dialog.set_values(self.class_info)
        if conf_dialog.exec_() :
            self.class_info.set_info(conf_dialog.get_values())        
    def refresh_conf_tab(self):

        self.ui.nagetive_range_label.setText(str(self.class_info.lower_range))
        self.ui.positive_range_label.setText(str(self.class_info.upper_range))
        self.ui.random_walk_label.setText(str(self.class_info.random_walk_number))
        self.ui.starting_number_label.setText(str(self.class_info.initial_state))
        self.ui.random_walk_distance_label.setText(str(self.class_info.repeat_time))
    def change_dimension(self, index):
        if(index == 0):
            self.ui.dimension_statistics_box.setEnabled(False)

        self.ui.statistics_graph.set_dimension(index)
    def refresh_statistics_tab_func(self):
        self.refresh_statistics_tab(None)

    def refresh_statistics_tab(self, index):
        index_dimension = ["y", "x"]
        index_percentage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        try:
            if(self.sender() == self.ui.dimension_statistics_box):
                dimension_current_index = index
            else:
                dimension_current_index = self.ui.dimension_statistics_box.currentIndex()
            if (self.sender() == self.ui.step_statistics_box):
                step_current_index = index
            else:
                step_current_index = self.ui.step_statistics_box.currentIndex()
            x_or_y  = index_dimension[dimension_current_index]
            length_of_set =  len(self.answer_set[x_or_y][0])
            final_value_set = array(zip(*self.answer_set[x_or_y])[int(round(length_of_set*index_percentage[step_current_index]/100.))-1])
            self.ui.minimum_value.setText(str(min(final_value_set)))
            self.ui.maximum_value.setText(str(max(final_value_set)))
            self.ui.mean_value.setText(str(reduce(lambda x, y: x + y, final_value_set) / float(len(final_value_set))))
            self.ui.standard_deviation_value.setText(str(final_value_set.std()))
            self.ui.tenth_percentile_value.setText(str(stats.scoreatpercentile(final_value_set, 90)))
            self.ui.ninetieth_percentile_value.setText(str(stats.scoreatpercentile(final_value_set, 10)))
            self.refersh_table(dimension_current_index)
        except Exception as e:
            #print e
            QtGui.QMessageBox.warning(self, 'Error',   
                "Did not get result: {0}".format(str(e))+ "\nMay be you did not specify any configeration." + "\nPlease click new to specify.", 
                QtGui.QMessageBox.Yes,
                QtGui.QMessageBox.No)
    def _add_graph(self):
        self.ui.statistics_graph= StatisticGraph(self.ui.graph_tab)
        #self.statistics_graph.display_data([1, 2], [3, 4], [4, 6], [0.5, 0.6], 0.5)
    def _add_table_header(self):
        #self.ui.result_table.setGeometry(QtCore.QRect(20, 30, 1000, 500))
        #TODO:
        #why can't I use this function in the table in
        self.ui.result_table.set_none_header()

        
        
    def _table_add_row(self, name_of_node):
        row_number = self.ui.result_table.rowCount()
        #add new row 
        self.ui.result_table.setRowCount(row_number+1)
        item = QtGui.QTableWidgetItem()
        #set the new columen for new name_of_node
        item.setText(QtGui.QApplication.translate("MainWindow", hex(name_of_node).rstrip("L").lstrip("0x"), None, QtGui.QApplication.UnicodeUTF8))
        #add it 
        self.ui.result_table.setVerticalHeaderItem(row_number, item)
    def setup_connections(self):
        QtCore.QObject.connect(self.ui.action_new, QtCore.SIGNAL(_fromUtf8("triggered()")), self.new_conf)
        QtCore.QObject.connect(self.ui.action_edit, QtCore.SIGNAL(_fromUtf8("triggered()")), self.edit_conf)
        QtCore.QObject.connect(self.ui.action_start, QtCore.SIGNAL(_fromUtf8("triggered()")), self.start_simulation)
        QtCore.QObject.connect(self.ui.action_stop,  QtCore.SIGNAL(_fromUtf8("triggered()")), self.stop_simulation)
        QtCore.QObject.connect(self.ui.action_clear, QtCore.SIGNAL(_fromUtf8("triggered()")), self.clear_simulation)
    def new_conf(self):
        """new configeration"""
        self.setup_simulation_parameters()
        self.refresh_conf_tab()
    def edit_conf(self):
        """edit configeration"""
        self.edit_simulation_parameters()
        self.refresh_conf_tab()
    def refersh_table(self, index=None):
        ## refersh table
        self.ui.result_table.clear ()
        index_dimension = ["y", "x"]
        if index is None:
            dimension_current_index = self.ui.dimension_statistics_box.currentIndex()
        else:
            dimension_current_index = index
        x_or_y = index_dimension[dimension_current_index]
        # arbitery
        walk_distance= range(len(self.answer_set[x_or_y][0]))
        walk_number = range(len(self.answer_set[x_or_y]))
#        print "number", len(self.answer_set[x_or_y][0])
#        print "walk_distance", walk_distance
#        print "walk_number", walk_number
        self.ui.result_table.set_horizonal_header(walk_distance)
        self.ui.result_table.set_vertical_header(walk_number)

        self.ui.result_table.set_columns(self.answer_set[x_or_y])

    def start_simulation(self):
        """start drawing"""
        #TODO:
        # calculation is done by graph_tab
        # this may not be good 
        
        # dimension 0 means 1d, 1 means 2d
        if(self.ui.statistics_graph.dimension == 1):
            self.ui.dimension_statistics_box.setEnabled(True)
        try:
            self.answer_set = self.ui.statistics_graph.plot_graph(self.class_info )     
            self.refresh_statistics_tab_func()
 #           self.refersh_table()      
            self.ui.information_widget.setCurrentIndex(1)
        

        except Exception as e:
            QtGui.QMessageBox.warning(self, 'Error',   
                "Did not get result: {0}".format(str(e))+ "\nMay be you did not specify any configeration." + "\nPlease click new to specify.", 
                QtGui.QMessageBox.Yes,
                QtGui.QMessageBox.No)
    def stop_simulation(self):
        """stop drawing"""
        
    def clear_simulation(self):
        """clear drawing"""
        self.ui.statistics_graph.clear_graph()
