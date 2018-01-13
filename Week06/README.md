# Genome-scale Algorithms Week 6 — exercises

## Building a suffix trie

With the code we have for building a trie from week 4, it should be relatively easy to build a suffix trie. If you used boolean string labels, change them to integer labels again—we know that there will be no duplicated strings. We also know that only leaves will have a label, so if you want, you can also exploit that, but at least the leaves need to contain an index.

Instead of having characters associated with edges, use an index into the string. This doesn’t change the complexity, but it is closer in spirit to suffix trees.

Modify your trie code to do this.

## Building a suffix tree from a suffix array

Prove that successive indices when you move along a non-brancing path in the suffix trie differ by exactly one. That is, if you take a sequence of non-branching nodes in trie, you get an interval of indices into your string.

To build a suffix tree from a suffix trie, you simply have to compress paths. If your nodes contain both a from and to index you can start out with your initial trie and simply identify non-branching paths and replace them with a single node consisting of the same interval as the path.

Try implementing this.

What is the complexity of this algorithm?