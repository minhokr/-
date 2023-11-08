partyA = set(["park", 'kim', 'lee'])
partyB = set(["park", 'choi',])

print('2개의 파이에 무도 찹석한 사람은 다음과 같습니다.')
print(partyA.intersection(partyB))
print(partyA.union(partyB))
print(partyA.symmetric_difference(partyB))
print(partyA.difference(partyB))
