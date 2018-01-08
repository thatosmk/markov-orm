mat=[1072,250,237,217]
row1 = [1000.0 , 50.0 , 0.0 , 0.0 , 20.0 , 2.0]
row2 = [10.0 , 200.0 , 30.0 , 0.0 , 5.0 , 5.0]
row3 = [5.0 , 20.0 , 150.0 , 50.0 , 2.0 , 10.0]
row4 = [1.0 , 10.0 , 30.0 , 100.0 , 1.0 , 75.0]
imat = [row1 , row2, row3 , row4]
##tmat = [[0.933,0.047,0,0,0.019,0.002],[0.04,0.80,0.12,0,0.02,0.02],[0.021,0.084,0.633,0.211,0.008,0.042],[0.005,0.046,0.138,0.461,0.005,0.346]]
##tmat_w= len(tmat[0])
##tmat_h= len(tmat)
##tmat_t = []

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

# round all entries to 1 decimal place
##for i in xrange(0, len(tmat)):
##
##    for j in xrange(0, len(tmat[0])):
##        tmat[i][j] = round(tmat[i][j],5)

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

#compete the dot product
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

def forcast(mat,tmat_t,n):
    forecast = []
    forecast.append(mat)
    for i in xrange(0,n):
        
        next_mat = dot(tmat_t,mat)
        forecast.append(next_mat)
        mat = next_mat    
    return forecast
def print_mat(mat):
    index = 0
    total = 0
    #look through first row of matrix to get column widths
    char_length = len(str(max(mat[0])))
    
    tabs = ["\t","\t\t"]

    if char_length >=5:
        tab_max = tabs[1]
    else: tab_max = tabs[0]
   
    print "Index"+tabs[0]+"|CD0"+tab_max+"|CD1"+tab_max+"|CD2"+tab_max+"|CD3"+tab_max+"|Repaid"+tab_max+"|W_Off"+tab_max+"||Total"    
    
    print str(index) +":"+tabs[0],
    index +=1   
    
    for j in mat[0]: 
    
        if len(str(round(j,2)))>=7:
            tab = tabs[0]           
        else: tab = tab_max        
        print "|%.1f"%j + tab,
    print              
       
    emat = iter(mat)
    next(emat)
    for i in emat:
        print str(index) +":"+tabs[0],
        index +=1      
        
        for j in i:            
            
            total += j        
            if len(str(round(j,2)))>=7:
                tab = tabs[0]
            else: tab = tab_max            
            print "|%.1f"%j + tab,           
        print  "||%.1f"%total
        total = 0
        
def sum_col(mat):
    #throw away first row
    nmat = mat[1:]
    # sum up row 5, repaid column
    # sum up row 6, w_off column
    repaid = 0
    w_off = 0
    for i in nmat:
        repaid+=i[4]
        w_off+=i[5]
    return (repaid,w_off)
tmat_t = transpose(tmat)    
##print print_mat((forcast(mat,tmat_t,1)))
##print sum_col(a)
##print sum_col(a)[0] + sum_col(a)[1]





row1 = [3 , 4 , 7 , 9]
row2 = [5 , 4 , -1 , 4]
row3 = [8 , 7 , 8 , 5]
row4 = [4 , 3 , 0 , 9]

mat = [row1 , row2 , row3 , row4]

# generate identity matrix
id_mat = []

for i in xrange(0,len(row1)):
    id_mat.append([])
    for j in xrange(0, len(row1)):
        if i==j:
            id_mat[i].append(1)
        else:
            id_mat[i].append(0)

###############################################

# Test on test_case

row12 = [1000.0 , 50.0 , 0.0 , 0.0 , 20.0 , 2.0]
row22 = [10.0 , 200.0 , 30.0 , 0.0 , 5.0 , 5.0]
row32 = [5.0 , 20.0 , 150.0 , 50.0 , 2.0 , 10.0]
row42 = [1.0 , 10.0 , 30.0 , 100.0 , 1.0 , 75.0]
imat = [row12 , row22, row32 , row42]
##tmat = [[0.933,0.047,0,0,0.019,0.002],[0.04,0.80,0.12,0,0.02,0.02],[0.021,0.084,0.633,0.211,0.008,0.042],[0.005,0.046,0.138,0.461,0.005,0.346]]
##tmat_w= len(tmat[0])
##tmat_h= len(tmat)
##tmat_t = []

#build transition matrix

row1_sum = sum(row12)
row2_sum = sum(row22)
row3_sum = sum(row32)
row4_sum = sum(row42)
row_sum = [row1_sum , row2_sum ,row3_sum , row4_sum]

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
for i in xrange(0,len(row1)):
    aug_mat.append(mat[i]+id_mat[i])


        


# normalise by 1st col Add check to make sure first elem is not zero and if it is skip then add 1st row wheree 1st non zero element 1 to first row.

for i in xrange(0,len(row1)):
    pos_1 = float(aug_mat[i][0])
    for j in xrange(0,len(aug_mat[0])):
        aug_mat[i][j] = aug_mat[i][j]/pos_1

# Substract row1 from all other rows

for i in xrange(1,len(row1)):
    for j in xrange(0,len(aug_mat[0])):
        aug_mat[i][j] =  aug_mat[i][j] - aug_mat[0][j]

# normalise by 2nd col
for i in xrange(1,len(row1)):
    pos_1 = float(aug_mat[i][1])
    for j in xrange(0,len(aug_mat[0])):
        aug_mat[i][j] = aug_mat[i][j]/pos_1

# use row 2 to get col of zeros in col 2 except in row 2
for i in xrange(0,len(row1)):
    co_eff = aug_mat[i][1]
    if i == 1:
        continue

    for j in xrange(0,len(aug_mat[0])):
        aug_mat[i][j] = aug_mat[i][j] - co_eff*aug_mat[1][j]

# normalise by 3rd col
for i in xrange(2,len(row1)):
    pos_1 = float(aug_mat[i][2])
    for j in xrange(0,len(aug_mat[0])):
        aug_mat[i][j] = aug_mat[i][j]/pos_1

# use row 3 to get col of zeros in col 3 except in row 3
for i in xrange(0,len(row1)):
    co_eff = aug_mat[i][2]
    if i == 2:
        continue

    for j in xrange(0,len(aug_mat[0])):
        aug_mat[i][j] = aug_mat[i][j] - co_eff*aug_mat[2][j]

# normalise by 4th col
for i in xrange(3,len(row1)):
    pos_1 = float(aug_mat[i][3])
    for j in xrange(0,len(aug_mat[0])):
        aug_mat[i][j] = aug_mat[i][j]/pos_1

# use row 4 to get col of zeros in col 4 except in row 4
for i in xrange(0,len(row1)):
    co_eff = aug_mat[i][3]
    if i == 3:
        continue

    for j in xrange(0,len(aug_mat[0])):
        aug_mat[i][j] = aug_mat[i][j] - co_eff*aug_mat[3][j]

inv_mat = []
for i in aug_mat:
    inv_mat.append(i[4:])
    
### get first_col
##col_1 = []
##for i in aug_mat:
##    col_1.append(i[0])

# is the first elemen 1
##if col_1[0] == 1:
##    continue
##    #do something
##else:
##
##    continue
    
## Check Matrices
        
##print id_mat
##print mat
##print "Augmented Matrix"
##for i in aug_mat:
##    for j in i:
##        print str(round(j,4)) + "\t\t",
##    print
##        
##print "\n"
##
##print "Transitional Matrix"
##for i in tmat:
##    for j in i:
##        print str(round(j,4)) + "\t\t",
##    print
##
##print "\n"
##
##print "Non absorbing matrix"
##for i in namat:
##    for j in i:
##        print str(round(j,4)) + "\t\t",
##    print
##
##print "\n"
##
##print "Absorbing matrix"
##for i in amat:
##    for j in i:
##        print str(round(j,4)) + "\t\t",
##    print
##
##print "\n"
##
##print "Intermediate matrix"
##for i in inter_matrix:
##    for j in i:
##        print str(round(j,4)) + "\t\t",
##    print
##
##print "\n"
##    
##print "Inverted matrix"
##for i in inv_mat:
##    for j in i:
##        print str(round(j,4)) + "\t\t",
##    print

def matrix_mul(m1,m2):
    t_mat = transpose(m1)
    return(dot(t_mat,m2))

mat=[[1072,250,237,217]]

##
##print "Markov Prediction"
##print "\n"
mpredict = matrix_mul(amat,inv_mat)
##for i in mpredict :
##    for j in i:
##        print str(round(j,4)) + "\t\t",
##    print





e_close = []
e_woff = []
for i in xrange(0,len(mpredict)):
    e_close.append(mat[0][i]*mpredict[i][0])
    e_woff.append(mat[0][i]*mpredict[i][1])
print "e_close = " + str(sum(e_close))
print "e_woff = " + str(sum(e_woff))
print "total = " + str(sum(e_close)+sum(e_woff))
##namat_t = transpose(namat)
##print_mat(forcast(inv_mat,namat_t,1))
