def findVowel(str):
    vowel="aeiouAEIOU"
    position=[]
    for index,char in enumerate(str):
        if char in vowel:
            position.append(index)
    return position if len(position)>0 else '-1'

str="h wrld"
print(findVowel(str))


def zigzac(str):
    if len(str)<3:
        return False

    for i in range(len(str)-2):
        a,b,c=str[i],str[i+1],str[i+2]
        if not ((a<b>c) or (a>b<c)):
            return False
    return True

str1=[1,3,2,4,4]
print(zigzac(str1))

def sum_of_squares(numbers):

    return sum(x ** 2 for x in numbers)

# Example usage
numbers = [1, 2, 3, 4, 5]
result = sum_of_squares(numbers)
print("The sum of squares is:", result)