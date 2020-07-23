numbers = [ 7, 5, 3, 2 , 1]
for x_count in numbers:
    output = ''
    for count in range(x_count): # zero up to x_count , first is 5
        output += 'x'
    print(output)
    #print('x' * x_count)
