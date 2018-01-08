import sys

##mat=[1072,250,237,217]

# Input Matrix
row1 = [1000.0 , 50.0 , 0.0 , 0.0 , 20.0 , 2.0]
row2 = [10.0 , 200.0 , 30.0 , 0.0 , 5.0 , 5.0]
row3 = [5.0 , 20.0 , 150.0 , 50.0 , 2.0 , 10.0]
row4 = [1.0 , 10.0 , 30.0 , 100.0 , 1.0 , 75.0]
imat = [row1 , row2, row3 , row4]
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
        # i think here you probably want to do float division 
        imat_c[i][j] = imat[i][j]/float(row_sum[i])

tmat = imat_c[:]
tmat_w= len(tmat[0])
tmat_h= len(tmat)
tmat_t = []

# -- this can be done in one line using a library,
# -- maybe you can consider using a library since you have
# mastered first principles?? think about it?

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
    # look through first row of matrix to get column widths
    # Find out where that 2 comes from
    char_length = len(str(max(mat[0]))) - 2
    
    
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
            if total < 0.00001:
                print 
                return 0
            
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

# perhaps it is also useful to add this if statement, 
# normally standard to include it, but please check if its useful to include it
# here
if __name__ == "__main__":
    n = sys.argv[1]

    if n.isdigit() == True:
        n = int(n)
        pass
    else:
        print "Enter an integer next time print. I'll give you one in the mean time."
        n=10
    fcast = (forcast(mat,tmat_t,n))
    print_mat(fcast)

    repaid = 0
    woff = 0


    iter_fcast = iter(fcast)
    next(iter_fcast)
    for i in iter_fcast:
        repaid += i[4]
        woff += i[5]

    print '{:>10} {:>11}'.format("eventual close off:",str(round(repaid,2)))
    print '{:>10} {:>11}'.format("eventual write off:",str(round(woff,2)))
    print '{:>19} {:>11}'.format("total:",str(round((repaid + woff),2)))

    ##print sum_col(a)
    ##print sum_col(a)[0] + sum_col(a)[1]


