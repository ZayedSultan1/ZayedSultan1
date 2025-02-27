#add task to a list 
#mark task as complete
#view tasks
#Quit
def add_task():#pass = ...
	#add a task from user
	task = input ("Enter a task : ")
	#define a task status
	task_info = {"task" : task , "status" : False}
	#add task from a dictionary into a list
	tasks.append(task_info)

def mark_task():
	
	
	#get list of incompleted tasks
	'''
	#first way : print out dictionaries
	for task in tasks:
		if task['status']==False:
			incompleted_tasks=task
		print(incompleted_tasks)
	'''
	#second way : ternary way : print out list of dictionaries
	incompleted_tasks=[ task for task in tasks if task["status"]==False]# task before for statement will be added to the same square brackets if condition inside for statement achieved
	print(incompleted_tasks)

			
	#show them to the user
	
	for i , task in enumerate(incompleted_tasks):
		print(f"{i+1}_ {task['task']}")
		print("_"*30)
		

	#get the task from the user
	task_number=int(input("Enter incompleted task to complete"))
	#mark task as completed
	tasks[task_number - 1]["status"]==True
	
	#print a message to the user
	print(tasks)
	
def view_tasks():
	...


tasks=[]
message=("1_ add task to a list\n2_ mark task as complete\n3_ view tasks\n4_ Quit")
while True:
	print(message)
	choice=input("Enter your choice : ")
	if choice == "1" :
		add_task()
	elif choice == "2" :
		mark_task()
	elif choice == "3" :
		view_tasks()
	elif choice == "4" :
		break
	else:
		print("error : Please enter a valid choice between 1 and 4")
		