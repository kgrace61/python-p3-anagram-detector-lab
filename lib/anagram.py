class Anagram:
    
    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, possible_anagrams):
        sorted_word = sorted(self.word)
        
        matches =[]
        
        for candidate in possible_anagrams:
            if candidate != self.word and sorted(candidate) == sorted_word:
                matches.append(candidate)
        return matches
            
        
        
    
    #takes a list of possible anagrams
    #words in list have the same letters as word given
    #how do i iterate over the list of words to see if the letters match? use sorted function
    #if word matches a word in list, add to list "matches"
    #if matches exist, or if matches is bigger than an empty list, return it
    #if no matches, return empty list