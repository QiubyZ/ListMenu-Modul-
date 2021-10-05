class MENU(dict):
	number = 0
	def __init__(self):
		super(MENU, self).__init__()
		
	def add(self, **kwargs):
		self.number += 1
		self.update({self.number:[kwargs.get("func"),kwargs.get("info")]})

	def showListMenu(self):
		for number, (func, info) in self.items():
			print(f"[{number}]. {info}")
			
	def getFunctionNumber(self, number):
		result = self.get(number)
		if(result != None):
			result[0]()
		return
