def draw_star():
    print('*',end='')

def draw_space():
    print(' ',end='')

def draw_middle(n):
    if 3==n:
        draw_star()
        draw_space()
        draw_star()
    else:
        draw_middle(n//3)
        draw_middle(n//3)
        draw_middle(n//3)
        print()
    
def draw_line(n):
    if 3==n:
        draw_star()
        draw_star()
        draw_star()
    else:
        draw_line(n//3)
        draw_line(n//3)
        draw_line(n//3)
        print()
    
N=int(input())
draw_line(N)
draw_middle(N)
draw_line(N)
