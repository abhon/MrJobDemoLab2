  
#! /usr/bin/env python

from mrjob.job import MRJob
import string

class MRCommonFriends(MRJob):
    """
    A class to count word frequency in an input file.
    """

    def mapper(self, _, line):
        """
        This is a mapper function: it finds words in each line of input,
        and yields (key, value) pairs of the form (word, 1), so that the
        reducer can sum the number of words later.
        
        Parameters:
            -: None
                A value parsed from input and by default it is None because the input is just raw text.
                We do not need to use this parameter.
            line: str
                each single line a file with newline stripped
            Yields:
                (key, value) pairs of the form where key is word and value is 1
        """
        my_network = line.split(sep = ',')
        my_friends = my_network[1].split(sep = ' ')
        for i in my_friends:
            key = tuple(sorted((my_network[0], i)))

            yield (key, my_friends)

    def reducer(self, friend_combination, friends):
        """
        The reducer takes (key, list(values)) as input, and returns a single
        (key, result) pair. This is specific to `mrjob`, and isn't usually
        required by Hadoop.
        This function just runs a sum across the list of the values (which are
        all 1), returning the word as the key and the number of occurrences
        as the value.
        
        Parameters:
            friend_combination: tuple
                tuple consisting of the sorted order of a friend combination
            counts: list
                list containing sets of the two friend groups
            Yields:
                friend_combination
                    tuple consisting of the sorted order of a friend combination
                common_friends: set
                    
        """
        friend_group = [set(i) for i in list(friends)]

        common_friends = friend_group[0].intersection(friend_group[1])
        
        yield (friend_combination, common_friends)


# this '__name__' == '__main__' clause is required: without it, `mrjob` will
# fail. The reason for this is because `mrjob` imports this exact same file
# several times to run the map-reduce job, and if we didn't have this
# if-clause, we'd be recursively requesting new map-reduce jobs.
if __name__ == '__main__':
    # this is how we call a Map-Reduce job in `mrjob`:
    MRCommonFriends.run()