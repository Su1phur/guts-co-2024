import datetime
from sys import platform
import psutil
import sched, time
from numpy import base_repr
from distutils.spawn import find_executable
import os
import timeit

def loop(scheduler, loop_number):
    print("Loop: " + str(loop_number))
    loop_number += 1
    true_counter = 0
    if datetime.datetime.today().weekday() == 5: # today is Sat
        true_counter += 1

    if not platform == "linux" or not platform == "linux2": # not linux
        true_counter += 1

    if psutil.cpu_count(logical = False) > 5: # has more than 5 physical cpu cores
        true_counter += 1

    if datetime.datetime.now().second > 15: # curent sec > 15
        true_counter += 1

    if psutil.virtual_memory().percent > 20 and psutil.virtual_memory().percent < 70: # 30 < ram usage < 70
        true_counter += 1
    
    base20_sec = base_repr(datetime.datetime.now().second, base = 20)
    
    def base20_find_alphabet(string):
        for char in string:
            if char.isalpha():
                return True

    if base20_find_alphabet(base20_sec) == True: # if current second converted into base 20 has a alphabet
        true_counter += 1

    env_paths = os.environ['PATH'] + r";C:\Program Files (x86)\Steam" # if Steam is installed
    if find_executable('steam', env_paths) is not None:
        true_counter += 1
    
            
    if psutil.cpu_freq().max > 2500: # cpu has max greater than 2.5Ghz
        true_counter += 1

    def is_prime(n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n < 9: return True
        if n%3 == 0: return False
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n % f == 0: return False
            if n % (f+2) == 0: return False
            f += 6
        return True 
    
    if is_prime(loop_number) != True: # the number of loops done is not prime
        true_counter += 1 

    if true_counter == 9:
        print(loop_number)
        print("Successful exit")
    else: 
        scheduler.enter(1, 1, loop, (scheduler, loop_number))


def main():
    my_scheduler = sched.scheduler(time.time, time.sleep)
    my_scheduler.enter(1, 0, loop, (my_scheduler, 0))
    my_scheduler.run()

main()