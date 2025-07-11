import threading
import time

def walk_dog(dog_name):
    time.sleep(8)
    print(f"You finish walking the {dog_name}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

#Executes sequentially
# walk_dog()
# take_out_trash()
# get_mail()

# When using multi-threading they executes concurrently
chore1 = threading.Thread(target=walk_dog,args=("Puppy",))  #arguments must be passed to the function 
                                                            #as a tuple of second keyword argument named as args
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete")