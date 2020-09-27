def mat_builder(mat_dim):
    mat_dim_list = mat_dim.split()
    mat_dim_int = [int(x) for x in mat_dim_list]
    i = mat_dim_int[0]
    j = mat_dim_int[1]
    mat = []
    print("Enter matrix:")
    for i in range(i):
        row = input().split()
        row_fl = [float(x) for x in row]
        mat.append(row_fl)
    return mat

def mat_sum(a, b):
    if [len(row) for row in a] == [len(row) for row in b]:
        sum_mats = []
        for i in range(len(a)):
            sum_mats.append([])
            for j in range(len(a[i])):
                sum_mats[i].append(a[i][j] + b[i][j])
        return sum_mats             
    else:
        return "ERROR"

def mat_scalar(mat, scalar):
    mat_scalar = []
    for i in range(len(mat)):
        mat_scalar.append([])
        for j in range(len(mat[i])):
            mat_scalar[i].append(mat[i][j] * scalar)
    return mat_scalar
    
def print_mat(mat):
    for i in range(len(mat)):
        print(" ".join([str(round(x, 3)) for x in mat[i]]))

def mult_row_column(row, column):
    summ = 0
    for i in range(len(row)):
        summ += row[i] * column[i]
    return summ
    
def mat_multiply(a, b):
    if len(a[0]) == len(b):
        multiply_mats = []
        for i in range(len(a)):
            multiply_mats.append([])
            aa = a[i]
            for j in range(len(b[i])):
                bb = [row[j] for row in b]
                multiply_mats[i].append(mult_row_column(aa, bb))
        return multiply_mats             
    else:
        return "ERROR"

def mat_trans(mat):
    trans = []
    for i in range(len(mat[0])):
        trans.append([])
        for j in range(len(mat)):
            trans[i].append(mat[j][i])        
    return trans
    
def mat_trans_side(mat):
    mat_rev_row = []
    for i in mat:
        mat_rev_row.append(i[::-1])
    trans = []
    for i in range(len(mat_rev_row[0])):
        trans.append([])
        for j in range(len(mat_rev_row)):
            trans[i].append(mat_rev_row[j][i])
    trans_side = []
    for i in trans:
        trans_side.append(i[::-1])        
    return trans_side
    
def mat_trans_ver(mat):
    mat_rev_row = []
    for i in mat:
        mat_rev_row.append(i[::-1])        
    return mat_rev_row    
    
def mat_trans_hor(mat):       
    return mat[::-1]              

def deter_two(mat):
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

def mat_deter(mat):
    i = len(mat)
    j = len(mat[0])
    if i != j or not i:
        return "ERROR"
    elif i == 1:
        return mat[0][0]
    else:
        det = 0
        for d in range(j):
            det += cofactor_mat(mat, 0, d) * mat_deter(minor_mat(mat, 0, d))   
        return det
       
def minor_mat(mat, i, j):
    minor = mat[:]
    res = []
    for x in range(len(minor)):
        row = minor[x][:]
        row.pop(j)
        res.append(row)
    res.pop(i)
    return res

def cofactor_mat(mat, i, j):
    co = mat[i][j] * pow(-1, (i + j))
    return co

def cofactors(mat):
    cofactors = []
    for i in range(len(mat)):
        cofactors.append([])
        for j in range(len(mat[i])):
            cofactors[i].append(mat_deter(minor_mat(mat, i, j)) * pow(-1, (i + j)))
    return cofactors    

def mat_inv(mat):
    co_mat = mat_trans(cofactors(mat))
    if mat_deter(mat) == 0:
        return "This matrix doesn't have an inverse."
    else:
        scalar = 1 / mat_deter(mat)
    mat_inv = mat_scalar(co_mat, scalar)
    return mat_inv

while True: 
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    
    action = input("Your choice: ")
    
    if action == "0": 
        break
    
    if action == "1":
        first_mat_dim = input("Enter size of first matrix: ")
        first_mat = mat_builder(first_mat_dim)
        second_mat_dim = input("Enter size of second matrix: ")
        second_mat = mat_builder(second_mat_dim)
        if mat_sum(first_mat, second_mat) == "ERROR":
            print("ERROR")
        else:
            print("The result is:")
            print_mat(mat_sum(first_mat, second_mat))
        print()
    
    if action == "2":
        mat_dim = input("Enter size of first matrix: ")
        mat = mat_builder(mat_dim)
        scalar = int(input("Enter constant: "))
        mat_scalar = mat_scalar(mat, scalar)
        print("The result is:")
        print_mat(mat_scalar)
        print()
    
    if action == "3":
        first_mat_dim = input("Enter size of first matrix: ")
        first_mat = mat_builder(first_mat_dim)
        second_mat_dim = input("Enter size of first matrix: ")
        second_mat = mat_builder(second_mat_dim)
        if mat_multiply(first_mat, second_mat) == "ERROR":
            print("ERROR")
        else:
            print("The result is:")
            print_mat(mat_multiply(first_mat, second_mat))
        print()
    
    if action == "4":
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
        trans_type = input("Your choice: ")
        print()
        mat_dim = input("Enter size of first matrix: ")
        mat = mat_builder(mat_dim)
        
        if trans_type == "1":
            mat_trans = mat_trans(mat)
            print("The result is:")
            print_mat(mat_trans)    
            print()
        
        if trans_type == "2":
            mat_trans_side = mat_trans_side(mat)
            print("The result is:")
            print_mat(mat_trans_side)    
            print()
        
        if trans_type == "3":
            mat_trans_ver = mat_trans_ver(mat)
            print("The result is:")
            print_mat(mat_trans_ver)    
            print()    
        
        if trans_type == "4":
            mat_trans_hor = mat_trans_hor(mat)
            print("The result is:")
            print_mat(mat_trans_hor)    
            print() 
            
    if action == "5":
        mat_dim = input("Enter size of first matrix: ")
        mat = mat_builder(mat_dim)
        mat_deter = mat_deter(mat)
        print("The result is:")
        print(mat_deter)
        print()   
    
    if action == "6":
        mat_dim = input("Enter size of first matrix: ")
        mat = mat_builder(mat_dim)
        mat_inv = mat_inv(mat)
        print("The result is:")
        print_mat(mat_inv)    
        print()   
        
