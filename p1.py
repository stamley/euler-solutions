def mul_of_3_or_5():
	s = 0
	for i in range(1000):
		if i % 3 == 0 or i % 5 == 0:
			s += i
	return s

print(mul_of_3_or_5())