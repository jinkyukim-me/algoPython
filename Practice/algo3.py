score = list(map(int, input().split()))

maxScore = max(score)
minScore = min(score)

averageScore = int(sum(score) - (maxScore + minScore)) / (len(score) - 2)

finalScore = int(maxScore + minScore + averageScore)

print(int(finalScore))


