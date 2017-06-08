import sys

def tax_input_checker(typed_input):
    """
    returns true if the input string cannot be converted to a float, and false if otherwise
    """
    try:
        f = float(typed_input)
    except ValueError:
        return False
    return True

def admission():
    
    if len(sys.argv) == 3:
        
        income = sys.argv[1]
        
        if tax_input_checker(income) == False:
            print 'please re-enter your income in an appropriate format'
            

        losses = sys.argv[2]
        
        if tax_input_checker(losses) == False:
            print 'please re-enter your losses in an appropriate form'
        
        return income, losses
    else:
        print "please input your income followed by your losses"
        exit()

    


