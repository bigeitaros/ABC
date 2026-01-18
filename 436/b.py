N = int(input())
grid = [[0 for i in range(N)] for j in range(N)]

grid[0][(N-1)// 2] = 1
previous_write_pos_x = 0
previous_write_pos_y = (N-1)//2
previous_write_num = 1
for i in range(N**2 - 1):
    if(grid[(previous_write_pos_x - 1) % N][(previous_write_pos_y+1) % N] == 0):
        grid[(previous_write_pos_x - 1) % N][(previous_write_pos_y+1) % N] = previous_write_num + 1
        previous_write_num = previous_write_num + 1
        previous_write_pos_x = (previous_write_pos_x - 1) % N
        previous_write_pos_y = (previous_write_pos_y + 1) % N
    else: 
        grid[(previous_write_pos_x + 1) % N][previous_write_pos_y] = previous_write_num + 1
        previous_write_num = previous_write_num + 1
        previous_write_pos_x = (previous_write_pos_x + 1) % N
        previous_write_pos_y = previous_write_pos_y


for i in grid:
    print(*i)