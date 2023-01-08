from datetime import date

class Person:
  def __init__(self, name, height, birthdate):
    self._name = name
    self._height = height
    self._birthdate = birthdate
    # Set the name, height and birthdate of the
    # newly created Person object to the argument
    # objects.
    # - name is a str
    # - height is an int object in centimetres
    # - birthdate is a date object from the
    # module datetime
  
  def get_name(self):
    return str(self._name)
    # Return the name of the person as a str.
    
  def get_height(self):
    return int(self._height)
    # Return the hight of the person in cm as an
    # int.
    
  def get_age(self):
    today = date.today()
    birdthdate=self._birthdate
    y = today.year - birdthdate.year
    if today.month < birdthdate.month or today.month == birdthdate.month and today.day < birdthdate.day:
        y -= 1
    return y    
    
    #person_age=abs(birdthdate-today)
    #years=person_age.days//365
    #return years    
    # Return the age of the person in years.
    
  def get_description(self):
    age = self.get_age()
    return self.get_name()+" is "+str(self.get_height())+" cm high and is "+str(age)+" years old."    
    # Return a string object of the form: Name is
    # N cm high and is M years old, where N and M
    # are integers  
  
def main():
  Bob = Person('Daniel', 210, date(1995,11,16))
  print(Bob.get_description())

main()
  