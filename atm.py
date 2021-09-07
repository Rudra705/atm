import time
class atm():

    def __init__(self,account,checkBalance,cashWithdrawl):
        self.account = account
        self.checkBalance = checkBalance
        self.cashWithdrawl = cashWithdrawl

    def account():
        print("Your account number is XXXXXXXX84798")
        time.sleep(3)
    
    def checkBalance():
        print("You already know your bank balance no need to ask ...")
        time.sleep(3)

    def cashWithdrawl():
        cash = int(input("Enter the amount of money you want to withdraw\n"))
        currency = input("Enter the name of sign of the currency in which you want to withraw\n")
        print("Your",cash,currency,"is on the way !") 
        time.sleep(3)
        


def main():
    task  = int(input("Enter what you want to do(Enter the corresponding number!):\n [1] Account [2] Check Balance [3] Cash Withdrawl \n"))
    if task == 1:
        atm.account()
    elif(task == 2):
        atm.checkBalance()
    elif(task == 3):
        atm.cashWithdrawl()
    else:
        print("Invalid !!! Enter the CORRESPONDING NUMBER.\n")
        main()



card_number = input("Enter the card_number\n")
count = 0;
for i in range(0, len(card_number)):  
    if(card_number[i] != ' '):  
        count = count + 1  

if count == 16:
    pin = input("Enter your pin\n")
    if len(str(pin)) == 4:
        main()
    else:
        print("Invalid!!! Pin should be of 4 characters\n")
        time.sleep(3)
else:
    print("Invalid!!! According to International laws, card number should be of 16 characters\n")
    time.sleep(3)