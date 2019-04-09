import threading
import time

#You need to have a function, threads execute a function

def sleeper(n,name):
	print("Hi i am{}. Going to sleep for 5 seconds \n".format(name))
	time.sleep(n)
	print('{} has woken up from sleep \n '.format(name))


threads_list = [] #holds out threads after we initialize them

start = time.time()
for i in range(5):
	t = threading.Thread(target=sleeper,name='thread{}'.format(i), args = (5,'thread{}'.format(i)))
	threads_list.append(t)
	t.start()
	print("{} has started".format(t.name))

for t in threads_list:
	t.join() #makes sure the threads all end before the hello statement
end = time.time()

executiontime = (end-start)
print('execution time is: ',executiontime)


print('hello') #these will run even when t is running demonstrating concurrency if not locked
print('hellofriend')