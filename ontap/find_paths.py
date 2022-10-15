def read_inputs(file_name):
    # Open the input file
    f = open(file_name, 'r')

    # Read the first line to get N
    N = int(f.readline())

    C = []
    for i in range(N):
        row = f.readline().split()
        C.append(row)

    f.close()
    return N, C


N, C = read_inputs("DL.INP")

best_path = []  # Tuyen duong di toi uu
min_cost = 999999999  # Luu chi phi nho nhat

visited = [False for i in range(N)]  # Danh dau dia diem da tham quan
path = []  # Tuyen duong di dang duoc xay dung
start_pos = 0  # Dia diem xuat phat


def calculate_cost(path):
    total_cost = 0
    for k in range(len(path) - 1):
        start = path[k]
        finish = path[k + 1]
        total_cost += int(C[start][finish])
    return total_cost


def find_paths(i):
    global min_cost, visited, path, best_path
    path.append(i)
    visited[i] = True
    if len(path) == N:
        path.append(start_pos)
        cost = calculate_cost(path)
        if cost < min_cost:
            min_cost = cost
            best_path = path[:]
        path.pop()
    for j in range(N):
        if visited[j] is False:
            find_paths(j)
    visited[i] = False
    path.pop()


find_paths(start_pos)


def save_output(file_name):
    # open file to write
    f = open(file_name, 'w')

    # write the best distance
    f.write(str(min_cost) + "\n")
    for i in range(len(best_path) - 1):
        f.write(str(best_path[i] + 1) + "->")
    f.write(str(best_path[-1] + 1))


save_output("DL.OUT")
