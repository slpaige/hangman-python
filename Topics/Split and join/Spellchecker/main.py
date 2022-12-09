dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

words = input().split(" ")

not_correct = 0

for word in words:
    if word not in dictionary:
        not_correct += 1
        print(word)

if not_correct == 0:
    print("OK")
