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
	incompleted_tasks=[ task for task in tasks if task["status"]==False]# task before for statement will be added to the same square brackets if condition inside ifstatement achieved
	

    #if not incompleted_tasks:
	if len(incompleted_tasks)==0:
		print("no tasks to mark as completed")
		return
	
	for i , task in enumerate(incompleted_tasks):
		print(f"{i+1}_ {task['task']}")
		print("_"*30)
		

	#get the task from the user
	task_number=int(input("Enter incompleted task to complete"))
	#mark task as completed
	incompleted_tasks[task_number - 1]["status"]=True
	
	#print a message to the user
	print("task marked completed")
	
def view_tasks():
	if not tasks:
		print("no tasks to view")
		return
	
	for i , task in enumerate(tasks):
		if task["status"]:
			status='✅'
		else:
			status='❌'
			
		print(f"{i+1}_ {task['task']} {status}")


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
		