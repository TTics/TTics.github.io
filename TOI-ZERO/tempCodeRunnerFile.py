red_slope = red_bounce[i+1] - red_bounce[i]
    if red_bounce[i] < blue_bounce[i] and red_slope > blue_slope:
        bounce_count +=1
        red_slope = 0
    if red_bounce[i] > blue_bounce[i] and red_slope < blue_slope:
        bounce_count +=1
        blue_slope = 0