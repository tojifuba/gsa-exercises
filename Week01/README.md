# Genome-scale Algorithms Week 1 — exercises

## Read-mapping

Download the read-mapping tool [bwa](https://github.com/lh3/bwa). You can do this either by downloading a [zip-file](https://github.com/lh3/bwa/archive/master.zip) or by cloning the git repository

```sh
$ git clone https://github.com/lh3/bwa.git
```

After downloading (and unzipping if you downloaded the zip-file), go to the directory and compile the tool.

```sh
$ cd bwa
$ make
```

For some test data, download [ref.fa](ref.fa), [exact-samples.fq](exact-samples.fq), and [exact-samples.txt](exact-samples.txt). The first contain a reference genome I have simulated using the script [simulate-fasta.py](simulate-fasta.py). I ran the command

```sh
$ python simulate-fasta.py -n 20 -m 10000 > ref.fa
```

to create 20 chromosomes of length 10,000 each. You can use the script to simulate your own data for more testing.

The other two files contain strings that match exactly in the reference genome. I have sampled them from the reference using the [simulate-fastq.py](simulate-fastq.py) script using this command:

```sh
$ python simulate-fastq.py -n 10 -m 100 -l exact-samples.txt ref.fa > exact-samples.fq
```

The [exact-samples.txt](exact-samples.txt) file contains four columns, the first is the chromosome I have sampled from, the second the index into the chromosome where I sampled, the third is the sub-sequence of the chromosome, and the fourth column contains a mutated version of the sampled sequence. For the exact matches, the third and the fourth columns differ, but you can simulate inexact subsequences if you use the option `-d` with `simulate-fastq.py`.

Before you can use `bwa` for read-mapping you must index the reference genome. You do this with the command

```sh
$ bwa index ref.fa
```

This creates a number of files that `bwa` will use when mapping reads against the reference.

```sh
$ ls ref.*
ref.fa     ref.fa.amb ref.fa.ann ref.fa.bwt ref.fa.pac ref.fa.sa
```

```sh
$ bwa mem ref.fa exact-samples.fq
```

You can now compare the positions where we got the reads from with the matches that bwa finds:

```sh
$ less -S exact-samples.txt
$ bwa mem ref.fa exact-samples.fq | less -S
```

Check that these matches.

Now, try simulating inexact matches and run `bwa` again with these. Inspect the hits and the CIGAR strings.

## CIGAR strings

I simulate random mutations to a sampled sequence using this Python function:

```python
def mutate(seq, d):
	seq = list(seq)
	for _ in range(d):
		mutation = random.randrange(3)
		position = random.randrange(len(seq))
		if mutation == 0:
			seq[position] = random.choice(DNA)
		elif mutation == 1:
			del seq[position]
		else:
			seq = seq[:position] + [random.choice(DNA)] + seq[position:]
	return ''.join(seq)
```

Strictly speaking it doesn’t necessarily give you a string at edit-distance *d* since mutations only have a 3/4 chance of changing the nucleotide at the given position, but *d* is a max distance anyway.

An alternative approach would be to simulate a CIGAR string:

```python
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
```

Strictly speaking, this doesn’t simulate a CIGAR string since such a string does not have the edit symbols represented by one character per position in the read but represent these as sequences of numbers and symbols, but we can create these strings and then compress them into real CIGAR strings. We can also use the simulated strings to modify reads according to the CIGAR. Below I have simulated strings (first column) that compresses to the CIGAR strings in the second columns and I have used them to modify the sequence in the third column into the strings in the fourth column.

```
======X=D=	8M1D1M	GCGCACGCGG	GCGCACGCG
======X=X=	10M	TTGGGATCTA	TTGGGAGCAA
========DI	8M1D1I	CGAGAAAGTG	CGAGAAAGA
=X====X===	10M	ATTAGTGTAC	ACTAGTATAC
========D=	8M1D1M	TCTATCTACG	TCTATCTAG
====X===I=	8M1I1M	GGATATACGT	GGATGTACTG
==I=====X=	2M1I7M	TCTCTTGATA	TCGTCTTGCT
X====I====	5M1I4M	GCGTTCAGCC	ACGTTCCAGC
=X=====D==	7M1D2M	AAAAGCGAGT	ACAAGCGGT
X========I	9M1I	ACGCCTCAAG	TCGCCTCAAT
```

Write functions to compress such simulated strings into proper CIGAR sequences and to modify a read according to the CIGAR.

Use this code to simulate reads in FASTQ format and map them with `bwa`. Compare the CIGARs that `bwa` finds to those you have simulated.

## FASTA files

At some point you will have to write a read mapper that can read in a FASTA files, so you might as well write a parser for it now… Write a parser that reads a FASTA file into a structure where you have information about the name of each sequence—taken from the FASTA header—and where you have the entire sequences stored.

## FASTQ files

You will also have to read FASTQ files at some point, so write a parser for it now. Write a parser that lets you iterate through all the reads in the FASTQ file.
