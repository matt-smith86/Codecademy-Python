"""Ask the user to input a word in English.
Make sure the user entered a valid word.
Convert the word from English to Pig Latin.
Display the translation result."""

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print new_word
    new_word = word[1:len(word)] + first + pyg
    word = original.lower()
    first = word[0]
    pyg = 'ay'
else:
    print 'empty'
