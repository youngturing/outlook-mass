# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'separator_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Separator(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(351, 170)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_separator = QtWidgets.QLabel(Dialog)
        self.label_separator.setObjectName("label_separator")
        self.gridLayout.addWidget(self.label_separator, 0, 0, 1, 1)
        self.line_edit_separator = QtWidgets.QLineEdit(Dialog)
        self.line_edit_separator.setMaximumSize(QtCore.QSize(100, 16777215))
        self.line_edit_separator.setObjectName("line_edit_separator")
        self.gridLayout.addWidget(self.line_edit_separator, 0, 1, 1, 1)
        self.push_button_ok_sep = QtWidgets.QPushButton(Dialog)
        self.push_button_ok_sep.setMaximumSize(QtCore.QSize(100, 16777215))
        self.push_button_ok_sep.setObjectName("push_button_ok_sep")
        self.gridLayout.addWidget(self.push_button_ok_sep, 1, 0, 1, 1)
        self.push_button_cancel_sep = QtWidgets.QPushButton(Dialog)
        self.push_button_cancel_sep.setMaximumSize(QtCore.QSize(100, 16777215))
        self.push_button_cancel_sep.setObjectName("push_button_cancel_sep")
        self.gridLayout.addWidget(self.push_button_cancel_sep, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_separator.setText(_translate("Dialog", "Change separator to:"))
        self.push_button_ok_sep.setText(_translate("Dialog", "Ok"))
        self.push_button_cancel_sep.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_Separator()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())