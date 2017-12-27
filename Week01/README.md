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

For some test data, download [ref.fa](ref.fa), [exact-samples.fq](exact-samples.fq), and [exact-samples.txt](exact-samples.txt). The first contain a reference genome I have simulated using the script [simulate-fasta.py](simulate-fast.py). I ran the command

```sh
$ python simulate-fasta.py -n 20 -m 10000 > ref.fa
```

to create 20 chromosomes of length 10,000 each. You can use the script to simulate your own data for more testing.

The other two files contain strings that match exactly in the reference genome. I have sampled them from the reference using the [simulate-fastq.py](simulate-fast.py) script using this command:

```sh
$ python simulate-fastq.py -n 10 -m 100 -l exact-samples.txt ref.fa > exact-samples.fq
```

The [exact-samples.txt](exact-samples.txt) file contains four columns, the first is the chromosome I have sampled from, the second the index into the chromosome where I sampled, the third is the sub-sequence of the chromosome, and the fourth column contains a mutated version of the sampled sequence. For the exact matches, the third and the fourth columns differ, but you can simulate inexact subsequences if you use the option `-d` with `simulate-fastq.py`.

