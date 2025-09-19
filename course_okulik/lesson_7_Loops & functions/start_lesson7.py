s = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'.split()
current_s = []
final_s = []
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        current_s.append(s[i])
        current_s.append(s[i+1])
print(current_s)


