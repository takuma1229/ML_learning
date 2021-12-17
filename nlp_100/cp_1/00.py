S = "stressed"

ans = []

for i in range(len(S)):
    ans.append(S[len(S)-i-1])

print("".join(ans))
