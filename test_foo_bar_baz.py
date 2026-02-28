import pytest

from foo_bar_baz import foo_bar_baz

def test_zero():
	result:str = foo_bar_baz(0)
	assert(type(result) is str), \
		"foo_bar_baz(0) should return a string.  Got: " + str(type(result))

	assert(result == ""), \
		"Expected: ||\n     Got: |" + result + "|"

def test_negatives():
	for i in range(-100, 0):
		result:str = foo_bar_baz(i)

		assert(type(result) is str), \
			"foo_bar_baz(" + str(i) + ") should return a string.  Got: " + str(type(result))
		
		assert(result == ""), \
			"Expected: ||\n     Got: |" + result + "|"

def test_positives():
	limit:int = 4000

	for i in range(1, limit):
		result:str = foo_bar_baz(i)
		assert(type(result) is str), \
			"foo_bar_baz(0) should return a string.  Got: " + str(type(result))
		
		assert(result != ""), \
			"foo_bar_baz(" + str(i) + ") should not return an empty string."

		split_result:list = result.split(" ")

		for j in range(1, len(split_result)):
			if (j % 3 == 0) and (j % 5 == 0):
				assert(split_result[j-1] == "Baz")
			elif j % 3 == 0:
				assert(split_result[j-1] == "Foo")
			elif j % 5 == 0:
				assert(split_result[j-1] == "Bar")
			else:
				assert(split_result[j-1] == str(j))

def test_same_output():
	result_one = foo_bar_baz(40)
	result_two = foo_bar_baz(40)

	assert(result_one == result_two), "Results should be the same."

def test_different_output():
	result_one = foo_bar_baz(40)
	result_two = foo_bar_baz(20)

	assert(result_one != result_two), "Results should not be the same."

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