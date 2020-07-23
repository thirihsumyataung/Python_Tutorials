#Write a program that asks the user to enter three test scores
#Program should display each test score
#as well as the average of the score

test1_score = input('Test1 Score : ')
test2_score = input('Test 2 Score: ')
test3_score = input('Test 3 Score: ')

avg = round((float(test1_score) + float(test2_score) + float(test3_score)) / 3.0, 2)
print('**************************')
print('Test 1 Score is :' + test1_score)
print('Test 2 Score is :' + test2_score)
print('Test 3 Score is :' + test3_score)
print('Average of the test score is : ' + str(avg))
print('**************************')

