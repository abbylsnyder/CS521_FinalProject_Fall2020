"""
Abby Snyder
MET CS 521 A2
Fall 2020
Final Project – Unit Tests
"""

from finalProj import Dog

testDog = Dog("Australian Cattle Dog","M","Short","Moderate","High")

#valid input for sizes
assert Dog.validSize("XS") == True
assert Dog.validSize("S") == True
assert Dog.validSize("M") == True
assert Dog.validSize("L") == True
assert Dog.validSize("XL") == True
assert Dog.validSize("small") == False

assert testDog.matchSize("M") == True
assert testDog.matchSize("S") == False

assert Dog.validCoat("SHORT") == True
assert Dog.validCoat("SMOOTH") == True
assert Dog.validCoat("WIRE") == True
assert Dog.validCoat("MEDIUM") == True
assert Dog.validCoat("LONG") == True
assert Dog.validCoat("MODERATE") == False

assert testDog.matchCoat("SHORT") == True
assert testDog.matchCoat("LONG") == False

assert Dog.validActivity("LOW") == True
assert Dog.validActivity("MODERATE") == True
assert Dog.validActivity("HIGH") == True
assert Dog.validActivity("MEDIUM") == False

assert testDog.matchActivityLevel("HIGH") == True
assert testDog.matchActivityLevel("MEDIUM") == False

