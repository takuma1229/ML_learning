S = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
S = S.split()

num_list = []
for i in range(len(S)):
    num_list.append(len(S[i]))

print(num_list)
