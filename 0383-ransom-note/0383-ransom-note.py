class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Create a dictionary to keep number of characters count.
        dictionary = {}

        # Iterate through magazine to count number of available characters and 
        # store them in the dictionary.
        for char in magazine:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1

        # Iterate through the ransomNote to see what characters are needed and
        # update dictionary number of characters available.
        for char in ransomNote:
            if char in dictionary and dictionary[char] > 0:
                dictionary[char] -= 1
            else:
                return False
        
        return True


        