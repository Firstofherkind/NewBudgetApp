# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Budget:
    
    def __init__(self, category):
        self.category = category
        self.amount = 10000
        
    def deposit(self):
        amountToDep = int(input('How much would you like to deposit? \n'))
        self.amount += amountToDep
        return self.amount
    def withdrawal(self):
        amountToWit = int(input('How much would you like to withdraw? \n'))
        self.amount -= amountToWit
        return self.amount
    def check_Bal(self, amount):
        #amountToCheck = int(input('Enter the amount you would like to check: \n'))
        if self.amount < amount:
            return False
        else:
            return True
    def transfer(self, amount, category):
        #amountToTrans = int(input('Enter the amount you want to transfer: \n'))
        #categoryToTransTo = input('enter the category to transfer to: \n')
        if self.check_Bal(amount) == True:
            self.amount -= amount
            cat_1.amount += amount
            return f'you have transferred {amount} to {cat_1.category}.'
        
        else: 
            return f'You do not have sufficient balance to make the transfer'
    
cat_1 = Budget(('food'))
print(cat_1.deposit())
print(cat_1.withdrawal())
print(cat_1.check_Bal(300))
print(cat_1.transfer(1300, 'Clothing'))

    