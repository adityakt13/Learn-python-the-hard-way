x = "There are %d types of people." % 10 # %d is used for displaying digit
binary = "binary" 
do_not = "don't"
y = "Those who know % s and those who %s ." %(binary,do_not) # %s is used for displaying string

print(x)
print(y)

print("I said: %r."%x) # %r is used for displaying string as it is i.e with quotes and in raw form
print("I also said: %s."%y) # %s gives us the string we have put inside 

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation %hilarious)

v = "This is the left side.."
w = "This is the right side."

print(v+w)