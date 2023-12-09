from PyQt6.QtWidgets import *
from Proj2gui import *
from Accounts import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.submitButton.clicked.connect(lambda: self.submit())

    def submit(self):
        name = self.typeName.text()
        password = self.typePassword.text()
        passwordCheck = self.typePasswordCheck.text()
        if name == '':
            self.accountPageGuide.setText('Please enter a name for the account.')
        elif password == '':
            self.accountPageGuide.setText('Please enter a password.')
        elif passwordCheck != password:
            self.wrongPasswordLabel.setVisible(True)
        else:
            self.submitButton.setVisible(False)
            self.accountLabel.setText(f'Account Name: {name}')
            self.accountPageGuide.setText('Choose an option below.')
            self.passwordLabel.setVisible(False)
            self.typePassword.setVisible(False)
            self.typeName.setVisible(False)
            self.savingsCheckBox.setVisible(False)
            self.checkPasswordLabel.setVisible(False)
            self.typePasswordCheck.setVisible(False)
            self.wrongPasswordLabel.setVisible(False)
            self.depositButton.setVisible(True)
            self.withdrawalButton.setVisible(True)
            self.amountLabel.setVisible(True)
            self.amountInput.setVisible(True)
            self.balanceLabel.setVisible(True)
            self.submitButton2.setVisible(True)
            self.backButton.setVisible(True)
            if self.savingsCheckBox.clicked:
                account = Account('name')
            else:
                account = SavingAccount('name')
            if self.submitButton2.clicked:
                if self.depositButton.clicked:
                    try:
                        amount = int(self.amountInput)
                        if account.deposit(amount) == False:
                            self.accountPageGuide.setText('Please determine an amount.')
                        else:
                            account.deposit(amount)
                            self.balanceLabel.setText(f'Account balance = {account.get_balance():.2f}')
                    except ValueError:
                        self.accountPageGuide.setText('Please determine an amount.')
                elif self.withdrawalButton.clicked:
                    try:
                        amount = int(self.amountInput)
                        if account.withdraw(amount) == False:
                            self.accountPageGuide.setText('Please determine an amount.')
                        else:
                            account.withdraw(amount)
                            self.balanceLabel.setText(f'Account balance: {account.get_balance():.2f}')
                    except ValueError:
                        self.accountPageGuide.setText('Please determine an amount.')
                else:
                    self.accountPageGuide.setText('Please deposit or withdrawal.')
            elif self.backButton.clicked:
                self.submitButton.setVisible(True)
                self.accountLabel.setText('Account Name:')
                self.accountPageGuide.setText('Create an account.')
                self.passwordLabel.setVisible(True)
                self.typePassword.setVisible(True)
                self.typeName.setVisible(True)
                self.savingsCheckBox.setVisible(True)
                self.checkPasswordLabel.setVisible(True)
                self.typePasswordCheck.setVisible(True)
                self.wrongPasswordLabel.setVisible(False)
                self.depositButton.setVisible(False)
                self.withdrawalButton.setVisible(False)
                self.amountLabel.setVisible(False)
                self.amountInput.setVisible(False)
                self.balanceLabel.setVisible(False)
                self.submitButton2.setVisible(False)
                self.backButton.setVisible(False)
