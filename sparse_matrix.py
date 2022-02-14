# Author: Emily Su
# Last Revised: February 2022

import prompt
from goody import type_as_str


class Sparse_Matrix:
    '''Constructs Sparse_Matrix object and defines operators for it.
    Sparse_Matrix is represented by a dictionary.
    Any row, column index that is not a key in the dictionary implicitly stores 0.'''
    def __init__(self, rows: int, cols: int, *matrix: (int, int, int)): 
        '''Parameters:
        rows (int): number of rows for Sparse_Matrix
        cols (int): number of columns for Sparse_Matrix
        *matrix (3-tuple): optional tuple(s) where index 0 is row index (int); index 1 is column index (int); index 2 is value (int or float) to be stored at index
        
        Attributes:
        rows (int): row size of Sparse_Matrix
        cols (int): column size of Sparse_Matrix
        matrix (dict): key (2-tuple of ints) is row, column index; value (non-zero int or float) is value stored at index''' 
        assert (type(rows) is int) and (rows > 0), 'Sparse_Matrix.__init__: invalid row argument (' + str(rows) + ') of ' + type_as_str(rows) + ' type; must be int greater than 0'
        assert (type(cols) is int) and (cols > 0), 'Sparse_Matrix.__init__: invalid column argument (' + str(cols) + ') of ' + type_as_str(cols) + ' type; must be int greater than 0'
        
        matrix_dict = {}
        for tup in matrix:
            assert (type(tup[0]) is int) and (type(tup[1]) is int), 'Sparse_Matrix.__init__: invalid row, column index type(s) of ' + type_as_str(rows) + ' and ' + type_as_str(cols) + '; must be non-negative int'
            assert (-1 < tup[0] < rows) and (-1 < tup[1] < cols), 'Sparse_Matrix.__init__: invalid row, column index (' + str(tup[0]) + ',' + str(tup[1]) + '); must be within Sparse_Matrix size (' + str(rows) + ',' + str(cols) + ')'
            assert (tup[0], tup[1]) not in matrix_dict, 'Sparse_Matrix.__init__: row and column index (' + str(tup[0]) + ',' + str(tup[1]) + ') duplicated'
            assert type(tup[2]) is (int or float), 'Sparse_Matrix.__init__: invalid matrix value type of ' + type_as_str(tup[2]) + '; must be int or float'
            
            if tup[2] != 0:
                matrix_dict[(tup[0],tup[1])] = tup[2]
        
        self.rows = rows
        self.cols = cols
        self.matrix = matrix_dict
             
           
    def __str__(self):
        size = str(self.rows)+'x'+str(self.cols)
        width = max(len(str(self.matrix.get((r,c),0))) for c in range(self.cols) for r in range(self.rows))
        return size+':['+('\n'+(2+len(size))*' ').join ('  '.join('{num: >{width}}'.format(num=self.matrix.get((r,c),0),width=width) for c in range(self.cols))\
                                                                                             for r in range(self.rows))+']'
                                                                                        
    
    def size(self) -> (int, int):
        '''Returns 2-tuple where index 0 is row size (int); index 1 is column size (int)'''
        return (self.rows, self.cols)
    
    
    def __len__(self) -> int:
        '''Returns number of 0 and non-zero values in Sparse_Matrix'''
        return self.rows*self.cols
    
    
    def __bool__(self) -> bool:
        '''Return:
        False: Sparse_Matrix stores all 0 values
        True: Sparse_Matrix stores any non-zero values'''
        if len(self.matrix) != 0:
            return True
        else:
            return False
    
    
    def __repr__(self) -> str:
        '''Returns a printable representational string of Sparse_Matrix.
        String format example: Sparse_Matrix(3, 3, (0, 0, 1), (1, 1, 1), (2, 2, 1))'''
        triples_list = []
        
        for k, v in self.matrix.items():
            triples_list.append(str((k[0],k[1],v)))
        
        triples_str = ','.join(triples_list)
        
        return 'Sparse_Matrix(' + str(self.rows) + ', ' + str(self.cols) + ', ' + triples_str + ')'
        
    
    def __getitem__(self, row_col):
        '''Returns value of Sparse_Matrix at row_col argument.
        If row_col argument is illegal (not 2-tuple of ints; or index outside of Sparse_Matrix size), raises TypeError.
        
        Parameter:
        row_col (2-tuple of ints): index 0 is row index (int); index 1 is column index(int)'''
        if (type(row_col) is not tuple) or (len(row_col) != 2) or (type(row_col[0]) is not int) or (type(row_col[1]) is not int):
            raise TypeError('Sparse_Matrix.__getitem__: invalid argument (' + str(row_col) + ') of ' + type_as_str(row_col) + ' type; must be 2-tuple of ints')
        if (row_col[0] < 0) or (row_col[0] > self.rows - 1):
            raise TypeError('Sparse_Matrix.__getitem__: invalid row index (' + str(row_col[0]) + '); must be within Sparse_Matrix size (' + str(self.rows) + ',' + str(self.cols) + ')')
        if (row_col[1] < 0) or (row_col[1] > self.cols - 1):
            raise TypeError('Sparse_Matrix.__getitem__: invalid column index (' + str(row_col[1]) + '); must be within Sparse_Matrix size (' + str(self.rows) + ',' + str(self.cols) + ')')
        else:
            if row_col not in self.matrix:
                return 0
            else:
                return self.matrix[row_col]
    
    
    def __setitem__(self, row_col, value):
        '''Updates Sparse_Matrix with value argument at row_col argument.
        If row_col argument is illegal (not 2-tuple of ints; or index outside of Sparse_Matrix size), raises TypeError.
        If value argument is not numeric, raises TypeError.
        
        Parameters:
        row_col (2-tuple of ints): index 0 is row index (int); index (1) is column index (int)
        value (int or float): updated value for Sparse_Matrix'''
        if (type(row_col) is not tuple) or (len(row_col) != 2) or (type(row_col[0]) is not int) or (type(row_col[1]) is not int):
            raise TypeError('Sparse_Matrix.__setitem__: invalid argument (' + str(row_col) + ') of ' + type_as_str(row_col) + ' type; must be 2-tuple of ints')
        
        if (row_col[0] < 0) or (row_col[0] > self.rows - 1):
            raise TypeError('Sparse_Matrix.__setitem__: invalid row index (' + str(row_col[0]) + '); must be within Sparse_Matrix size (' + str(self.rows) + ',' + str(self.cols) + ')')
        
        if (row_col[1] < 0) or (row_col[1] > self.cols - 1):
            raise TypeError('Sparse_Matrix.__setitem__: invalid column index (' + str(row_col[1]) + '); must be within Sparse_Matrix size (' + str(self.rows) + ',' + str(self.cols) + ')')
        
        if type(value) is not (int or float):
            raise TypeError('Sparse_Matrix.__setitem__: invalid value type of ' + type_as_str(value) + '; must be int or float')
        
        else:
            if (value == 0) and (row_col in self.matrix):
                self.matrix.pop(row_col)
            elif value != 0:
                self.matrix[row_col] = value
    
    
    def __delitem__(self, row_col):
        '''Deletes key in Sparse_Matrix row_col argument.
        This is the same as setting the value at row_col argument to 0.
        If row_col argument is illegal (not 2-tuple of ints; or index outside of Sparse_Matrix size), raises TypeError.
        
        Parameter:
        row_col (2-tuple of ints): index 0 is row index (int); index 1 is column index (int)'''
        if (type(row_col) is not tuple) or (len(row_col) != 2) or (type(row_col[0]) is not int) or (type(row_col[1]) is not int):
            raise TypeError('Sparse_Matrix.__delitem__: invalid argument (' + str(row_col) + ') of ' + type_as_str(row_col) + ' type; must be 2-tuple of ints')
        
        if (row_col[0] < 0) or (row_col[0] > self.rows - 1):
            raise TypeError('Sparse_Matrix.__delitem__: invalid row index (' + str(row_col[0]) + '); must be within Sparse_Matrix size (' + str(self.rows) + ',' + str(self.cols) + ')')
        
        if (row_col[1] < 0) or (row_col[1] > self.cols - 1):
            raise TypeError('Sparse_Matrix.__delitem__: invalid column index (' + str(row_col[1]) + '); must be within Sparse_Matrix size (' + str(self.rows) + ',' + str(self.cols) + ')')
        
        if row_col in self.matrix:
            self.matrix.pop(row_col)
    
    
    def row(self, r) -> tuple:
        '''Returns tuple of all values in given r argument from left to right.
        If r argument is illegal (not int; or outside of Sparse_Matrix size), raises Assertion Error.
        
        Parameter:
        r (int): row that values will be returned from'''
        assert (type(r) is int) and (-1 < r < self.rows), 'Sparse_Matrix.row: invalid argument (' + str(r) + ') of ' + type_as_str(r) + ' type; must be int within Sparse_Matrix size (' + str(self.rows) + ',' + str(self.cols) + ')'
        
        row_values = []
        for i in range(self.cols):
            if (r,i) not in self.matrix:
                row_values.append(0) 
            else:
                row_values.append(self.matrix[(r,i)])

        return tuple(row_values)
    
    
    def col(self, c) -> tuple:
        '''Returns tuple of all values in given c argument from top to bottom.
        If c argument is illegal (not int; or outside of Sparse_Matrix size), raises Assertion Error.
        
        Parameter:
        c (int): column that values will be returned from'''
        assert (type(c) is int) and (-1 < c < self.cols), 'Sparse_Matrix.col: invalid argument (' + str(c) + ') of ' + type_as_str(c) + ' type; must be int within Sparse_Matrix size (' + str(self.rows) + ',' + str(self.cols) + ')'
        
        col_values = []
        for i in range(self.rows):
            if (i,c) not in self.matrix:
                col_values.append(0)
            else:
                col_values.append(self.matrix[(i,c)])
                
        return tuple(col_values)
    
    
    def details(self) -> str:
        '''Returns string indicating Sparse_Matrix size -> dictionary -> tuple of all rows.
        String format example: 3x3 -> {(0, 0): 1, (1, 1): 5, (2, 2): 1} -> ((1, 0, 0), (0, 5, 0), (0, 0, 1))'''
        all_rows = []
        for i in range(self.rows):
            all_rows.append(self.row(i))
            
        matrix_size = str(self.rows) + 'x' + str(self.cols)
        
        return matrix_size + ' -> ' + str(self.matrix) + ' -> ' + str(tuple(all_rows))
    
    
    def __call__(self, new_rows, new_cols):
        '''Resets Sparse_Matrix row and column size with new_row and new_col arguments.
        Deletes any values whose index lies outside of re-sized Sparse_Matrix.
        If new_row or new_col arguments are not integers, raises AssertionError.
        
        Parameters:
        new_rows (int): new Sparse_Matrix row size
        new_cols (int): new Sparse_Matrix column size'''
        assert (type(new_rows) is int) and new_rows > 0, 'Sparse_Matrix.__call__: invalid row (' + str(new_rows) + ') of ' + type_as_str(new_rows) + ' type; must be int greater than 0'
        assert (type(new_cols) is int) and new_cols > 0, 'Sparse_Matrix.__call__: invalid column (' + str(new_cols) + ') of ' + type_as_str(new_cols) + ' type; must be int greater than 0'
        
        # create copy of sparse matrix dictionary to update
        matrix_copy = {}
        for k, v in self.matrix.items():
            matrix_copy[k] = v
            
        for k1 in matrix_copy.keys():
            if k1[0] >= new_rows:
                for c in range(self.cols):
                    self.__delitem__((k1[0],c))
            if k1[1] >= new_cols:
                for r in range(self.rows):
                    self.__delitem__((r,k[1]))
        
        del self.rows
        del self.cols
        
        self.rows = new_rows
        self.cols = new_cols
    
    
    def __iter__(self) -> tuple:
        '''Yields 3-tuple where index 0 is row index (int); index 1 is column index (int); index 2 is value (int or float) stored at index.
        Tuples yielded are sorted in increasing order of index 2 (value).'''
        for k, v in sorted(self.matrix.items(), key = lambda x: (x[1])):
            yield (k[0], k[1], v)
    
    
    def __pos__(self):
        '''Returns new Sparse_Matrix with same values.'''
        matrix = [(k[0], k[1], v) for k, v in self.matrix.items()]
        return Sparse_Matrix(self.rows, self.cols, *matrix)
    
    
    def __neg__(self):
        '''Returns new Sparse_Matrix with negated values.'''
        matrix = [(k[0], k[1], -v) for k, v in self.matrix.items()]
        return Sparse_Matrix(self.rows, self.cols, *matrix)
    
    
    def __abs__(self):
        '''Returns new Sparse_Matrix with all non-negative values.'''
        matrix = [(k[0], k[1], abs(v)) for k, v in self.matrix.items()]
        return Sparse_Matrix(self.rows, self.cols, *matrix)
    
    
    def __add__(self, right):
        '''Returns new Sparse_Matrix by adding right argument to self.
        If type of right argument is not int, float, or Sparse_Matrix, raises TypeError.
        If right argument is Sparse_Matrix, but not the same size, raises AssertionError.
        
        Parameter:
        right (int, float, or Sparse_Matrix): operand to be added to left operand'''
        if type(right) is Sparse_Matrix:
            assert self.size() == right.size(), 'Sparse_Matrix.__add__: Sparse_Matrix size(s) incompatible for +: ' + str(self.size()) + ' and ' + str(right.size())
            matrix = [(k[0], k[1], v + right[(k[0], k[1])]) for k, v in self.matrix.items()]
        elif type(right) is (int or float):
            matrix = [(k[0], k[1], v + right) for k, v in self.matrix.items()]
        else:
            raise TypeError('Sparse_Matrix.__add__: unsupported operand type(s) for +: ' + type_as_str(right) + ' and Sparse_Matrix')
        
        return Sparse_Matrix(self.rows, self.cols, *matrix)
    
    
    def __radd__(self, left):
        return self.__add__(left)
    
    
    def __sub__(self, right):
        '''Returns new Sparse_Matrix by adding negated right argument to self.
        If type of right argument is not int, float, or Sparse_Matrix, raises TypeError.
        If right argument is Sparse_Matrix, but not the same size, raises AssertionError.
        
        Parameter:
        right (int, float, or Sparse_Matrix): operand to be subtracted from left operand'''
        if type(right) is Sparse_Matrix:
            assert self.size() == right.size(), 'Sparse_Matrix.__sub__: Sparse_Matrix size(s) incompatible for -: ' + str(self.size()) + ' and ' + str(right.size())
            return self.__add__(right.__neg__())
         
        elif type(right) is (int or float):
            return self.__add__(-right)
        
        else:
            raise TypeError('Sparse_Matrix.__sub__: unsupported operand type(s) for -: ' + type_as_str(right) + ' and Sparse_Matrix')
    
    
    def __rsub__(self, left):
        if type(left) is (int or float):
            matrix = [(k[0], k[1], left - v) for k, v in self.matrix.items()]
            return Sparse_Matrix(self.rows, self.cols, *matrix)
        
        else:
            return self.__sub__(left)
    
    
    def __mul__(self, right):
        '''Returns new Sparse_Matrix by multiplying right argument with self.
        If type of right argument is not int, float, or Sparse_Matrix, raises TypeError.
        If right argument is Sparse_Matrix and self.cols not equal to right.rows, raises AssertionError.
        
        Parameter:
        right (int, float, or Sparse_Matrix): operand to be multiplied with left operand'''
        if type(right) is Sparse_Matrix:
            assert self.cols == right.rows, 'Sparse_Matrix.__mul__: Sparse_Matrix size(s) incompatible for *: ' + str(self.size()) + ' and ' + str(right.size())
        
            matrix = []
            for r in range(self.rows):
                for c in range(right.cols):
                    value = 0
                    for i in range(self.cols):
                        value += (self.row(r)[i] * right.col(c)[i])
                    matrix.append((r, c, value))
            return Sparse_Matrix(self.rows, right.cols, *matrix)
        
        elif type(right) is (int or float):
            matrix = [(k[0], k[1], v * right) for k, v in self.matrix.items()]
            return Sparse_Matrix(self.rows, self.cols, *matrix)
        
        else:
            raise TypeError('Sparse_Matrix.__mul__: unsupported operand type(s) for *: ' + type_as_str(right) + ' and Sparse_Matrix')
        
    
    def __rmul__(self, left):
        return self.__mul__(left)
        
        
    def __pow__(self, right):
        '''Returns new Sparse_Matrix by taking power of right argument to self.
        If type of right argument is not int, raises TypeError.
        If right argument is less than 1, raises AssertionError.
        If self.rows not equal to self.cols, raises AssertionError.
        
        Parameter:
        right (int): non-negative integer representing exponent'''
        if type(right) is int:
            assert right > 0, 'Sparse_Matrix.__pow__: invalid operand (' + str(right) + ') for **: must be non-negative int'
            assert self.rows == self.cols, 'Sparse_Matrix.__pow__: Sparse_Matrix size ' + str(self.size()) + ' incompatible for **: must have equal rows and columns'
            
            pow_mat = self
            for __ in range(1, right):
                power = pow_mat.__mul__(self)
                pow_mat = power
        
            return pow_mat
            
        else:
            raise TypeError('Sparse_Matrix.__pow__: unsupported operand type(s) for **: ' + type_as_str(right) + ' and Sparse_Matrix')
    
    
    def __eq__(self, right) -> bool:
        '''Returns bool indicating whether the right argument is equal to self.
        Parameter:
        right (int, float, or Sparse_Matrix): operand to be compared against self.
        
        Returns:
        True: right argument (Sparse_Matrix) is same size and has same pair-wise values as self; or all values of self are equal to right argument (int or float)
        False: type of right argument is not int, float, or Sparse_Matrix; right argument (Sparse_Matrix) is different size or has different pair-wise values from self; or values of self are not equal to right argument (int or float)'''
        if type(right) is Sparse_Matrix:
            if (right.size() == self.size()) and (right.details().split(' -> ')[2] == self.details().split(' -> ')[2]):
                return True
        
        elif type(right) is (int or float):
            if right == 0 and self.__bool__() is False:
                return True
            
            elif right != 0:
                all_values = list(self.matrix.values())
                if all_values.count(right) == self.__len__():
                    return True

        return False
         
    
    def __setattr__(self, name, value):
        '''Ensures that Sparse_Matrix does not store attributes other than: rows, cols, and matrix.
        If attempt is made to add new attributes or re-bind existing attribute to Sparse_Matrix, raises AssertionError.
        
        Parameters:
        name (str): namespace of attribute
        value: attribute value'''
        assert (name in ['rows', 'cols', 'matrix']) and (name not in self.__dict__), 'Sparse_Matrix.__setattr__: Sparse_Matrix object cannot store new attributes or re-bind existing attributes'
        
        if name in ['rows', 'cols', 'matrix']:
            if name not in self.__dict__:
                self.__dict__[name] = value
    

if __name__ == '__main__':
    #Simple tests
    m = Sparse_Matrix(3,3, (0,0,1),(1,1,3),(2,2,1))
    print(m)
    print(repr(m))
    print(m.details())
    
    print('\nlen and size')
    print(len(m), m.size(),)
    
    print('\ngetitem and setitem')
    print(m[1,1])
    m[1,1] = 0
    m[0,1] = 2
    print(m.details())
    
    print('\niterator')
    for r,c,v in m:
        print((r,c),v)
    
    print('\nm, m+m, m+1, m==m, m==1')
    print(m)
    print(m+m)
    print(m+1)
    print('m == m: ' + str(m==m))
    print('m == 1: ' + str(m==1))
    
    # print()
    # import driver
    # driver.default_file_name = 'bscp22W22.txt'
    # # driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
    # # driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
    # # driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    # driver.driver()
