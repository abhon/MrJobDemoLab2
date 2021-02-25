  
#! /usr/bin/env python

from mrjob.job import MRJob

class MRCommonFriends(MRJob):
    """
    A class to find common friends between two friends
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
                each single line from csv with the individual, followed by all of their friends
                (e.g.: A,C D G Z)
            Yields:
                (key, value) pairs of the form where key is the friend combination and value is the 
                all the friends of the individual.
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
        This function changes both friend groups to sets and takes the interestion
        of the two groups
        
        Parameters:
            friend_combination: tuple
                tuple consisting of the sorted order of a friend combination
            friends: list
                list containing sets of the two friend groups
            Yields:
                friend_combination
                    tuple consisting of the sorted order of a friend combination
                common_friends: interesection of the two friend groups
                    
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