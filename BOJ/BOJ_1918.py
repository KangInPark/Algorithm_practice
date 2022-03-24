grade = {"(": 0, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2}

s = input()
st = []
answer = ""
for c in s:
    if c not in grade:
        answer += c
    else:
        if not st:
            st.append(c)
        elif c == "(":
            st.append(c)
        elif c == ")":
            while st:
                tmp = st.pop()
                if tmp == "(":
                    break
                answer += tmp
        else:
            if grade[c] > grade[st[-1]]:
                st.append(c)
            else:
                chk = grade[c]
                while st:
                    if grade[st[-1]] < chk:
                        break
                    answer += st.pop()
                st.append(c)
while st:
    answer += st.pop()
print(answer)
