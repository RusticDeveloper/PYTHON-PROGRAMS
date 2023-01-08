from datetime import date
def create_person(name, height, birthdate):
  a_person=Person()
  a_person.name=name
  a_person.height=height
  a_person.birthdate=birthdate
  return a_person
  # Return a a new person object with the given
  # name, height and birthdate.
  # - name is a str
  # - height is an int object in centimetres
  # - birthdate is a date object from the
  # module datetime
def get_age(person):
  today= date.today()
  birdthdate=person.birthdate
  person_age=abs(birdthdate-today)
  years=person_age.days//365
  return years
  pass
  # Return the age of the person in years.
def get_description(person):
  age=get_age(person)
  return person.name+" is "+str(person.height)+" cm high and is "+str(age)+" years old."
  pass
  # Return a string object of the form: Name is
  # N cm high and is M years old, where N and M
  # are integers
  
class Person:
  pass

def main():
  d = date(1976,7,14)
  Person1=create_person('Michael',190, d)
  
  #print(d)
  print(get_description(Person1))
  # Create a person named 'Michael', with height
  # 190 cm, who was born on August 14, 1976 and
  # output a description of this individual.
  
  #Michael is 190 cm high and is 46 years old.
  #Michael is 190 cm high and is 46 years old.
  #None  
main()