# math_seq 1
a = 3
num1 = int(a)
num2 = int(a*a)
num3 = int(a*a*a)

print(num1 + num2 + num3)

# math_seq 2
import math

a, b = 4, 8
mean = (a + b) / 2
variance = (a - mean)**2 + (b - mean)**2
dev = math.sqrt(variance / 2)

print(dev)

# math_seq 3
point1 = [3, 0]
point2 = [6, 4]
distance = (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2

print(distance**0.5)

# math_seq 4
height = 5
weight = 100
bmi = weight / (height*height)

print(bmi)

# math_seq 5
num = 3432
new_num1 = num // 1000
new_num2 = (num - new_num1*1000)

print(new_num2)

# math_seq 6
(x1, y1) = (5, 3)
(x2, y2) = (7, 9)

mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2

print((mid_x, mid_y))

# math_seq 7
container = [11, 23, 35]
result = container[0] + container[-1]

print(result)

# math_seq 8
num_list = [5, 3, 8, 4, 9]

first_answer = max(num_list)
second_answer = min(num_list)

print(first_answer - second_answer)

# math_seq 9
adjacent = 12
hypo = 13
opposite = (hypo**2 - adjacent**2)**0.5

print(opposite)

# math_seq 10
num = 4
denom = 8

percent = num*100 / denom

print(str(percent) + '%')

# math_seq 11
adults = 15
ratio_ad_ch = 2.5
children = adults / ratio_ad_ch

print(children)

# math_seq 12
len_inch = 3
breadth_inch = 5
inch_to_ft = 3
result = len_inch*inch_to_ft*breadth_inch*inch_to_ft

print(result)

# math_seq 13
h_atoms = 2
o_atoms = 2
num_molecules = 12
total_atoms = num_molecules*(h_atoms + o_atoms)

print(total_atoms)

# math_seq 14
apples, pears, oranges = 5, 4, 2
num_pieces = apples*4 + pears*4 + oranges*8

print(num_pieces)

# math_seq 15
import math

number1, number2 = 4, 3
number1_small = math.sqrt(number1)
number2_big = number2**2

print(number1_small + number2_big)

# math_seq 16
to_div = 3
to_add = 5
to_sub = 10
num1 = 4
num2 = num1 + (to_add*5)
num2 -= to_sub
num1 = 1
num2 = (num2 - num1) / to_div

print(num2)

# math_seq 17
x, y = 2, 4
result1 = x**2 + y**2
result2 = (x + y)**2
total = result1 + result2

print(total)

# math_seq 18
a, b, c = 1, 3.5, 10
smooth = (a + c) // 2
diff = abs(smooth - b)

print(diff)

# math_for 1
group_data = [1, 5, 3]
num = 3

for value in group_data:
    product = num*value

print(product)

# math_for 2
numbers = [5, 7, 4, 8]
answers = []

for value in numbers:
    answers.append(value - 1)

print(answers)

# math_for 3
num = 5
sum_num = 0

for n in range(num + 1):
    sum_num += n

print(sum_num)

# math_for 4
nums = [10, 2, 30]
prod = 1

for n in nums:
    prod = prod*n

print(prod)

# math_for 5
num_list = [45, 60, 37]
cage = []

for num in num_list:
    cage.append(num % 15)

print(cage)

# math_for 6
num = [3, 7, 0, 1, 2, 2]
new_num = 1

for x in range(1, len(num), 2):
    new_num *= num[x]

print(new_num)

# math_for 7
nums = [3, 5, 8]
difference = 0

for num in nums:
    difference = num - difference

print(difference)

# math_for 8
n = 3
total = 0

for i in range(n, -1, -1):
    total += i*i*i

print(total)

# math_for 9
people = 12
families = people / 4
candy = 0

for family in range(int(families)):
    candy += 2

print(candy)

# math_for 10
constant = 1
number_terms = 3
r = 2
total = 0

for i in range(number_terms):
    total += constant*r**i

print(total)

# math_for 11
list1 = [4, 4, 6]
list2 = [1, 2, 4]
list3 = [3, 2, 1]

for i in range(len(list1)):
    list3[i] += list1[i] + list2[i]

print(list3)

# math_for 12
tuple_list = [(1, 2), (3, 4), (-1, 9)]
certain_sum = 0

for num_pair in tuple_list:
    certain_sum += num_pair[1]

print(certain_sum)

# math_for 13
num_list = [3, 1, 0, -2, 5]
total = 0

for index, num in enumerate(num_list):
    total += index*num

print(total)

# math_for 14
l = list()

for i in range(1, 4):
    l.append(i**2)

print(l[-2:])

# math_for 15
index_list = [1, 0, 2]
num_list = [1, 4, 6]
ans_list = []

for i in range(len(index_list)):
    ans_list.append(num_list[index_list[i]])

print(ans_list)

# math_for 16
numbers = [1, 2, -2, -8, 0]
stride = 2
result = []

for idx in range(0, len(numbers), stride):
    result.append(numbers[idx] - 1)

print(result)

# math_for 17
numbers = [4, 5, 3, 8, 3, 2, 5]
length = len(numbers)
answer = 0

for i in range(length // 2 + 1):
    answer += numbers[i]

print(answer)

# math_for 18
start = 3
total = 0

for i in range(start, -1, -1):
    total -= i*i
print(total)

# math_if 1
n = 1800

if abs(1000 - n) <= 100:
    print(1)
elif abs(2000 - n) <= 100:
    print(1)
else:
    print(0)

# math_if 2
x, y, z = 3, 3, 3
add = x + y + z

if x == y == z:
    add = add*3
print(add)

# math_if 3
num1, num2, num3 = 3, 2, 2

if num1 == num2 or num2 == num3 or num1 == num3:
    add = 0
else:
    add = num1 + num2 + num3
print(add)

# math_if 4
dollars1, dollars2 = 10, 6
dollar_sum = dollars1 + dollars2

if dollar_sum in range(15, 20):
    print(20)
else:
    print(dollar_sum)

# math_if 5
predicted = 13
actual = 11
error = 2

if (predicted - actual < error) or (predicted - actual > -1*error):
    print(predicted - actual + error)
else:
    print(predicted - actual - error)

# math_if 6
big_num, small_num = 64, 16

if big_num % small_num == 0:
    print(1)
else:
    print(0)

# math_if 7
mine, yours, hers = 5, 3, 2

if yours < mine and mine < hers:
    print(mine)

elif hers < mine and mine < yours:
    print(mine)

elif hers < yours and yours < mine:
    print(yours)

elif mine < yours and yours < hers:
    print(yours)

else:
    print(hers)

# math_if 8
year = 2018
if (year % 400 == 0):
    print("A")
elif (year % 100 == 0):
    print("B")
elif (year % 4 == 0):
    print("C")
else:
    print("D")

# math_if 9
dog_age = 12

if dog_age <= 2:
    human_age = dog_age*10.5
else:
    human_age = 21 + (dog_age - 2)*4

print(human_age)

# math_if 10
import math

num1, num2, num3 = 10, 12, 14

if math.sqrt(num1 + num2 + num3).is_integer():
    print(num1 + num2 + num3)
else:
    print(num2 + num3)

# math_if 11
entries = [123, 32, 43, 10, 0, -2, -59, 12, 0]

if entries[0] // 100 in entries:
    print(entries[0] // 100)
elif entries[0] % 100 in entries:
    print(entries[0] % 100)
elif entries[0] // 10 in entries:
    print(entries[0] // 10)

# math_if 12
player1, player2 = 10, 10

if player1 < 10:
    print("b")
elif player2 == 10:
    print("b")
elif player2 < 10:
    print("a")
elif player1 == 10 and player2 == 10:
    print("tie")

# math_if 13
list1 = [12, 34, 36, 71, 3, 42]
list2 = [53, 23, 16, 24, 5, 15]
list3 = [1, 34, 10, 91, 43, 26]
number = 34

if number in list1 or (number in list2 and number in list3):
    print(list1[0])
elif number in list2 or (number in list3 and number in list1):
    print(list2[0])
elif number in list3 or (number in list1 and number in list2):
    print(list3[0])

# math_if 14
predicted = 8
actual = 10
error = 3

if (predicted - actual < error) and (predicted - actual > -1*error):
    print(predicted - actual)
else:
    print(error)

# math_if 15
apples, oranges = 3, 8

if apples == oranges:
    print(apples + oranges)
elif abs(apples - oranges) == 5 or (apples + oranges) == 5:
    print(apples*oranges)
else:
    print(apples - oranges)

# math_if 16
temperature = 70
humidity = 100

if temperature >= 100:
    print("A")
elif temperature >= 92 and humidity > 75:
    print("B")
elif temperature > 88 and humidity >= 85:
    print("C")
elif temperature == 75 and humidity <= 65:
    print("D")
else:
    print("E")

# math_if 17
side1 = 12
side2 = 14
side3 = 124

if side1 == side2 and side2 == side3:
    print(1)
elif side1 == side2 or side2 == side3 or side1 == side3:
    print(2)
else:
    print(3)

# math_if 18
bears, dogs, wolves = 10, 4, 16

if (bears > dogs) and (bears > wolves):
    print(wolves)
elif (dogs > bears) and (dogs > wolves):
    print(bears)
elif (wolves > bears) and (wolves > dogs):
    print(dogs)

# str_seq 1
first_name = "Fernando"
last_name = "Federiko"

print(last_name + " " + first_name)

# str_seq 2
filename = "alphabet.java"
modified = filename.split(".")

print(modified[-1])

# str_seq 3
color_list = ["Red", "Green", "White", "Black"]

print((color_list[0], color_list[-1]))

# str_seq 4
mine = "red"
yours = "green"

temp = mine
mine = yours
yours = temp

print(mine, yours)

# str_seq 5
fruit = "banana"
result = fruit[-1:] + fruit[1:-1] + fruit[:1]

print(result)

# str_seq 6
tag = "i"
word = "MIT"
new_word = "<" + tag + ">" + word

print(new_word)

# str_seq 7
string1 = "onion"
new_string = string1[-2:]
multiplied = new_string*4

print(multiplied)

# str_seq 8
string1 = "WEEKEND"

print(string1[:4].lower() + string1[4:])

# str_seq 9
word = "python"
new_word = word[0].upper() + word[1:-1] + word[-2].upper()

print(new_word)

# str_seq 10
food_list = ["crab", "lettuce", "carrot"]
food_list[1] = food_list[2] + food_list[1]

print(len(food_list[1]))

# str_seq 11
word_one = "rap"
word_two = "hat"

word_three = len(word_two)*word_one + word_two

print(word_three)

# str_seq 12
basket = "groceries"
new_basket = basket[1:3]

print(new_basket[0])

# str_seq 13
drink_one = "wine"
drink_two = "beer"

mix = drink_one[:2] + drink_two + drink_one[:2]

print(mix)

# str_seq 14
rodent_one = "rat"
rodent_two = "mouse"

hybrid = rodent_one[1:] + rodent_two[3]*2

print(hybrid)

# str_seq 15
alpha = "star"
beta = alpha + alpha

print(beta[2:5])

# str_seq 16
returned = "wow"
returned = returned*2

print(returned[2:4])

# str_seq 17
code = "he.elk.set.to"
decode = code.split("e")

print(decode[-1])

# str_seq 18
word1 = "apple"
word2 = "orange"

word_created = word1 + word2
word_created += word1

print(word_created)

# str_for 1
pet = "cat"
n = len(pet)
result = ""

for i in range(n):
    result = result + pet

print(result)

# str_for 2
sentence = "red fox"
empty = ""

for char in sentence:
    empty = empty + char + "s"

print(empty)

# str_for 3
words_list = ["PHP", "Code", "Hack"]
word_len = ""

for n in words_list:
    word_len += str(len(n))

print(word_len)

# str_for 4
words_list = ["apple", "carrot", "orange"]

for word in words_list:
    new_word = ">" + word

print(new_word)

# str_for 5
puzzle = "crow"
word_bank = []

for i in range(len(puzzle) - 1):
    word_bank.append(puzzle[i] + puzzle[i + 1])

print(word_bank)

# str_for 6
word = "outer"
letters = "the"
classifier = []

for letter in letters:
    classifier.append(letter in word)

print(classifier)

# str_for 7
string1 = "humdrum"
string2 = ""

for index in range(2):
    char = string1[index]
    string2 += char*index

print(string2)

# str_for 8
code = "set"
answer = ""

for index in range(1, 3):
    answer = answer + code[index] + "ab"

print(answer)

# str_for 9
animal = "pigs"
new_word = ""

for char in range(len(animal) - 1, -1, -2):
    new_word += animal[char]

print(new_word)

# str_for 10
fruits = ["apple", "plum", "fig"]
count = 0

for fruit in fruits:
    count += len(fruit)

print(count)

# str_for 11
food = "cop"
storage = ""

for ind in range(len(food)):
    storage += food[ind]*ind

print(storage)

# str_for 12
plant = "clover"
seed = "seed"
new_seed = ""

for index in range(len(seed)):
    new_seed += plant[index]

print(new_seed)

# str_for 13
word = "hello"
open_string = ""

for char in word:
    open_string += char*2

print(open_string)

# str_for 14
letter = "q"
pronouns = ["I", "you"]

for index in range(len(pronouns)):
    pronouns[index] = pronouns[index] + letter

print(pronouns)

# str_for 15
word = "babyface"
outcome = ""

for number in range(2):
    outcome += word[-(number + 2)]

print(outcome)

# str_for 16
given = "sausage"
back = ""

for digit in range(3):
    back += given[2*digit]

print(back)

# str_for 17
piece1 = "gab"
piece2 = "cab"
answer = []

for ind in range(len(piece1)):
    answer.append(piece1[ind] == piece2[ind])

print(answer)

# str_for 18
classroom = ["An", "May", "John"]
class_list = ""

for name in classroom:
    class_list += name[1]

print(class_list)

# str_if 1
string = "Array"

if string[:2] == "ra":
    print(string)
else:
    print("ra" + string)

# str_if 2
old = "stuff"
threshold = 2

if len(old) < 2:
    threshold = len(old)

new = old[:threshold]

print(new)

# str_if 3
word = "characteristic"

if len(word) <= 6:
    print(word)
else:
    print(word[0:3])

# str_if 4
string = "resource"

if len(string) < 2:
    print("--")
else:
    print(string[0:2] + string[-2:])

# str_if 5
description = "interesting"

if description[-3:] == "ing":
    description += "ly"
else:
    description += "ing"

print(description)

# str_if 6
goal = "program"

if len(goal) <= 3:
    print(goal)
else:
    print(goal[:3])

# str_if 7
address = "https://www.mit.edu/bcs"

if address[0] == "h" and address[-1] == "/":
    print(address[1])
elif address[0] == "h":
    print(address[-1])
else:
    print(address)

# str_if 8
food = "popcorn"

if len(food) % 4 == 0:
    print(food)
else:
    print(food[-1::-1])

# str_if 9
word = "crybaby"
index = "crx"

if word[:len(index)] == index:
    print(1)
else:
    print("Nothing")

# str_if 10
general = "aardvark"
specific = general[:2]

if specific[0] == specific[1]:
    print(general)
else:
    print(specific)

# str_if 11
reply = ["hey", "me", "too"]

if len(reply[2]) < 2:
    reply = "ab"

print(reply)

# str_if 12
letters = ["a", "e", "t", "o", "u"]
word = "CreepyNuts"

if (word[1] in letters) and (word[6] in letters):
    print(0)
elif (word[1] in letters) or (word[6] in letters):
    print(1)
else:
    print(2)

# str_if 13
body_one = "eat"
body_two = "ear"

if (body_one[0] == body_two[0]) and (body_one[2] == body_two[2]):
    print(0)
elif (body_one[0] == body_two[0]) and (body_one[1] == body_two[1]):
    print(1)
else:
    print(2)

# str_if 14
sentence = "I am a"
word = "cat"

if len(word) > 3:
    print(word)
elif sentence[-1] == word[1]:
    print(sentence)
else:
    print(sentence + " " + word)

# str_if 15
name = "Gauss"
set1 = "art"
set2 = "science"

if name[1:3] in set1:
    print(1)
elif name[-1] in set2:
    print(2)
else:
    print(0)

# str_if 16
school = "middle"
sports = "football"

if school in sports:
    print(1)
elif len(school) > len(sports):
    print(2)
else:
    print(3)

# str_if 17
original = "coyote"
copy = original[3:6]

if len(copy)*2 > len(original):
    print(copy)
else:
    print(original)

# str_if 18
book = "anemone"

if (book[2] == book[-1]) and (book[1] == book[-3]):
    print(1)
elif book[2] == book[-1]:
    print(2)
else:
    print(3)
