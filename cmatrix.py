import curses
import random
import time

def matrix_effect(screen):
    curses.curs_set(0)
    screen.nodelay(True)
    screen.timeout(100)
    
    columns = []

    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    while True:
        key = screen.getch()
        if key == 27:  
            break
        
        
        sh, sw = screen.getmaxyx()
        safe_height = sh - 1 
        safe_width = sw - 1  
        
        
        if len(columns) != safe_width + 1:
            columns = [0] * (safe_width + 1)
        
        screen.clear()
        
        for i in range(safe_width + 1):
            if columns[i] == 0:
                if random.randint(0, 1) == 0:
                    columns[i] = random.randint(1, safe_height)  
            
            if columns[i] > 0:
            
                if 0 <= columns[i] - 1 < safe_height:
                    screen.addstr(columns[i] - 1, i, " ", curses.color_pair(2))
                if 0 <= columns[i] < safe_height:
                    char = chr(random.choice(
                        list(range(48, 58)) +  
                        list(range(65, 91)) +  
                        list(range(97, 123))   
                    ))
                    screen.addstr(columns[i], i, char, curses.color_pair(1))
                columns[i] += 1
            
            if columns[i] >= safe_height:
                columns[i] = 0
        
        screen.refresh()
        time.sleep(0.05)

if __name__ == "__main__":
    curses.wrapper(matrix_effect)
