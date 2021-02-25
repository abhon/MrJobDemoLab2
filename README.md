# MrJobDemoLab2
This demo shows how to find common friends between two individuals using Map-Reduce and MRJob. Data is given in the Friends.csv file, and is in the format:

|Individual|Friend|
|----------|------|
| A | B D E |
| B | A D|
| D | A B|
| E | A |

To find common friends, our **mapper** should produce **keys** that are combination of and individual and a friend, and the **value** for each key is the individual's friends. Note that we would like our keys to be tuples in sorted alphabetical order, so the reducer can combine the output of each key, as 
(A,B) is different from (B,A). For our example above, the mapper would then generate the following key value pairs:

|Key|Value|
|----------|------|
| (A,B) | [B D E] |
| (A,D) | [B D E]|
| (A,E) | [B D E]|
|----------|------|
| (A,B) | [A D] |
| (B,D) | [A D] |
|----------|------|
| (A,D) | [A B] |
| (B,D) | [A B] |
|----------|------|
| (A,E) | [A] |
|----------|------|

Once we have all the keys, the reducer takes all values associated with key, and we then take the **interesection** between the two sets. For example, let's take key (A,B). This key has values [[B, D, E],[A ,D]]. Taking the intersection of these two sets results in the following output on the map-reduce job:

(A,B)     [D]

Looking above at our original table, individuals A and B only have friend D in common, so this is correct. In order to run the job locally, go to the `\src` file and run `python MrJob_CommonFriends.py ../Friends.csv`