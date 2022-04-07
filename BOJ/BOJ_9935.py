data = input().strip()
sub = input().strip()
st = []
n = len(sub)
for c in data:
    st.append(c)
    if len(st) >= n:
        if "".join(st[-n:]) == sub:
            del [st[-n:]]
if not st:
    print("FRULA")
else:
    print("".join(st))
