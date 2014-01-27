# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hexgui.ui'
#
# Created: Tue Jan 14 12:48:00 2014
#      by: PyQt4 UI code generator 4.10
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hex_source = QtGui.QLineEdit(self.centralwidget)
        self.hex_source.setObjectName(_fromUtf8("hex_source"))
        self.verticalLayout.addWidget(self.hex_source)
        self.bin_display = QtGui.QLineEdit(self.centralwidget)
        self.bin_display.setObjectName(_fromUtf8("bin_display"))
        self.verticalLayout.addWidget(self.bin_display)
        self.part_value = QtGui.QLabel(self.centralwidget)
        self.part_value.setObjectName(_fromUtf8("part_value"))
        self.verticalLayout.addWidget(self.part_value)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.hex_dest = QtGui.QLineEdit(self.centralwidget)
        self.hex_dest.setObjectName(_fromUtf8("hex_dest"))
        self.verticalLayout.addWidget(self.hex_dest)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.part_value.setText(_translate("MainWindow", "value", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hexgui.ui'
#
# Created: Tue Jan 14 12:55:44 2014
#      by: PyQt4 UI code generator 4.10
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hex_source = QtGui.QLineEdit(self.centralwidget)
        self.hex_source.setObjectName(_fromUtf8("hex_source"))
        self.verticalLayout.addWidget(self.hex_source)
        self.binary_value = QtGui.QLabel(self.centralwidget)
        self.binary_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.binary_value.setObjectName(_fromUtf8("binary_value"))
        self.verticalLayout.addWidget(self.binary_value)
        self.part_value = QtGui.QLabel(self.centralwidget)
        self.part_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.part_value.setObjectName(_fromUtf8("part_value"))
        self.verticalLayout.addWidget(self.part_value)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.hex_dest = QtGui.QLineEdit(self.centralwidget)
        self.hex_dest.setReadOnly(True)
        self.hex_dest.setObjectName(_fromUtf8("hex_dest"))
        self.verticalLayout.addWidget(self.hex_dest)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.binary_value.setText(_translate("MainWindow", "binary_value", None))
        self.part_value.setText(_translate("MainWindow", "part_value", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hexgui.ui'
#
# Created: Tue Jan 14 14:02:46 2014
#      by: PyQt4 UI code generator 4.10
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hex_source = QtGui.QLineEdit(self.centralwidget)
        self.hex_source.setObjectName(_fromUtf8("hex_source"))
        self.verticalLayout.addWidget(self.hex_source)
        self.binary_value = QtGui.QLabel(self.centralwidget)
        self.binary_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.binary_value.setObjectName(_fromUtf8("binary_value"))
        self.verticalLayout.addWidget(self.binary_value)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.part_value = QtGui.QLabel(self.centralwidget)
        self.part_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.part_value.setObjectName(_fromUtf8("part_value"))
        self.verticalLayout.addWidget(self.part_value)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.binary_value.setText(_translate("MainWindow", "binary_value", None))
        self.pushButton.setText(_translate("MainWindow", "show!", None))
        self.part_value.setText(_translate("MainWindow", "part_value", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hexgui.ui'
#
# Created: Tue Jan 14 14:03:34 2014
#      by: PyQt4 UI code generator 4.10
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hex_source = QtGui.QLineEdit(self.centralwidget)
        self.hex_source.setObjectName(_fromUtf8("hex_source"))
        self.verticalLayout.addWidget(self.hex_source)
        self.binary_value = QtGui.QLabel(self.centralwidget)
        self.binary_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.binary_value.setObjectName(_fromUtf8("binary_value"))
        self.verticalLayout.addWidget(self.binary_value)
        self.show_button = QtGui.QPushButton(self.centralwidget)
        self.show_button.setObjectName(_fromUtf8("show_button"))
        self.verticalLayout.addWidget(self.show_button)
        self.part_value = QtGui.QLabel(self.centralwidget)
        self.part_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.part_value.setObjectName(_fromUtf8("part_value"))
        self.verticalLayout.addWidget(self.part_value)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.binary_value.setText(_translate("MainWindow", "binary_value", None))
        self.show_button.setText(_translate("MainWindow", "show!", None))
        self.part_value.setText(_translate("MainWindow", "part_value", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hexgui.ui'
#
# Created: Tue Jan 14 14:06:25 2014
#      by: PyQt4 UI code generator 4.10
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hex_source = QtGui.QLineEdit(self.centralwidget)
        self.hex_source.setObjectName(_fromUtf8("hex_source"))
        self.verticalLayout.addWidget(self.hex_source)
        self.binary_value = QtGui.QLabel(self.centralwidget)
        self.binary_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.binary_value.setObjectName(_fromUtf8("binary_value"))
        self.verticalLayout.addWidget(self.binary_value)
        self.show_button = QtGui.QPushButton(self.centralwidget)
        self.show_button.setObjectName(_fromUtf8("show_button"))
        self.verticalLayout.addWidget(self.show_button)
        self.part_value = QtGui.QLabel(self.centralwidget)
        self.part_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.part_value.setObjectName(_fromUtf8("part_value"))
        self.verticalLayout.addWidget(self.part_value)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.binary_value.setText(_translate("MainWindow", "binary_value", None))
        self.show_button.setText(_translate("MainWindow", "show!", None))
        self.part_value.setText(_translate("MainWindow", "part_value", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hexgui.ui'
#
# Created: Tue Jan 14 15:26:17 2014
#      by: PyQt4 UI code generator 4.10
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hex_source = QtGui.QLineEdit(self.centralwidget)
        self.hex_source.setObjectName(_fromUtf8("hex_source"))
        self.verticalLayout.addWidget(self.hex_source)
        self.binary_value = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.binary_value.setFont(font)
        self.binary_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.binary_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.binary_value.setObjectName(_fromUtf8("binary_value"))
        self.verticalLayout.addWidget(self.binary_value)
        self.show_button = QtGui.QPushButton(self.centralwidget)
        self.show_button.setObjectName(_fromUtf8("show_button"))
        self.verticalLayout.addWidget(self.show_button)
        self.part_value = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.part_value.setFont(font)
        self.part_value.setAlignment(QtCore.Qt.AlignCenter)
        self.part_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.part_value.setObjectName(_fromUtf8("part_value"))
        self.verticalLayout.addWidget(self.part_value)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.binary_value.setText(_translate("MainWindow", "binary_value", None))
        self.show_button.setText(_translate("MainWindow", "show!", None))
        self.part_value.setText(_translate("MainWindow", "part_value", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hexgui.ui'
#
# Created: Tue Jan 14 15:27:34 2014
#      by: PyQt4 UI code generator 4.10
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hex_source = QtGui.QLineEdit(self.centralwidget)
        self.hex_source.setObjectName(_fromUtf8("hex_source"))
        self.verticalLayout.addWidget(self.hex_source)
        self.binary_value = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.binary_value.setFont(font)
        self.binary_value.setAlignment(QtCore.Qt.AlignCenter)
        self.binary_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.binary_value.setObjectName(_fromUtf8("binary_value"))
        self.verticalLayout.addWidget(self.binary_value)
        self.show_button = QtGui.QPushButton(self.centralwidget)
        self.show_button.setObjectName(_fromUtf8("show_button"))
        self.verticalLayout.addWidget(self.show_button)
        self.part_value = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.part_value.setFont(font)
        self.part_value.setAlignment(QtCore.Qt.AlignCenter)
        self.part_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.part_value.setObjectName(_fromUtf8("part_value"))
        self.verticalLayout.addWidget(self.part_value)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.binary_value.setText(_translate("MainWindow", "binary_value", None))
        self.show_button.setText(_translate("MainWindow", "show!", None))
        self.part_value.setText(_translate("MainWindow", "part_value", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hexgui.ui'
#
# Created: Tue Jan 14 15:45:13 2014
#      by: PyQt4 UI code generator 4.10
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hex_source = QtGui.QLineEdit(self.centralwidget)
        self.hex_source.setObjectName(_fromUtf8("hex_source"))
        self.verticalLayout.addWidget(self.hex_source)
        self.binary_value = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.binary_value.setFont(font)
        self.binary_value.setAlignment(QtCore.Qt.AlignCenter)
        self.binary_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.binary_value.setObjectName(_fromUtf8("binary_value"))
        self.verticalLayout.addWidget(self.binary_value)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.part_value = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.part_value.setFont(font)
        self.part_value.setAlignment(QtCore.Qt.AlignCenter)
        self.part_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.part_value.setObjectName(_fromUtf8("part_value"))
        self.verticalLayout.addWidget(self.part_value)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.binary_value.setText(_translate("MainWindow", "binary_value", None))
        self.part_value.setText(_translate("MainWindow", "part_value", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hexgui.ui'
#
# Created: Wed Jan 15 11:09:55 2014
#      by: PyQt4 UI code generator 4.10
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hex_source = QtGui.QLineEdit(self.centralwidget)
        self.hex_source.setObjectName(_fromUtf8("hex_source"))
        self.verticalLayout.addWidget(self.hex_source)
        self.binary_value = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.binary_value.setFont(font)
        self.binary_value.setAlignment(QtCore.Qt.AlignCenter)
        self.binary_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.binary_value.setObjectName(_fromUtf8("binary_value"))
        self.verticalLayout.addWidget(self.binary_value)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.index_range = QtGui.QLabel(self.centralwidget)
        self.index_range.setMaximumSize(QtCore.QSize(16777215, 20))
        self.index_range.setAlignment(QtCore.Qt.AlignCenter)
        self.index_range.setObjectName(_fromUtf8("index_range"))
        self.verticalLayout.addWidget(self.index_range)
        self.part_value = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.part_value.setFont(font)
        self.part_value.setAlignment(QtCore.Qt.AlignCenter)
        self.part_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.part_value.setObjectName(_fromUtf8("part_value"))
        self.verticalLayout.addWidget(self.part_value)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.binary_value.setText(_translate("MainWindow", "binary_value", None))
        self.index_range.setText(_translate("MainWindow", "TextLabel", None))
        self.part_value.setText(_translate("MainWindow", "part_value", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hexgui.ui'
#
# Created: Wed Jan 15 11:17:35 2014
#      by: PyQt4 UI code generator 4.10
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hex_source = QtGui.QLineEdit(self.centralwidget)
        self.hex_source.setObjectName(_fromUtf8("hex_source"))
        self.verticalLayout.addWidget(self.hex_source)
        self.binary_value = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.binary_value.setFont(font)
        self.binary_value.setAlignment(QtCore.Qt.AlignCenter)
        self.binary_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.binary_value.setObjectName(_fromUtf8("binary_value"))
        self.verticalLayout.addWidget(self.binary_value)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.index_range = QtGui.QLabel(self.centralwidget)
        self.index_range.setMaximumSize(QtCore.QSize(16777215, 20))
        self.index_range.setAlignment(QtCore.Qt.AlignCenter)
        self.index_range.setObjectName(_fromUtf8("index_range"))
        self.verticalLayout.addWidget(self.index_range)
        self.part_value = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.part_value.setFont(font)
        self.part_value.setAlignment(QtCore.Qt.AlignCenter)
        self.part_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.part_value.setObjectName(_fromUtf8("part_value"))
        self.verticalLayout.addWidget(self.part_value)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.binary_value.setText(_translate("MainWindow", "binary_value", None))
        self.index_range.setText(_translate("MainWindow", "range", None))
        self.part_value.setText(_translate("MainWindow", "part_value", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hexgui.ui'
#
# Created: Wed Jan 15 11:54:14 2014
#      by: PyQt4 UI code generator 4.10
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hex_source = QtGui.QLineEdit(self.centralwidget)
        self.hex_source.setObjectName(_fromUtf8("hex_source"))
        self.verticalLayout.addWidget(self.hex_source)
        self.binary_value = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.binary_value.setFont(font)
        self.binary_value.setAlignment(QtCore.Qt.AlignCenter)
        self.binary_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.binary_value.setObjectName(_fromUtf8("binary_value"))
        self.verticalLayout.addWidget(self.binary_value)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.index_range = QtGui.QLabel(self.centralwidget)
        self.index_range.setMaximumSize(QtCore.QSize(16777215, 20))
        self.index_range.setAlignment(QtCore.Qt.AlignCenter)
        self.index_range.setObjectName(_fromUtf8("index_range"))
        self.verticalLayout.addWidget(self.index_range)
        self.part_value = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.part_value.setFont(font)
        self.part_value.setAlignment(QtCore.Qt.AlignCenter)
        self.part_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.part_value.setObjectName(_fromUtf8("part_value"))
        self.verticalLayout.addWidget(self.part_value)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "hexgui", None))
        self.binary_value.setText(_translate("MainWindow", "binary_value", None))
        self.index_range.setText(_translate("MainWindow", "range", None))
        self.part_value.setText(_translate("MainWindow", "part_value", None))

