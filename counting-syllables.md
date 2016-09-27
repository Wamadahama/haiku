# Estimating Syllables

Counting the amount of syllables in a statement is tricky. English is a volatile language and it doesn't have any rules and defines a syllable as "uninterupted sound".

## Background information
The two basic structures to look at here are consonants and vowels.

There are two parts to a syllable:

- Onset
- Rime
Consists of two parts -- The nucleus and the coda

The Onset has to be a consonant sound and the Rime is typically a vowel.

So for example we have the word

**ITERATOR** which is **four** syllables

to break this down to its consonant and vowel sounds it would be

VCVCVCVC

Now to split this on the Onset and Rime

VC VC VC VC

Getting a count of these results in four.

We note that each syllable consists of an onset ```c``` and a rime ```v```. With this information we can establish that getting a count of vowels is a good basis for estimating syllables.

There are a few exceptions however.

For example consider the following work

**week** which is one syllable
CVVC
CV VC

If we count the amount of vowels in this then we will get two. Which is an improper guess for amount of syllables.

This applies to many words like

creek - CCV VC
bleak - CCV VC
beak  - CV VC
weak  - CV VC
wreak - CCV VC

There is a pattern here.

If there are contiguous vowels then they only count as one syllable.

## Programmatically getting a count of syllables

This method is not 100% accurate but comes close aside from a couple base cases.
