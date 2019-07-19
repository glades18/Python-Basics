import platform
import math
import mymodule
import fibo
import sys
import os
import statistics


def show_platform():
        return platform.system()

print(show_platform())


def directory():
         return dir(math)

print(directory())


def module_greetings(name):
        greeting = mymodule.greeting(name)

        return greeting

print(module_greetings(name))


def fibonacci_seq(num):
        sequence = fibo.fib(num)

        return sequence

print(fibonacci_seq(num))


def sys_path():
        return sys.path

print(sys_path())


def working_dir():
        return os.getcwd()

print(working_dir())


def remove_dir(directory):
        os.rmdir(directory)

remove_dir(directory)


def list_directories(directory):
        return os.listdir(directory)

print(list_directories(directory))


def mean(num_list):
        return statistics.mean(num_list)

print(mean(num_list))


def median(num_list):
        return statistics.median(num_list)

print(median(num_list))

            