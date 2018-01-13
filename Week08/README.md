# Genome-scale Algorithms Week 8 — exercises

## Building a suffix array

If we have a suffix tree—which we should by now—then it is simple to build a suffix array in linear time. You just need to traverse the tree in lexicographical order. So this week, we will implement that.

### Traversing in lexicographical order

To traverse in lexicographical order in linear time, we must be able to traverse the children of any given node in lexicographical order. Well, technically we could search for each character in order, since we assume that the alphabet size is constant in most of what we do, but we know it isn’t real.

If you don’t already have your children in order—no pun intended—then what strategy would you use to traverse the tree in lexicographical order?

As a group exercise, discuss various strategies and we will discuss them. You won’t have to implement them, so you can get as creative as you want.

### Building the suffix array

A strategy that you *should* be able to implement is this: make a list with the length of the alphabet size and simply bucket the children into it each time you recurse to a new node. You cannot reuse the say array here if you traverse the tree recursively since that would break the bucketing of parental nodes, but you don’t need to modify the tree in any way to implement an algorithm like this:

1. At the given node, bucket all the children.
2. In the correct order, traverse the bucket list.
3. If there is a child in a bucket, recurse.

What would the complexity of this approach be?

Try to implement this strategy to build a suffix array from a suffix tree.
