Families={ 'charley':
           {'sam':
            {'boxy','rosy'},
             'nila':{'pepsi'}},
           'devi':
               {'Tommy':{'Tony'},
                'Timmy':{'Hamster'},
                'Tammy':{'Hamster'}},
            'carlos':
                {'Diego':'cat','ferret':'fox'}
           }
for parent,children in Families.items():
    print(f"{parent} has {len(children)} kid(s):")
    print(f"{',and '.join([str(child) for child in[*children]])}")