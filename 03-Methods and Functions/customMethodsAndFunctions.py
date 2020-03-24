# Defining a __function called myFunction()
def my_function(name):
    """
    DOCSTRING: Here is how we can define a function
    """
    print(name + " here is the definition of a function in python")

# Call a __function called myFunction()
my_function(name="Kisquish")

# find out if the word "dog" is in the string
def dog_string(st):
    return "dog" in st.lower()
    """if "dog" in st.lower():
        return True
    else:
        return False
        """
print("\n")
#st = input("Enter a string: ")
#result = dog_string(st)
#print(result)

#print(dog_string(st))
print(dog_string(input("Enter a string: ")))

print("\n")
#PIG LATIN

