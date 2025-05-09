"""Just simple toolkit used for basic sudoku generation & editing"""

ERROR_VAL_INIT = "Invalid value. E.g. 'sector_dimensions' are always > 2 and 'fill_charset' is > sector_dimensions[0]*sector_dimensions[1]"
ERROR_VAL_GET_N = "Invalid value. 'n' must always be > 0 and < sector's width*height when accessing rows and columns. Also value 'chr' should belong to 'fill_charset' and be 1 char length"

class Sudoku:
    """Sudoku class - used for everything"""
    def __init__(self, sector_dimensions : list[int] = [3,3], fill_charset : str = "123456789"):
        if sector_dimensions[0] >= 2 and sector_dimensions[1] >= 2 and len(fill_charset) >= sector_dimensions[0]*sector_dimensions[1]:
            self.__sector_width  = sector_dimensions[0]
            self.__sector_height = sector_dimensions[1]
            self.__fill_charset = fill_charset
            self.__grid = [[_] for _ in range((self.__sector_width*self.__sector_height)**2)]
        else:
            raise ValueError(ERROR_VAL_INIT)
    
    # Gets full grid
    def get_grid(self):
        return self.__grid
    
    # Gets row with idx N
    def get_row(self, n : int):
        if n > 0 and n <= self.__sector_width*self.__sector_height:
            return self.__grid[(n-1)*(self.__sector_width*self.__sector_height):n*(self.__sector_width*self.__sector_height)]
        else:
            raise ValueError(ERROR_VAL_GET_N)

    # Gets column with idx N
    def get_column(self, n : int):
        if n > 0 and n <= self.__sector_width*self.__sector_height:
            return self.__grid[n-1::(self.__sector_width*self.__sector_height)]
        else:
            raise ValueError(ERROR_VAL_GET_N)
    
    # Gets sector with idx N
    def get_sector(self, n : int):
        if n > 0 and n <= self.__sector_width*self.__sector_height:
            __t = []
            for i in range((n-1)//self.__sector_height*self.__sector_height+1, (n-1)//self.__sector_height*self.__sector_height+self.__sector_height+1, 1):
                __t.extend(self.get_row(i)[(self.__sector_height-1-(self.__sector_height*self.__sector_width-n)%self.__sector_height)*self.__sector_width : (self.__sector_height-1-(self.__sector_height*self.__sector_width-n)%self.__sector_height)*self.__sector_width + self.__sector_width])
            return __t
        else:
            raise ValueError(ERROR_VAL_GET_N)
    # Gets cell with idx N
    def get_cell(self, n : int):
        if n > 0 and n <= (self.__sector_width*self.__sector_height)**2:
            return self.__grid[n-1]
        else:
            raise ValueError(ERROR_VAL_GET_N)
    # Sets cell with idx N
    def set_cell(self, n : int, val : str):
        if n > 0 and n <= (self.__sector_width*self.__sector_height)**2 and len(val) == 1 and (val in self.__fill_charset):
            self.__grid[n-1][0] = val 
        else:
            raise ValueError(ERROR_VAL_GET_N)
