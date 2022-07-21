last_dx = None
last_dy = None
new_height = None
counter = 0


def new_heightL(paddle_frect, other_paddle_frect, ball_frect, table_size):
    global lastx, lasty, cur_x, cur_y, height, x_dist
    global counter, last_dx, last_dy
    global new_start_counter
    global new_height
    total_bounces = 0

    
    if counter == 0:
        lastx = 221
        lasty = 141
        counter += 1
    
    
    #radius of the ball
    radius = (ball_frect.size[1]/2)
    
    cur_x = ball_frect.pos[0] + (radius) #current x location of ball
    cur_y = ball_frect.pos[1] + (radius) #current y location of ball
    
    if cur_x - lastx != 0 and cur_y - lasty != 0:
        dx = cur_x - lastx
        dy = cur_y - lasty
        tan = dy/dx
        last_dx = dx
        last_dy = dy
        
    elif cur_y - lasty == 0:
        dx = last_dx
        dy = last_dy
        tan = dy/dx
    
    else:
        return cur_y
        
    if tan < 0.1 and tan > 0:
        tan  = 0.1
    elif tan > -0.1 and tan < 0:
        tan  = -0.1
    
    #tan is negative if going to upper right corner
    #tan is positive if going to lower right corner

    lastx = cur_x
    lasty = cur_y
    
    if dx < 0: #if ball is travelling to the left
        
        x_dist = cur_x - radius - 10
        
        height =  -1 * tan * x_dist
        
        
        if (cur_y - height) < 280 and (cur_y - height) > 0:
            return cur_y + height
        
        bounce = 0
        #while ball bounces
        while ((cur_y - height) > 280 or (cur_y - height) < 0) and bounce < 15:
            #the less than 20 is to prevent an infinite loop
            total_bounces +=1
                
            #when the ball bounces from the bottom
            if tan < 0:
                y_dist = 280 - cur_y
                
                deltax = -1*y_dist/tan 
                cur_x -= deltax
                cur_y = 280
                tan = -tan
                
                x_dist = cur_x - radius - 10
                height = -1*tan * x_dist
                bounce += 1
                
            elif tan > 0:                    
                y_dist = cur_y
                
                deltax = y_dist/tan
                cur_x -= deltax
                cur_y = 0
                tan = -tan
                
                x_dist = cur_x - radius - 10
                height = -1*tan * x_dist
                bounce += 1
                
        return cur_y - height
        
        
    else:
        return  140
        
        #((ball_frect.pos[1]+ball_frect.size[1]/2)+\
         #       (other_paddle_frect.pos[1]-other_paddle_frect.size[1]/2))/2
            
            
            
            
def new_heightR(paddle_frect, other_paddle_frect, ball_frect, table_size):
    global lastx, lasty, cur_x, cur_y, height, x_dist
    global counter, last_dx, last_dy
    global new_start_counter
    global new_height
    total_bounces = 0
    
    if counter == 0:
        lastx = 221
        lasty = 141
        counter += 1
        
    radius = (ball_frect.size[1]/2)
    
    cur_x = ball_frect.pos[0] - (radius)
    cur_y = ball_frect.pos[1] + (radius)
    
    if cur_x - lastx != 0 and cur_y - lasty != 0:
        dx = cur_x - lastx
        dy = cur_y - lasty
        tan = dy/dx
        last_dx = dx
        last_dy = dy
        
    elif cur_y - lasty == 0:
        dx = last_dx
        dy = last_dy
        tan = dy/dx
        
    else:
        
        return cur_y
        
    if tan < 0.1 and tan > 0:
        tan  = 0.1
    elif tan > -0.1 and tan < 0:
        tan  = -0.1
        
    lastx = cur_x
    lasty = cur_y
    
    if dx > 0:
        
        x_dist = 415 - cur_x 
        
        height = tan * x_dist
        
        if (cur_y + height) < 265 and (cur_y + height) > 0:
            
           
            return cur_y + height
            
            
        
        bounce = 0
            
        while ((cur_y + height) > 265 or (cur_y + height) < 15) and bounce < 50:
            #the less than 20 is to prevent an infinite loop
            total_bounces +=1
                
            #when the ball bounces from the bottom
            if tan < 0:
                y_dist = cur_y - radius
                
                deltax = -1*y_dist/tan 
                cur_x += deltax
                cur_y = 15
                tan = -tan
                
                x_dist = 415 - cur_x
                height = tan * x_dist
                bounce += 1
                
            elif tan > 0:                    
                y_dist = 265 - cur_y
                
                deltax = y_dist/tan
                cur_x += deltax
                cur_y = 265
                tan = -tan
                
                x_dist = 415 - cur_x 
                height = tan * x_dist
                bounce += 1
        
        print (height)

        
        if height < 0:
            return 265 + height
        else:
            return  height
        
        
    else:
        return  140           
            
            
            
            
            
            
            
            
                    

def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    global new_height
    
    aim_factor = ((table_size[0]-other_paddle_frect.pos[0])/(table_size[0])) + 20
    
    if paddle_frect.pos[0] >= (table_size[0]/2):
        final_height = new_heightR(paddle_frect, other_paddle_frect, ball_frect, table_size)
        
        if final_height != new_height:
            final_height, new_height = new_height, final_height
            
        
        
    else:
        final_height = new_heightL(paddle_frect, other_paddle_frect, ball_frect, table_size)
        if final_height != new_height:
            final_height, new_height = new_height, final_height
    

    
    
    if final_height > table_size[1]/2:
    
        if final_height < paddle_frect.pos[1]+paddle_frect.size[1]*2/3: 
            return "up"
        
        else:
            return "down"

    else:
        if final_height < paddle_frect.pos[1]+(paddle_frect.size[1])*2/3:
            return "up"
        
        else:
            return "down"
