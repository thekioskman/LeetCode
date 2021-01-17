strs = ["ron","huh","gay","tow","moe","tie","who","ion","rep","bob","gte","lee","jay","may","wyo","bay","woe","lip","tit","apt","doe","hot","dis","fop","low","bop","apt","dun","ben","paw","ere","bad","ill","fla","mop","tut","sol","peg","pop","les"]


#hashing accounting for repated characters hashing with primes creates unique numbers regardless of length, of order. Its actually crazy 
string_val = {}
string_val["a"] = 2
string_val["b"] = 3
string_val["c"] = 5
string_val["d"] = 7
string_val["e"] = 11
string_val["f"] = 13
string_val["g"] = 17
string_val["h"] = 19
string_val["i"] = 23
string_val["j"] = 29
string_val["k"] = 31
string_val["l"] = 37
string_val["m"] = 41
string_val["n"] = 43
string_val["o"] = 47
string_val["p"] = 53
string_val["q"] = 59
string_val["r"] = 61
string_val["s"] = 67
string_val["t"] = 71
string_val["u"] = 73 
string_val["v"] = 79
string_val["w"] = 83
string_val["x"] = 89
string_val["y"] = 97
string_val["z"] = 101

output = {}

total = 1
for string in strs:
  for letter in string:
    total *= string_val[letter]
  
  #str_total = str(len(string)) +str(total)
  
  
  
  if total in output:
    output[total].append(string)
  else:
    output[total] = [string]

  total = 1


return_list = list(output.values())

print(output)
print( return_list)
