a = 2 * 2
b = 3 * 4

print(a + b)


a = 3
a = "sky"
print(a)

dollars_per_hour = 50
hours_worked = 40
total_dollars = dollars_per_hour * hours_worked
print(total_dollars)

mya = "hisbjvs"
type(mya)


print(type(mya))



a = 101     # Changing this makes the next branc not execute

if a == 100:
	print("100 is my favorite number!")
print(a)



a = 100
if a == 100: print("huwhfohwe")


## Exercise: if statements

## Notice Needed

s = "HJH"
if len(s) > 12:
	print("long")
elif len(s) < 8:
	print("short")
else:
	print("Medium")
	
	

## Lists
	
my_numbers_and_sth = [1, 2, 3, "test"]
print(my_numbers_and_sth)

print(my_numbers_and_sth[3]) # the result will be 'test'

## Assign values to a specific list

my_numbers_and_sth[0] = 37942
print(my_numbers_and_sth)

my_list_of_lists = [[3, 2, 1], [4, 5, 6]]

print(my_list_of_lists[0][2]) # This will be the third items of the first list


my_numbers = [0, 5, 10, 15]
my_total = 0
for number in my_numbers: # number is 0, then 5, then 10, then 15
	print(number)
	my_total += number # +=: shorthand for my_total = my_total + number
print("Average: " + str(my_total / len(my_numbers)))

my_grades = [4, 3, 2, 3, 4]
letter_grades = []
for g in my_grades:
	if g == 4:
		letter_grades.append('A')
	elif g == 3:
		letter_grades.append('B')
	elif g == 2:
		letter_grades.append('C')
print(letter_grades)



my_movies = [("No", 4), ("Rogue One", 4.5), ("Casablanca", 5), ("The Great Escape", 3), ("Cats", 1)]

good_movies = []
for movie, stars in my_movies:
	if stars >= 4:
		good_movies.append((movie, stars))
print(good_movies)

days_per_month = {'January': 31, 'February': 28, 'March': 31}

for month, days in days_per_month.items():
	print(f'{month} has {days} days')

txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(', ')

print(x)

	