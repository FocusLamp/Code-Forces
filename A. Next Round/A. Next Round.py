participants_and_minimum_score = list(map(int, input().split()))

participants = list(map(int, input().split()))

number_of_participants = participants_and_minimum_score[0]
minimum_score = participants_and_minimum_score[1]

score_limit_position = participants[minimum_score - 1]

advancers = 0

for participant in participants:
    if participant > 0 and participant >= score_limit_position:
        advancers += 1

print(advancers)