
import re

regex = r"[0-9][0-9]:[0-9][0-9](\n| (p|a)m | (p|a)\.m\.)?"

file = open("Output.txt", "r")
test_str = file.read()
file.close()

matches = re.finditer(regex, test_str)
output = ""

for matchNum, match in enumerate(matches):
	output += match.group() 
	output += "\n"
	
file = open("Regex.txt", "w")	
file.write(output)
file.close()
print(output)
    
