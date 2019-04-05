# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:19:13 2019

@author: Joey Roe
CS 2302
Professor: Fuentes
TA: Anindita Nath, Maliheh Zargaran
Assignment: Lab 5
Date: 04/04/2019
Purpose: To store data using binary search trees and hash tables and compare the 
running times

"""
import numpy as np
import math
import time


class bst(object):
    def __init__(self, item, right = None, left = None):
        self.item = item
        self. right = right         #Constructor for binary search tree
        self.left = left
        
        
        
class HashTable(object):
    def __init__(self,size):  
        self.item = []
        self.numOfItems = 0
        for i in range(size):         #Constructor for hash table
            self.item.append([])



def turnWordToNumber(theWord):
    charNums = []
    for i in range(len(theWord)):           #turns the word to ascii number
        charNums.append(ord(theWord[i]))
    return sum(charNums)


        
def treeInsert(tree, newItem):
    if tree == None:
        tree = bst(newItem)
    elif newItem[0] > tree.item[0]:
        tree.right = treeInsert(tree.right, newItem)
    else:
        tree.left = treeInsert(tree.left, newItem)
    return tree

    
def searchBST(T, k):
    if T is None or T.item[0] == k:
        return T
    if T.item[0] < k:
        return searchBST(T.right, k)
    if T.item[0] > k:
        return searchBST(T.left, k)

        

#def FindAndPrintBST(T,k):
#    f = searchBST(T,k)
#    if f is not None:
#        print(f.item[0],'found')
#    else:
#        print(k,'not found')


def findHeightTree(tree):            #finds the height of the tree
    if tree == None:
        return -1
    else:
        a = 1 + findHeightTree(tree.left) #height of left
        b = 1 + findHeightTree(tree.right)  #height of right
    if a >= b:
        return a
    if b >= a:               #returns which ever side is greater, a or b
        return b
    
    
def numOfNodes(T):
    if T is None:
        return 0
    return 1 + numOfNodes(T.left) + numOfNodes(T.right)
        


        
def searchHash(H, theKey):
    bucket = (turnWordToNumber(theKey))% len(H.item) #determines which bucket to search
    temp = H.item[bucket]
    for i in range(len(temp)):
        temp2 = temp[i]        #for the chained list
        for j in range(len(temp2)):
            if temp2[0] == theKey:   #if item found it gets returned
                return temp[i]
    else:
        return None             #if it isn't found none is returned
        


       

def doubleSizeHash(H):
    H2 = HashTable(len(H.item) * 2 + 1)
    for i in range(len(H.item)):       #doubles the size of the hash table + 1
        for j in H.item[i]:
            hashTableInsert(H2, j)
    return H2




    
def hashTableInsert(H,k):
    numForWord = turnWordToNumber(k[0])#because k is a list the first element in the list is the word
    b = numForWord%len(H.item)          #uses ascii value to insert in hash table
    H.item[b].append(k)
    H.numOfItems += 1
    
    



#def InOrderD(T, space):
#    if T is not None:
#        InOrderD(T.right, space+'  ')
#        print(space, T.item[0])                   #draws the tree
#        InOrderD(T.left, space+'  ')





def NumOfFileLines(fileName):
    count = 0
    with open(fileName, 'rb') as f:             #method for getting number of lines in the file
        for line in f:
            count += 1
    return count



def theBigListMaker(numOfLines, fileName):           #makes a list based off the file
    newFile = open(fileName, encoding = "Latin-1")
    newList = [None] * numOfLines
    for i in range(numOfLines):
        newList[i] = newFile.readline()
    return newList


    
#This method makes a list inside of a list it makes the first element in the list 
# the word, then the second is the 50 numbers 
def listInListMaker(theList):
    newList = []
    for i in range(len(theList)):
        innerList = theList[i].split(" ", 1)  #seperates the word and numbers
        innerListNums = innerList[1].split(" ", 50) #splits up the 50 numbers,but they're still strings     
        for j in range(len(innerListNums)):
            innerListNums[j] = float(innerListNums[j]) #turns the numbers into real numbers
        innerListNums = np.array(innerListNums)
        newList.append([innerList[0], innerListNums]) #append the word and the list of 50 numbers to the newList
    return newList
    



    

def similarBST(word1, word2, tree):   #compares the words to see if they're similar
    if searchBST(tree, word1) == None or searchBST(tree, word2) == None: #checks if they're in the tree
        return None
    w1 = searchBST(tree, word1)     #assigns the actual value for word 1 and 2
    w2 = searchBST(tree, word2)
    temp = w1.item[1]
    temp2 = w2.item[1]           #the 50 nums of both words
    numerator = 0
    for i in range(len(temp)):                        
        numerator = numerator + (temp[i] * temp2[i])  #dot product
    w1Val = 0 #value for word 1
    for i in range(len(temp)):
        w1Val = w1Val + (temp[i]**2) #add all 50 nums squared in word 1
    w1Val = math.sqrt(w1Val) #get the square root
    w2Val = 0 #value for word 2
    for i in range(len(temp2)):
        w2Val = w2Val + (temp2[i]**2)    #add all 50 nums squared in word 2
    w2Val = math.sqrt(w2Val) #get square root
    denominator = w1Val * w2Val #multiply them
    return (numerator / denominator) + 0.0000000000000002



def similarHash(word1, word2, H):   #compares the words to see if they're similar
    if searchHash(H, word1) == None or searchHash(H, word2) == None:   #checks if the words are in the hash
        return None
    w1 = searchHash(H, word1)      #the actual value of word 1 and 2
    w2 = searchHash(H, word2)
    temp = w1[1]               #only the 50 numbers for word 1 and 2
    temp2 = w2[1]
    numerator = 0
    for i in range(len(temp)):                        
        numerator = numerator + (temp[i] * temp2[i]) #dot product
    w1Val = 0 #value for word 1
    for i in range(len(temp)):
        w1Val = w1Val + (temp[i]**2) #add the 50 nums squarerd in the first word
    w1Val = math.sqrt(w1Val)   #get the square root of the sum
    w2Val = 0   #vaule for word 2
    for i in range(len(temp2)):
        w2Val = w2Val + (temp2[i]**2)      #add 50 nums in word 2 squared
    w2Val = math.sqrt(w2Val)   #square root of the sum
    denominator = w1Val * w2Val    #multiply them
    return (numerator / denominator) + 0.0000000000000002      #returns the similarity
        




        



#Main        

theFile = open('data.txt', encoding = "Latin-1")  #the first very large file
theFile2 = open('data3.txt', encoding = "Latin-1")  #second file a lot smaler
b = NumOfFileLines('data.txt')
s = NumOfFileLines('data3.txt')


bigList = theBigListMaker(b, 'data.txt')
anotherList = listInListMaker(bigList)


smallList = [line.rstrip('\n') for line in open('data3.txt')]
for i in range(len(smallList)):
    smallList[i] = smallList[i].split(" ", 1)
    
    
looper = True
while looper == True:
    print('Choose table implementation')
    print('Type 1 for binary search tree or 2 for hash table with chaining')
    userInput = input()
    if userInput == '1' or userInput == '2':
        looper = False
      
if userInput == '1':                #for the binary search Tree
    print()
    print('Building binary search tree')
    startBST = time.time()
    tree = None
    for i in range(len(anotherList)):
        tree = treeInsert(tree, anotherList[i])
    endBST = time.time()
    totalTimeBST = (endBST - startBST) * 1000
    print('Binary Search Tree stats:')
    print()
    print('Number of Nodes: ', numOfNodes(tree))
    print('Height: ', findHeightTree(tree))
    print('Running time for binary search tree construction: ', totalTimeBST,'milliseconds')
    print()
    print('Reading word file to determine similarities')
    print()
    startBST2 = time.time()
    for i in range(len(smallList)):
        print('Similarity ', smallList[i], '= ', similarBST(smallList[i][0], smallList[i][1], tree))
    endBST2 = time.time()
    totalSim = (endBST2 - startBST2) * 1000
    print()
    print('Running time for binary search tree query processing: ', totalSim, 'milliseconds')

    
if userInput == '2':                   #for the hash table
    print()
    print('Building hash table with chaining')
    startHash = time.time()
    H = HashTable(7)
    initialHsize = len(H.item)
    for i in range(len(anotherList)):
        if (H.numOfItems // len(H.item)) == 1:
            H = doubleSizeHash(H)
        hashTableInsert(H, anotherList[i])
    endHash = time.time()
    totalTime = (endHash - startHash) * 1000
    hashSize = len(H.item)
    print('Hash table stats: ')
    print()
    print('Initial  hash table size: ', initialHsize)
    print('Final table size: ', hashSize)
    print('Load factor: ', (H.numOfItems / len(H.item)))
    print('Percentage of empty lists: ', (100 - (H.numOfItems / len(H.item)) * 100))
    print('Standard deviation of the lengths of the lists: ')
    print('Running time for hash table construction: ', totalTime, 'milliseconds')
    print('Reading word file to determine similarities')
    print()
    
    for i in range(len(smallList)):
        print('Similarity ', smallList[i], '= ', similarHash(smallList[i][0], smallList[i][1], H))

    
