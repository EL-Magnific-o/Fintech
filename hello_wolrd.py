# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello khalid!" with the name in a variable
name = "khalid"
print("Hello", name,'!')	# with a comma
print("Hello "+ name+'!')	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 47
print(f"Hello {name}!")	# with a comma
print(f"Hello"+{name}+"!")
pass	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "cookie"
fave_food2 = "chocolate"
print("I love to eat {} and {} ".format(fave_food1,fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string
<div class="open_grepper_editor" title="Edit & Save To Grepper"></div><div class="open_grepper_editor" title="Edit & Save To Grepper"></div>