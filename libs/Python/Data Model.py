# Every object in python has three features after it has been created
# 1) Identity -< kind of address in memory and used by 'is' to compare two objects
# id(x) returns the identity of an object
# 2) type
# 3) Value

a = 4
print('The id of a is ', id(a))
print('The type of a is ', type(a))
print('THe value of a is ', a)

def sample_function(x, y=10):
    """
    This text here is the documentation of this function
    and everyone should also write docs for their functions.
    """
    print('You are in the function')
    a = 3
    global b
    b = 10
    key = 'Some Function'
    return(a,b, key)

#-------------------------------------------------------------------------------------------------
# Callable methods to a functions

# To get documentation of a function
print('\nThe __doc__ method ', sample_function.__doc__)

# To get the name name of a function
print('\nThe __name__ method ', sample_function.__name__)

# To get the qualified name i.e. the class heiarchy in which the function is present
print('\nThe __qualname__ method ', sample_function.__qualname__)

# To get the modele name inwhich function is defined
print('\nThe __module__ method ', sample_function.__module__)

# TO get the default arguments of a function
print('\nThe __default__ method ', sample_function.__defaults__)

# To get the code inside the function
print('\nThe __code__method n', sample_function.__code__)

# To get the globals defined inside the function
print('\nThe __globals__ method n', sample_function.__globals__)
#-------------------------------------------------------------------------------------------------


print('\n\n')
# Instance methods
# Special method names for classes

#--------------------------------------------------------------------------------------------------
class sample:
    # We rarely use this function but remember it is this function that creates our instance
    #    def __new__(*args, **kwargs):
    #        # To create a new instance of a class
    #        # You need not define it
    #        # It is called using super().__new__(class_name, constructor arguments)
    #        pass

    def __init__(self, val):
        # Called after our instance has been created by __new__
        # The code in this function would be automatically executed when you create a class
        self.val = val
        print('\nClass instance created with value = %d\n'%(self.val))

    def __del__(self):
        # Called when the instance has to be deleted using
        # del instance_name
        print('The instance object hsa been deleted\n')

    def __repr__(self):
        # Used when you want to print the instance object using
        # print(instance_object_name)
        return 'The object has 1 variable whose value is %d\n'%(self.val)
        # The return value should be a string

    def __str__(self):
        # Called by str(object) and the build in function format() and print() to compute
        # printable string representation of an object.
        # The only difference between __repr__ and __str__ is that in __str__ we can use
        # a more convenient and concise representation.
        text = 'Did you know that you print various tree structures using __str__'
        return text
        # Also notice that it has replaced __repr__  by commenting this function and
        # printing the object

    # Comaprison functions used to compute comparisons between x and y
    def __lt__(self, other):    # Less than
        if(self.val < other.val):
            print('x is less than y')
            return True
        return False
    def __le__(self,other):     # less than equal to
        pass
    def __gt__(self, other):    # greater than
        pass
    def __ge__(self, other):    # greater than equal to
        pass
    def __eq__(self, other):    # equal to
        pass
    def __ne__(self, other):    # not equal to
        pass
    # These functions would return NotImplemented if it does not perform the operation on self and other
    # Use these functions as
    # x<y, x!=y  where x and y are class instance objects


    def __hash__(self):
        # If you want to use hash(object)
        # It would be used to create a hash for the object
        return hash(self.val)

        # Some things to remember
        # Do not create a hash if object contains mutable objects
        # If class does not define__eq__ you should not define __hash__

    def __bool__(self):
        # Used to use class objects in boolean operations
        if(self.val > 0):
            return True

A = sample(10)
print(A)

print('\n Using the __bool__')
if(A):
    print(A)
#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
# Customizing attribute access
class Sample:
    def __getattr__(self, attribute_name):
        # Called when attribute_name is not found in the class tree
        print('The attribute you are looking for is not defined by you')
        # Do something about it, if you want to

    def __getattribute__(self, name):
        # If defined it would replace the __getattr__
        # It should return the attribute value or raise some exception
        self.__getattribute__(self, name)
        return 10

    def __setattr__(self, name, value):
        # Called when an attribute assignment is attempted
        print('Inside __setattr')
        self.__setattr__(self, name, value)
        # Note this is note the correct syntax but you can check the error messages to check

    def __init__(self, val):
        self.val = val

    def __delattr__(self, name):
        # Same as __setattr__
        pass

    def __dir__(self):
        # Used when dir(object) is called. It must return a sequence
        pass
    # I did not discuss their syntax in much detail as you would rarely implement themselves
    # But you can use them to check whether your class has certain attributes or not and things like that


# A = Sample(10)
# print(A.some_attribute)    # Looking for an attribute that I have not defined

#---------------------------------------------------------------------------------------------------

# Descriptors
# They are used to access the __dict__ of the owner class as internally classses are implemented as dictionaries
class Descriptors:
    def __get__(self, instance, owner):
        pass
    def __set__(self, instance, value):
        pass
    def __delete__(self, instance):
        pass
    def __set_name__(self, owner, name):
        # Called when class is created to set name of owner class
        pass
    def __objclass__(self):
        # Used by inspect module
        pass
    # when you hand code all the function you can directly use the methods as object.__get__(x)
    # But they are not commonly hand coded

#---------------------------------------------------------------------------------------------------

# By defualt class objects are stored as dictionary. When you create a large number of instnaces
# than you can face memory issues. To solve this you can use __slots__ which just reserves enough
# space for the variables
class class_using_slots:
    def __slots__(self):
        self.var1 = None
        self.var2 = None
        self.var3 = None

    def __init__(self, x, y, z):
        self.var1 = x
        self.var2 = y
        self.var3 = z
        # Now if i try to create a new variable
#        try:
#            self.new_var = 10
#        except:
#            print('You could not create the new variable')

eg = class_using_slots(10,20,30)


