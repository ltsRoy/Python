def combine_dicts():
    a = {'a':25,'b':72,'c':281,'d':18}
    b = {'a':21,'b':92,'j':628,'c':271,'d':82,'e':62}
    
    combined_dict = {}

    for key in a:
        if key in b:
            combined_dict[key] = a[key] + b[key]
        else:
            combined_dict[key] = a[key]

    
    for key in b:
        if key not in a:
            combined_dict[key] = b[key]
    print (combined_dict)

combine_dicts()