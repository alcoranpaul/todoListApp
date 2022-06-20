"""todoList
A simple todo List app

Version: 3
Author: Paul Adrian A. Reyes
Date: June 20, 2022
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem


class Ui_MainWindow(object):
    projects = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ToDoList_App")
        MainWindow.resize(1050, 750)
        MainWindow.setMinimumSize(QtCore.QSize(1050, 750))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # Line Project
        self.lineEdit_LineProj = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_LineProj.sizePolicy().hasHeightForWidth())
        self.lineEdit_LineProj.setSizePolicy(sizePolicy)
        self.lineEdit_LineProj.setMinimumSize(QtCore.QSize(174, 54))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(12)
        self.lineEdit_LineProj.setFont(font)
        self.lineEdit_LineProj.setObjectName("lineEdit_LineProj")
        self.gridLayout_2.addWidget(self.lineEdit_LineProj, 2, 0, 2, 2)

        # Delete Project
        self.pushButton_DeleteProj = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.deleteProj())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_DeleteProj.sizePolicy().hasHeightForWidth())
        self.pushButton_DeleteProj.setSizePolicy(sizePolicy)
        self.pushButton_DeleteProj.setMinimumSize(QtCore.QSize(96, 24))
        font = QtGui.QFont()
        font.setFamily("Fira Code SemiBold")
        font.setPointSize(10)
        self.pushButton_DeleteProj.setFont(font)
        self.pushButton_DeleteProj.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.pushButton_DeleteProj.setObjectName("pushButton_DeleteProj")
        self.gridLayout_2.addWidget(self.pushButton_DeleteProj, 0, 1, 1, 1)

        # New Project
        self.pushButton_NewProj = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.newProj())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_NewProj.sizePolicy().hasHeightForWidth())
        self.pushButton_NewProj.setSizePolicy(sizePolicy)
        self.pushButton_NewProj.setMinimumSize(QtCore.QSize(96, 24))
        font = QtGui.QFont()
        font.setFamily("Fira Code SemiBold")
        font.setPointSize(10)
        self.pushButton_NewProj.setFont(font)
        self.pushButton_NewProj.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.pushButton_NewProj.setObjectName("pushButton_NewProj")
        self.gridLayout_2.addWidget(self.pushButton_NewProj, 0, 0, 1, 1)

        # Project List
        self.listWidget_ProjList = QtWidgets.QListWidget(self.centralwidget, clicked=lambda: self.getItem())
        self.listWidget_ProjList.setObjectName("listWidget_ProjList")
        self.gridLayout_2.addWidget(self.listWidget_ProjList, 4, 0, 1, 2)

        # Add Item
        self.pushButton_AddItem = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.addItem())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_AddItem.sizePolicy().hasHeightForWidth())
        self.pushButton_AddItem.setSizePolicy(sizePolicy)
        self.pushButton_AddItem.setMinimumSize(QtCore.QSize(75, 24))
        font = QtGui.QFont()
        font.setFamily("Fira Code SemiBold")
        font.setPointSize(10)
        self.pushButton_AddItem.setFont(font)
        self.pushButton_AddItem.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.pushButton_AddItem.setObjectName("pushButton_AddItem")
        self.gridLayout_2.addWidget(self.pushButton_AddItem, 0, 3, 1, 1)

        # Delete Item
        self.pushButton_DeleteItem = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.deleteItem())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_DeleteItem.sizePolicy().hasHeightForWidth())
        self.pushButton_DeleteItem.setSizePolicy(sizePolicy)
        self.pushButton_DeleteItem.setMinimumSize(QtCore.QSize(75, 24))
        font = QtGui.QFont()
        font.setFamily("Fira Code SemiBold")
        font.setPointSize(10)
        self.pushButton_DeleteItem.setFont(font)
        self.pushButton_DeleteItem.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.pushButton_DeleteItem.setObjectName("pushButton_DeleteItem")
        self.gridLayout_2.addWidget(self.pushButton_DeleteItem, 0, 2, 1, 1)

        # Clear Items
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clearAll())
        font = QtGui.QFont()
        font.setFamily("Fira Code SemiBold")
        font.setPointSize(10)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout_2.addWidget(self.pushButton_clear, 0, 4, 1, 1)

        # Line Item
        self.lineEdit_LineItem = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_LineItem.sizePolicy().hasHeightForWidth())
        self.lineEdit_LineItem.setSizePolicy(sizePolicy)
        self.lineEdit_LineItem.setMinimumSize(QtCore.QSize(525, 54))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(12)
        self.lineEdit_LineItem.setFont(font)
        self.lineEdit_LineItem.setObjectName("lineEdit_LineItem")
        self.gridLayout_2.addWidget(self.lineEdit_LineItem, 2, 2, 2, 3)

        # Item List
        self.listWidget_ItemList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_ItemList.sizePolicy().hasHeightForWidth())
        self.listWidget_ItemList.setSizePolicy(sizePolicy)
        self.listWidget_ItemList.setMinimumSize(QtCore.QSize(600, 100))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(12)
        self.listWidget_ItemList.setFont(font)
        self.listWidget_ItemList.setObjectName("listWidget_ItemList")
        self.gridLayout_2.addWidget(self.listWidget_ItemList, 4, 2, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # Save
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_AddItem.setText(_translate("MainWindow", "Add"))
        self.pushButton_DeleteProj.setText(_translate("MainWindow", "Delete Proj"))
        self.pushButton_NewProj.setText(_translate("MainWindow", "New Proj"))
        self.pushButton_DeleteItem.setText(_translate("MainWindow", "Delete"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))

    # Functions

    def readItems(self, allItems: list, listType: QtWidgets):
        """Reads the items of a project
        """
        listType.clear()
        for item in allItems:
            listType.addItem(item)

    def addItem(self):
        """ Adds item to list
        """
        projectName = self.listWidget_ProjList.currentItem().text()  # Grab the current/selected item in projects
        allItems = self.projects.get(projectName)  # Grab the array item of the project
        item = self.lineEdit_LineItem.text()  # Grabs the item in line item box
        allItems.append(item)  # Add Item to list
        # self.listWidget_ItemList.addItem(item)
        self.readItems(allItems, self.listWidget_ItemList)  # Reads the contents of the project
        self.lineEdit_LineItem.setText("")  # Clear item box
        self.projects[projectName] = allItems  # Update project Items

    def deleteItem(self):
        """Deletes Item in list
        """
        projectName = self.listWidget_ProjList.currentItem().text()  # Grab the current/selected item in projects
        allItems = self.projects.get(projectName)  # Grab the array item of the project
        clicked = self.listWidget_ItemList.currentRow()  # Grab the selected row
        item = self.listWidget_ItemList.takeItem(clicked).text()  # Delete selected row
        allItems.remove(item)
        self.projects[projectName] = allItems  # Update project Items

    def clearAll(self):
        """Clears all items in list
        """
        self.listWidget_ItemList.clear()  # Clear List
        projectName = self.listWidget_ProjList.currentItem().text()  # Grab the current/selected item in projects
        allItems = []  # Create an empty list
        self.projects[projectName] = allItems  # Update project Items

    def newProj(self):
        """Create a new project
        """
        project = self.lineEdit_LineProj.text()  # Grabs the item in the project item box
        item = QListWidgetItem(project)
        self.projects[item.text()] = []  # Create an empty array to hold items
        self.listWidget_ProjList.addItem(item)  # Append project to Project list
        self.listWidget_ProjList.setCurrentItem(item)
        self.lineEdit_LineProj.setText("")  # Clear item box

    def deleteProj(self):
        """Delete a project
        """
        projectRow = self.listWidget_ProjList.currentRow()  # Grab Project Row
        projectName = self.listWidget_ProjList.takeItem(projectRow).text()  # Get Project and remove
        del self.projects[projectName]  # Delete project from dictionary

    def getItem(self):
        projectName = self.listWidget_ProjList.currentItem().text()  # Grab the current/selected item in projects
        allItems = self.projects.get(projectName)  # Grab the array item of the project
        self.readItems(allItems, self.listWidget_ItemList)  # Reads the contents of the project


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
