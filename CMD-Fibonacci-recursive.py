"""Python CMD program for printing Fibonacci series from 0 to input value(number_Of_Series) with a recursive function.
using Python version 3.11.4
@version : 1.0
@license: MIT License
@author : Arman Azarnik
contact me at : armanazarnik@gmail.com
"""

def main():
    """
    main function for interacting with the user
    """
    while(True):
    # while loop to keep the program running

        print("Please enter the number of fibonacci series :")
        number_Of_Series = int(input())
        # casting the input string into integer

        print("Your Fibonacci serie :")
        result = store_Fibonacci_series_in_array(number_Of_Series)
        # storing Fibonacci serie array in result variable 

        array_Printer(result)
        print("**************************************************")


def Fibonacci_Serie_Generator_Recursive(number):
    """
    function for generating the Fibonacci series with a recursive function.
    @param number: the input for serie number.
    @type text: int
    @return: Fibonacci serie number
    @rtype: integer
    @examples: 
     >>> Fibonacci_Serie_Generator_Recursive(0)
         
     >>> Fibonacci_Serie_Generator_Recursive(5)
         3
    """
    if(number == 1):
        return 0

    elif(number == 2):
        return 1
    
    else:
        return Fibonacci_Serie_Generator_Recursive(number - 1) + Fibonacci_Serie_Generator_Recursive(number - 2)
    

def store_Fibonacci_series_in_array(number):
    """
    function for storing the generated Fibonacci serie in  an array.
    @param number: the input for serie number.
    @type text: int
    @return: Fibonacci_Series
    @rtype: array of integers
    @examples: 
     >>> Fibonacci_Serie_Generator_Recursive(0)
         []
     >>> Fibonacci_Serie_Generator_Recursive(5)
         [0, 1, 1, 2, 3]
    """
    Fibonacci_Series = [None]*(number)
    # initializing an empty array with lenght of number

    for i in range(0, number):
        Fibonacci_Series[i] = Fibonacci_Serie_Generator_Recursive(i+1)
        # storing Fibonacci serie numbers, first number in index 0, second number in index 1 and ...

    return Fibonacci_Series


def array_Printer(array):
    """
    function for printing each array element in a line.
    @param array: an array of elements.
    @type text: anything like integer, double and string.
    @examples: 
         array_1 = []
         array_2 = [1, 2, 3]
     >>> array_Printer(array_1)
          
     >>> array_Printer(array_2)
         1
         2
         3
    """
    for element in array:
        print(element)


if __name__ == '__main__':
    main()
    # run the main function after executing this file