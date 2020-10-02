# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_structures_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from modules.AVL import avl
from modules.OPTIMALTREE import optimaltree
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 771, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_avl = QtWidgets.QWidget()
        self.tab_avl.setObjectName("tab_avl")
        self.box_avl = QtWidgets.QGroupBox(self.tab_avl)
        self.box_avl.setGeometry(QtCore.QRect(0, 40, 761, 451))
        self.box_avl.setObjectName("box_avl")
        self.graphics_avl = QtWidgets.QGraphicsView(self.box_avl)
        self.graphics_avl.setGeometry(QtCore.QRect(10, 20, 751, 431))
        self.graphics_avl.setObjectName("graphics_avl")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_avl)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 401, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_input_avl = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.txt_input_avl.setObjectName("txt_input_avl")
        self.horizontalLayout.addWidget(self.txt_input_avl)
        self.btn_insert = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_insert.setObjectName("btn_insert")
        self.horizontalLayout.addWidget(self.btn_insert)
        self.btn_search = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout.addWidget(self.btn_search)
        self.btn_delete = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        self.lbl_avl = QtWidgets.QLabel(self.tab_avl)
        self.lbl_avl.setGeometry(QtCore.QRect(450, 0, 281, 41))
        self.lbl_avl.setText("")
        self.lbl_avl.setObjectName("lbl_avl")
        self.tabWidget.addTab(self.tab_avl, "")
        self.tab_optimal = QtWidgets.QWidget()
        self.tab_optimal.setObjectName("tab_optimal")
        self.box_optimal_tree = QtWidgets.QGroupBox(self.tab_optimal)
        self.box_optimal_tree.setGeometry(QtCore.QRect(9, 79, 741, 411))
        self.box_optimal_tree.setObjectName("box_optimal_tree")
        self.graphics_optimal_tree = QtWidgets.QGraphicsView(self.box_optimal_tree)
        self.graphics_optimal_tree.setGeometry(QtCore.QRect(-5, 21, 751, 391))
        self.graphics_optimal_tree.setObjectName("graphics_optimal_tree")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_optimal)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 441, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_input_frequency_optimal_tree = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_input_frequency_optimal_tree.setObjectName("txt_input_frequency_optimal_tree")
        self.gridLayout.addWidget(self.txt_input_frequency_optimal_tree, 1, 1, 1, 1)
        self.btn_insert_optimal_tree = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_insert_optimal_tree.setObjectName("btn_insert_optimal_tree")
        self.gridLayout.addWidget(self.btn_insert_optimal_tree, 1, 2, 1, 1)
        self.lbl_frequecy_optimal_tree = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_frequecy_optimal_tree.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_frequecy_optimal_tree.setObjectName("lbl_frequecy_optimal_tree")
        self.gridLayout.addWidget(self.lbl_frequecy_optimal_tree, 0, 1, 1, 1)
        self.lbl_key_optimal_tree = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_key_optimal_tree.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_key_optimal_tree.setObjectName("lbl_key_optimal_tree")
        self.gridLayout.addWidget(self.lbl_key_optimal_tree, 0, 0, 1, 1)
        self.btn_build_optimal_tree = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_build_optimal_tree.setObjectName("btn_build_optimal_tree")
        self.gridLayout.addWidget(self.btn_build_optimal_tree, 1, 3, 1, 1)
        self.txt_input_key_optimal_tree = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_input_key_optimal_tree.setObjectName("txt_input_key_optimal_tree")
        self.gridLayout.addWidget(self.txt_input_key_optimal_tree, 1, 0, 1, 1)
        self.btn_search_optimal_tree = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_search_optimal_tree.setObjectName("btn_search_optimal_tree")
        self.gridLayout.addWidget(self.btn_search_optimal_tree, 1, 4, 1, 1)
        # self.btn_cost_optimal_tree = QtWidgets.QPushButton(self.gridLayoutWidget)
        # self.btn_cost_optimal_tree.setObjectName("btn_cost_optimal_tree")
        # self.gridLayout.addWidget(self.btn_cost_optimal_tree, 0, 4, 1, 1)
        self.lbl_optimal_tree = QtWidgets.QLabel(self.tab_optimal)
        self.lbl_optimal_tree.setGeometry(QtCore.QRect(460, 30, 281, 41))
        self.lbl_optimal_tree.setText("")
        self.lbl_optimal_tree.setObjectName("lbl_optimal_tree")
        self.tabWidget.addTab(self.tab_optimal, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.scene = QtWidgets.QGraphicsScene()
        self.btn_insert.clicked.connect(self.insert_avl)
        self.btn_search.clicked.connect(self.search_avl)
        self.btn_delete.clicked.connect(self.delete_avl)
        self.avl = avl.AvlTree()
        self.avl_step = 0

        self.btn_insert_optimal_tree.clicked.connect(self.insert_optimal)
        self.btn_search_optimal_tree.clicked.connect(self.search_optimal)
        self.btn_build_optimal_tree.clicked.connect(self.build_optimal)
        self.opt = optimaltree.OptimalTree()
        self.keys = []
        self.freq = []


    def load_avl(self):
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(QtGui.QPixmap('./modules/AVL/graphviz_avl/avl_graph.png'))
        self.graphics_avl.setScene(self.scene)

    def insert_avl(self):
        if self.txt_input_avl.text() == '':
            return
        self.avl.insert(int(self.txt_input_avl.text()))
        self.avl.show('Step: ' + str(self.avl_step) + '\n Insert(' + self.txt_input_avl.text() + ')')
        self.avl_step += 1
        self.txt_input_avl.setText('')
        self.load_avl()

    def delete_avl(self):
        if self.txt_input_avl.text() == '':
            return
        self.avl.delete(int(self.txt_input_avl.text()))
        self.avl.show('Step: ' + str(self.avl_step) + '\n Delete(' + self.txt_input_avl.text() + ')')
        self.avl_step += 1
        self.txt_input_avl.setText('')
        self.load_avl()

    def search_avl(self):
        if self.txt_input_avl.text() == '':
            return
        if self.avl.find(int(self.txt_input_avl.text())):
            self.avl.show('Step: ' + str(self.avl_step) + '\nThe key ' + self.txt_input_avl.text() + ' was found')
        else:
            self.avl.show('Step: ' + str(self.avl_step) + '\nThe key ' + self.txt_input_avl.text() + ' was not found')
        self.avl_step += 1
        self.txt_input_avl.setText('')
        self.load_avl()

    def load_optimal(self):
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(QtGui.QPixmap('./modules/OPTIMALTREE/graphviz_optimal/optimal_graph.png'))
        self.graphics_optimal_tree.setScene(self.scene)

    def insert_optimal(self):
        if self.txt_input_key_optimal_tree.text() == '':
            return
        if self.txt_input_frequency_optimal_tree.text() == '':
            return
        self.keys.append(int(self.txt_input_key_optimal_tree.text()))
        self.freq.append(int(self.txt_input_frequency_optimal_tree.text()))
        self.txt_input_key_optimal_tree.setText('')
        self.txt_input_frequency_optimal_tree.setText('')

    def search_optimal(self):
        if self.txt_input_key_optimal_tree.text() == '':
            return
        if self.opt.find(int(self.txt_input_key_optimal_tree.text())):
            self.opt.show('The key ' + self.txt_input_key_optimal_tree.text() + ' was found')
        else:
            self.opt.show('The key ' + self.txt_input_key_optimal_tree.text() + ' was not found')
        self.txt_input_key_optimal_tree.setText('')
        self.load_optimal()

    def build_optimal(self):
        self.opt = optimaltree.OptimalTree(self.keys, self.freq)
        self.opt.build()
        self.opt.show('Optimal tree cost: ' + str(self.opt.total_cost))
        self.load_optimal()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.box_avl.setTitle(_translate("MainWindow", "AVL"))
        self.btn_insert.setText(_translate("MainWindow", "Insert"))
        self.btn_search.setText(_translate("MainWindow", "Search"))
        self.btn_delete.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_avl), _translate("MainWindow", "AVL"))
        self.box_optimal_tree.setTitle(_translate("MainWindow", "Optimal Tree"))
        self.btn_insert_optimal_tree.setText(_translate("MainWindow", "Insert"))
        self.lbl_frequecy_optimal_tree.setText(_translate("MainWindow", "Frequency"))
        self.lbl_key_optimal_tree.setText(_translate("MainWindow", "Key"))
        self.btn_build_optimal_tree.setText(_translate("MainWindow", "Build"))
        self.btn_search_optimal_tree.setText(_translate("MainWindow", "Search"))
        # self.btn_cost_optimal_tree.setText(_translate("MainWindow", "Cost"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_optimal), _translate("MainWindow", "Optimal Tree"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
