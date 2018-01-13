# Genome-scale Algorithms Week 4 — exercises

## Tries

Implement a program that reads in a number of strings from a file and then checks if another string is found in the tree.

Such a program, of course, consists of two parts:

1. Building the trie
2. Searching for a string in an existing trie

where, obviously, part two should be able to reuse a lot of functionality from part one.

### Data structure

When drawing a trie, we have an abstract view on the data structure, but when you actually have to implement it, you need to work out some details.

1. How do you represent nodes and edges in the tree?
2. How do you implement the relationship between parent and children so it is easy to search for the right child when you are at a node?

Keep in mind here, that you do not necessarily have to explicitly represent things such as an actual trie or an actual edge—it might suffice represent nodes and some pointers. 

We could implement it as simple as this:

```c
struct trie {
    char in_edge_label;
    int string_label;
    struct trie *sibling;
    struct trie *children;
};
```

Here, a trie is just a number of nodes connected together by linked list of siblings and a linked list of children. When you want to search along the children of a node, you start at the node pointed to by `children` and then follow then links of `siblings`. We can represent the root as a node that just has a list of children and simply never look at its edge label.

Depending on your programming language, there might be more natural ways to represent tries, but do not over-engineer it. Keep it simple.

Also, as a side note: if we only want to check for the existence of a string in the tree, we do not need to have string labels; it suffices with a boolean value that tells us if there are any strings that leads to a given node. That also alleviate the problem of having to deal with duplicate strings.

### Building the trie

You can take this approach to building a trie:

1. Have a function for creating an empty trie, or alternatively a trie consisting of a single string.
2. Have a function for inserting a string into an existing trie.

Obviously.

There is some merit in having a function for building a trie from a single string—whether you start with an empty trie or a single-string trie. If you have a function for searching down a trie until you either run out of trie or of string, then a construction algorithm can look like this:

1. Search for the node where you can’t go any longer.
2. If this is because you ran out of string, that means that this is where the string should be in the trie. Update the string label or string boolean to reflect that this string belong here.
3. If it is because you have run out of trie, then you have found the node where you should add a new child.
4. Build a trie from the suffix of the string that is left after the search, and insert that in the list of children.

### Searching in the trie

Obviously, step 1 and 2 in the algorithm above can be used for searching. 

1. If you search down the trie and run out of trie, the string is not there. 
2. If you run out of string but there is no string label at the node you reach, the string you are searching for is a prefix of a string in the trie, but the string itself is not actually there.
3. If there *is* a string label, then the string was in the trie.


