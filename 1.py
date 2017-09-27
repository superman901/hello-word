def MAX(vector):
	child_ = []
	sum_ = 0
	for i in vector:
		if i > 0:
			sum_ += i
			child_.append(i)
	return sum_,child_
if __name__ == '__main__':
     sum_,child_=MAX(vector = [1,2,3,4,-5,-34])
     print(sum_)