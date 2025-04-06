## Calculate Average of Values in a List
#
#list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#def average(list_: list) -> float:
#    return print(sum(list_) / len(list_))
#
#average(list_)

## Filter Data Above a Threshold

#list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#def filter_above_threshold(list_: list) -> list:
#    threshold = 7
#    for i in list_[:]:
#        if i >= threshold:
#            list_.remove(i)
#        else:
#            continue
#
#filter_above_threshold(list_)
#print(list_)

## Count Unique Values in a List

#list_ = [1, 2, 3, 3, 3, 2, 7, 2, 8, 8]
#
#def count_unique(list_: list) -> float:
#    return print(len(set(list_)))
#
#count_unique(list_)

## Convert Celsius to Fahrenheit in a List

#list_ = [35, 24, 12, 40, 0]
#
#def celsius_to_fahrenheit(list_: list) -> list:
#    for i in range(0, len(list_)):
#        list_[i] = (9/5) * list_[i] + 32
#
#celsius_to_fahrenheit(list_)
#print(list_)

## Find Missing Values in a Sequence

import timeit
import random

sequence = list(range(1, 100_001))
removed = random.sample(sequence, 5000)
for r in removed:
    sequence.remove(r)

def using_set():
    complete = set(range(min(sequence), max(sequence)+1))
    missing = complete - set(sequence)
    return list(missing)

def using_list():
    missing = []
    for num in range(min(sequence), max(sequence)+1):
        if num not in sequence:
            missing.append(num)
    return missing

time_set = timeit.timeit(using_set, number=1)
time_list = timeit.timeit(using_list, number=1)

print(f"Time using set: {time_set:.4f} seconds")
print(f"Time using list: {time_list:.4f} seconds")