print 'Blake Anneberg Homework Chapter 2'

print "Exerciese 3.1"
#repeat_lyrics() #NameError: name 'repeat_lyrics' is not defined


print "Exerciese 3.2"

#Traceback (most recent call last):
#  File "/Users/banneberg/chapter3_exercises.py", line 15, in <module>
#    repeat_lyrics()
#  File "/Users/banneberg/chapter3_exercises.py", line 12, in repeat_lyrics
#    print_lyrics()
#NameError: global name 'print_lyrics' is not defined


print "Exerciese 3.3"
right_justify ='                                                                 allen'
print len('                                                                 allen')
print right_justify

print "Exerciese 3.4" #had to look up how to do this, was kinda confusing...

def do_twice(f, arg):
	f(arg)
	f(arg)

def print_twice(arg):
    print arg
    print arg

do_twice(print_twice, 'spam')
print ''

def do_four(f, arg):
	do_twice(f, arg)
	do_twice(f, arg)

do_four(print_twice, 'spam')
print ''