class COR(object):

	def corp(self,income,incurred_loss):

		if income < 80000:
			tax = (income*0.2)
	
		elif income >= 80000:
			tax = (income - incurred_loses)*0.2
		return tax
		print (tax)
