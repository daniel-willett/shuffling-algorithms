# Shuffling Algorithms

Recently I thought about coding up a boardgame I played and came to the realisation that I needed a way to 'shuffle' the cards used in the game. Further to this, I thought about what to do if I wanted some kind of 'uneven' shuffle where certain cards gain probabilistic weighting.

As far as I can tell, not much research appears to have been done into this area of Maths/Computer Science. We have "Fisher–Yates shuffle", which to be fair is a very good algorithm. But I'm interested in seeing what other algorithms do as well as if I want to weight certain cards.

## The idea

We take a set of `1-52` meant to represent the 52 cards in a playing deck. Then we shuffle (from the sorted state) and record it into `results.csv`. From that we take inspiration from this [blog post](https://bost.ocks.org/mike/algorithms/#shuffling) and make the colour maps.

For each card `i` in `1-52` we count how many times it appeared in position `j` in `1-52`. For `n` many shuffles we should see `count(i,j)/n ~ 1/52` (I think)

## The code

The shuffling is done in Go and stored to a CSV file. This is because Go is fast and we can leaverage Goroutines to do millions of shuffles very quickly.

Then we use Pandas (and possibly NumPy) in Python to read the CSV and produce the data.
