#!/usr/bin/env python

import sys

from drhtaxes.admission import admission


def main():

    income, losses = admission()
    
    print income, losses
        
   
if __name__ == '__main__':
    main()


