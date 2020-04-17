numberReferee = int(input())

scoreList = []

for i in range(numberReferee):
    scoreList.append(int(input()))

participantAverageScore = int((sum(scoreList) - (max(scoreList) + min(scoreList))) \
                              / (len(scoreList) - 2))

print(participantAverageScore)

