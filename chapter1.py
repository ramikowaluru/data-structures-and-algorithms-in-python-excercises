#R-1.1
def is_multiple(n,m):
	"""Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise."""
	if n%m==0:
		return True
	return False


#R-1.2
def is_even(k):
	"""Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""
	if "{0:b}".format(k)[0]=='1':
		return "odd"
	return "even"


def minmax(data):
	minimum,maximum=data[0],data[0]
	for element in data:
		if element<minimum:
			minimum=element
		if element>maximum:
			maximum=element
	return str(minimum)+" and "+str(maximum)


if __name__ == "__main__":
	print("is m multiple of n? {}".format(is_multiple(10,2)))
	print("k is {}".format(is_even(9)))
	print("min and maximum of {} is {}".format([2,5,3,4],minmax([2,5,3,4])))
