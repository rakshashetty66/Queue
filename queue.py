queue=[]

def enqueue():
    element=input("Enter the element: ")
    queue.append(element)
    print(f"{element}is added to queue!")

def dequeue():
    if not queue:
        print("queue is empty!")
    else:
        e=queue.pop(0)
        print(f"removed element: {e}")

def display():
    print(queue)

while True:
    print("Select the Operation: \n 1.Add \n 2.Remove \n 3.Show \n 4.quit")
    choice=int(input("Enter Choice: "))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter the correct Operation!")
