S = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
S = S.split()

num_li = [0, 4, 5, 6, 7, 8, 14, 15, 18]

dic = {}

for i in range(len(S)):
    if i in num_li:
        s = S[i][0]
        dic[s] = i
    else:
        s = S[i][0:2]
        dic[s] = i

print(dic)
