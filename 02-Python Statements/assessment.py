#!/usr/bin/env python3
print("#Q1")
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)

print("\n#Q2")
for n in range(0,10):
    if n%2 == 0:
        print(n)

print("\n#Q3")
numberDividedBy3 = []
for n in range(1, 50):
    if n%3 == 0:
        numberDividedBy3.append(n)
print(numberDividedBy3)

print("\n#Q4: Go through the string below and if the length of a word is even print 'even!'")
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2 == 0:
        print(f'{word}    has an    {len(word)}    numbers of letter')

print("\nQ5: ")
""" 
Write a program that prints the integers from 1 to 100. 
But for multiples of three print "Fizz" instead of the number, 
and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz". """
for n in range(1,100):
    if n%3 == 0 and n%5 == 0:
        print("FizzBuzz")
    elif n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else:
        print(n)


print("\nQ6: Use List Comprehension to create a list of the first letters of every word in the string below:")
st = 'Create a list of the first letters of every word in this string'
firstLetter = []
for word in st.split():
    firstLetter.append(word[0])
print(firstLetter)