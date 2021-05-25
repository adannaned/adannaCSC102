# -*- coding: utf-8 -*-
"""
Created on Tue May 25 12:18:36 2021

@author: SST-LAB
"""

class XBank:
    loggedinCounter = 0
    def __init__(self, theatmpin,theaccountbalance,thename):
        self.atmpin = theatmpin
        self.accountbalance = theaccountbalance
        self.name = thename
        
    def CollectMoney(self, amounttowithdraw):
        if(amounttowithdraw > self.accountbalance):
            print(f"sorry we are not able to process at this time")
        else:
            print(f"Collect your cash...Thanls for banking with XBank")
            
    def ChangePin(self, newPin):
        self.atmpin = newPin
        print("Your Pin has been changed...Thanks for banking with XBank")
    @classmethod()
    def NoOfCustomersLoggedin (cls):
        print("we have a total of" + str(XBank.loggedinCounter) + "that have logged")
        
        
        
 f = open(C:\\Users\\SST-LAB\\Documents\\adannaCSC102\\database.txt", 'r')
         
#print(f.readline())
password = []
accountB = []
name = []
breaker = []
for x in f:
    breaker = x.split(' ')
    password.append(breaker[0])
    accountB.append(breaker[1])
    name.append(breaker[2])
                    