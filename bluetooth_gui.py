# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/stefan/SpyderWorkspace/Bluetooth/bluetooth_gui.ui'
#
# Created: Tue Mar 31 12:57:43 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(397, 363)
        self.cBDataSelection = QtGui.QComboBox(Dialog)
        self.cBDataSelection.setGeometry(QtCore.QRect(10, 280, 131, 27))
        self.cBDataSelection.setAcceptDrops(True)
        self.cBDataSelection.setEditable(True)
        self.cBDataSelection.setMaxVisibleItems(3)
        self.cBDataSelection.setMaxCount(3)
        self.cBDataSelection.setObjectName(_fromUtf8("cBDataSelection"))
        self.cBDataSelection.addItem(_fromUtf8(""))
        self.cBDataSelection.addItem(_fromUtf8(""))
        self.cBDataSelection.addItem(_fromUtf8(""))
        self.pbConnect = QtGui.QPushButton(Dialog)
        self.pbConnect.setGeometry(QtCore.QRect(10, 330, 98, 27))
        self.pbConnect.setObjectName(_fromUtf8("pbConnect"))
        self.pbDisconnect = QtGui.QPushButton(Dialog)
        self.pbDisconnect.setGeometry(QtCore.QRect(150, 330, 98, 27))
        self.pbDisconnect.setObjectName(_fromUtf8("pbDisconnect"))
        self.tlTextline = QtGui.QLineEdit(Dialog)
        self.tlTextline.setGeometry(QtCore.QRect(150, 280, 241, 27))
        self.tlTextline.setObjectName(_fromUtf8("tlTextline"))
        self.pbClose = QtGui.QPushButton(Dialog)
        self.pbClose.setGeometry(QtCore.QRect(290, 330, 98, 27))
        self.pbClose.setObjectName(_fromUtf8("pbClose"))
        self.widget = matplotlibWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 381, 261))
        self.widget.setObjectName(_fromUtf8("widget"))

        self.retranslateUi(Dialog)
        self.cBDataSelection.setCurrentIndex(0)
        QtCore.QObject.connect(self.cBDataSelection, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.tlTextline.clear)
        QtCore.QObject.connect(self.pbConnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.tlTextline.clear)
        QtCore.QObject.connect(self.pbDisconnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.tlTextline.clear)
        QtCore.QObject.connect(self.pbClose, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.cBDataSelection.setItemText(0, _translate("Dialog", "Temperature", None))
        self.cBDataSelection.setItemText(1, _translate("Dialog", "Air Humidity", None))
        self.cBDataSelection.setItemText(2, _translate("Dialog", "No Data", None))
        self.pbConnect.setText(_translate("Dialog", "Connect PI", None))
        self.pbDisconnect.setText(_translate("Dialog", "Disconnect", None))
        self.tlTextline.setText(_translate("Dialog", "No Datatyp Selected", None))
        self.pbClose.setText(_translate("Dialog", "Close", None))

    def __del__(self):
        print (self.name, 'died')
        
from matplotlibwidgetFile import matplotlibWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())