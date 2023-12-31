# Form implementation generated from reading ui file 'Proj2gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 240))
        MainWindow.setMaximumSize(QtCore.QSize(300, 240))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.typeName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.typeName.setGeometry(QtCore.QRect(170, 30, 113, 20))
        self.typeName.setObjectName("typeName")
        self.accountLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.accountLabel.setGeometry(QtCore.QRect(10, 35, 80, 10))
        self.accountLabel.setObjectName("accountLabel")
        self.submitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(119, 170, 62, 20))
        self.submitButton.setObjectName("submitButton")
        self.accountPageGuide = QtWidgets.QLabel(parent=self.centralwidget)
        self.accountPageGuide.setGeometry(QtCore.QRect(0, 10, 300, 10))
        self.accountPageGuide.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.accountPageGuide.setObjectName("accountPageGuide")
        self.passwordLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(10, 60, 60, 10))
        self.passwordLabel.setObjectName("passwordLabel")
        self.typePassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.typePassword.setGeometry(QtCore.QRect(170, 55, 113, 20))
        self.typePassword.setObjectName("typePassword")
        self.savingsCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.savingsCheckBox.setGeometry(QtCore.QRect(97, 80, 106, 15))
        self.savingsCheckBox.setObjectName("savingsCheckBox")
        self.checkPasswordLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.checkPasswordLabel.setGeometry(QtCore.QRect(10, 105, 90, 16))
        self.checkPasswordLabel.setObjectName("checkPasswordLabel")
        self.typePasswordCheck = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.typePasswordCheck.setGeometry(QtCore.QRect(170, 103, 113, 20))
        self.typePasswordCheck.setObjectName("typePasswordCheck")
        self.wrongPasswordLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.wrongPasswordLabel.setVisible(False)
        self.wrongPasswordLabel.setGeometry(QtCore.QRect(55, 123, 90, 10))
        self.wrongPasswordLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wrongPasswordLabel.setObjectName("wrongPasswordLabel")
        self.depositButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.depositButton.setVisible(False)
        self.depositButton.setGeometry(QtCore.QRect(30, 32, 69, 15))
        self.depositButton.setObjectName("depositButton")
        self.withdrawalButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.withdrawalButton.setVisible(False)
        self.withdrawalButton.setGeometry(QtCore.QRect(30, 57, 69, 15))
        self.withdrawalButton.setObjectName("withdrawalButton")
        self.amountLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.amountLabel.setVisible(False)
        self.amountLabel.setGeometry(QtCore.QRect(10, 100, 50, 10))
        self.amountLabel.setObjectName("amountLabel")
        self.amountInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.amountInput.setVisible(False)
        self.amountInput.setGeometry(QtCore.QRect(80, 95, 113, 20))
        self.amountInput.setObjectName("amountInput")
        self.balanceLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.balanceLabel.setVisible(False)
        self.balanceLabel.setGeometry(QtCore.QRect(20, 160, 100, 10))
        self.balanceLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.balanceLabel.setObjectName("balanceLabel")
        self.submitButton2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submitButton2.setVisible(False)
        self.submitButton2.setGeometry(QtCore.QRect(20, 170, 62, 20))
        self.submitButton2.setObjectName("submitButton2")
        self.backButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.backButton.setVisible(False)
        self.backButton.setGeometry(QtCore.QRect(120, 170, 62, 20))
        self.backButton.setObjectName("backButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.accountLabel.setText(_translate("MainWindow", "Account Name:"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.accountPageGuide.setText(_translate("MainWindow", "Create an account."))
        self.passwordLabel.setText(_translate("MainWindow", "Password:"))
        self.savingsCheckBox.setText(_translate("MainWindow", "Savings Account"))
        self.checkPasswordLabel.setText(_translate("MainWindow", "Check password:"))
        self.wrongPasswordLabel.setText(_translate("MainWindow", "Password is incorrect."))
        self.depositButton.setText(_translate("MainWindow", "Deposit"))
        self.withdrawalButton.setText(_translate("MainWindow", "Withdrawal"))
        self.amountLabel.setText(_translate("MainWindow", "How much?"))
        self.balanceLabel.setText(_translate("MainWindow", "Account balance: "))
        self.submitButton2.setText(_translate("MainWindow", "Submit"))
        self.backButton.setText(_translate("MainWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
