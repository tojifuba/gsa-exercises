# Genome-scale Algorithms Week 2 — exercises

## Exact pattern matching

Your first project will involve implementing exact pattern matching algorithms. When you do so, you will, of course, also need to test them. This means both testing that they have the correct behaviour and that they have the correct running time.

As a warm-up exercise for the project, we can do this for the naïve algorithm. First, you should consider the following questions:

1. How would you test the correctness of the algorithm?
2. If you convince yourself that you have a working implementation, how would you use that to test the correctness of more sophisticated algorithms?
3. How do you test the running time of an algorithm? Does it complicate matters if the complexity depend on more than one parameter?

Once you have come to solutions to these questions, implement the naïve algorithm and code to test correctness and test that the algorithm works as intended.

## Generating strings

An easy way to do inexact pattern matching, if we have an implementation of exact pattern matching, is to reduce the first problem to the second. If, given a pattern string, we can generate all strings at a certain edit distance from the pattern, then we can simply search for *all* the strings.

This might even be a good solution—who knows? But consider this:

1. How many strings are at a given edit distance from a given string?
2. Can you derive a recursion for answering this question? The answers in such questions are not always closed formed—that depends on whether we can solve a recursion equation, but a place to start is to get the recursion.
3. From the recursion, can you derive an asymptotic complexity? Either lower bound or upper bound, if not exact.
4. If the lower and upper bound, which is more important for this particular problem?

Now try and implement the recursion and plot the number of strings at various edit distance to strings of various lengths.

As a bonus challenge, derive an algorithm for actually generating the strings and implement that. Since, in the SAM format, matches contain CIGAR strings together with positions of matches, can you extend the algorithm so it generates *both* near by strings and the CIGAR string corresponding to the edits?
