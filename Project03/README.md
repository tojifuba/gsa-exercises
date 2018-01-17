# Project 3 — Finding tandem repeats

This project is about the finding all occurrences of tandem repeats in strings.

You should implement the Stoye-Gusfield algorithm for finding all occurrences of tandem repeats in a string S of length n in time O(n log n + occ), where occ is the number of occurrences you find. The algorithm is described in the paper [Simple and Flexible Detection of Contiguous Repeats Using a Suffix Tree](http://csiflabs.cs.ucdavis.edu/~gusfield/tcs.pdf) and on the slides from the lecture about finding tandem repeats. To implement the algorithm, you need a working implementation of a suffix tree construction algorithm. You should have that from mandatory project 2, if not, then it is time to fix it. Based on your implementation of the algorithm, you should write an application which counts the number of occurrences of branching tandem repeats and the number of occurrences of non-branching tandem repeats.

Your application should take one argument: the filename of the string to search for tandem repeats. E.g. if the file abaabaabbba.txt contains the string "abaabaabbba\n", then the application should be called as:

```sh
./tandem abaabaabbba.txt
```

and should output:

```sh
4 3
```

You can see the slides from the lecture about finding tandem repeats for an illustration of the occurrence of tandem repeats in the string abaabaabbba.

For debugging purposes you might also want your program to output the actual occurrences. To achieve the desired O(n log n) running time for finding all occurrences of branching tandem repeats, you should be careful not the spend more time than O(|Small(v)|) at node v, e.g. if you construct the leaf-list of v by concatenating the leaf-lists of its children, you can use linked lists with a pointer to the last element, such that concatenation can be done in constant time.

The project should be in groups of 2-3 students. It will not be graded.

## Material

To test your application, you can use the testdata in [testdata.zip](testdata.zip).

that contains the following text files, with corresponding expected output. (In the out-files, the input string is indexed from position 0.)
* abaabaabbba.txt. Expected output 4 3, see abaabaabbba.out.
* abcabc.txt. Expected output 1 0, see abcabc.out.
* mississippi.txt. Expected output 4 1, see mississippi.out.
* fib10.txt (the 10th [Fibonacci string](https://en.wikipedia.org/wiki/Fibonacci_word)). Expected output 65 170, see fib10.out.
* fib15.txt (the 15th Fibonacci string). Expected output 751 4477, see fib15.out.
* gene1.txt (a DNA string). Expected output 410 134, see gene1.out.
* gene2.txt (another DNA string). Expected output 795 449, see gene2.out.
* protein1.txt (the protein encoded by gene1). Expected output 22 8, see protein1.out.
* protein2.txt (the protein encoded by gene2). Expected output 21 2, see protein2.out.

## Evaluation

You should upload your solution to Blackboard before the lecture  17/4. Your TA will then pair up groups (if you haven’t done that already) and exchange your solution with another. The other solution you get, you should test and if you are up to it, review the code and the report.

The solution you upload should contain code for building the program `tandem` (with the appropriate build tools for the programming language you have chosen), and a one-page Pdf file where you address the following questions:

* Insights you may have had while implementing the algorithm,
* Problems encountered, if any,
* An experiment which verifies that your implementation uses no more than time O(n log n) for finding/counting all occurrences of branching tandem repeats.

