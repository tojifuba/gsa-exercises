# Project 4 — Suffix arrays and BW-match

You should implement a suffix array construction algorithm. You can chose to implement the naive algorithm where you explicitly sort strings or the O(n) skew algorithm. After constructing the suffix array, you should implement the binary search based and the Burrows-Wheeler based search algorithm.

The algorithms should be implemented in two programs named `search-bs` and `search-bw` for the binary search and Burrows-Wheeler algorithms, respectively. These program should take two arguments, the filename of a file containing the string to search in and the pattern to search for. The programs should output the positions where the second argument appears in the string in the first. E.g. if the file mississippi.txt contains the string "mississippi\n", then the programs should be called as:

```sh
search-bs mississippi.txt ss
search-bw mississippi.txt ss
```

and the output should consist of the indices

```sh
3 6
```

With the suffix array search algorithms, you are not guaranteed that the output is sorted, but if you sort it, you should get the output files in the material below.

The project should be in groups of 2–3 students. It will not be graded.

## Material 

To test your application, you can use the following text files, with corresponding expected output:

* [mississippi.txt](mississippi.txt). Result when searching for "ss": [mississippi.out](mississippi.out)
* [banana.txt](banana.txt). Result when searching for "ana": [banana.out](banana.out)
* [walrus-and-carpenter.txt](walrus-and-carpenter.txt). Result when searching for "Walrus": [walrus-and-carpenter.out](walrus-and-carpenter.out)
* [ancient-mariner.txt](ancient-mariner.txt). Result when searching for "Albatross": [ancient-mariner.out](ancient-mariner.out)

## Evaluation

You should upload your solution to Blackboard before the lecture  3/4. Your TA will then pair up groups (if you haven’t done that already) and exchange your solution with another. The other solution you get, you should test and if you are up to it, review the code and the report.

The solution you upload should contain code for building the program `search-st` (with the appropriate build tools for the programming language you have chosen), and a one-page Pdf file where you address the following questions:

* Insights you may have had while implementing and comparing the algorithms.
* Problems encountered, if any.
* An experiment that verifies the correctness of your implementations.
* An experiment that verifies that your implementation of `search-bs` uses no more time than O(m log n) to search (after the suffix array has been constructed).
* An experiment that verifies that your implementation of `search-bw` uses no more time than O(m) to search (after the suffix array has been constructed).

