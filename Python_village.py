#1: Installing Python
import this

#2: Variables and Some Arithmetic
a^2 * b^2 = c^2

if a = 2 and b =2:
    print(c)

a = 837
b = 799
d = a**2 + b**2
print(d)

#3: Strings and Lists
s = "19EpvvmklpvJdW9heZtPlhhCuElDzpfgrxGofbaxXwTOierdqyZ3R3mizu5okTisxq4S1i4atpdrKetupa6GhZAEAgIboA6rHW57jARiRkhb3NvbJ0o2nuhPcW3JL8GxkPXxVpw1yEHI77z6yIiwapegZaq3niVuZdF5uyhbcalvuspk."
a = 76
b = 81
c = 168
d = 173

print(s[a:b+1], s[c:d+1])

#4: Conditions and Loops

a = 4454
b = 8710

lst = []                # Way 1
total_sum = 0           # Way 2

for i in range(a, b):
    if i % 2 != 0:
        lst.append(i)
        total_sum += i
print(sum(lst))         # way 1
print(total_sum)        # way 2

# 5: Working with Files
#Assumes 1-based numbering: hence have to print odd number of line numbers
text = '''`Twas brillig, and the slithy toves
Some things in life are bad, they can really make you mad
  Did gyre and gimble in the wabe:
Other things just make you swear and curse
All mimsy were the borogoves,
When you're chewing on life's gristle, don't grumble give a whistle
  And the mome raths outgrabe.
This will help things turn out for the best
"Beware the Jabberwock, my son!
Always look on the bright side of life
  The jaws that bite, the claws that catch!
Always look on the right side of life
Beware the Jubjub bird, and shun
If life seems jolly rotten, there's something you've forgotten
  The frumious Bandersnatch!"
And that's to laugh and smile and dance and sing
He took his vorpal sword in hand:
When you're feeling in the dumps, don't be silly, chumps
  Long time the manxome foe he sought --
Just purse your lips and whistle, that's the thing
So rested he by the Tumtum tree,
So, always look on the bright side of death
  And stood awhile in thought.
Just before you draw your terminal breath
And, as in uffish thought he stood,
Life's a counterfeit and when you look at it
  The Jabberwock, with eyes of flame,
Life's a laugh and death's the joke, it's true
Came whiffling through the tulgey wood,
You see, it's all a show, keep them laughing as you go
  And burbled as it came!
Just remember the last laugh is on you
One, two! One, two! And through and through
Always look on the bright side of life
  The vorpal blade went snicker-snack!
And always look on the right side of life
He left it dead, and with its head
Always look on the bright side of life
  He went galumphing back.
And always look on the right side of life'''

lsttt = text.split('\n')

for i in range(len(lsttt)):
    if i % 2 != 0:              # if the remainder of i%2 is not 0 print i
        print(lsttt[i])
        #print(i)

# 6 - Dictionaries
text = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

text_to_list = text.split(' ')
#print(text_to_list)

count_dict = {}
count = 0

for i in text_to_list:
    if i not in count_dict:
        count_dict[i] = 0
#print(count_dict)
    if i in count_dict:
        count_dict[i] += 1
print(count_dict)

for k,v in count_dict.items():
    print(k,v)
