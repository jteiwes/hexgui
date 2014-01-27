# -*- coding: utf-8 -*-

"""The user interface for our app"""

import os,sys

# Import Qt modules
from PyQt4 import QtCore
from PyQt4.QtCore import QObject
from PyQt4 import QtGui

from threading import Thread
import time

# Import the compiled UI module
from hexgui_ui import Ui_MainWindow

# Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.active = True
        self.all_binary =""
        # This is always the same
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        # Line.connect(Line, SIGNAL("textChanged(QString)"), Label, SLOT("setText(QString)"))
        self.ui.hex_source.connect(self.ui.hex_source, QtCore.SIGNAL("textChanged(QString)"), self.input_changed)
        self.ui.hex_source.connect(self.ui.hex_source, QtCore.SIGNAL("returnPressed()"), self.input_calc)
        # self.ui.show_button.connect(self.ui.show_button, QtCore.SIGNAL("clicked()"), self.show_part)
        self.refresh_show_part = Thread(target=self.show_part)
        self.refresh_show_part.start()
        
    def input_calc(self):
        current_input = str(self.ui.hex_source.text())
        try:
            new_input = hex(eval(current_input))
        except:
            print "could not eval this [%s]" % current_input
            new_input = current_input
        self.ui.hex_source.setText(new_input)
        
    def input_changed(self, text):
        try:
            hex_input = int(str(text), 16)
        except:
            return
        binary_text = bin(hex_input)[2:]
        leading_zeros = '0' *(int(((len(binary_text)/8)+1)*8) - len(binary_text))
        self.all_binary = str("%s%s" % (leading_zeros,binary_text))
        all_separated = ""
        for i in range(len(self.all_binary)):
            if i% 8 == 0:
                all_separated += "|"
            elif i % 4 == 0:
                all_separated += "."
            all_separated += self.all_binary[i]
        all_separated += "|"
        self.ui.binary_value.setText(all_separated)


    def show_part(self):
        while(self.active):
            time.sleep(.3)
            if(not self.ui.binary_value.hasSelectedText()):
                self.ui.part_value.setText("")
                self.ui.index_range.setText("")
                continue
            all_text = self.ui.binary_value.text()
            bin_text = self.ui.binary_value.selectedText()
            index_start = self.ui.binary_value.selectionStart()
            non_bit_values = 0
            for ch in ["|", "."]:
                non_bit_values += all_text[0:index_start].count(ch)
            index_start -= non_bit_values
            
            for ch in ["|", "."]:
                if ch in bin_text:
                    bin_text = bin_text.replace(ch, "")
            if len(bin_text) == 0:
                continue
                
            index_end = index_start + len(bin_text)
            
            self.ui.index_range.setText("[%d:%d]" % (len(self.all_binary)-index_start-1, len(self.all_binary)-index_end))
            
            dez_val = int(str(bin_text), 2)
            hex_text = (str("%x"%dez_val))
            try:
                asc_text = chr(dez_val)
            except:
                asc_text = ""
            self.ui.part_value.setText(str("0x%s (%d) %s" % (hex_text, dez_val, asc_text)))
        
    def quit(self):
        self.active = False
        self.refresh_show_part.join(.5)
        
            
def main():
    # Again, this is boilerplate, it's going to be the same on
    # almost every app you write
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    window.connect(app, QtCore.SIGNAL("lastWindowClosed()"), window.quit)
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()