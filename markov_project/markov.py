import pysql.sql_python as sqlpy

##mat=[1072,250,237,217]
# this matrix is 
##row1 = [1000.0 , 50.0 , 0.0 , 0.0 , 20.0 , 2.0]
##row2 = [10.0 , 200.0 , 30.0 , 0.0 , 5.0 , 5.0]
##row3 = [5.0 , 20.0 , 150.0 , 50.0 , 2.0 , 10.0]
##row4 = [1.0 , 10.0 , 30.0 , 100.0 , 1.0 , 75.0]

mat_sql = sqlpy.test()

row1 = list(mat_sql[0])
row2 = list(mat_sql[1])
row3 = list(mat_sql[2])
row4 = list(mat_sql[3])

imat = [row1 , row2, row3 , row4]

for i in xrange(0, len(mat_sql)):
    mat_sql[i] = list(mat_sql[i])

##print mat_sql
##for i in mat_sql:
##    for j in i:
##        print type(j)

##imat = []
##
##for i in mat_sql:
##    imat.append(list(i))

imat_original = []
for i in imat:
    imat_original.append(list(i))

mat = []
for i in imat:
    mat.append(sum(i))
#build transition matrix

row1_sum = sum(row1)
row2_sum = sum(row2)
row3_sum = sum(row3)
row4_sum = sum(row4)
row_sum = [row1_sum , row2_sum ,row3_sum , row4_sum]

imat_c = imat[:]

for i in xrange(0,len(imat)):
    for j in xrange(0, len(imat[0])):
        imat_c[i][j] = imat[i][j]/row_sum[i]

tmat = imat_c
tmat_w= len(tmat[0])
tmat_h= len(tmat)
tmat_t = []

#transpose of tmat
def transpose(matrix):
    
        
    tmat_w= len(matrix[0])
    tmat_h= len(matrix)
    tmat_t = []
    for i in xrange(0,tmat_w):
        tmat_t.append([])
        for j in xrange(0,tmat_h):
            tmat_t[i].append(matrix[j][i])

    
    return tmat_t

#compute the dot product
def dot(matrix_1,matrix_2):

      
    next_mat = []
    for k in xrange(0,len(matrix_2)):
        next_mat.append([])
        for i in xrange(0,len(matrix_1)):
            temp = 0
            for j in xrange(0, 4):
               
                temp += matrix_2[k][j]*matrix_1[i][j]
           
            next_mat[k].append(temp)
        
            
    return next_mat
def print_mat(mat,title):
    index = 0
    
    #look through first row of matrix to get column widths
    char_length = len(str(max(mat[0])))
    
    tabs = ["\t","\t\t"]

    if char_length >=5:
        tab_max = tabs[1]
    else: tab_max = tabs[0]
   
    print str(title) + "\n"
    print str(index) +":"+tabs[0],
    index +=1   
    
    for j in mat[0]: 
    
        if len(str(round(j,2)))>=7:
            tab = tabs[0]           
        else: tab = tab_max
        if j < 1:
            print "|%.4f"%j + tab,
        else:
            print "|%.1f"%j + tab,
    print              
       
    emat = iter(mat)
    next(emat)
    for i in emat:
        print str(index) +":"+tabs[0],
        index +=1      
        
        for j in i:            
                    
            if len(str(round(j,2)))>=7:
                tab = tabs[0]
            else: tab = tab_max            
            if j < 1:
                print "|%.4f"%j + tab,
            else:
                print "|%.1f"%j + tab,
        print
    print "\n"
       
#Number of non absorbing states
nas = len(tmat)

# generate identity matrix
id_mat = []

for i in xrange(0,nas):
    id_mat.append([])
    for j in xrange(0, nas):
        if i==j:
            id_mat[i].append(1)
        else:
            id_mat[i].append(0)

###############################################

## imat gets lost in aliasing, have to re-assign it, should fix it
imat = []
for i in imat_original:
    imat.append(list(i))
    

imat_c = imat[:]

for i in xrange(0,len(imat)):
    for j in xrange(0, len(imat[0])):
        imat_c[i][j] = imat[i][j]/row_sum[i]

tmat = imat_c

###### Seperate into non-absorbing and absorbing matrix
namat = []
for i in xrange(0, len(tmat)):
    namat.append(tmat[i][:4])

amat = []
for i in xrange(0, len(tmat)):
    amat.append(tmat[i][4:])

# Sub non absorbing matrix from id_matrix

inter_matrix = []
for i in id_mat:
    inter_matrix.append(list(i))

for i in range(0, len(inter_matrix)):
    for j in xrange(0,len(inter_matrix[0])):
        inter_matrix[i][j] = inter_matrix[i][j] - namat[i][j]
                    


#### Pass in intermediate matrix

mat = inter_matrix[:]
################################################

# generate augmented matrix
aug_mat = []
for i in xrange(0,nas):
    aug_mat.append(mat[i]+id_mat[i])
   

# must make it neater
# normalise by 1st col Add check to make sure first elem is not zero and if it is skip then add 1st row wheree 1st non zero element 1 to first row.

for i in xrange(0,nas):
    pos_1 = float(aug_mat[i][0])
    for j in xrange(0,len(aug_mat[0])):
        aug_mat[i][j] = aug_mat[i][j]/pos_1

# Substract row1 from all other rows

for i in xrange(1,nas):
    for j in xrange(0,len(aug_mat[0])):
        aug_mat[i][j] =  aug_mat[i][j] - aug_mat[0][j]

# normalise by 2nd col
for i in xrange(1,nas):
    pos_1 = float(aug_mat[i][1])
    for j in xrange(0,len(aug_mat[0])):
        aug_mat[i][j] = aug_mat[i][j]/pos_1

# use row 2 to get col of zeros in col 2 except in row 2
for i in xrange(0,nas):
    co_eff = aug_mat[i][1]
    if i == 1:
        continue

    for j in xrange(0,len(aug_mat[0])):
        aug_mat[i][j] = aug_mat[i][j] - co_eff*aug_mat[1][j]

# normalise by 3rd col
for i in xrange(2,nas):
    pos_1 = float(aug_mat[i][2])
    for j in xrange(0,len(aug_mat[0])):
        aug_mat[i][j] = aug_mat[i][j]/pos_1

# use row 3 to get col of zeros in col 3 except in row 3
for i in xrange(0,nas):
    co_eff = aug_mat[i][2]
    if i == 2:
        continue

    for j in xrange(0,len(aug_mat[0])):
        aug_mat[i][j] = aug_mat[i][j] - co_eff*aug_mat[2][j]

# normalise by 4th col
for i in xrange(3,nas):
    pos_1 = float(aug_mat[i][3])
    for j in xrange(0,len(aug_mat[0])):
        aug_mat[i][j] = aug_mat[i][j]/pos_1

# use row 4 to get col of zeros in col 4 except in row 4
for i in xrange(0,nas):
    co_eff = aug_mat[i][3]
    if i == 3:
        continue

    for j in xrange(0,len(aug_mat[0])):
        aug_mat[i][j] = aug_mat[i][j] - co_eff*aug_mat[3][j]

inv_mat = []
for i in aug_mat:
    inv_mat.append(i[4:])
    

def matrix_mul(m1,m2):
    t_mat = transpose(m1)
    return(dot(t_mat,m2))

##mat=[[1072,250,237,217]]
mat = row_sum

#Final multiplication
mpredict = matrix_mul(amat,inv_mat)


###########################################
##Print Results
###########################################

print_mat(imat_original, "Input Matrix")
print_mat(tmat, "Transitional Matrix")
print_mat(namat, "Non Absorbring Matrix")
print_mat(amat, "Absorbring Matrix")
e_close = []
e_woff = []
for i in xrange(0,len(mpredict)):
    e_close.append(mat[i]*mpredict[i][0])
    e_woff.append(mat[i]*mpredict[i][1])
    
print '{:>19} {:>11}'.format("eventual repaid:",str(round(sum(e_close),2)))
print '{:>10} {:>11}'.format("eventual write off:",str(round(sum(e_woff),2)))
print '{:>19} {:>11}'.format("total:",str(round((sum(e_close)+sum(e_woff)),2)))

erp = sum(e_close)
ewo = sum(e_woff)
total = erp+ewo

sqlpy.push_to_sql("result",erp,ewo,total)

