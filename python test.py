def as_integer(an_object):
  if isinstance(an_object,str):
    try:
      return int(an_object)
    except:
      return None
  
    
def main():
  list_items=['20', 10, len, True, '-six', '-10', '0']
  for item in list_items:
    #print(type(item))
    print(as_integer(item))
 
main() 
    