def append_fibonacci(integer_list):
    if(len(integer_list)<2):
       integer_list.append(1)
    else:
        addition=integer_list[-2]+integer_list[-1]
        integer_list.append(addition)
  # Modify the argument list of integers by
  # appending a new integer that is the sum
  # of the last two integers in the list.
  # If the list has fewer than two elements
  # add the int object 1 to the list.
def main():
    list_values=[3, 5, 8]
    append_fibonacci(list_values)
    return list_values
  # Call the append_fibonacci function on this
  # list: [3, 5, 8] and output the result object
  #[3, 5, 8, 13]

print(main())