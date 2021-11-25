class Car:
  pass
#dlaczego nic się nie drukuje
my_car=Car()
type(my_car)

# co jest źle?
class Car:  
   def __init__(self):
       pass
#dlaczego nic się nie drukuje? linia 12. Jest agument top_speed i color ?
class Car:
    def __init__(self,make,model_name,top_speed,color):
       self.make = make
       self.model_name = model_name
       self.top_speed=top_speed
       self.color=color
mustang=Car(make="ford",model_name="mustang",color="white",top_speed="250")
print(mustang)
print(mustang.make)

# co jest źle? próbuje ze spacjami/ odstępami itp - nic nie pomaga
def __str__(self):
    return f'{self.color}{self.make} {self.model_name}'
print(mustang)

# nic się nie drukuje 
def __repr__(self):
    return f" Car(make={self.make} model={self.model_name} top spedd={self.top.speed} color={self.color}"
print(Car)

#eq się nie podświetla
def __eq__(self,other):
   return(
       self.make==other.make and
       self.model_name== other.model_make and
       self.top.speed== other.top_speed and
       self.color==other.color
   )

