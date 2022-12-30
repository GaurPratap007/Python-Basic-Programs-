#Formatting using .format() method
print('This is a string {}'.format("INSERTED"))
#Using indexing while formatting
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
#using keyword as variable names while formatting
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

#Float formatting i.e varying precision and width
result = 1000/7777
print("The result without formatting is", result)
print("The result with formatting {r:1.2f}".format(r=result))
#The f strings method
name = "Gaurav"
print(f'Hello, my name is {name}')
