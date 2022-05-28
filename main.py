# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

def find_anagrams(word, word2):
    # Sort the inputed Strings
    sorted_str1 = sorted(word)
    sorted_str2 = sorted(word2)

    if len(sorted_str1) == len(sorted_str2):
        if sorted_str1 == sorted_str2:
            return True
        else :
            return False
    else :
        return False

result = find_anagrams(input("enter word\n"), input("enter word\n"))

print(result)