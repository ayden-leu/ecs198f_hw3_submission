import pytest

from foo_bar_baz import foo_bar_baz

def test_zero():
	result:str = foo_bar_baz(0)
	assert(result != ""), \
			"foo_bar_baz(" + str(i) + ") should have handled the zero or raised an error."

def test_negatives():
	for i in range(-100, 0):
		result:str = foo_bar_baz(i)
		assert(result != ""), \
			"foo_bar_baz(" + str(i) + ") should have handled the negative integer or raised an error."

def test_positives():
	outputUpToLimit:str = [
		"1", "2", "Foo", "4", "Bar", "Foo", "7", "8", "Foo", "Bar",
		"11", "Foo", "13", "14", "Baz", "16", "17", "Foo", "19", "Bar",
		"Foo", "22", "23", "Foo", "Bar", "26", "Foo", "28", "29", "Baz",
		"31", "32", "Foo", "34", "Bar", "Foo", "37", "38", "Foo", "Bar", 
		"41", "Foo", "43", "44", "Baz", "46", "47", "Foo", "49", "Bar", 
		"Foo", "52", "53", "Foo", "Bar", "56", "Foo", "58", "59", "Baz", 
		"61", "62", "Foo", "64", "Bar", "Foo", "67", "68", "Foo", "Bar", 
		"71", "Foo", "73", "74", "Baz", "76", "77", "Foo", "79", "Bar", 
		"Foo", "82", "83", "Foo", "Bar", "86", "Foo", "88", "89", "Baz", 
		"91", "92", "Foo", "94", "Bar", "Foo", "97", "98", "Foo", "Bar"
	]

	for i in range(1, len(outputUpToLimit)+1):
		expected = ""
		for j in range(i):
			expected += outputUpToLimit[j]
			if j+1 != i:  expected += " "

		result:str = foo_bar_baz(i)
		assert(type(result) is str), \
			"foo_bar_baz(" + str(i) + ") should return a string.  Got: " + str(type(result))

		assert(result == expected), \
			"Expected: |" + expected + "|\n" + \
			"     Got: |" +  result  + "|"

if __name__ == "__main__":
	print("test_foo_bar_baz.py should be ran with pytest.")

# I assume that crashing the program when given a non-integer input is supposed to happen.
# If not, then uncomment the below tests.

# def test_input_float():
# 	result:str = foo_bar_baz(3.5)
# 	assert(type(result) is str), \
# 		"foo_bar_baz(" + str(i) + ") should return a string.  Got: " + str(type(result))

# 	assert(result == ""), \
# 		'Expected: ""\n     Got: ' + result

# def test_input_string():
# 	result:str = foo_bar_baz("a string")
# 	assert(type(result) is str), \
# 		"foo_bar_baz(" + str(i) + ") should return a string.  Got: " + str(type(result))

# 	assert(result == ""), \
# 		'Expected: ""\n     Got: ' + result

# def test_input_callable():
# 	def example_func():
# 		print("hi!")

# 	result:str = foo_bar_baz(example_func)
# 	assert(type(result) is str), \
# 		"foo_bar_baz(" + str(i) + ") should return a string.  Got: " + str(type(result))

# 	assert(result == ""), \
# 		'Expected: ""\n     Got: ' + result
