import numpy as np

                            # ------------------- CONVERT LIST TO ARRAY --------------------------------

lst = [1,2,3,4,5]
print(type(lst))

arr = np.array(lst)
print(arr)
print(type(arr)) # class 'numpy.ndarray'   here nd is n dimenstion

                                #  ------         SHAPE OF ARRAy --------------------------------

print(arr.shape) #(5,)  5 elements in array


print()



#       --------------------generate random numbers------------------------------------------------
print("random numbers")
array=np.random.random((3,5)) # 3*3 matrix array
print(array)

# ----------------------------------  random------------------------------------------------------------------------------------------------

arr= np.random.randint(1,10,(3,5))
print(arr)
#  output   [[9 7 2 1 7]
#           [6 9 7 5 5]
#              [4 9 7 1 8]]

#  array=np.random.random()  it will print one random number between 0 and 1


# ----------------------------ARANGE------------------------------------------------

print(np.arange(1,10,1))  # same as range in for loop


# -------------------- Linespace ----------------------------------------------------------------
print(np.linspace(1,20,5))  # here 1 is starting point
                                # 20 is ending point
                                # we want 5 values b/w 1 and 20 THESE IS THE MAIN DIFFERENCE B/W Arange and linespace


# -----------------------------reshape ----------------------------------------------------------------
array=np.reshape(array,(5,3)) # 5 = rows , 3=cols
print(array)

# --------------------------  ARTHMATIC OPERATIONS------------------------------------------------
#  +-*/**%
array=np.arange(1,10,2)
print()
print("Arthmatic operations")
print("multi")
print(array*5)  
print("add")
print(array+1)  
print("sub")
print(array-1)  
print("remainder")
print(array%5) 
print("square") 
print(array**2)  #square
print("cubic")
print(array**3)  #cubic

# ------------------max and min---------------------------

array= np.array([
                    [1,2,3,4],
                    [5,8,9,6],
                    [1,2,4,5]
                ])
print(array.max())  # here 9 is max
print(array.min())  # here 1 is min

#   RoW WISE MAX and min  FOR ROW-WISE axis = 1
print(array.max(axis=1))  # max are [4 9 5]
print(array.min(axis=1))  # min are [1 5 1]


#  COL-wise max and min    FOR COL-WISE axis=0
print(array.min(axis=0))  # min are [1 2 3 4]
print(array.max(axis=0)) # max are [5 8 9 6]


# ------------------------SUM -------------------------------
print(array.sum())

#  --------------------------- MULTIPLY Add Divide 2 arrays -------------------------------


print()
print("2 arrays multiply")
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)

arr2=np.array([[9,8,7],[6,5,4],[3,2,1]])
print(arr2)


print("multiply")
print(arr1*arr2) # it should have same number of rows and columns then only it works

print("\nadd\n")
print(arr1+arr2) 
print("\nsub")
print(arr1-arr2)


# ----------------- dot operator   any type of matrix multipliction 3*3 or 3*2 any type--------------------------------------------------------

#  dot operator works on 1st row of arr1  MULTIPLY with 1 col of arr2 
print(arr1.dot(arr2))
arr3=np.array([[1,2,3],
               [4,5,6]])


arr4=np.array([[9,8],
            [6,5],
            [3,2]])
print(arr3.dot(arr4))


# -------------------------- matrix access  OR SLICING        `----------------------------------------------------------------

print(arr3[:])  # all elemtns in  2*3f
#   or
print(arr3[:,:]) #same as above  but selecting done here  :rows,:cols
arr3=np.array([
               [10,5,1111],
                [5,2,2122],
               ])
print(arr3[1:,1:]) #same as above but selecting done here 1 row: 1 col NOTE index from 0
print("1,1 value is")
print(arr3[1,1]) # output is 2


#  --------------------------SORTING  (arr,axis=1 or 0,kind="mergesort"or anysorting techinque)-----------------------------

print(np.sort(arr3,axis=1,kind="mergesort")) # sorting on row wise because axis=1
print(np.sort(arr3,axis=0,kind="mergesort")) # sorting on col wise because axis=0



# --------------------------MERGING (vstack,hstack)------------------------------

arr1=np.array([[9,8,7],[6,5,4],[3,2,1]])
arr2=np.array([[9,8,7],[6,5,4],[3,2,1]])

#  vstack

print(np.vstack((arr1,arr2)))

print("hstack")
print(np.hstack((arr1,arr2)))


#  -----------------------SPLIT (vsplit,hsplit)------------------------------
arr1=np.array([[9,8,7,8],[6,5,4,10],[3,2,1,11],[3,2,1,12]])
arr2=np.array([[9,8,7,23],[6,5,4,22],[3,2,1,21]])
print(np.hsplit(arr1,2))
print(np.vsplit(arr1,2))

# ---------------------------------MEAN STandard Deviation AND VARIENCE-------

print("MEAN")
arr=np.random.randint(1,100,(4,4))
print(arr.mean())

print("STANDARD DEviation")
print(arr.std())

print("varience")
print(arr.var())


# ----------------------FILTER---------------------
arr = np.arange(1,10)
print("filter")
print(arr[arr>5])   # filter method


# ------------------------TRANSPOSE -------------------

arr = np.random.randint(1,10,(2,5))
print(arr.T)