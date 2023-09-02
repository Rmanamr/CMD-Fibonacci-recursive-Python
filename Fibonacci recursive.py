"""Print Fibonacci series from 0 to input(numberOfSeries) with recursive function"""

def main():
    while(True):
        print("Please enter the number of fibonacci series :")
        numberOfSeries = int(input())
        print("************")
        for i in range(1, numberOfSeries+1):
            print(fib(i))


def fib(n):
    if(n == 1):
        return 0
    elif(n == 2):
        return 1
    else:
        return fib(n-1)+fib(n-2)


if __name__ == '__main__':
    main()


#by Arman Azarnik