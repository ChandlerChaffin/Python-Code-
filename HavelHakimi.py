import random
def remove_zed(sequence):
	no_zero_sequence = []
	for item in sequence:
		if item != 0:
			no_zero_sequence.append(item)
	return no_zero_sequence
def sort_descending(sequence):
	descending_sequence = sorted(sequence, reverse = True)
	return descending_sequence
def length_check(N, sequence):
	seq_len = len(sequence)
	if seq_len < N:
		return True
	else: 
		return False
def front_elemin(N, descended_sequence):
	for item in descended_sequence[:N]:
		descended_sequence.append(item-1)
	descended_sequence = descended_sequence[N:]
	return descended_sequence
def Havel_Hakimi_Algo(sequence):
	sequence = remove_zed(sequence)
	if len(sequence) == 0:
		return True
	else:
		sequence = sort_descending(sequence)
		N = sequence.pop(0)
		if length_check(N, sequence):
			return False
		else: 
			sequence = front_elemin(N, sequence)
			return Havel_Hakimi_Algo(sequence)
def gen_rand_arr(length):
	out_arr = []
	counter = length
	while counter != 0:
		out_arr.append(randint(0,length))
		counter -= 1
	return out_arr

		
	

		
	

print(Havel_Hakimi_Algo([0,2,1]))
