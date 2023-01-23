# Excise 1

# Try defining an object that represents a student. Include at least 3 variables that describe the student, including age. Define a constructor and a method get_olderO which increases the student's age by the argument. You don't need to define all the getters and setters.

class Student:
    def __init__(self) -> None:
        self.name = "John"
        self.age = 20
        self
    
    def get_older(self, age):
        self.age = age
        return self.age
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age
    
    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"
    
    def __repr__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"

student = Student()
print(student)
student.set_name("John")
student.set_age(20)
print(student)
student.get_older(21)
print(student)



# Excise 2

# Modify the robot code above to have a non-static method pew(), a static robots_ destroyed variable, and a non-static dead variable. On calling robot.pew(target), if the target or the shooter (self) was dead, do nothing. If both are alive, announce that the caller of pewO is firing at its target, set the target to dead, increment robots_destroyed, and print the value of robots_destroyed.

class Robot:
  robot_count = 0 # static variable
  
  # TODO robots_destroyed initialized here

  def __init__(self):
    self.name = "robot" + str(Robot.robot_count)
    print("Hello, " + self.name + "!")
    Robot.update_robot_count() # static method, uses Class name

  def update_robot_count(): # notice no "self"
    Robot.robot_count += 1
    
  def pew(self, target):
    
    # Some code here
    robots_destoryed = 0
    dead = False
    
    # Fire at and destroy another robot.
    if target.dead == True or self.dead == True:
        return
    else:
        print(self.name + " is firing at " + target.name)
        target.dead = True
        robots_destoryed += 1
        print(robots_destoryed)
    

    # TODO Check that both self and target are alive

    
    # TODO To make the target dead
    Robot.robots_destroyed += 1
    print(f'Robots destroyed: {Robot.robots_destroyed}')
    
    # TODO increment robots_destroyed
    robots_destoryed += 1
    print(f'Robots destroyed: {robots_destoryed}')

    # TODO update Robot.robots_destroyed
    print(f'Robots destroyed: {Robot.robots_destroyed}')