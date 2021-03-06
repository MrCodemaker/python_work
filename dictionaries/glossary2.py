glossarys = {
'concatenation':
'is the operation of gluing objects of a linear structure, usually strings.',
'interpreter':
'is a program or a technical tool that interprets.',
'floating-point number':
'is the formulaic representation that approximates a real number' +
'so as to support a trade-off between range and precision.',
'variable':
'a memory address that is otherwise addressable,' +
'the address of which can be used to access the data.',
'list':
'this is an abstract data type representing an ordered' +
'set of values in which some value can occur more than once.',
}

for term, definition in glossarys.items():
    print("\nBelow are 5 terms and their definitions")
    print(term.title() + " " + definition())
