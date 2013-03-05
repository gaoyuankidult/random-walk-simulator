# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gao/Desktop/Tianhua_Guo_Homework/Seocnd/configeration.ui'
#
# Created: Mon Mar  4 18:02:39 2013
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_conf_dialog(object):
    def setupUi(self, conf_dialog):
        conf_dialog.setObjectName(_fromUtf8("conf_dialog"))
        conf_dialog.resize(239, 207)
        conf_dialog.setWindowTitle(QtGui.QApplication.translate("conf_dialog", "Configeration Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.formLayoutWidget = QtGui.QWidget(conf_dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 221, 181))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.conf_layout = QtGui.QFormLayout(self.formLayoutWidget)
        self.conf_layout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.conf_layout.setMargin(0)
        self.conf_layout.setObjectName(_fromUtf8("conf_layout"))
        self.initial_state_label = QtGui.QLabel(self.formLayoutWidget)
        self.initial_state_label.setToolTip(QtGui.QApplication.translate("conf_dialog", "you can set the initial state here", None, QtGui.QApplication.UnicodeUTF8))
        self.initial_state_label.setText(QtGui.QApplication.translate("conf_dialog", "Initial state", None, QtGui.QApplication.UnicodeUTF8))
        self.initial_state_label.setObjectName(_fromUtf8("initial_state_label"))
        self.conf_layout.setWidget(0, QtGui.QFormLayout.LabelRole, self.initial_state_label)
        self.initial_state_value = QtGui.QLineEdit(self.formLayoutWidget)
        self.initial_state_value.setObjectName(_fromUtf8("initial_state_value"))
        self.conf_layout.setWidget(0, QtGui.QFormLayout.FieldRole, self.initial_state_value)
        self.random_number_label = QtGui.QLabel(self.formLayoutWidget)
        self.random_number_label.setToolTip(QtGui.QApplication.translate("conf_dialog", "you can set the random node number here", None, QtGui.QApplication.UnicodeUTF8))
        self.random_number_label.setText(QtGui.QApplication.translate("conf_dialog", "random number", None, QtGui.QApplication.UnicodeUTF8))
        self.random_number_label.setObjectName(_fromUtf8("random_number_label"))
        self.conf_layout.setWidget(1, QtGui.QFormLayout.LabelRole, self.random_number_label)
        self.random_numner_value = QtGui.QLineEdit(self.formLayoutWidget)
        self.random_numner_value.setObjectName(_fromUtf8("random_numner_value"))
        self.conf_layout.setWidget(1, QtGui.QFormLayout.FieldRole, self.random_numner_value)
        self.upper_range_label = QtGui.QLabel(self.formLayoutWidget)
        self.upper_range_label.setToolTip(QtGui.QApplication.translate("conf_dialog", "you can set the upper range for the uniform distribution of random work here.\n"
"It should be positive.", None, QtGui.QApplication.UnicodeUTF8))
        self.upper_range_label.setText(QtGui.QApplication.translate("conf_dialog", "upper range", None, QtGui.QApplication.UnicodeUTF8))
        self.upper_range_label.setObjectName(_fromUtf8("upper_range_label"))
        self.conf_layout.setWidget(2, QtGui.QFormLayout.LabelRole, self.upper_range_label)
        self.upper_range_value = QtGui.QLineEdit(self.formLayoutWidget)
        self.upper_range_value.setObjectName(_fromUtf8("upper_range_value"))
        self.conf_layout.setWidget(2, QtGui.QFormLayout.FieldRole, self.upper_range_value)
        self.lower_range_label = QtGui.QLabel(self.formLayoutWidget)
        self.lower_range_label.setToolTip(QtGui.QApplication.translate("conf_dialog", "you can set the lower range for the uniform distribution of random work here.\n"
"It should be negative.", None, QtGui.QApplication.UnicodeUTF8))
        self.lower_range_label.setText(QtGui.QApplication.translate("conf_dialog", "lower range", None, QtGui.QApplication.UnicodeUTF8))
        self.lower_range_label.setObjectName(_fromUtf8("lower_range_label"))
        self.conf_layout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lower_range_label)
        self.lower_range_value = QtGui.QLineEdit(self.formLayoutWidget)
        self.lower_range_value.setObjectName(_fromUtf8("lower_range_value"))
        self.conf_layout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lower_range_value)
        self.conf_ok_button = QtGui.QPushButton(self.formLayoutWidget)
        self.conf_ok_button.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.conf_ok_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.conf_ok_button.setText(QtGui.QApplication.translate("conf_dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.conf_ok_button.setDefault(True)
        self.conf_ok_button.setObjectName(_fromUtf8("conf_ok_button"))
        self.conf_layout.setWidget(5, QtGui.QFormLayout.FieldRole, self.conf_ok_button)
        self.conf_cancle_button = QtGui.QPushButton(self.formLayoutWidget)
        self.conf_cancle_button.setText(QtGui.QApplication.translate("conf_dialog", "Cancle", None, QtGui.QApplication.UnicodeUTF8))
        self.conf_cancle_button.setDefault(False)
        self.conf_cancle_button.setFlat(False)
        self.conf_cancle_button.setObjectName(_fromUtf8("conf_cancle_button"))
        self.conf_layout.setWidget(5, QtGui.QFormLayout.LabelRole, self.conf_cancle_button)
        self.repeat_time_label = QtGui.QLabel(self.formLayoutWidget)
        self.repeat_time_label.setToolTip(QtGui.QApplication.translate("conf_dialog", "you should put random walk distance here.", None, QtGui.QApplication.UnicodeUTF8))
        self.repeat_time_label.setText(QtGui.QApplication.translate("conf_dialog", "repeat time", None, QtGui.QApplication.UnicodeUTF8))
        self.repeat_time_label.setObjectName(_fromUtf8("repeat_time_label"))
        self.conf_layout.setWidget(4, QtGui.QFormLayout.LabelRole, self.repeat_time_label)
        self.repeat_time_value = QtGui.QLineEdit(self.formLayoutWidget)
        self.repeat_time_value.setObjectName(_fromUtf8("repeat_time_value"))
        self.conf_layout.setWidget(4, QtGui.QFormLayout.FieldRole, self.repeat_time_value)

        self.retranslateUi(conf_dialog)
        QtCore.QMetaObject.connectSlotsByName(conf_dialog)
        conf_dialog.setTabOrder(self.initial_state_value, self.random_numner_value)
        conf_dialog.setTabOrder(self.random_numner_value, self.upper_range_value)
        conf_dialog.setTabOrder(self.upper_range_value, self.lower_range_value)
        conf_dialog.setTabOrder(self.lower_range_value, self.repeat_time_value)
        conf_dialog.setTabOrder(self.repeat_time_value, self.conf_cancle_button)
        conf_dialog.setTabOrder(self.conf_cancle_button, self.conf_ok_button)

    def retranslateUi(self, conf_dialog):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    conf_dialog = QtGui.QDialog()
    ui = Ui_conf_dialog()
    ui.setupUi(conf_dialog)
    conf_dialog.show()
    sys.exit(app.exec_())

