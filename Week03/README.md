# Genome-scale Algorithms Week 3 — exercises

## Border arrays

The algorithm for constructing border arrays is relatively straightforward, as long as you are careful with the indexing. Implement it in your preferred programming language—if that is C, there is already an implementation on the slides, so don’t look there before you are done.

We define the border array `ba` such that `ba[i]` is the longest border of `x[1..i]`. Now, define `bax` such that `bax[i]` is the longest border of `x[1..i]` where `x[bax[i]+1]` differs from `x[i+1]`, that is, the *next* character after the border and the position in `x` must be different.

Can you derive an algorithm for computing `bax`?

A hint here is that either `bax[i]=ba[i]`, when the additional condition is satisfied, or else it must be the longest border of `x[1..ba[i]]` where the condition is satisfied (can you show why?). This is a value that can be found in `bax`.

## Exact pattern matching

Implement the exact pattern matching algorithm based on border arrays in your preferred programming language—if that is C, there is already an implementation on the slides, so don’t look there before you are done.

Remember, you don’t actually have to construct the concatenation of the pattern and string to do this—you just need to “fake” it.
