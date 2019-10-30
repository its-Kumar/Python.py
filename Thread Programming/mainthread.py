import threading

print("Current thread that is running : ",threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print("Main thread")
else:
    print("Some other thread")
    
    