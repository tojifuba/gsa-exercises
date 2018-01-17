# Project 2 — Suffix tree construction

You should implement a suffix tree construction algorithm. You can chose to implement the naive O(n^2^) time construction algorithm as discussed in class, or McCreight suffix tree O(n) time construction algorithm Write the suffix tree as an abstract data structure that can be reused in project 3, and then write an application that uses the suffix tree exact pattern search algorithm (similar to slowscan) to report all indices in a string where a given pattern occurs.

The algorithm should be implemented in a program named `search-st`. This program should take two arguments, the filename of a file containing the string to search in and the pattern to search for. The program should output the positions where the second argument appears in the string in the first. E.g. if the file mississippi.txt contains the string "mississippi\n", then the programs should be called as:

```sh
search-st mississippi.txt ss
```

and the output should consist of the indices

```sh
3 6
```

With the suffix tree search algorithm, you are not guaranteed that the output is sorted, but if you sort it, you should get the output files in the material below.

The project should be in groups of 2–3 students. It will not be graded.

## Material 

To test your application, you can use the following text files, with corresponding expected output:

* [mississippi.txt](mississippi.txt). Result when searching for "ss": [mississippi.out](mississippi.out)
* [banana.txt](banana.txt). Result when searching for "ana": [banana.out](banana.out)
* [walrus-and-carpenter.txt](walrus-and-carpenter.txt). Result when searching for "Walrus": [walrus-and-carpenter.out](walrus-and-carpenter.out)
* [ancient-mariner.txt](ancient-mariner.txt). Result when searching for "Albatross": [ancient-mariner.out](ancient-mariner.out)

## Evaluation

You should upload your solution to Blackboard before the lecture  13/3. Your TA will then pair up groups (if you haven’t done that already) and exchange your solution with another. The other solution you get, you should test and if you are up to it, review the code and the report.

The solution you upload should contain code for building the program `search-st` (with the appropriate build tools for the programming language you have chosen), and a one-page Pdf file where you address the following questions:

* Insights you may have had while implementing and comparing the algorithms.
* Problems encountered, if any.
* An experiment that verifies the correctness of your implementations.
* An experiment that verifies that your implementation of `search-st` uses no more time than O(n) or O(n^2^) (depending on algorithm) for constructing the suffix tree and no more than O(m) for searching in it.. Remember to explain your choice of test data. What are "best" and "worst" case inputs?
