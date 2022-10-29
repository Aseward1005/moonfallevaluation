import numpy as np
import sys
class MatrixOps:
    def __init__(self, seed=None):
        # We use a predetermined seed to evaluate correct implementation
        if seed:
            np.random.seed(seed)

        self._matrix = np.random.randint(0,10, size=(10,10))
        self._kernel = np.random.randint(-2,2, size=(3,3))
    
    def largest_index(self, matrix):
        #''' Make this function return a tuple of the (row, col) 
            #index of the largest value in the matrix '''
        max = -sys.maxsize - 1 #set max to the smallest possible size
        out = (0, 0)           #initialize the output

        for i in range(0, matrix.shape[0]):
            for j in range(0, matrix.shape[1]): #assume the matrix is square
                if (matrix[i, j] > max):
                    max = matrix[i, j]
                    out = (i, j)

        return out

    def convolve(self, kernel, matrix):
        #''' Make this function return the result of a 2D convolution '''
        #flip the kernel
        kernel = np.flip(kernel, 0)
        kernel = np.flip(kernel, 1)
        #math stuff
        #to determine which parts of the kernel overlap where:
        #assuming a 3x3 kernel
        #kernel[1][1] = matrix[i][j]
        #kernel[0][0] = matrix[i-1][j-1]
        #kernel[n][m] = matrix[i + n-1][j + m-1]
        matrix2 = np.zeros((matrix.shape[0]+2, matrix.shape[1]+2))
        for i in range(-1, matrix.shape[0] + 1):
            for j in range(-1, matrix.shape[1] + 1):
                sum = 0
                for ki in range(0, kernel.shape[0]):
                    for kj in range(0, kernel.shape[1]):
                        if ((i + ki-1) < 0 or (i + ki-1) >= matrix.shape[0] or (j + kj-1) < 0 or (j + kj-1) >= matrix.shape[1]): #if out of range
                            sum += 0
                        else:
                            sum += matrix[(i + ki-1), (j + kj-1)] * kernel[ki, kj]
                matrix2[i+1, j+1] = sum


        #with parallel programming, this is much faster. 
        #each part of the process doesn't need to know about what's going on in other parts of the process
        #this makes it highly parallelizable
        #the convolution equation can be done in chunks of the matrix all at once (likely faster)
        #or alternatively, the multiplication can be done in parallel and the sum done back in main
        #given more time, I could probably implement this

        return matrix2

    def run(self):
        print("Largest index is at ", self.largest_index(self._matrix))
        
        print("Result of convolution:")
        print(self.convolve(self._kernel, self._matrix))


if __name__ == "__main__":
    # If this file is run directly from the command line, run a test of the program
    m = MatrixOps()


    print("Running with matrix ")
    print(m._matrix)
    print("and kernel ")
    print(m._kernel)

    m.run() 