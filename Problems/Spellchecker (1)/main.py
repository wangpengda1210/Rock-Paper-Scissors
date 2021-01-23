dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

words = input().split(" ")
all_correct = True

for word in words:
    if word not in dictionary:
        print(word)
        all_correct = False

if all_correct:
    print("OK")
