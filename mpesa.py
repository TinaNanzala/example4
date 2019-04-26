class MpesaAccount:
	def __init__(self,name,phone_number):
		self.name = name
		self.phone_number = phone_number
		self.balance =0
		self.deposits=[]
		self.withdrawals=[]
		self.loan=0
	def deposit(self,amount):
		deposit=amount
		self.balance = self.balance + amount
		self.deposits.append(deposit)
		print ("Hello {}, you have successfuly deposited Ksh{} into your account {}. Your new M-pesa balance is Ksh{}.".format(self.name,amount,self.phone_number,self.balance))
	def withdrawals(self,amount):
		if self.balance>amount:
			self.balance = self.balance-amount
			self.withdrawals.append(amount)
			print ("Hello {}, you have successfully withdrawn Ksh{} from your account {}. Your new M-pesa balance is Ksh{}.".format(self.name,amount,self.phone_number,self.balance))
		else:
			print ("Sorry {}, you have insufficient funds to facilitate your withdrawal. Your current balance is Ksh{}.".format(self.name,self.balance))

	def check_balance(self):
			balance=self.balance
			print ("Hello {}, your M-pesa balance is Ksh{}".format(self.name,self.balance))
	def my_deposits(self):
		for x in self.deposits:
			print(x)
	def my_withdrawals(self):
		for a in self.withdrawals:
			print(a)
	def give_loan(self,amount):
		loan=amount
		if len (self.deposits)>=5 and amount<1/3 * sum(self.deposits) and self.loan==0:
			self.loan = self.loan +amount
			print("You can take a loan")

		else:
			print("sorry you cant be loaned")
	def loan_repayment(self,cash):
		repayment=cash
		if self.loan>cash:
			self.loan=self.loan-cash
			customer=("Hello{} ,you have paid a loan of {} your loan balance is{} ".format(self.name,cash,self.loan))
			print(customer)
		




     