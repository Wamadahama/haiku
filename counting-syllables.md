# Estimating Syllables

Counting the amount of syllables in a statement is tricky. English is a volatile language and defines a syllable as "uninterupted sound" which doesn't really give us to much to go on.

Short of having a word database with a syllable count, there is no 100% accurate way of determining the amount of syllables in a word. There are various English dialects that have different syllable counts of different words, and there are times where [english just doesn't make sense](https://www.youtube.com/watch?v=ZXa8cO9mXFk)

## Breaking down a syllable
The two basic structures to look at here are consonants and vowels.

There are two parts to a syllable:

### The Onset
This represents a consonant sound, which can be one or more consonants

### The Rime
This is further broken down into two portions, the nucleus and the optional coda

The nucleus is typically a vowel or a combination of vowels

The coda (which means tail in Latin) is another consonant sound.

An example 2 syllable word that has all three compontents is **essay**

ESSAY
ES-SAY
VC CVC

*Syllable 1:*
Nucleus : E
Onset   : S

*Syllable 2:*
Onset  :  S
Nucleus:  A
Coda   :  Y



---

## Breaking Down syllables

Using the 4 syllable word **ITERATOR** for example, could be broke down into the following syllable structure:

IT-ER-AT-OR
VCVCVCVC
VC VC VC VC

If we consider then separate syllables we not that each syllable consists of a onset ```c``` and a rime ```v```. With this information we can establish that getting a count of vowels is a good basis for estimating syllables. Essentially all we are doing is counting the amount of nuclei.


---

## List of Rules That Are Exceptions

### Contiguous Vowel Rule
Contiguous vowels are called dipthongs

Consider the following word:

**week** which is one syllable
CVVC
CV VC

If we count the amount of vowels in this then we will get two. Which is an improper guess for amount of syllables.

This applies to many words like

creek - CCVVC
bleak - CCVVC
beak  - CVVC
weak  - CVVC
wreak - CCVVC
coin  - CVVC

There is a pattern here. If there are contiguous vowels then they only count as one syllable because a nucleus can be a cluster of vowels.

There is an exception to this rule, when the word ends in *-ian* then the  i and the an should be considered separate syllables

Examples:
am-phib-i-an
bar-bar-i-an
au-thor-it-ar-i-an
in-di-an

---

### Silent Vowel Rule
Often time in English there are silent vowels at the end of a word.

For example: **Time**
TIME
CVCV

Using the above principle, this should have 2 syllables. But because the *e* in tim**e** is considered to be 'silent' and cannot be used to account for a syllable.

There is an exception to this, the tail **le** is accountable for a syllable.

For example: **particle**

PARTICLE
CVCCVCVC
CVCC VC VC

Here the VC structure at the end of the word accounts for a syllable, even though it is ending with e.

---

### Trailing es and ed rule
Both *es* and *ed* can be truncated from a word if the consonant sound before it is not 't', 'i', or 's'

For example **truncated** should not be replaced because if the -ted, but but the ed in raced should be truncated because c is not t,i,or s.

---

## Rules that need to be added
- tri/bi
- mc

# Programmatically getting a count of syllables

Using the above information we can write a method that can a syllable count of about %75-80 of English words.

## Algorithm psuedo code
```ruby
syllable_count = 0
syllable_count = count_vowels(word)

if word ends in "ian"
  syllable_count -= (contiguous_vowel_count(word) - 1)
else   
  syllable_count -= contiguous_vowel_count(word)
end

if word ends in "e" and doesnt end in "le"
  syllable_count -= 1   
end

if word ends in ed or es and word[-3] doesnt = t,i,or s
  syllable_count -= 1
end
```

This should be able to produce a semi-accurate count on how many syllables there are in a statement. There are still exceptions. Compound things like facebook, or treehouse will not work.

# Sources

http://eayd.in/?p=232
http://sitr.us/2007/09/24/anatomy-of-a-syllable.html
https://en.wikipedia.org/wiki/Syllable
https://en.wikipedia.org/wiki/Diphthong
