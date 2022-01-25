#Exercise 1
# Reverse the list below in-place using an in-place algorithm.
# For extra credit: Reverse the strings at the same time.

# def swapwords(words,w,x,y,z):
#     words[w],words[x],words[y],words[z]=words[z][::-1],words[y][::-1],words[x][::-1],words[w][::-1]
#     return(words)

# words = ['this' , 'is', 'a', 'sentence', '.']
# print(f"o.g. list:{words}")

# swapwords(words,0,1,2,3)
# print(f"upgraded edition:{words}")

#Exercise 2
# Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
# Should output:
# {'a': 5,
# 'abstract': 1,
# 'an': 3,
# 'array': 2, ... etc...

#I'm not sure how to make it count the word a vs the letter a

# a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

# def splitty(stringy):
#     #split words from string, count occurances & put into dictionary 
#     dicto = {}
#     for word in a_text.split(' '):
#         dicto[word.lower()] = stringy.count(word)

#     return(dicto)

    #use dictionary to make NEW dictionary, sorted by the key 'occurances'
    # sorted_values = sorted(dicto.values(),reverse=True)
    # sorted_dicto = {}
    # print(dicto.keys())
    # for x in sorted_values:
    #     for y in dicto.keys():
    #         if dicto[y] == x:
    #             sorted_dicto[y] == dicto[y]

#     return(sorted_dicto)

# print(splitty(a_text))

#exercise 3
#Write a program to implement a Linear Search Algorithm. 
# Also in a comment, write the Time Complexity of the following algorithm.

# #Time Complexity: O(n)
# def linearSearch(listy,value):
#     for val in listy:
#         if val==value:
#             return(f"your number {value} IS in the list.")

# #test
# listy = list(range(101))
# print(linearSearch(listy,8))

# nums = [1,3,5,7]
# x = [x*2-1 for x in nums[-2:]]
# print(x)

# def fib(n):
#     if n ==1:
#         return n
#     else:
#         return fib(n-1) - fib (n-2)

# print(fib(3))

# class Toy():
#     kind = 'Car'

#     def __init__(self,rooftop,horn,wheels):
#         self.rooftop = rooftop
#         self.horn = horn
#         self.wheels = wheels

# hotwheels_car = Toy(1,1,3)

# print(hotwheels_car.rooftop)

# hotwheels_car.rooftop = 0

# print(hotwheels_car.rooftop)

class Parent(object):
    def __init__(self):
        self.value = 4

class Child(Parent):
    def get_value(self):
        return self.value + 1

c = Child()
print(c.get_value())
