count = 0
for i in range( 1, 10):
    if i % 2 == 0:
        print(i)
        count = count + 1

print(f'We have {count} even numbers.')