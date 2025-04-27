count = [int(i) for i in input().split()]
red_bounce = [int(i) for i in input().split()]
blue_bounce = [int(i) for i in input().split()]
red_slope = 0
blue_slope = 0
red_up_space = 0
blue_up_space = 0
red_down_space = 0
blue_down_space = 0
red_up = True
blue_up = True
score = 0
def spacecount(start, end):
    space = end - start
    return(start, space)

def countcount(start, space, anothercolorstart, anothercolorspace, time):
    global red_up, blue_up  # Use global variables for red_up and blue_up
    bounce_count = 0  # Initialize bounce_count
    if time % 2 == 0:
        red_up = True
        blue_up = False
    elif time % 2 == 1:
        red_up = False
        blue_up = True
    if anothercolorstart < space + start and anothercolorstart + anothercolorspace > start and ((blue_up == False and red_up == True) or (red_up == False and blue_up == True)):
        bounce_count += 1
    if ((blue_up == True and red_up == True) or (blue_up == False and red_up == False)) and start < anothercolorstart and space > anothercolorspace:
        bounce_count +=1
    if ((blue_up == True and red_up == True) or (blue_up == False and red_up == False)) and start < anothercolorstart and space > anothercolorspace:
        bounce_count += 1
    return(bounce_count)

for i in range(min(count[0], count[1]) - 1):  # Prevent index out-of-range errors
    red_start, red_space = spacecount(red_bounce[i], red_bounce[i+1])
    blue_start, blue_space = spacecount(blue_bounce[i], blue_bounce[i+1])
    score += countcount(red_start, red_space, blue_start, blue_space, i)
    for i in range(max(count[0], count[1])):
       score += countcount(red_bounce[i], spacecount(red_bounce[i], red_bounce[i+1]), blue_bounce[i], spacecount(blue_bounce[i], blue_bounce[i+1]), i)
       print(score)