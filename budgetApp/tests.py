from django.test import TestCase

# Create your tests here.
import datetime
months = [i for i in range(1, 13)]
print(months)

months_choices = []

for m in months:
    d = datetime.date(2022, m, 1)
    pair = (m, d.strftime("%B"))
    months_choices.append(pair)



print(months_choices)