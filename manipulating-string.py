# Objective: make a program that reads a sentence and displays:
# - How many times does the letter 'a' appear
# - In What position does it first appear
# - In what position does she last appear

text = input(str('Write something: ')).upper().strip()
a = text.count('A')
first_a = text.find('A')+1
last_a = text.rfind('A')+1
print('The letter "A" appears {} times in the sentence.\nThe first letter appeared at position {}.\nAnd the last letter appeared at position {}. '.format(a, first_a, last_a))
