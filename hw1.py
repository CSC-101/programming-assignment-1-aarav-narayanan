from typing import List

import data

# Write your functions for each part in the space below.

# Part 1
#Purpose to use the word and find the number of vowels within that string
#Input is the string and the output the count of vowels that is within the string
# Ex. input is "Hello World"  Output: 3
def vowel_count(x:str)->int:
    vowels="aeiouAEIOU"
    count=0
    for v in x: #For loop allows each character in the string to see if the letter is in vowels and then count will raise by one
        if v in vowels: #Check if the character is in the vowels string
            count +=1
    return count

# Part 2
#Purpose is to create a new list that contains sublists that have a length of two
#Input if the nested lists that have an integer number Ex. [[2,3],[6],[7],[4,5,6],[9,7]]
#output is the new list that has sublists with a length of 2. Ex. [[2,3],[9,7]]
def short_lists(x:list[list[int]])-> list[list[int]]:
    return[new_list for new_list in x if len(new_list)==2] #helps filter in the lists that have a length of 2 as stated with the if statement

# Part 3
#Purpose of the function is to sort of the sublists that have a length of 2 while the rest of the list stays the same
#Input is the list within a list like [[5,3],[6],[7,8,9]] and
# output is the list but with the sublists that have a length of 2 being sorted Ex. [[3,5],[6],[7,8,9]]
def ascending_pairs(x:list[list[int]])-> list[list[int]]:
    new_list=[] #Start off with an empty list
    for sublist in x: #Checks each index in the list and then goes into an if statement to see if each index has a length of two.
        if len(sublist)==2:
            new_list.append(sorted(sublist)) #sort function would help sort it from lowest to highest in the sublist and the new lis would also be appended either way
        else:
            new_list.append(sublist)
    return new_list
# Part 4
#Purpose of the function is to add up the cents and dollars together as well show any remaining cents left
#Input would the two prices with each price having dollars and cents like Price(2,15) and Price(3,25)
#Output would be the combined price that is within the object Price like Price(5,40)
def add_prices(price1: data.Price, price2:data.Price):
    cents=price1.cents+price2.cents  #Adds the two cents together
    dollars= price1.dollars+price2.dollars #Adds the two dollars section together
    dollars=dollars+cents//100 #adds dollars and cents but as an integer which would bring a rounded down answer
    cents=cents%100  #It will sow the remainder of the cents which would be helpful to classify the cents variable
    return data.Price(dollars,cents)

# Part 5
#Purpose to classify the coordinates to each variable and return the area of the rectangle
#Input would be the top_left and bottom_right coordinates using the Point class to give the coordinates
#an example would be Rectangle(top_left=Point(0,0),bottom_right(2,-4))
#Out put would be the area calculated using those points and it is given in absolute value to avoid negative numbers
def rectangle_area(rec:data.Rectangle)->float:
    x1 = rec.top_left.x #defining the coordinates to each variable
    y1 = rec.top_left.y
    x2 = rec.bottom_right.x
    y2 = rec.bottom_right.y
    base=x2-x1  #find the base by subtracting the x coordinates and the same goes for the height with the y coordinates
    height=y2-y1
    area=base*height
    return abs(area)

# Part 6
# Purpose is to give the title of the book that contain the author
#input would be the list like [Books([author1],"title1),Books([author2],"title2)]
#output would be the new list that gives the title of books that have a specific author
#and example would be looking for titles with author 1 and it gives ["title1"]
def books_by_author(author:str, title:list[data.Book])-> list[data.Book]:
    return [title.title for title in title if author in title.authors] #Filers out titles that don't have that author's name

# Part 7
#Purpose is to use the rectangle points to generate a circle
#Input would be the x and y coordinate points and the output would be the center and radius for the circle.
def circle_bound(rec:data.Rectangle)->data.Circle:
    center_x=(rec.top_left.x + rec.bottom_right.x)/2  #Uses the midpoint formula by using the x and y coordinates in top left or bottom right
    center_y =(rec.top_left.y + rec.bottom_right.y) / 2
    center=data.Point(center_x,center_y)
    x_corner=rec.top_left.x #Use the top left coordinates to get the distance formula
    y_corner =rec.top_left.y
    x_change = x_corner - center_x #Subtract between the two points for y and x and then square it
    x_squared = x_change ** 2
    y_change = y_corner - center_y
    y_squared = y_change ** 2
    add = x_squared + y_squared  #Add the two squared x and y and then take the square root of it.
    radius= add**0.5
    return data.Circle(center,radius)
# Part 8
#Purpose of this is to give a list of employees who are have a below average pay
# Input would be the list of employees' names and that also contains the pay rate Ex. [Employee(Name1,pay1), Employee(name1,pay2)]
#output would the names of the employees Ex. ["Name1]
def below_pay_average(employee:list[data.Employee])->list[str]:
    total=0
    for employees in employee: #adds up the total pay rate that employees get
        total=total+employees.pay_rate
    average=total/len(employee) #uses the total and divide it by the length of the list
    below_average=[]
    for employees in employee: #check for each index of which employee's pay rate is less than the average pay rate
        if employees.pay_rate<average: #Once it checks the below_average list will append the employees name
            below_average.append(employees.name)
    return below_average


