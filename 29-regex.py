import re 

txt = "My full name is Dondrey Taylor"
x = re.search("^My.*Taylor$", txt)
print(x)