class Tax(object):
    """
    This class takes income and loss as the input and claculates the individual tax based on tier income and loss.
    """
    def calc_tax(self,income):
        try:
            if income < 10000:
                return income
            elif 10000 < income < 30000:
                return income - (income*0.17)
            elif 30000 < income < 70000:
                return income - (income*0.28)
            else:
                return income - (income*0.35)
        except ValueError:
            pass
