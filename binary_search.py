# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 17:20:33 2022

@author: VARUN
"""

nums = []
print(end="How Many Number to Enter ? ")
tot = int(input())
print(end="Enter " + str(tot) + " Numbers: ")
for i in range(tot):
    nums.insert(i, int(input()))

for i in range(tot-1):
    for j in range(tot-i-1):
        if nums[j]>nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp

print(end="\nThe List is: ")
for i in range(tot):
    print(end=str(nums[i]) + " ")

print(end="\nEnter a Number to Search: ")
search = int(input())
first = 0
last = tot-1
middle = int((first+last)/2)
while first <= last:
    if nums[middle]<search:
        first = middle+1
    elif nums[middle]==search:
        print("\nThe Number Found at Position: " + str(middle+1))
        break
    else:
        last = middle-1
    middle = int((first+last)/2)
if first>last:
    print("\nThe Number is not Found in the List")