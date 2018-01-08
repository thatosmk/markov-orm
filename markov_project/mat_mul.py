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
            tmat_t[i].append(tmat[j][i])
    return tmat_t

#compete the dot product
def dot(matrix_1,matrix_2):
    next_mat = []
    for i in xrange(0,len(matrix_1)):
        temp = 0
        for j in xrange(0, 4):
           
            temp += matrix_2[j]*matrix_1[i][j]
       
        next_mat.append(temp)
        
    return next_mat

def forcast(mat,tmat_t,n):
    forecast = []
    forecast.append(mat)
    for i in xrange(0,n):
        tmat_t = transpose(tmat)
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
    
print print_mat((forcast(mat,tmat_t,238)))
##print sum_col(a)
##print sum_col(a)[0] + sum_col(a)[1]


