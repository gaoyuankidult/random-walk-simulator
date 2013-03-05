from Ui_configeration import *
from extra_method import _fromUtf8
from conf_info import ConfInfo

class ConfDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(ConfDialog, self).__init__(parent)
        self.ui = Ui_conf_dialog()
        self.ui.setupUi(self)
        self.setup_connections()

    def __init__(self, parent=None):
            super(ConfDialog, self).__init__(parent)
            self.ui = Ui_conf_dialog()
            self.ui.setupUi(self)
            # use new style signals
            self.setup_connections()      
    def set_values(self, conf_info):
        self.conf_info = conf_info
        self.ui.initial_state_value.setText(str(self.conf_info.initial_state))
        self.ui.lower_range_value.setText(str(self.conf_info.lower_range))
        self.ui.random_numner_value.setText(str(self.conf_info.random_walk_number))
        self.ui.upper_range_value.setText(str(self.conf_info.upper_range))
        self.ui.repeat_time_value.setText(str(self.conf_info.repeat_time))
        

    def get_values(self):
        """return 4 values that go from the dialog"""
        return [float(self.ui.initial_state_value.text()), 
                int(self.ui.random_numner_value.text()),
                float(self.ui.upper_range_value.text()),
                float(self.ui.lower_range_value.text()), 
                int(self.ui.repeat_time_value.text())]
    def accept(self):
        """accepted the configeration"""
        super(ConfDialog, self).accept()  # call the accept method of QDialog. 
                                           # super is needed 
                                           # since we just override the accept method
    def reject(self):
        """cancle the configeration"""
        super(ConfDialog, self).reject()  # call the accept method of QDialog. 
                                           # super is needed 
                                           # since we just override the accept method
    def setup_connections(self):
        QtCore.QObject.connect(self.ui.conf_ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.accept)
        QtCore.QObject.connect(self.ui.conf_cancle_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.reject)
