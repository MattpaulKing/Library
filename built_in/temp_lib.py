import time

def do_something(seconds):
   print(f"Sleeping {seconds} seconds . . .")
   time.sleep(seconds)
   return f"Done sleeping {seconds}"