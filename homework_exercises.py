#Exercise 1 -- reverse the list & words

words = ['this' , 'is', 'a', 'sentence', '.']

def swapwords(words,w,x,y,z):
    words[w],words[x],words[y],words[z]=words[z][::-1],words[y][::-1],words[x][::-1],words[w][::-1]
    return(words)

words = ['this' , 'is', 'a', 'sentence', '.']
print(f"o.g. list:{words}")

swapwords(words,0,1,2,3)
print(f"upgraded edition:{words}")

#Exercise 2 - count how many distinct words are in the string below, 
# then output a dictionary with the words as the key 
# and the value as the amount of times that word appears in the string.

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def splitty(stringy):
    #split words from string, count occurances & put into dictionary 
    seto=set()
    dicto = {}
    for word in a_text.split(' '):
        seto.add(word)
    for word in seto:
        dicto[word.lower()] = a_text.count(word.lower())
    return(dicto)

print(splitty(a_text))

#I also tried (and failed) to order the dictionary. But I guess i shouldn't
#be trying to order unordered things 


#Exercise 3

#Time Complexity: O(n) - the time grows exactly as the length of the object grows

def linearSearch(listy,value):
    for val in listy:
        if val==value:
            return(f"your number {value} IS in the list.")

#test
listy = list(range(101))
print(linearSearch(listy,8))