s = "pwwkew"

if not(s):
  print(0)

seen = {}
sub_list = [0 for x in range(len(s))]
sub_list[0] = 1
seen[s[0]] = 1


for i in range(1,len(s)):
  if s[i] in seen:
    if (i+1) - seen[s[i]] <= sub_list[i-1]:
      sub_list[i] = i+1 - seen[s[i]]
    else:
      sub_list[i] = sub_list[i-1] +1
    
    seen[s[i]] = i+1
  else:
    sub_list[i] = sub_list[i-1] + 1
    seen[s[i]] = i+1


print(sub_list)
