import re
final_sum = 0.0
with open('sample1.txt') as f:
    lines = f.readlines()
    for line in lines :
      output = re.findall("[0-9]+",line)
      for op in output :
        final_sum += float(op)
print (final_sum)
    
