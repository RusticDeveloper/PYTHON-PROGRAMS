def append_fibonacci(integer_list):
    if(len(integer_list)<2):
        integer_list.append(1)
    else:
        addition=integer_list[-2]+integer_list[-1]
        integer_list.append(addition)
        return addition
    # Modify the argument list of integers by
    # appending a new integer that is the sum
    # of the last two integers in the list.
    # If the list has fewer than two elements
    # add the int object 1 to the list.
def fibonacci(max):
    actual_fibonacci=1
    fibo_list=[1,1]
    while(actual_fibonacci<max):
        actual_fibonacci=append_fibonacci(fibo_list)
    if(actual_fibonacci>max):
        fibo_list.pop()
    return fibo_list
    # Return a list that contains all Fibonacci
    # numbers that are less than or equal
    # to the argument integer.
def main():
    value=input("Enter a non-negative integer >")
    try:
        integer_value=int(value)
        return fibonacci(integer_value)           
    except:
        return (value+"is not a non-negative integer")
     
        
print(main())
    # Input a non-negative integer, n. Output
    # the Fibonacci numbers that are less than
    # or equal to that number, in order. If the
    # input is not a valid non-negative integer,
    # output a warning message.
    #Enter a non-negative integer >23
    #The Fibonacci series starts with: [1, 1, 2, 3, 5, 8, 13, 21]
    #Enter a non-negative integer >13
    #The Fibonacci series starts with: [1, 1, 2, 3, 5, 8, 13]
    #Enter a non-negative integer >0
    #The Fibonacci series starts with: []
    #Enter a non-negative integer >ten
    #ten is not a non-negative integer    