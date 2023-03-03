'''
Write a Python program to print a specified list after removing the 0th, 4th and 5th
elements. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
'''
sampleList = ['Red', 'Green', 'White', 'Black','Pink', 'Yellow']
sampleList.remove([0])
sampleList.remove([4])
sampleList.remove([5])
print (sampleList)