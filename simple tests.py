# Output the argument list, the largest
# element in the list and the second largest
# element in the list
#The largest and second largest elements in the list ['computer', 'science', 'university', 'alberta', 'edmonton'] are university and science

def largest_two(target_list):
    copy_list=target_list.copy()
    first_largest=max(copy_list)
    second_largest=sec_largest(copy_list)
    print("The largest and second largest elements in the list", target_list ,"are" ,first_largest ,"and", second_largest)

def sec_largest(list_2_trim):
    list_2_trim.remove(max(list_2_trim))
    second_max=max(list_2_trim)
    return second_max

largest_two(['computer', 'science', 'university', 'alberta', 'edmonton'])


