# what are data structures? 
# 	data structures are different ways of organizing data on your computer, that can 
# 	be used effectively 
# 	first in first out 

# what is algo?
# set of steps to acomplish a task 

# algo in my dail life 
# get up 
# clean the yard 
# bath 
# study 
# break 
# eat 
# study 
# walk 
# eat 
# study 
# sleep


# algo in CS 
# set of rules for a computer to accomplish a task 
# input data 
# calculation 
# stop when answer found


# how do google and fb transmit live video across the internet? 
# 	compression algo


# how to find shortest path on the map? 
# 	dijstra's algo 

# what makes a good algo?
# 	correctness 
# 	efficiency
# 	what are data structures and algo important?
# 		input(data)

# 		processing 

# 		output(information )

# 		computer science 
# 		algo 

# 	problem solving skills 
# 	fundamentals concenpts of programming in limited time 


# 	types of data structures 

# 		data structures 

# 		primitive 			
# 		integer				
# 		float				
# 		character			
# 		string
# 		boolean



# 		non primitive

# 		linear -------- 
# 		|					
# 		Static(array)

# 		Dynamic
# 		linked last, 
# 		stack, 
# 		queue		

# 		non Linear
# 		tree
# 		graph

# types of algo 
# 	-simple recursive algo 
# 	-divide and conquer algo
# 	-dyna,ic programmingn algo 
# 	-brute force algo 
# 	-randomized algo 


# simple recursive algo 
	algo Sum(A,n)
		if n=1
			returnA[0]
		s = Sum(a, n-1) /*recurse on all but last*/
		s = s + A[n-1] /* add last element */
	return s 

# divide and conquer 
# 	-divide the problem into smaller subproblems of the same type, and solve these subproblems recursively 
# 	-combine the solutions to the subprobelms into a solution to the original problem

# 	e.g quick sort and merge sort 

# dynamic programming algo 
# 	-they work based on memorizaion 
# 	-to find the best solution

# greedy algo 
# 	-we take the best we can without worrying about future consequences 
# 	-we hope that by choosing a local optimum solution at each step, we will end up at a global optimum solution 

# brute force algo 
# 	-it simply tries all possibilies until a satisfactory solution is found 

# randomized algo 
# 	-use a random number at least once during the computation to make a decison

# RECURSION 
# 	what is Recursion?
# 	Recursion = a way of solving a problem by having a function calling itself  


# 	- performing the same operation multiple times with different inputs 
# 	- inn every step we try smaller inputs to make the problem smaller
# 	- base condition is needed to stop the recursion, othwise infinit loop will occur

	def openRussionDOll(doll):
	if doll == 1:
		print('all dolls are opened')
	else:
	openRussionDoll(doll-1)


# why recursion ?
# 	1. recusive thinking is really important in programming and it helps you break down big problems into smaller ones and easier to use 
# 	-when to choose recursion?
# 	>if you can divide the problem into similar sub problems
# 	>design an algo to compute nth...
# 	>write code to list the n..
# 	>implement a method to compute all.
# 	>practice 

# 	2. the prominent usage of recusion in data structures like tree and graphs 
# 	3. interviews 
# 	4. is is used in many algo(divide and conquer, greedy and dynamic prgramming )

# how recursion works?
# 	1. a nethod calls it self 
# 	2. exit from infinite loop


	# e.g 
		def recursionMethod(parameters):
		if exit from condition satisied:
			return some value
		else:
			recursionMethod(modiefied parametrs)


	def firstMethod():
	secondMethod()
	print('i am the first method ')


	def secondMethod():
	thirdMethod()
	print('i am the second method ')


	def thirdMethod():
	forthMethod()
	print('i am the third method ')


	def forthMethod():
	print('i am the forth method ')

# last in, first out

	def recrsiveMethod(n):
	if n<1:
		print('n is less than 1')
	else:
	recursiveMethod(n-1)
	print(n)

	# recursiveMethod(4)
	# |
	# -recursiceMethod(3)
	# 	|
	# 	-recursiveMethod(2)
	# 		|
	# 		-recursiveMethod(1)
	# 			|
	# 			-recursiveMethod(0) 	n is less than 1

# recursive vs iterative solutions 
def powerOfTwo(n):
	if n ==0:
		return 1
	else:
		power = powerOfTwo(n-1)
		return power * 2



def powerOfTwo(n):
	i = 0
	power = 1
	while i < n:
		power = power * 2 
		i = i + 1
	return power

# 5.

# when to use/avoid recursion? 
	
	# when to use it?
	# -when we cal easily breakdown a problem into similar subproblem
	# -when we are fine with extra overhead(both time and space) that comes with it 
	# -when we need working solution instead of effiecient one
	# -when traverse a tree(a tree is collection objection that is linked  to one another)
		# -preoder tree traversal :15,9,3,1,4,12,23,17,82
	# -whenwe use memoization in recursion

	# when avoid it?
	# -if time and complexity matter for us 
	# -recursion uses memory. if we use embedded memory. for example an application that takes more memory in the phonne is not different 
	# -recursion can be slow

# how to write recursio in 3 steps?

# factorial 
# Use the permutations at least as early as the 12th century by Indian scholars.
# It's a product of all positive integers, less than or equal to M Factorial denoted by an exclamation mark.
# This notation was introduced by French mathematician Clifton Grant in 1888

	# -it is the product of all positive integers less than or equal to n
	# -denoted by n!(Christain kramp in 1808)
	# -only postive numbers 
	# - 0!=1

	e.g 1
	4! = 4*3*2*1 = 24

	e.g 2 
	10 = 10*9*8*7*6*5*4*3*2*1=36,28,800

	n! = n*(n-1)*(n-2)*...*2*1

	# step 1: recursive case - The flow 
	n! = n * (n-1) * (n-2) * 2 * 1 			--> n! = n * (n-1)!
					(n-1)
	(n-1)! = (n-1)* (n-1-1)* (n-1-2)*...*2*1=(n-1)*(n-2)*...*2*1


	# step 2: base case - the stopping criterion 
	-0!=1
	-1!=1

	# step 3: unintential case - the constraint
	-factorial(-1)??
	-factorial(1.5)??

	def factorial(n):
    assert n >= 0 and int(n) == n, 'the number must be positive only!'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

       # factorial(4) = 24

       # 				factorial(4)
       # 				|			6
       # 				|_ 4* factorial(3)
       # 							|			2
       # 							|- 3 * factorial(2)
       # 										|
       # 										|-2*factorial(1)
       													# 1

# fibonacci  numbers - Recursion
# Fibonnaci sequence is a sequence of numbers in which number is the sum of two preceding ones and the sequence starts from 0 and 1

	0,1,1,2,3,5,8,13,21,34,55,89... 

	# step 1: Recursive case - thhe flow 

	5=3+2 		f(n) = f(n-1) + f(n-2)

	# step 2: base case - the stopping criterion
	-0 and 1

	# step 3: unintentional case - the constraint 
	-fib(-1) ??
	-fib(1.5) ??

	0,1,1,2,3,5,8,13,21,34,55,89... 

	fib(4)=3
		|	2		1
		|-fib(3)+fib(2)	1	0
			|		|-fib(1)+fib(0)
			|	1 		1
			|-fib(2) + fib(1)
				|	1		0
				|-fib(1)+fib(0)

# interview question -1

# how to find the sum of digits of a postive integer number using recursion ?

# step 1: Recursive case - thhe flow 
10 10/10 = 1 and remainder = 10d(n) n%10 +f(f/10)
54 54/10 = and remainder= 4
112 112/10 = 11 and remainder = 2 
				11/10 and remainder 1
# step 2: base case - the stopping criterion
-0
-1
# step 3: unintentional case - the constraint 
-1
1.5
def findnumer()

interview question 2
how to calculate power of a number using recursion?

step 1: Recursive case - thhe flow 
xn=x*x*x..(n times)..*x 		xn = x * xn -1

24=2*2*2*2

xa*xb*xa+2

x3 x4 = x3+4 

# step 2: base case - the stopping criterion
-n = 0
- n = 1


# step 3: unintentional case - the constraint 
-n =1
-n =1.5 

-power(-1,2) ??
-power(3.2,1)
-power(2,1.5) ??
-power(2,-1) ??


# interview question -3

how to find gcd(greater common divisor ) of two numbers using recursion?

# step 1: recursive case - the flow 

# gcd is the largest postive integer that divides the numbers without a remainder 

# gcd(2,12)=4

8 = 2 * 2 * 2 			gcd(a, 0)=0
						gcd(a,b) = gcd(b,a mod b)


12 = 2 * 2 * 3

Eucidean algorithm
gcd(48,18)
step 1: 48/18 = 2 remainder 12
step 2: 18/12 = 1 remainder 6
step 3: 12/6 = 2 remainder 0



# step 2: base case - the stopping criterion
-b= less than a
-a greater than b 



# step 3: unintentional case - the constraint 
# b = 1.5
# a = -1
positive int 
convert negative numbers to positive


interview question -4

step 1: recursive case - the flow 

step1 : divide the number by 2 
step2 : get the integer qoutient for the next iteration
step3 : get the remainder for the binary digit
step3 : repeat the steps until the qoutient s equal to 0

# 13 to binary 			f(n) = n mod 2 + 10 * f(n/2)
division by | qoutient | remainder 


# step 2: base case - the stopping criterion
-0


# step 3: unintentional case - the constraint 

# -------------------------------------- BIG O
# big O 

# BIG o NOTATATION 

# Big O is the lang and metric we use to describe the efficiency of algorithms


# O(N),O(N2),O(2N)

# time complexity : O(wh)

# BIG O 
# algo run time notations 

# best case 
# average case 
# worst case 

# quick sort algo 
# o(n log n)

# Big O, Big Theta and Big Omega 

# big O: it is a complexity that is going to be less or equal to the worst case 
# big -(big-Omega): it is a complexity that is going to be atleast more than the best case
# big Theta (big- dot o): it is a complexity that is within bounds of the worst and the best cases

# Big O - O(n)
# big omega- omega(1)
# Big O-DOT O(N/2)

# complexity | name |sample


# O(1)- constant #index in an array
array = [1, 2, 3, 4, 5]
array[0]

# O(N) - Linear time since it is visiting every element of array

array = [1, 2, 3, 4, 5]
for element in array:
	print(element)

# O(logN) logarithmic time 

array = [1, 2, 3, 4, 5]
for index in range(0, len(array), 3):
	print(array[index])
# //logarithmic time since it is visiting only some elements

# O(LogN) - Logarithmic time 

# binary search

# O(N2) - Quadric time

array = [1, 2, 3, 4, 5]
for x in array: 
	for y in array:
		print(x,y)

O(2n) - Exponential time 
def fib(n):
	if 1 <= 1:
		return n 
	return fibonnaci(n-1) + fib(n-2)
4.

# drop constants and non dominant terms
# drop constant 

# O(2n) --> O(N)

# drop non dominant terms

# O(N2+N) --> O(N2)

# O(N+logN) -->O(N)

# O(2*2+1000N100) --> O(2n)

# why do we drop constants and non dominant terms?

# it is very possible that O(N) code is faster than O(1) code for specific inputs 
# different computers arch have different constant factors 

# fast computer fast memory access lower constant 
# slow computer slow memory access higher constant 
# diff algo with the same basic idea and computional complexity might have slightly different constants 

# example: a*(b-c) VS 	a*b a*c 

# -as n -> oo, constant are not really a big idea 


add vs multiply 

for a in arrayA:
	print(a)

for b in ArrayB:
	print(b)
# add the runtimes : O(A+B)
# -if your algo is in the form "do this, then when you are all done, do that" then you add the run times

for a in arrayA:
	for b in arrayB:
		print(a,b)

# multiply the run times:O(A*B)

# -if your algo is in the form " do this for each time you do that" then you multiply the run times

# how to measure the codes using the big O?
# view pdf 7 from big notation

def findBigNum(sampleArray):
	bigNUm = sampleArray[0] #---------> O(1)
	for index in range(1, len(sampleArray)): #---------> O(n)
		if sampleArray[index] > bigNUm: #---------> O(1)
			bigNUm = sampleArray[index] #---------> O(1)
	print(bigNUm) #---------> O(1)

	# time complexity: O(1) + O(n) + O(1) = O(n)

	# how to measure Recursive algo?

	array = [7,5,6,2,4,6,36,455,456,5,4,8,4,8,45,6,584,8,561,5]
	def findBigNumRec(sampleArray, n ): # #---------> M(n)
		if n == 1: ##---------> O(1)
			return sampleArray[0] #---------> O(1)
		return max(sampleArray[n-1], findnumerRec(sampleArray, n-1)) #---------> M(n-1)

		# M(n)=O(1)+M(n-1)
		# M(1)=O(1)

	# M(n-1)=O(1)+M((n-1)-1)
	M(n-2)=O(1)+M((n-2)-1)

		# explamation
		A = [11,4,12,7] n=4

		findnumerRec(a,4)

	def f(n):
		if n <= 1:
			return 1 
		return f(n-1) + f(n-1)


	def foo(array):
		sum = 0 
		product = 1

		for i in array:
			sum += i 

# interview question 
# what is the runtime of the below code?

		for i in array:
			product *= i 
		print("sum = "+str(sum)+", product = "+str(product))


# Arrays 
	# -it is a box of macrons 
	# -all macrons in this box are next to each other 
	# -each macaroon can be idenitified uniquely based on their location 
	# -the size of box cannot be changed 
	4|3|1|6|8|10

	# -array can store data of specified type 
	# elements of an array are located in a contigous 
	# -each element of an array has a unique index
	# -the size of an array is predefined and cannot be modiefied

	what is an arraY?
	# in CS, an array is a data structure consisting of a collection of elements, each identified by at least one array index or key. an array is tored such that the position element can be computed from its index by a mathemathical formula 

	why do we need an array?
	3 variables 
	number 1 
	number 2 
	number 3
	what if 500 integer?
	are we going to use 500 variables?
	the answer is an array 


	types of array

	# arrays 
	# one dimensional array: an array with a bunch of values having been declared with a single index
	# a[i] -> between 0 and n. a[3] or a[0]



	# multi dimensional 
	# two dimensional array: an array with a bunch of values having been declared with double index 
	# a[i][j] -> i and j between 0 and n. a[0][4] a[2][5]

	# three
	# three dimensional array: an array with a bunch of values having been declared with triple index 
	# a[i][j][k] -> i,j and k between 0 and n. A[0][0][1]. A[2][0][2]


	# four  dimensional 
	N dimensional

# Array in memory 
	one dimensional
	two dimensional array  
	three dimensional array


# creatign an array 
	# when we create an array, we:
	# -assign it to a variable 
	# define the type of elements that it will store 
	# define its size(maximum numbers of elements)

	myArr=[]

creating an array (array module)

from array impor t* 
arrayName = array(typecode, [intitializers])

# insertion

myArray = 'a','b','c'
myArray[3] = 'f'
myArray[5] = 'd'


# insertion, when an array is full. 

# array traversal 

myArray '','','','','',''

myArray[0]='a'
myArray[1]='b'
myArray[2]='c'
myArray[3]='d'
myArray[4]='e'
myArray[5]='f'

def traversal(array):
	for in in array: # -------->O(1)
		print(i) #-------->O(1)

# access array in element 
# how can we tell the computer which particular value we would like to access?

<arrayName>[index]

myArray[0]='a'


def accEle(array, index):
    if index > len(array): # -------->O(1)
        print('there is not any element in this index') # -------->O(1)
    else:  
        print(array[index]) # -------->O(1)
# time complexity O(1) space complexity O(1)


# Finding an element 

myArray='','','','','',

myArray[2]
# binary search

def searchInArray(array, value): 
	for i in array: # -------->O(n)
		if i == value: # -------->O(1)
			return array.index(value) # -------->O(1)
	return 'the element does not exist in this array' # -------->O(1)

# time complexity o(n)
# space complexity: o(1)


# deletion 

4|3|1|6|8|10
4||1|6|8|10
4|6|8|10||
# 
# time complexity: O(n)


# time complexity 

operation | time complexity | space complexity


# one dimensional array 
# an array with a bunch of values having been declared with double index 
# a[i][j] -> i and j between 0 and n 

# metrics, temperatues, 

# when we create an array, we:
# assign it a variable 
# define the type of elements that it will store
# define its size(maximum numbers of elements)

# insertion - two dimensional array


# adding column 
# 3
# 6
# 9
# time complexity = O(mn)


# adding Row 

# time complexity=o(mn)

# accces an elment of two dimensional array

	# in 2d we have two indexes, the rows , the second is column 
	#a[i][j] i is the row index and j is column index

# traversing 2d array 


# searchig two D array

# linear search 

# deletion - 2D array 

# time plexity = o(mn)

# deleting row 

# time complexity = O(mn)

# time and space complexity 
# operation | time complexity | space complexity

# creating an empty array 
# inserting a column/row in a array 
# traversing a given array
# accesing a given cell
# searching a given value 
# deleting a given value 

# when to us/avoid arrays ?
	# when to use
	# -to store mulitple variables of same data type 
	# -random access

	# when to avoid 
	# -same data type elements
	# -reserve memory 


# pythons lists 
	# a list is a data structure that holds an ordered collection of items
		# [,j,j,j,j,j] ellemtns of items 
		# [10,20,32,14,] int 
		# ['ed', 'eddy', 'eddie'] string
		# [0.5,1,2,3,4,5,'boom'] string, int, float 
		# ['jump', 2.0, 4,[12,60]] string, int, float, nested lists

# lists vs aarays
	# similarities 
	# both data structures are mutable 
	# both can be indexed and iterated throuiugh 
	# they can be sliced 

	# arrays
	# arithemtic operation

	# lists 
	# data types
	# can be diff

	# arrays
	# same data type 


# time and space complexity in python lists 


# finding number of above average temps

# input('how many's temperatue)

# input('day 1s high temp:')

# input('day 2 high temp ')

# output=avergae-
# 1 day(s) above average

# dictionares
# a dictionary is a collection which is unordered, changeable and indexed
# miller: a person who owns or works in a corn mill
# key value pairs
mydict{'mmiller':'aperson who owns or works in a corn mill',
		'programmer': 'a person who writes computer programs'}


# dictionary in memory
	# a hash table is a way of doing key-value lookups. you store the values in an array, and then use a hash function to find the index of the array cell that correspnds to your key-value pair

	# # dictionary vs list
	# unordered - ordered 
	# access via key - access via index
	# collection of key value pairs - collection of elements 
	# preferred when you have unique key values- preferred when you have ordered data
	# no duplicate memebers - allow duplicate memebers

	# t&s complexity in python dict
	# creating a dict 
	# inserting a value 
	# traversing a given dict
	# accessing a given cell 
	# searching a  given value 
	# deleting a given value

# tuples
# a tuple is an immutable sequence pf python objects 
# tuples are comparable and hasable

t='t','j','f','f','f','dfv','ffs','fd'
j=('f','t','j','f','f','f','dfv','ffs','fd')


# linked list
# linked list is a form of sequential collection and it does not have to be in oder. a linked list is made up of indepenedent nodes that may contain any type of data and each node has a reference to the next node in the link

# linked list vs arrays 

# elements of linked list are independent objects 
# variable size - the size of a linked list is not predefined 
# insertion and removals in list are very effiecent
# random access - accessing an element is very efficient in arrays 

# types of linked lists 
	# singly linked list 
	# circular singly linked list
	# doubly linked list 
	# circular doubly linked list

# creation of singly linked list 
	# create head and tail init with null
	# create a blank node and assign a value to it and reference to null
	# link head and tail with these node

# insertion 
	# at the beginning of the linked list 
	# after a node in the middle of linked list
	# at the end of the linked list

# linked list search 


# singly linked list deletion 
	deleting the first node 
	deleting any give node
	deleting the last node 

# creation of circular linked list 
	

# circular singly linked list - insertion 
	# insert at the beginning of linked list 
	# insert at the specified location of linked list 
	# insert at the end of linked list
# circular singly linked list -deletion 
	# -deleting the first node 
	# -deleting any given node 
	# -deleting the last node

# time and space complexity of circular singly linked list 
	# creation 
	# insertion
	# searching 
	# traversing 
	# deletion of a node 
	# deletion of linked list 

# double linked  list
	

# double linked list- INsert
	# -inser at the beginning of linked list 
	# -insert at the specified location of linked list 
	# -insert at the end of linked list 

# insertion algo - doubly linked list 
	

# deleting linked list -deletion
	# deleting the first node
	# delete any given node
	# deleeting the last node


# delete entire singly linked list 

# creation of circular singly linked list
	
#what is a stack
	# stack is data that store items in a last-in/first-out manner
	LIFO method 
	# website back button

# stack op
	cretae stack
	customstack()
	push()
	pop()
	peek()
	isEmpty() 
	isFull() 
	deleteStack() 

# stack creation
	# stack using list 
	# easy to implement 
	# speed problem when iot grows 

	# stack using linked list 
	# fast performance 


# create an object of linked list class

# when to avoid/use stacks
	# use lifo functionality 
	# thec hance of data corruption 

avoid 
# randoma ccess is not possibile 

# what a queue?
	# queue is a data structure that stores items in a first-in/first-out manner
	# a nre addition to this queue happens at the end of the queue 
	# first person in the queue willbe served first 
	# fifo method- first in first out 

what we need queue data structurr?
	# utilize first coming data first, while others wait for ther turn 
	# fifo method -first in first out
	# point of sale, print queue,call center phone systems 

# queue oerations
	# craete queue
	# enqueue
	# dequeue 
	# isempty
	# isfull
	# deleteQueue

# implemntation 
	# python list
	# -queue without capapcity 
	# -queue with capacity (circular queue)
	# linked list

# create queue using python list no capacity
	# customQueue=[]
	enqueue() method


# queue with fixed capacity(circular queue)
	
# create a queue
	# create an object of linked list class 
	enqueue() method 

# methods 
	deque()
	append()
	popleft()
	clear()

# python queue
	# fifo queue --> queue(maxSize=0)
	# lifo queue
	# priority queue
# methods 
	qsize()
	empty()
	full()
	put()
	get()
	task()
	task_done()
	join()

what is a tree?
	a tree is a nonlinear data structure with hierchial relationshipbetween its elements without any cycle,its basically reversed froma real life tree
	drinks 
	^
	hot cold 
		^
	(tea coffee) (non alcholic alcholic)
properties:
	# represent hierchial data
	# each nodehas two compoments: data and a link toits sub category 
	# base category andsub categories under it 

# why tree ?
	# quicker and easier access to the data  
	# store hierchial data, like folder structure,organization,xml/html data 
	# there are different typesof data stryctyreas which perform better in various situations 
	# binary search tree, avl, red black tree, trie 


# in order traversal of binary tree
	# left sub tree  
	# root node
	# right sub tree 

# tree terminology
	# root: top node without parent 
	# edge:a link between parent and child 
	# leaf: a node which does not have children 
	# sibling: a child of same parent
	# ancestor: parent, grandparent, great grandparent of a node 
	# depth of node: a length of the path from root to node
	# height of node: a length of the path from the node to the deepest node
	# deptg of tree: depth of root node
	# height of tree: height of root node 

# binary tree
	# binary tree the data structure in which each node has at most two children, often reffered to as the left and right children
	# binary tree is a fsamily of data structure(bst, heap tree, avl, red black tree, synatx tree)
	huffman coding problem,heap prioiry problem and expression parsing problems can be solved efficiently usiing binary trees  

types of binary tree 
	full binary tree 
	perfect binary tree 
	complete binary tree
	balanced binary tree 

# binary 
	linked lsts 
	python list (array)
	left=cell[2x]
	right chld=cell[2x*+1]

# create binry tree using linked list
	# creation of tree 
	# insertion of a node 
	# deletion of node 
	# search for a value 
	# traverse all nodes
	# deletion of tree

# newTrree=Tree()

traversal of binary tree
	depth first search 
	preorder traversal 
	inorder traversal 
	post order traversal 

	breadth first search 
	level order traversal


# insert a node in binary tree
	# a root node is blank
	# the treeists and we have to look for a first vacant place 

delete enttire binary tree 
rootNode=None
rootNode.leftchild=None 
rootNode.leftchild=None 


# insert a node in a binary 
	# the binary tree is full 
	# we have to look for a first vacant place

# search for a node in binary tree(python list)

# level order traversal 
	# deepestnode=lastusedindex

# what is a binary search tree?
	# in the left subtree the value of a node is less than or equal to its parent node value.
	# in the right subtree the value of a node is greater than its parent node's value

why binary seach?
	# it performs faster than binary tree when inserting and deleting nodes 

# common op on binary search tree 
# 	creation of tree 
# 	insertion of a node 
# 	deletion of a node 
# 	search for a value 
# 	traverse all nodes deletion of tree 

# depth first search 
# 	preorder traversal 
# 	inorder traversal 
# 	post order traversal
# breadth first search 
# 	levle order traversal 

# delete a node from binary search tree 
	# the node to be deleted is a leaf node 
	# the node has one child 
	# the node has two children

# delete entire binary search tree
	# rootNode=None 
	# rootNode.leftchild=None 
	# rootNode.rightchild=None 

# what is avl tree?
	# a avl tree is a self-balancing binary search tree(bst) where the difference between heights of left and right subtrees cannot be more than one for all nodes
	# if at any time heights of left and right subtree differ by more than one, then rebalancing is done to restore avl property, this process is called rotation
# why do we need an avl tree?

# common operations on AVL trees
# 	creation of avl tree 
# 	search for a node in avl tree
# 	traverse all nodes in avl 
# 	insert a node in avl trees 
# 	delete a node from avl trees 
# 	delete the entire avl trees 	

newAVL=AVL()
rooNode=None 
leftchild=None 
rigthchild=None

# preorder
# 	rootNode
# 	left subtree 
# 	right subtree

# inorder
# 	left subtree
# 	rootNode
# 	right subtree

# postOrder traversal 
# 	left subtree 
# 	right subtree
# 	rooNode

# level order 
	# rootNode
	# left subtree 
	# right subtree

# search for a node
	

# insert a node in avl tree
	# rotation is not required 
	# rotation is required
	# ll, lr, rr, rl 
# insert a node in avl tree(all together)

# rotation is not required 
	# rotation is required

# delete a node
	# the tree does not exist 
	# rotation is not required 
		# the node to be deleted has a child 
	# rotation is required (ll,lr,rr,rl)

# delete a node from avl tree (all together)
	

# del entire avl tree 
	# rootnode=None 
# 	rootNode.leftchild=None 
# 	rootNode.rigthcild=None 

# binary heap 
	
# what is is binary heap?
	# a binary heap is a binary tree with following properties
	# a binary heap is either min heap or max heap. in a min binary heap, the key at root mist be minimum among all keys present in binary heap. the same property must be recursively true for all nodes in binary tree.g
	# its a complete tree(all levels completely filled except the last level and the last level has all keys as left as possible). this property of binary heap makes them suitable to be stored in array 

why do need a binary heap? 
	# find the minimum or maximum number among a set of numbers in logN time. and also we want to make sure that inserting addtional numbers does not take more than O(logN)time. and also want to make sure that inserting additional numbers does not take more than O(logN) time

# possible solutions 
	# store the numbers in sorted array

# practial use
	# prims algorithm
	# heap sorts 
	# prioiry queue

# types of binary heap 
	# min heap -the value of each node is less than or equal to the value of both its children 
	# max heap heap- it is exactly the opposite of min heap that is the value of each node is more than or equal to the value of both its children 

# common operations on binary heap 
# 	creation of binary heap 
# 	peek top of binary heap 
# 	extract min/extract max
# 	traversal of binary heap 
# 	size of binary heap 
# 	insert value in binary heap 
# 	delete the entire binary heap 

# implementation options 
# 	array implementation
# 	reference/pointer implementation

# extract a node from binary heap 


delete entire binary heape 
customList=None 

trie

# what is a trie?
	# a trie is a tree-based data structure that organizes information in hierchy
	# strings 

# properties 
# 	it is typically used to store or search strings in a space and time efficient way 
# 	any node in a trie can store non repetitive multiple characters 
# 	every node stores link of the next character of the string 
# 	every node keeps track of the 'end of the string'

# why do we needf trie?
# to solve standard problems in efficient way 
	# spelling checker 
	# auto completion

# common operations 
	# creation 
	# insertion 
	# search for a string in trie 
	# deletion from trie


# insert a string in a trie

# 	case1 : a trie is blank 
# 	case3: 

# # search for a string in trie 
# 	# case1: string doesnt exist 
# 	case2: 

# practical use of trie  
# 	auto completion
# 	spelling checker 
	
# hashing 

# what is hashing ?
# 	hashing is method of sorting indexing data. the idea behind hashing is to allow large amounts of data to be indexed using keys commmonly created by formulas 

# why hashing? 
# 	it it time efficient in case of search operation 

# hashing termilogy 
# 	hash function: it is a function that be used to map arbiitrary size to data of fixed size
# 	key:input data by user 
# 	hash value: a value that is return by hash function 
# 	hash table: it is a data structure which implements an associative array abstract data type, a structure that can map keys to values 
# 	collision: a collion occurs when two different keys to a hash function produce the same output 

hash functions
	mod function

	def mod(number, cellNUmber):
		return number % cellNUmber

	ASCII function


	def modASCII(string, cellnumber):
		total=0
		for i in string:
			total+=ord(i)
		return total%cellNumber

# properties of a good hash function 
	# it distributes hash values uniformly across hash table 
	# it has to use all input data 

# collison resolution techniques 
	direct chaining: implements the buckets as linked list. colliding element are store in this list 
	open addressing: colliding elements are stored in other vacant buckets. during storage and lookup these are found through so called probing.
		linear probing: it places new key into closestt following empty cell 
		quadric probing: adding arbitary quadric polynomial to the index until an empty cell is found  
		double hasing: interval between probes is computed by another hash function 

hash table is ful 
	direct chaining 
	this situation will never arise 

	open addressing 
	creat 2x size of current hash table and recall hashing for current keys 

pros and cons of collision resolution techinques 
	direct chaining
		hash table never gets full 
		huge linked list cause performance leaks(time complexity for search becomes O(n).)

	open addressing 
	easy implementation 
	when hash table is full, creation of new table afffects performance(time complexity for search operation becomesO(o).)

	if the input size is known we alwaus use 'open addressing'
	if we perform deletion operation frequently, we use 'direct chaining'

practial use of hashing  
	password on servers/verifaction
	file system:file path is mapped to physical location on disk 

# pros and cons pf hashing 
	on average insertion/deletion/search operations take O(1) time
	when hash function is not enough insertion/deletion/search operations take O(n)time

what is sorting?
	bubnle sort 
	selection sort 
	inserion sort 
	bucket sort 
	merge sort 
	quick sort 
	heap sort 

what is sorting?
	by definition sorting refers to arranging data in a particular format: either ascending descending 
	practial use of sorting
		MS excell: built in functions to sort data
		oneline shopping: shoppinh websites generally have options of sortbing by price, review, ratings 

# types pf sorting?
	# space used
		# in place sorting: sorting algorithms which does not require any extra space for sorting 
		e.g bubble sort 

		out place: sorting algorithms which requires an extra space for sorting
		example: merge sort 

		stablitity 
		stable sorting: if a sorting algorithms after ssorting the contents does not change the sequence of similar content in which they appear, then this sorting is called stable sorting 
		e.ginsetion sort

		unStable sorting: if a sorting algorithms after sorting the content changes the sequence of similar content in which they appear, then its called unsatble sort 
		quick sort 


sorting terminology 
	increasing order 
	-if successive element is greater than the previous one 

	decreasing order 
	-if successive element is less than the previous one 


	non increasing order #(duplicates)
	-if successive element is less than or equal to its previous elment in the sequence 

	non decreasing order #(duplicates)
	-if  successive element is greater than or equal to its previous elment in sequence

which one to select? 
	-stablitity 
	-space efficient
	-time efficient


bubble sort 
	-bubble sort is also reffereds as sinking sort 
	-we repeatedly compare each pair of adjacent items and swap them if they are in the wrong order 

when to use bubble sort? 
	when input is already sorted 
	space is a concern 
	easy to implement

when to avoid bubble sort?
	average time complexity is poor  

selection sort 
	# -in case of selection we repeatedly find the minimum element and move it to the sorted part of array to make unsorted part sorted 
	divide it(sorted/unsorted)
	performs well in small list 

when to use selection sort?
	when we insuffirecent memory 
	easy to implement

when to avoid selection sort?
	when time is a concern 

insertion sort 
	divide the given array into two part 
	take first element from unsorted array and find its correct postion in sorted array 
	repeat until unsorted array 

when to avoid insertion?
	when we have insuffirecent memory 
	easy to implement 
	whenw we have continious inflow of numbers and we want to keep them sorted 
when to avoid insertion sort?
	when time is a concern

bucket sort 
	create buckets and distrubute elements of array into buckets 
	sort buckets individually 
	merge buckets after sorting

	-number of buckets=round(sqrt(numberof elements))
	-appropriate bucket=cell(value*number of buckets/max value)

when to use bucket? 
	when input uniformly distrubuted over range 
when to avoid bucket?
	when is a concern 

merger sort 
	merge sort is a divide and conquer algo 
	divide the input array in two halves and we keep halving recursively until they become too small that cannot be broken further 
	merge halves by sorting them

when to use merge sort?
	when yuo need stale sort 
	when average expected time is O(NlogN)

when to avoid?
	when space is a concern

quick sort 
	quick sort is a divide and conquer algorithm
	find pivot number and make sure smalller numbers located at the left od the pivot and bogger number are located at the right of the pivot 
	unlike merge sort extra space is not required	

when to use quick sort?
	when average expected time is O(NlogN)


when to avoid quick sort?
	when space is a concern
	when you need stable sort 

10