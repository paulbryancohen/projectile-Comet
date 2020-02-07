''' a collection is an object that contains a 
    set - collection of unique objects
    list - mutable sequence of objects
    Dictionary - collection of key/ value pairs
    tuple - immutable sequence of objects

    mutable - can be chanched after created
'''

cities = ["New York", "Trenton", "Paris", "London"]
interests = ["Learning Python","Automate the Boring Stuff with Python","Python for Data Analysis","Fluent Python","Python for Kids","Hello Web App",]


for item in interests.copy():
    interests.remove(item)
    print("removed")




def list_display(display_name, wishes):
    print (display_name + " : ")
    for wish in wishes:
        print (" * " + wish)

list_display("Interest", interests)
list_display("Cities", cities)