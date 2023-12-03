# Exercice 00 ------------------------------------------------------------------

kata0 = (19, 42, 21)
print('The three numbers are:', end=' ')
index = 0
for num in kata0:
    print(f"{num}", end='')
    if index < len(kata0) - 1:
        print(', ', end='')
    else:
        print('.')
    index += 1
print()

# Exercice 01 ------------------------------------------------------------------

kata1 = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for key, value in kata1.items():
    print(key, ' was created by ', value)
print()
# Exercice 02 ------------------------------------------------------------------

from datetime import datetime

kata2 = (2019, 9, 25, 3, 30)

date_time = datetime(*kata2)
formated_date = datetime.strftime(date_time, "%Y/%m/%d %H:%M")
print(formated_date)


# Exercice 03 ------------------------------------------------------------------

kata3 = "The right format"

len = len(kata3)
index = 0
while index < 42 - len - 1:
    print('-', end='')
    index += 1
print(kata3)
print()

# Exercice 04 ------------------------------------------------------------------

kata4 = (0, 4, 132.42222, 10000, 12345.67)

print(f"Module_0{kata4[0]}, ex_0{kata4[1]} : {kata4[2]:.2f}, {kata4[3]:.2e}, {kata4[4]:.2e}")