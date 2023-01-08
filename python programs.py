def filter_ints(word_list):
  int_list=[]
  not_int_list=[]
  for item in word_list:
    if(as_integer(item)==None):
      not_int_list.append(item)
    else:
      int_list.append(as_integer(item))
  return (int_list,not_int_list)
  # Return a tuple containing two lists.
  # The first list should contain an int
  # for each element of the argument list
  # that is a string that represents
  # a valid integer. The second list should
  # contain all the elements of the argument
  # list that do not represent valid integers.
    
def as_integer(an_object):
  if isinstance(an_object,str):
    try:
      return int(an_object)
    except:
      return None
    
def main():
  string_input=input("Enter some integers >")
  list_input=string_input.split()
  answers_tuple=filter_ints(list_input)
  ints_tupple_list = str(answers_tuple[0].copy())
  #print(ints_tupple_list)
  print("The sum of:",ints_tupple_list,"is",sum(answers_tuple[0]))
  if(len(answers_tuple[1])):
    print("These words are not integers:",str(answers_tuple[1]))
  # Prompt the user to enter some integers,
  # separated by blanks. Output a list of the
  # valid integers and the sum of these
  # integers. If the list contains some
  # "words" that are not valid integers, then
  # output a list of these "error words". If not,
  # do not output a list of these "error words".
  
main()
  
  #Enter some integers >2 4 six 8 ten 12 14
  #The sum of: [2, 4, 8, 12, 14] is 40
  #These words are not integers: ['six', 'ten']
  
 #Enter some integers >1 3 5
#The sum of: [1, 3, 5] is 9