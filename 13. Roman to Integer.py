class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #create a key:value dictionary of roman numerals 
        map = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000}
                
        prev_char = 0 #declare a previous character variable with a value of 0
        total = 0 #declare a total variable with a value of 0
        
        for char in s[::-1]: #loop through each character in the input string, reversed [start:stop:step]
            if map[char] < prev_char: #if the current character's value is less than the previous character's value
                total -= map[char] #deduct the current character's value from the total 
            else: #otherwise
                total += map[char] #add the current character's value to the total
            prev_char = map[char] #assign the current character's value to the previous character variable
        return (total) #after looping through each character, return the sum