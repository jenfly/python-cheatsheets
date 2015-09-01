def visit(animals, name):
    print('Welcome to the zoo, ' + name + '! We have: ')
    for key in animals:
        print('  %d %s' % (animals[key], key))

animals = {'zebras': 5, 'elephants': 4, 'penguins': 10}
name = 'Jennifer'
visit(animals, name)
