class Tax(object):
    """
    This class takes income and loss as the input and claculates the individual tax.
    """
    def calc_tax(self,income):
        """
        The function tries to calculate the income tax for every individual depending on the level of income.
        """
        try:
            if income < 10000:
                return 0
            elif 10000 < income < 30000:
                return income*0.17
            elif 30000 < income < 70000:
                return income*0.28
            else:
                return income*0.35
        except ValueError:
            pass
