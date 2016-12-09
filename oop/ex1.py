#Given the following Person class:
#
# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#
#     def greet(self, other_person):
#         print 'Hello %s, I am %s!' % (other_person.name, self.name)
# Write code to
# Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.

##THE OTHER WAY##
class Person(object):
    def __init__ (self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting = 0

    def greet(self, person):
        print "Hello %s, I'm %s!" % (person.name, self.name)
        self.greeting = self.greeting + 1

    def greeting_count(self):
        return self.greeting

    def print_contact_info(self):
        return self.email + " " + self.phone

    def add_friend (self, person):
        return self.friends.append(person)

    def num_friends (self):
        print len(jordan.friends)

    def __repr__(self):
        return self.name, self.email, self.phone


sonny = Person ("Sonny", "sonny@hotmail.com", "483-485-4948")


print "%s's email is %s and phone number is %s." % (sonny.name, sonny.email, sonny.phone)

# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.

jordan = Person ("Jordan", "jordan@aol.com", "495-586-3456")

# Have sonny greet jordan using the greet method.
sonny.greet(jordan)


# Have jordan greet sonny using the greet method.
jordan.greet(sonny)

# Write a print statement to print the contact info (email and phone) of Sonny.
print "You can contact %s at %s and %s." % (sonny.name, sonny.email, sonny.phone)

# Write another print statement to print the contact info of Jordan.
print "You can contact %s at %s and %s." % (jordan.name, jordan.email, jordan.phone)


# Make your own class
#
# Create a class Vehicle. A Vehicle object will have 3 attributes:
#
# make
# model
# year
# A vehicle is created thus:
#
# car = Vehicle('Nissan', 'Leaf', 2015)
# And you can access it's attributes individually like so:
#
# print car.make, car.model, car.year

class Vehicle(object):
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car = Vehicle("Nissan", "Leaf", 2015)

print "Today I'll ride the %s %s!" % (car.year, car.make)


#Add a method 2
# Go back to the Person class. Add a print_contact_info method to the Person class that will print out the contact info for a object instance of Person. You will use it thus:
#
# >>> sonny.print_contact_info()
# Sonny's email: sonny@hotmail.com, Sonny's phone number: 483-485-4948

print sonny.print_contact_info()

# Add an instance variable (attribute)
# Add a friends instance variable (attribute) to the Person class. You will initialize it to an empty list within the constructor (__init__). Once you've done this you should be able to add a friend to a person using list's append method:
#
#
# jordan.friends.append(sonny)
#
jordan.add_friend(sonny)

# sonny.friends.append(jordan)
# You should also be able to get the number of friends a person has by using the len function on his friends:
#

jordan.num_friends()
sonny.num_friends()
jordan.greet(sonny)
jordan.greet(sonny)
print jordan.greeting_count()

sonny.greet(jordan)
print sonny.greeting_count()
