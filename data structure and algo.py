what are data structures? 
	data structures are different ways of organizing data on your computer, that can 
	be used effectively 
	first in first out 

what is algo?
set of steps to acomplish a task 

algo in my dail life 
get up 
clean the yard 
bath 
study 
break 
eat 
study 
walk 
eat 
study 
sleep


algo in CS 
set of rules for a computer to accomplish a task 
input data 
calculation 
stop when answer found


how do google and fb transmit live video across the internet? 
	compression algo


how to find shortest path on the map? 
	dijstra's algo 

what makes a good algo?
	correctness 
	efficiency
	what are data structures and algo important?
		input(data)

		processing 

		output(information )

		computer science 
		algo 

	problem solving skills 
	fundamentals concenpts of programming in limited time 


	types of data structures 

		data structures 

		primitive 			
		integer				
		float				
		character			
		string
		boolean



		non primitive

		linear -------- 
		|					
		Static(array)

		Dynamic
		linked last, 
		stack, 
		queue		

		non Linear
		tree
		graph

types of algo 
	-simple recursive algo 
	-divide and conquer algo
	-dyna,ic programmingn algo 
	-brute force algo 
	-randomized algo 


simple recursive algo 
	algo Sum(A,n)
		if n=1
			returnA[0]
		s = Sum(a, n-1) /*recurse on all but last*/
		s = s + A[n-1] /* add last element */
	return s 

divide and conquer 
	-divide the problem into smaller subproblems of the same type, and solve these subproblems recursively 
	-combine the solutions to the subprobelms into a solution to the original problem

	e.g quick sort and merge sort 

dynamic programming algo 
	-they work based on memorizaion 
	-to find the best solution

greedy algo 
	-we take the best we can without worrying about future consequences 
	-we hope that by choosing a local optimum solution at each step, we will end up at a global optimum solution 

brute force algo 
	-it simply tries all possibilies until a satisfactory solution is found 

randomized algo 
	-use a random number at least once during the computation to make a decison

RECURSION 
	what is Recursion?
	Recursion = a way of solving a problem by having a function calling itself  


	- performing the same operation multiple times with different inputs 
	- inn every step we try smaller inputs to make the problem smaller
	- base condition is needed to stop the recursion, othwise infinit loop will occur

	def openRussionDOll(doll):
	if doll == 1:
		print('all dolls are opened')
	else:
	openRussionDoll(doll-1)


why recursion ?
	1. recusive thinking is really important in programming and it helps you break down big problems into smaller ones and easier to use 
	-when to choose recursion?
	>if you can divide the problem into similar sub problems
	>design an algo to compute nth...
	>write code to list the n..
	>implement a method to compute all.
	>practice 

	2. the prominent usage of recusion in data structures like tree and graphs 
	3. interviews 
	4. is is used in many algo(divide and conquer, greedy and dynamic prgramming )

how recursion works?
	1. a nethod calls it self 
	2. exit from infinite loop


	e.g 
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

last in, first out

	def recrsiveMethod(n):
	if n<1:
		print('n is less than 1')
	else:
	recursiveMethod(n-1)
	print(n)

	recursiveMethod(4)
	|
	-recursiceMethod(3)
		|
		-recursiveMethod(1)



