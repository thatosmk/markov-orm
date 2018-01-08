import pysql.sql_python as sqlpy
#import sys

# Fetch matrix from sql: Kinda a demo, all parameters hard coded in sqlpy
mat_sql = sqlpy.test()
col_names =  sqlpy.get_col_names("markov")
# Listify from tuple
for i in xrange(0, len(mat_sql)):
    mat_sql[i] = list(mat_sql[i])

# Make a copy, incase of aliasing mistake later, remember to fix remove if possible
imat_original = []
for i in mat_sql:
    imat_original.append(list(i))

# mat is the totals of each row
mat = []
for i in mat_sql:
    mat.append(sum(i))

#build transition matrix
#########################################################
    
row_sum = []
for i in mat_sql:
    row_sum.append(sum(i))
    
# 
tmat = []
for i in mat_sql:
    tmat.append(i)
    
for i in xrange(0,len(mat_sql)):
    for j in xrange(0, len(mat_sql[0])):
        tmat[i][j] = mat_sql[i][j]/row_sum[i]

# Maybe useful

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
            
            for j in xrange(0, len(matrix_2[0])):
                

##                print str(matrix_2[k][j]) + " * " + str(matrix_1[i][j])
                
##                print "here"
##                for m in matrix_1:
##                    print m
##                print "to here"
                
                temp += matrix_2[k][j]*matrix_1[i][j]
           
            next_mat[k].append(temp)
        
    return next_mat

def forcast(mat,a,n):
##    print mat
    
    forecast = []
    forecast.append(mat)
    tmat_t = transpose(a)
##    for j in tmat_t:
##        print j
    for i in xrange(0,n):
        
        next_mat = dot(tmat_t,mat)
        forecast.append(next_mat)
        mat = next_mat    
    return forecast

#compute the dot product
def dot2(matrix_1,matrix_2,nonas):

    next_mat = []
    for k in xrange(0,len(matrix_2)):
        
        
        next_mat.append([])
        for i in xrange(0,len(matrix_1)):
            temp = 0
            
            for j in xrange(0, nonas):
                

##                print str(matrix_2[k][j]) + " * " + str(matrix_1[i][j])
                
##                print "here"
##                for m in matrix_1:
##                    print m
##                print "to here"
                
                temp += matrix_2[k][j]*matrix_1[i][j]
           
            next_mat[k].append(temp)
        
    return next_mat

def forcast2(mat,a,nonas,n):
##    print mat
    
    forecast = []
    forecast.append(mat)
    tmat_t = transpose(a)
##    for j in tmat_t:
##        print j
    for i in xrange(0,n):
        
        next_mat = dot2(tmat_t,mat,nonas)
        forecast.append(next_mat)
        mat = next_mat    
    return forecast

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


###### Seperate into non-absorbing and absorbing matrix
namat = []
for i in xrange(0, len(tmat)):
    namat.append(tmat[i][:nas])

amat = []
for i in xrange(0, len(tmat)):
    amat.append(tmat[i][nas:])

# Sub non absorbing matrix from id_matrix

inter_matrix = []
for i in id_mat:
    inter_matrix.append(list(i))

for i in range(0, len(inter_matrix)):
    for j in xrange(0,len(inter_matrix[0])):
        inter_matrix[i][j] = inter_matrix[i][j] - namat[i][j]

#### Pass in intermediate matrix

# generate augmented matrix
aug_mat = []
for i in xrange(0,nas):
    aug_mat.append(inter_matrix[i]+id_mat[i])


# Calculate inverse of augmented matrix

# normalise by kth col: Add check to make sure first elem is not zero and if it is skip then add 1st row wheree 1st non zero element 1 to first row.
for k in xrange(0,len(aug_mat)):
                
    for i in xrange(k,nas):
        
        pos_1 = float(aug_mat[i][k])
        for j in xrange(0,len(aug_mat[0])):
            aug_mat[i][j] = aug_mat[i][j]/pos_1

    # Substract rowk from all other rows

    for i in xrange(0,nas):
        if k==0:
            co_eff = 1
        else:
            co_eff = aug_mat[i][k]
                    
        if i == k:
            continue
        for j in xrange(0,len(aug_mat[0])):
            aug_mat[i][j] =  aug_mat[i][j] - co_eff*aug_mat[k][j]

   
##################################################################################

inv_mat = []
for i in aug_mat:
    inv_mat.append(i[nas:])
    

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
##print_mat(tmat, "Transition Matrix")
##print_mat(namat, "Non Absorbring Matrix")
##print_mat(amat, "Absorbring Matrix")

results = {}
for i in xrange(0,len(mpredict[0])):
    results[str(i)] = []

for i in xrange(0,len(mpredict)):
    for j in xrange(0,len(mpredict[i])):

        results[str(j)].append(mat[i]*mpredict[i][j])

total = []
for i in sorted(results.iterkeys()):
    total.append(float(sum(results[i])))
    print '{:<0} {:<1} {:>11}'.format("a_State:",i ,str(round(total[int(i)],2)))

print "\t"

print '{:<0} {:<1} '.format("result of markov:",str(sum(total)))
print '{:>17} {:>2} '.format("row_sum:",str(sum(row_sum)))

print "\npushing results to database\n"

##print row_sum
##print tmat
print "Enter the number of months you want to run the forecast: "
n = (raw_input())
#n = sys.argv[1]

if n.isdigit() == True:
    n = int(n)
    pass
else:
    print "Enter an integer next time print. I'll give you one in the mean time."
    n=10

results_forecast = forcast2([row_sum],tmat,nas,n)
##print results

query = sqlpy.create_table_query_2(results_forecast,col_names, "results")
sqlpy.push_to_sql(query)
query = sqlpy.create_table_query(results, "eventuals")
sqlpy.push_to_sql(query)

