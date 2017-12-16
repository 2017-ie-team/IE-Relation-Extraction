import sys

test_path = sys.argv[1]

file = open(test_path)

total_number = 0
correct_number = 0

True_num = 0
True_total = 0
True_correct = 0

for line in file.readlines():
	element = line.split('\t')
	if len(element)<=1:
		continue
	total_number += 1
	#print(str(element[-2])+'\t'+str(element[-1]))
	if element[-2].strip() == element[-1].strip():
		correct_number += 1
	if 'True' in element[-2].strip():
		True_num += 1
	if 'True' in element[-1].strip():
		True_total += 1
	if 'True' in element[-1].strip() and 'True' in element[-2].strip():
		True_correct += 1

file.close()

print('The accuracy is %f, with total %d and correct %d' 
	% (float(correct_number) / float(total_number), total_number, correct_number))

print('There are %d ground Truth, and %d detected truth, correct are %d' 
	% (True_num,True_total,True_correct))

print('Rec\t%f\nPrec\t%f' % (float(True_correct)/float(True_num),float(True_correct)/float(True_total)))