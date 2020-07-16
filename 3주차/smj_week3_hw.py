import random

class Account:

    #계좌 개수
    account_num = 0

    # 유저 이름과 잔액만 매개변수로 받으면 됨
    def __init__(self, user, balance):
        self.deposit_num = 0 #입금횟수
        self.deposit_log = [] #입금기록
        self.withdraw_log = [] #출금기록
        self.bankname = 'SC은행'
        #랜덤 계좌번호
        self.user_account = str(random.randint(0,999)).zfill(3) + "-" + str(random.randint(0,99)).zfill(2) + "-" + str(random.randint(0,999999)).zfill(6)                                                                                                                  
        self.user = user #유저명
        self.balance = balance #잔액

        #계좌 하나 만들 때 마다 +1
        Account.account_num += 1

    #생성된 계좌 수    
    @classmethod
    def get_account_num(cls):
        print(cls.accoount_num)

    #입금
    def deposit(self, money):
        if (money >= 1):
            self.balance += money

        self.deposit_log.append(money)
        self.deposit_num += 1
        
        #이자
        if self.deposit_num % 5 == 0:
            self.balance = self.balance + (self.balance * 0.01)

    #출금
    def withdraw(self, money):
        if (self.balance > money):
            self.withdraw_log.append(money)
            self.balance -= money

    def display_info(self):
        print('은행이름:', self.bankname)
        print('예금주:', self.user)
        print('계좌번호:', self.user_account)
        print('잔고:', format(self.balance, ','))

    #출금내역
    def deposit_history(self):
        for money in self.deposit_log:
            print('+', format(money, ','))

    #입금내역
    def withdraw_history(self):
        for money in self.withdraw_log:
            print('-', format(money, ','))


#계좌 리스트 생성 및 유저 추가
account_list = []
user1 = Account("Moonyoung", 10000)
user2 = Account("Gangtea", 5000)
user3 = Account("Sangtea", 3000)
account_list.append(user1)
account_list.append(user2)
account_list.append(user3)

#입금 및 출금 기록 만들기
user1.deposit(10000000)
user2.deposit(100000)
user3.deposit(100000)
user1.withdraw(100000)
user2.withdraw(8000)
user3.withdraw(30000)

#출력
print('=== Moonyoung ===')
user1.deposit_history()
user1.withdraw_history()
print('잔고:', format(user1.balance, ','))
print()
print('=== Gangtea ===')
user2.deposit_history()
user2.withdraw_history()
print('잔고:', format(user2.balance, ','))
print()
print('=== Sangtea ===')
user3.deposit_history()
user3.withdraw_history()
print('잔고:', format(user3.balance, ','))
print()
print('=== 잔고 100만원 이상 ===')
for i in account_list:
    if i.balance >= 1000000:
        i.display_info()
    
            
