"""Print Fibonacci series from 0 to input(numberOfSeries) with recursive function"""

def main():
    while(True):
        print("Please enter the number of fibonacci series :")
        numberOfSeries = int(input())
        print("********************")
        for i in range(1, numberOfSeries+1):
            print(fibonacciSerieRecursive(i))


def fibonacciSerieRecursive(n):
    if(n == 1):
        return 0
    elif(n == 2):
        return 1
    else:
        return fibonacciSerieRecursive(n-1)+fibonacciSerieRecursive(n-2)


if __name__ == '__main__':
    main()


# by Arman Azarnik
# armanazarnik@gmail.com