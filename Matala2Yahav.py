## Yahav Shalom
## 207650052

#QA1
def reverse(sentence=None, reverse_word=None):
    if type(sentence) != str or type(reverse_word) != str:
        return "invalid input"
    if reverse_word not in sentence:
        return "The word was not found"
    else:
        new_word = reverse_word[::-1]
        newsentence = sentence.replace(reverse_word, new_word, 1)
        return str(newsentence)
        