def sqrt(value):
  return pow(value,value) 
  # Return a number that is the argument value
  # raised to the argument value power.
def main():
  from math import sqrt as square_root
  value=input("Enter a positive integer >")
  root=square_root(int(value))
  square=sqrt(root)
  print("The magic value for",value,"is",square_root(square))
  # Input a positive integer, call the sqrt
  # function from the math module using the
  # input value as an argument. Then, call the
  # above sqrt function on the result and call
  # the sqrt function from the math module on
  # that result. Finally, print the input number
  # and the final result.
  
  #Enter a positive integer >64
  #The magic value for 64 is 4096.0
main()

# Este programa muestra una lista de palabras a partr de una base y muestra la longitud de la cadena

def string_lengths(string_list):
    length_list=[]
    if(len(string_list)==0):
        print(string_list)
        print(length_list)
    else:
        for word in string_list:
            length_list.append(len(word))
        print(string_list)
        print(length_list)        
def main():
    string_input=input("Enter some words >")
    string_list=string_input.split()
    string_lengths(string_list)

main()
