# pp 13
txt = ''' Eight dollars a week or a million a year - what is the difference? A mathematician or a wit would give you the wrong answer. The magi brought valuable gifts, but that was not among them. - The Gift of the Magi, O'Henry'''
word_lists = [[w.replace(',','') for w in line.split() if w not in ['-']] for line in txt.replace('?','.').split('.')]
print(word_lists)
