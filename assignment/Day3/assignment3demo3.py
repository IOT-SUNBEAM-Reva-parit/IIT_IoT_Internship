# Function to count vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


# Function to count consonants
def count_consonants(s):
    count = 0
    for ch in s:
        if ch.isalpha() and ch.lower() not in "aeiou":
            count += 1
    return count


# Function to calculate ratio
def vowel_consonant_ratio(s):
    v = count_vowels(s)
    c = count_consonants(s)

    if c == 0:
        return "Consonants count is zero, ratio not possible"
    return v / c


# Main program
string = input("Enter a string: ")

vowels = count_vowels(string)
consonants = count_consonants(string)
ratio = vowel_consonant_ratio(string)

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Ratio of vowels to consonants:", ratio)