text = input().split()
new_str = ''
for ch in text:
    new_str += ch * len(ch)

print(''.join(new_str))
