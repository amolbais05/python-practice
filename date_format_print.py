import datetime

my_date = datetime.datetime(2019, 10, 2, 13, 46, 56)
print(my_date)

#October 02, 2019

sentence='{:%B %d, %Y}'.format(my_date)
print(sentence)

#October 02, 2019 fell on Wednesday and was 275 day of the year

sentence1='{0:%B %d, %Y} fell on {0:%A} and was {0:%j} day of the year'.format(my_date)
print(sentence1)