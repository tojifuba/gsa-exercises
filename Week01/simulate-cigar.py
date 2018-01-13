
import random
import argparse


DNA = 'ACGT'


def simulate_string(m):
	"""Simulate a DNA sequence of length m."""
	return ''.join([random.choice(DNA) for _ in range(m)])
	
def simulate_cigar(n, d):
	cigar = ['='] * n
	for _ in range(d):
		mutation = random.randrange(3)
		position = random.randrange(n)
		if mutation == 0:
			cigar[position] = 'X'
		elif mutation == 1:
			cigar[position] = 'D'
		else:
			cigar[position] = 'I'
	return ''.join(cigar)

def map_symbols(x):
	if x in ['X','=']: return 'M'
	return x

def compress_cigar(cigar):
	cigar = ''.join(map_symbols(x) for x in cigar)
	idx = [i for i in range(1,len(cigar)) if cigar[i-1] != cigar[i]]
	if idx == []:
		return "{}{}".format(len(cigar), cigar[0])
	start = [0] + idx
	to = idx + [len(cigar)]
	return ''.join("{}{}".format(t-s, cigar[s]) for s,t in zip(start,to))

def mutate_read(read, cigar):
	result = []
	j = 0
	for k in range(len(cigar)):
		if cigar[k] == '=':
			result.append(read[j])
			j += 1
		elif cigar[k] == 'X':
			result.append(random.choice(DNA))
			j += 1
		elif cigar[k] == 'I':
			result.append(random.choice(DNA))
		else:
			j += 1
	return ''.join(result)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(prog='simulate-fasta', usage='%(prog)s [options]',
									 description="Simulate random sequences and output them in FASTA format.")
	parser.add_argument('-n', nargs='?', type=int, help='Number of sequences, default 10', default=10)
	parser.add_argument('-m', nargs='?', type=int, help='The length of the sequences, default 10', default=10)
	parser.add_argument('-d', nargs='?', type=int, help='The maximum edit distance to mutate, default 2', default=2)
	args = parser.parse_args()

	for _ in range(args.n):
		seq = simulate_string(args.n)
		cigar = simulate_cigar(args.n, args.d)
		mutated_seq = mutate_read(seq, cigar)
		print('\t'.join([cigar, compress_cigar(cigar), seq, mutated_seq]))


