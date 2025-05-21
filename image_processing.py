# Name: Allison Meikle
# ID: 261071031
 
import doctest 
 
def is_valid_image(image):
    ''' (list<list>) --> bool
    Takes a nested list as input, and returns True if the nested list represents a valid (non-compressed) PGM image matrix and False otherwise.
    
    >>> is_valid_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    True
    
    >>> is_valid_image([[0], [0, 0], [0,0,0]])
    False
    
    >>> is_valid_image([['2x4', '155x3', '255x1'], ['11x8'], ['255x1', '300x7']])
    False
    '''
    
    is_valid = True
    row_lengths = []
    
    for row in image:
        for obj in row:
            if type(obj) != int or int(obj) < 0 and int(obj) > 255:
                is_valid = False
            
        row_lengths.append(len(row))
        
    if not(row_lengths.count(row_lengths[0]) == len(row_lengths)):
        is_valid = False
    
    return is_valid
                
 
def is_valid_compressed_image(image):
    ''' (list<list>) --> bool
    Takes a nested list as input, and returns True if the nested list represents a valid compressed PGM image matrix and False otherwise.
    
    >>> is_valid_compressed_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    False
    
    >>> is_valid_compressed_image([['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1']])
    True
    
    >>> is_valid_compressed_image([['2x4', '155x3', '255x1'], ['11x8'], ['255x1', '300x7']])
    False
    '''
    
    b_sums = []
    is_valid = True
    
    for row in image:
        b_sum = 0
        for obj in row:
            if 'x' not in str(obj):
                is_valid = False
            elif obj.count('x') > 1:
                is_valid = False
            else:
                index_of_x = obj.find('x')
                A = obj[:index_of_x]
                B = obj[index_of_x+1:]
                
                b_sum += int(B)
                
                if int(A) < 0 or int(A) > 255 or int(B) < 0 or int(B) > 255:
                    is_valid = False
                
        b_sums.append(b_sum)
        
    if not(b_sums.count(b_sums[0]) == len(b_sums)):
        is_valid = False
      
    return is_valid
 
def load_regular_image(filename):
    ''' (str) --> list<list>
    Takes a filename (string) of a PGM image file as input, and loads in the image contained in the file and returns it as an image matrix.
    If the resulting image matrix is found to not be in PGM format, an AssertionError is raised instead.
    
    >>> fobj = open('example.pgm', 'w')
    >>> fobj.write('P2\\n24 7\\n255\\n0  0  0  0  0  0 0   0   0   0   0   0 0   0   0   0   0   0 0   0   0   0   0  0\\n0 51 51 51 51 51 0 119 119 119 119 119 0 187 187 187 187 187 0 255 255 255 255  0\\n0 51  0  0  0  0 0 119   0   0   0 119 0 187   0 187   0 187 0 255   0   0 255  0\\n0 51  0  0  0  0 0 119   0   0   0 119 0 187   0 187   0 187 0 255 255 255 255  0\\n0 51  0  0  0  0 0 119   0   0   0 119 0 187   0 187   0 187 0 255   0   0   0  0\\n0 51 51 51 51 51 0 119 119 119 119 119 0 187   0 187   0 187 0 255   0   0   0  0\\n0  0  0  0  0  0 0   0   0   0   0   0 0   0   0   0   0   0 0   0   0   0   0  0')
    585
    >>> fobj.close()
    
    >>> load_regular_image('example.pgm')
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
#     >>> fobj = open('example.pgm', 'w')
#     >>> fobj.write('abcdefghi')
#     9
#     >>> fobj.close()
#     
#     >>> load_regular_image('example.pgm')
#     Traceback (most recent call last):
#     AssertionError: The selected file to load must be an image in the PGM format
     
    >>> fobj = open('example.pgm', 'w')
    >>> fobj.write('P2\\n24 7\\n255\\n1 2 3\\n4 5 6\\n7 8 9')
    29
    >>> fobj.close()
    
    >>> load_regular_image('example.pgm')
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    '''
    file = open(filename, 'r')
    
    first_chars = file.read(2)
    
    if first_chars != 'P2':
        raise AssertionError('The selected file to load must be an image in the PGM format')
        
    image = [[]]
    
    for line in file:
        line = line.strip('\n')
        line = line.replace(' ', ',')
        image.append(line.split(','))
    
    for row in image: 
        while '' in row: 
            for elmnt in row: 
                elmnt.strip(',') 
                if elmnt == '': 
                    row.pop(row.index(elmnt)) 
    
    for i in range(4):
        image.pop(0)
    
    for i in range(len(image)):
        for j in range (len(image[0])):
            image[i][j] = int(image[i][j])
    
    if not is_valid_image(image):
        raise AssertionError('The selected file to load must be an image in the PGM format')
    
    file.close()
    return image
    
def load_compressed_image(file):
    ''' (str) --> list<list>
    Takes a filename (string) of a compressed PGM image file as input, loads in the image contained in the file, and returns it as a compressed image matrix.
    If, during or after loading, the resulting image matrix is found to not be in compressed PGM format, then a AssertionError is raised instead.
    
    >>> fobj = open('new_example.txt', 'w')
    >>> fobj.write('P2C\\n24 7\\n255\\n0x24\\n0x1 51x5 0x1 119x5 0x1 187x5 0x1 255x4 0x1\\n0x1 51x1 0x5 119x1 0x3 119x1 0x1 187x1 0x1 187x1 0x1 187x1 0x1 255x1 0x2 255x1 0x1\\n0x1 51x1 0x5 119x1 0x3 119x1 0x1 187x1 0x1 187x1 0x1 187x1 0x1 255x4 0x1\\n0x1 51x1 0x5 119x1 0x3 119x1 0x1 187x1 0x1 187x1 0x1 187x1 0x1 255x1 0x4\\n0x1 51x5 0x1 119x5 0x1 187x1 0x1 187x1 0x1 187x1 0x1 255x1 0x4\\n0x24')
    357
    >>> fobj.close()
    
    >>> load_compressed_image('new_example.txt')
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    
#     >>> fobj = open('example2.txt', 'w')
#     >>> fobj.write('abcdefghi')
#     9
#     >>> fobj.close()
#     
#     >>> load_compressed_image('example2.txt')
#     Traceback (most recent call last):
#     AssertionError: The selected file to load must be an compressed image in the PGM format
    
    >>> fobj = open('valid_example.txt', 'w')
    >>> fobj.write('P2C\\n24 7\\n255\\n0x4\\n1x4\\n2x4\\n3x1 4x2 5x1')
    36
    >>> fobj.close()
    
    >>> load_compressed_image('valid_example.txt')
    [['0x4'], ['1x4'], ['2x4'], ['3x1', '4x2', '5x1']]
    '''
    file = open(file, 'r')
    
    first_chars = file.read(3)
    
    if first_chars != 'P2C':
        raise AssertionError('The selected file to load must be an compressed image in the PGM format')
        
    image = [[]]
    
    for line in file: 
        line = line.strip('\n') 
        line = line.replace(' ', ',') 
        image.append(line.split(',')) 
     
    for row in image: 
        while '' in row: 
            for elmnt in row: 
                elmnt.strip(',') 
                if elmnt == '': 
                    row.pop(row.index(elmnt)) 
    
    for i in range(4):
        image.pop(0)
    
    for row in image: 
        for item in row: 
            count = item.count('x') 
            if count != 1: 
                raise AssertionError('The selected file must be a valid compressed PGM image and cannot have invalid commands for each pixel')
    file.close()
    return image 
    
def load_image(filename):
    ''' (str) --> list<list>
    Takes a filename (string) of a file as input. Checks the first line of the file. If it is 'P2', then loads in the file as a regular PGM image and returns the image matrix.
    If it is 'P2C', then loads in the file as a compressed PGM image and returns the compressed image matrix.
    If it is anything else, then a AssertionError with an appropriate error message should be raised instead.
    
    >>> fobj = open('valid_example.txt', 'w')
    >>> fobj.write('P2C\\n24 7\\n255\\n0x4\\n1x4\\n2x4\\n3x1 4x2 5x1')
    36
    >>> fobj.close()
    
    >>> load_image('valid_example.txt')
    [['0x4'], ['1x4'], ['2x4'], ['3x1', '4x2', '5x1']]
    
#     >>> fobj = open('example2.txt', 'w')
#     >>> fobj.write('abcdefghi')
#     9
#     >>> fobj.close()
#     
#     >>> load_image('example2.txt')
#     Traceback (most recent call last):
#     AssertionError: The selected file must either be an image in the PGM format or an image in the compressed PGM image format.
 
    >>> fobj = open('example.pgm', 'w')
    >>> fobj.write('P2\\n24 7\\n255\\n0  0  0  0  0  0 0   0   0   0   0   0 0   0   0   0   0   0 0   0   0   0   0  0\\n0 51 51 51 51 51 0 119 119 119 119 119 0 187 187 187 187 187 0 255 255 255 255  0\\n0 51  0  0  0  0 0 119   0   0   0 119 0 187   0 187   0 187 0 255   0   0 255  0\\n0 51  0  0  0  0 0 119   0   0   0 119 0 187   0 187   0 187 0 255 255 255 255  0\\n0 51  0  0  0  0 0 119   0   0   0 119 0 187   0 187   0 187 0 255   0   0   0  0\\n0 51 51 51 51 51 0 119 119 119 119 119 0 187   0 187   0 187 0 255   0   0   0  0\\n0  0  0  0  0  0 0   0   0   0   0   0 0   0   0   0   0   0 0   0   0   0   0  0')
    585
    >>> fobj.close()
    
    >>> load_image('example.pgm')
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    '''
    file = open(filename, 'r')
    
    first_chars = file.read(3)
    
    image = [[]]
    
    if first_chars == 'P2C':
        image = load_compressed_image(filename)
    elif first_chars[:2] == 'P2':
        image = load_regular_image(filename)
    else:
        raise AssertionError('The selected file must either be an image in the PGM format or an image in the compressed PGM image format.')
       
    file.close()
    return image
 
def save_regular_image(nested_list, filename):
    ''' (list<list>, str) --> None
    Takes a nested list and a filename (string) as input, and saves it in the PGM format to a file with the given filename.
    If the image matrix given as input is not a valid PGM image matrix, instead raise a AssertionError with an appropriate error message.
    
    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> fobj = open("test.pgm", 'r')
    >>> fobj.read()
    'P2\\n10 3\\n255\\n0 0 0 0 0 0 0 0 0 0\\n255 255 255 255 255 255 255 255 255 255\\n0 0 0 0 0 0 0 0 0 0\\n'
    >>> fobj.close()
    
    >>> save_regular_image([[0]*9, [255]*8, [0]*10], "test.pgm")
    Traceback (most recent call last):
    AssertionError: The image matrix given must be a valid PGM image matrix
    
    >>> save_regular_image([[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]], "test.pgm")
    >>> fobj = open("test.pgm", 'r')
    >>> fobj.read()
    'P2\\n5 3\\n255\\n0 1 2 3 4\\n5 6 7 8 9\\n10 11 12 13 14\\n'
    >>> fobj.close()
    '''
    fobj = open(filename, 'w')
    
    if not is_valid_image(nested_list):
        raise AssertionError ('The image matrix given must be a valid PGM image matrix')
    
    width = str(len(nested_list[0]))
    height = str(len(nested_list))
    
    fobj.write ('P2\n' + width + ' ' + height + '\n255\n')
    
    for i in range (len(nested_list)):
        for j in range (len(nested_list[0])):
            if j == (int(width)-1):
                fobj.write(str(nested_list[i][j]))
            else:
                fobj.write(str(nested_list[i][j]) + ' ')
        
        fobj.write('\n')
        
    fobj.close()
    
def save_compressed_image(nested_list, filename):
    ''' (list<list>, str) --> None
    Takes a nested list and a filename (string) as input, and saves it in the compressed PGM format to a file with the given filename.
    If the image matrix given as input is not a valid compressed PGM image matrix, it raises an AssertionError.
    
    >>> save_compressed_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    
    >>> save_compressed_image([["0x5x2", "200x2"], ["111x7"]], "test.pgm.compressed")
    Traceback (most recent call last):
    AssertionError: The image matrix given must be a valid compressed PGM image matrix
    
    >>> save_compressed_image([['10x5', '2x4'], ['255x9'], ['120x7', '12x2']], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n9 3\\n255\\n10x5 2x4\\n255x9\\n120x7 12x2\\n'
    >>> fobj.close()
    '''
    
    fobj = open(filename, 'w')
    
    if not is_valid_compressed_image(nested_list):
        raise AssertionError ('The image matrix given must be a valid compressed PGM image matrix')
    
    width = 0
    for obj in nested_list[0]:
        index_of_x = obj.find('x')
        B = int(obj[index_of_x+1:])
        width += B
        
    height = len(nested_list)
    
    fobj.write ('P2C\n' + str(width) + ' ' + str(height) + '\n255\n')
    
    for line in nested_list:
        fobj.write (' '.join(line) + '\n')
        
    fobj.close()
 
def save_image(nested_list, filename):
    ''' (list<list>, str) --> None
    Takes a nested list and a filename (string) as input and based on the type of the elements in the nested list saves the image to the file specified by the file name
    as either a PGM image matrix or a compressed PGM image matrix. If the nested list is not a valid PGM image matrix it raises an AssertionError.
    
    >>> save_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    
    >>> save_image([["0x5x2", "200x2"], ["111x7"]], "test.pgm.compressed")
    Traceback (most recent call last):
    AssertionError: The given image matrix must be either a valid PGM image matrix or a valid PGM compressed image matrix
    
    >>> save_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> fobj = open("test.pgm", 'r')
    >>> fobj.read()
    'P2\\n10 3\\n255\\n0 0 0 0 0 0 0 0 0 0\\n255 255 255 255 255 255 255 255 255 255\\n0 0 0 0 0 0 0 0 0 0\\n'
    >>> fobj.close()
    '''
    
    if (not is_valid_image(nested_list)) and (not is_valid_compressed_image(nested_list)):
        raise AssertionError ('The given image matrix must be either a valid PGM image matrix or a valid PGM compressed image matrix')
    elif type(nested_list[0][0]) == int:
        save_regular_image(nested_list, filename)
    elif type(nested_list[0][0]) == str:
        save_compressed_image(nested_list, filename)
    
def invert(image):
    ''' (list<list>) --> list<list>
    Takes a (non-compressed) PGM image matrix as input, and returns the inverted image. If the input matrix is not a valid PGM image matrix, an AssertionError is raised instead.
    
    >>> image = [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    >>> invert(image)
    [[255, 155, 105], [55, 55, 55], [0, 0, 0]]
    >>> image == [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    True
    
    >>> invert ([[0]*10, [255]*10, [0]*10])
    [[255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255]]
    
    >>> invert([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15]])
    Traceback (most recent call last):
    AssertionError: The image matrix given must be a valid PGM image matrix
    '''
    if not is_valid_image(image):
        raise AssertionError ('The image matrix given must be a valid PGM image matrix')
    
    new_image = [[]]
    new_image.pop(0)
    
    for row in image:
        new_image.append(image[0][:])
    
    for i in range (len(image)):
        for j in range (len(image[0])):
            new_image[i][j] = 255 - image[i][j]
    
    return new_image
 
def flip_horizontal (image):
    ''' (list<list>) --> list<list>
    Takes a (non-compressed) PGM image matrix as input, and returns the image matrix flipped horizontally.
    If the input matrix is not a valid PGM image matrix, an AssertionError is raised instead.
    
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    [[5, 4, 3, 2, 1], [10, 10, 5, 0, 0], [5, 5, 5, 5, 5]]
    
    >>> flip_horizontal([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15]])
    Traceback (most recent call last):
    AssertionError: The image matrix given must be a valid PGM image matrix
    
    >>> flip_horizontal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
    '''
    
    if not is_valid_image(image):
        raise AssertionError ('The image matrix given must be a valid PGM image matrix')
    
    new_image = [[]]
    new_image.pop(0)
    
    for row in image:
        new_image.append(image[0][:])
    
    for i in range(len(image)):
        row = image[i]
        new_image[i] = row[::-1]
    
    return new_image
 
def flip_vertical(image):
    ''' (list<list>) --> list<list>
    Takes a (non-compressed) PGM image matrix as input, and returns the image matrix flipped vertically.
    If the input matrix is not a valid PGM image matrix, an AssertionError is raised instead.
    
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    [[5, 5, 5, 5, 5], [0, 0, 5, 10, 10], [1, 2, 3, 4, 5]]
    
    >>> flip_vertical([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
    [[13, 14, 15], [10, 11, 12], [7, 8, 9], [4, 5, 6], [1, 2, 3]]
    
    >>> flip_vertical([[1, 2, 3], [4, 5], [6, 7, 8]])
    Traceback (most recent call last):
    AssertionError: The image matrix given must be a valid PGM image matrix
    '''
    if not is_valid_image(image):
        raise AssertionError ('The image matrix given must be a valid PGM image matrix')
    
    new_image = [[]]
    new_image.pop(0)
    for row in image:
        new_image.append(image[0][:])
        
    for i in range(len(image)):
        new_image[len(image) -1 - i] = image[i]
        
    return new_image
 
def crop(image, top_left_row, top_left_coln, num_rows, num_colns):
    ''' (list<list>, int, int, int, int) --> list<list>
    Takes a (non-compressed) PGM image matrix, two non-negative integers and two positive integers as input.
    Returns an image matrix corresponding to the pixels contained in the target rectangle as specified by the crop integers given.
    If the input matrix is not a valid PGM image matrix, then an AssertionError with an appropriate error message is raised instead.
    
    >>> crop([[5, 5, 5], [5, 6, 6], [6, 6, 7]], 1, 1, 2, 2)
    [[6, 6], [6, 7]]
    
    >>> crop([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], 1, 0, 2, 3)
    [[4, 5, 6], [7, 8, 9]]
     
    >>> crop ([[1, 2, 3], [4, 5], [6, 7, 8]], 1, 1, 1, 1)
    Traceback (most recent call last):
    AssertionError: The image matrix given must be a valid PGM image matrix
    '''
    if not is_valid_image(image):
        raise AssertionError ('The image matrix given must be a valid PGM image matrix')
    
    new_image = [[]]
    new_image.pop(0) 
        
    for row in image:
        new_image.append(row[:])
    
    new_image = new_image[top_left_row:]
    
    
    for row in new_image:
        for i in range (top_left_coln):
            row.pop(0)
            
    while len(new_image) > num_rows:
        new_image.pop(-1)
    
    for row in new_image:
        while len(row) > num_colns:
            row.pop(-1)
        
    return new_image
 
def find_end_of_repetition(list_of_ints, index, target_num):
    ''' (list<int>, int, int) --> int
    Takes a list of integers and two non-negative integers (an index and a target number) as input.
    Looks through the list starting after the given index, and returns the index of the last consecutive occurrence of the target number.
    >>> find_end_of_repetition([5, 3, 5, 5, 5, -1, 0], 2, 5)
    4
    >>> find_end_of_repetition([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 6, 7)
    6
    >>> find_end_of_repetition([1, 1, 1, 1, 1, 1], 0, 1)
    5
    '''
    
    i = index
    while i < (len(list_of_ints)) and list_of_ints[i] == target_num:
        i += 1
    
    return (i-1)
    
def compress(image):
    ''' (list<list>) --> list<list>
    Takes a (non-compressed) PGM image matrix as input, compresses the matrix, and returns the compressed matrix.
    If the input matrix is not a valid PGM image matrix, then an AssertionError with an appropriate error message is raised instead.
 
    >>> compress([[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]])
    [['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']]
    
    >>> compress ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15]])
    Traceback (most recent call last):
    AssertionError: The image matrix given must be a valid PGM image matrix
    
    >>> compress([[1, 2, 3, 3, 3, 3], [4, 4, 4, 4, 5, 4], [7, 6, 6, 8, 7, 255]])
    [['1x1', '2x1', '3x4'], ['4x4', '5x1', '4x1'], ['7x1', '6x2', '8x1', '7x1', '255x1']]
    '''
    if not is_valid_image(image):
        raise AssertionError('The image matrix given must be a valid PGM image matrix')
    
    matrix = []
    
    width_of_image = len(image[0])
    all_coords = []
    
    for i in range (len(image)):
        row_coords = []
        for j in range (len(image[i])):
            row_coords.append(str(image[i][j]) + 'x' + str(find_end_of_repetition(image[i], j, image[i][j]) - j + 1))
            
        all_coords.append(row_coords)
                
    for k in range(len(all_coords)): 
        coord_row = [] 
        for l in range (len(all_coords[0])): 
             
             
            current_coord = all_coords[k][l] 
            x_index = current_coord.find('x') 
            pixel_val = current_coord[:x_index] 
             
            if l > 0: 
                last_coord = all_coords[k][l-1] 
                last_x_index = last_coord.find('x') 
                last_pixel_val = last_coord[:last_x_index] 
                 
                if pixel_val != last_pixel_val: 
                    coord_row.append(current_coord) 
            else: 
                coord_row.append(current_coord) 
        matrix.append(coord_row) 
        
    return matrix
    
def decompress(image):
    ''' (list<list>) --> list<list>
    Takes a compressed PGM image matrix as input. Decompresses the matrix by undoing the compression algorithm and returns the decompressed matrix.
    If the input matrix is not a valid compressed PGM image matrix, then an AssertionError is raised instead.
    
    >>> decompress([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']])
    [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]
    
    >>> decompress([["0x5x2", "200x2"], ["111x7"]])
    Traceback (most recent call last):
    AssertionError: The image matrix given must be a valid compressed PGM image matrix
    
    >>> decompress([['10x1', '11x2', '12x3'], ['13x4', '14x2'], ['255x3', '0x2', '255x1']])
    [[10, 11, 11, 12, 12, 12], [13, 13, 13, 13, 14, 14], [255, 255, 255, 0, 0, 255]]
    '''
    
    if not is_valid_compressed_image(image):
        raise AssertionError('The image matrix given must be a valid compressed PGM image matrix')
    matrix = []
    
    for i in range (len(image)):
        matrix_row = []
        for j in range (len(image[i])):
            obj = image[i][j]
            
            x_index = obj.find('x')
            
            pixel_var = int(obj[:x_index])
            num_reps = int(obj[x_index+1:])
            
            for k in range (num_reps):
                matrix_row.append(pixel_var)
            
        matrix.append(matrix_row)
    return (matrix)
 
def process_command(str_of_commands):
    ''' (str) --> None
    Takes a string as input corresponding to a series of space-separated image processing commands, and executes each command in turn.
    If an unrecognized command is part of the command string, a AssertionError should be raised with an appropriate error message.
    
    >>> process_command("LOAD<comp.pgm> CP DC INV INV SAVE<comp2.pgm>")
    >>> image = load_image("comp.pgm")
    >>> image2 = load_image("comp2.pgm")
    >>> image == image2
    True
    '''
    commands = str_of_commands.split(' ')
    load = commands[0]
    save = commands[-1]
    
    filename = load[load.find('<')+1:-1]
    new_filename = save[save.find('<')+1:-1]
    fobj = open(filename, 'w')
    
    image = load_image(filename)
    
    for command in commands:
        if command == 'INV':
            image = invert(image)
        elif command == 'FH':
            image = flip_horizontal(image)
        elif command == 'FV':
            image = flip_vertical(image)
        elif command == 'CR':
            top_left_row = int(command[3])
            top_left_coln = int(command[5])
            height = int(command[7])
            width = int(command[9])
            
            image = crop(image, top_left_row, top_left_coln, height, width)
            
        elif command == 'CP':
            image = compress(image)
        elif command == 'DC':
            image = decompress(image)
        else:
            raise AssertionError("One of the commands was invalid, the only valid commands are 'LOAD', 'SAVE', 'INV', 'FH', 'FV', 'CR', 'CP', and 'DC'.")
    
    fobj.close()
 
if __name__ == '__main__':
    doctest.testmod()
