vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

def count_vowels_consonants(tekst):
    count = {'vowels':0, 'consonants': 0}
    for i in tekst:
        if i.lower() in vowels.lower():
            count["vowels"]+=1
        elif i.lower() in consonants.lower():
            count["consonants"]+=1
    return count


tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(count_vowels_consonants(tekst))