# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:20:16 2021

@author: Sruti
"""
import sys
try:
    from PyQt5.QtWidgets import QWidget, QHBoxLayout, QComboBox
    from PyQt5.QtWidgets import QApplication, QComboBox, QMainWindow 
    from PyQt5.QtWidgets import QWidget, QVBoxLayout 
    from PyQt5.QtGui import QStandardItemModel 
    from PyQt5.QtCore import Qt
except ImportError:
    # needed for py3+qt4
    # Ref:
    # http://pyqt.sourceforge.net/Docs/PyQt4/incompatible_apis.html
    # http://stackoverflow.com/questions/21217399/pyqt4-qtcore-qvariant-object-instead-of-a-string
    if sys.version_info.major >= 3:
        import sip
        sip.setapi('QVariant', 2)
    from PyQt4.QtGui import QWidget, QHBoxLayout, QComboBox


class CheckableComboBox(QMainWindow):
    
    ####self is reference to main window
    def __init__(self, parent=None, items=[]):
        super(CheckableComboBox, self).__init__(parent)

        # layout = QHBoxLayout() #Linear horizontal layout
        
        
        myQWidget = QWidget()
        
        myBoxLayout = QVBoxLayout()
        
        myQWidget.setLayout(myBoxLayout)
        
        self.setCentralWidget(myQWidget)
        
        self.cb = QComboBox() #define dropdown list box
        
        self.items = items
        self.cb.addItems(self.items)   #Adds user defined item
        
        #if option selection gets changed
        
        #defined comboSelectionChanged at line 893 labelImg.py
        self.cb.currentIndexChanged.connect(parent.comboSelectionChanged)
        
        # print('new item added')

        # layout.addWidget(self.cb)
        # self.setLayout(layout)
        
        myBoxLayout.addWidget(self.cb)
        self.setLayout(myBoxLayout)
        
    def update_items(self, items):
        self.items = items

        self.cb.clear()
        self.cb.addItems(self.items)

    def handle_item_pressed(self, items): 
  
        # getting which item is pressed 
        item = self.model().itemFromIndex(items) 
  
        # make it check if unchecked and vice-versa 
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked) 
        else: 
            item.setCheckState(Qt.Checked) 
  
        # calling method 
        self.check_items() 
