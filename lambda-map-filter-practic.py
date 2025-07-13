#1.Square List: Write one line with map+lambda that converts[2,4,6,8] to[4,16,36,64]
print(list(map(lambda a:a**2,range(2,9,2))))

# 2. Add 3 to every number in the list [5, 0, 12] using map.
ans = list(map(lambda a:a+3,[5,0,12]))
print(ans)

# 3. Filter out negative numbers from [-4, 7, 0, -1, 9] using filter.
positive = list(filter(lambda a:a>=0,[-4,7,0,-1,9]))
print("positive no list: ",positive)

#4. Capitalize the first letter of each name in list using map.
name = ["riya", "PARUL", "neha"]
print("capitslize list :", list(map(lambda a:a.capitalize(),name)))

#5. Keep only the numbers divisible by 3 from range(1, 20) using filter.
print(list(filter(lambda a:a%3==0,range(1,20))))

#6 Double only even numbers, keep odd numbers as-is from [1, 2, 3, 4] using map + lambda.
def even_odd(i):
    if i % 2==0:
        return i*2
    else:
        return i

l = [1, 2, 3, 4]
res = list(map(even_odd,l))
print(res)

#7.Get the length of each word in ["apple", "banana", "kiwi"] using map.
res = list(map(lambda fruits:len(fruits),["apple", "banana", "kiwi"]))
print("length of each word:",res)

#8.Filter out only palindromes from ["level", "python", "radar", "data"]
res = list(filter(lambda name:name[::-1]==name,["level", "python", "radar", "data"]))
print("palindromes are:",res)

#9. From marks [32, 55, 67, 28, 90], filter marks >= 40, then square them.
marks =  [32, 55, 67, 28, 90]
result = list(filter(lambda a:a>=40,marks))
print("marks greater equal to 40 :",result)

# 10.From two lists (months, days), filter out months that have 31 days.
months = ["Jan", "Feb", "Mar", "Apr"]
days = [31, 28, 31, 30]
result = list(filter(lambda month:month[1] == 31,zip(months,days)))
print(result)

#11.Square all odd numbers from 1–15 and filter those whose square is less than 100.
squ = list(filter(lambda a:a%2 != 0 if a**2 < 100 else None ,range(1,16)))
resu = list(map(lambda a:a**2,squ))
print("squares of odd no > 100:",resu)

#12 Remove all vowels from the string "DataScience" using filter.
str = "DataScience"
res = ''.join(filter(lambda char:char not in "aioue",str )) # join combine all the char of the string into the empty string''
print("string after removing vowel:",res)

#13. Convert dictionary keys to uppercase: {"a":1, "b":2} → [("A", 1), ("B", 2)]
# Use map with dict.items()

#14.Cube all numbers from [1,2,3,4,5], filter even cubes, and sum them.
l1 = [1,2,3,4,5,]
cube = list(map(lambda a:a**3,l1))
# to filter even cubes
even_cubes = list(filter(lambda a:a%2 ==0,cube))
print(res)
# to sum all the cube
total = sum(even_cubes)
print("list of even cubes :",even_cubes)
print("sum of even cubes :",total)

#15.Find common elements from list1=[1,2,3] and list2=[3,4,1] using filter.
list1 = [1,2,3]
list2=[3,4,1]
common = list(filter(lambda a:a in list1,list2))
print(common)

#16.From a list of (city, temp) tuples, return names of cities with temp > 30.
l =  [("Delhi", 35), ("Pune", 29), ("Chennai", 33)]
temp = list(filter(lambda a:a[1]>30,l))
city = list(map(lambda a:a[0],temp))
print("city names whoes temp > 30:",city)

#17 Remove empty strings and whitespace-only strings from [" hello ", " ", "world", "", "python "]
l = [" hello ", " ", "world", "", "python "]
res = list(filter(lambda a:a.strip() ,l),)
print(list(map(lambda a:a.strip(),res)))

#18From numbers 2–50, filter out only prime numbers using filter and a lambda with is_prime logic.
#19. From a sentence, get lengths of all words and return the maximum length.
sen = "Python is super powerful"
l = sen.split()
leng = list(map(lambda a:len(a),l))
print("the length of each word:",leng)
print("maximum length:",max(leng))

#20. Sort digits of each number in descending order in the list
