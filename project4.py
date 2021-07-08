import random
from graphics import *
class PuzzleWindow:
    """This class is responsible for window operations."""

    def __init__(self, board, width, difficulty):
        """This is the constructor method for PuzzleWindow class.
    
        Args:
            board: Board object of the game. Type: Board.
            width: Width of the Puzzle Window. Type: Integer.
        """
        self.board = board
        self.cell_width = width / board.n
        self.bottom_margin = width * 0.2

        self.win = GraphWin('CS177 - Sliding puzzle game', 
                                width, width + self.bottom_margin, autoflush=False)

        self.timer_text = Text(Point(width/2, width + self.bottom_margin/2), '')
        self.timer_text.setSize(32)
        self.timer_text.draw(self.win)

        self.is_started = False
        self.start_time = 0

        self.rect_matrix = []
        self.text_matrix = []

        for i in range(self.board.n):
            rect_row = []
            text_row = []
            for j in range(self.board.n):
                p1 = Point(self.cell_width * j, self.cell_width * i)
                p2 = Point(self.cell_width * (j+1), self.cell_width * (i+1))
        
                r = Rectangle(p1, p2)
                r.setFill('blue')

                t = Text(r.getCenter(), '')
                t.setSize(32)
                t.setFill('white')

                r.draw(self.win)
                t.draw(self.win)

                rect_row.append(r)
                text_row.append(t)

            self.rect_matrix.append(rect_row)
            self.text_matrix.append(text_row)

        self.update()
        self.win.getMouse()
        
        for i in range(difficulty):
            self.board.shuffle_one()
            self.update()    
        self.main_loop()

    def update(self):
        """This function updates the text in rectangles in the window.

        You are expected to call `setText()` function for each 
        self.text_matrix[i][j]. The value for each self.text_matrix[i][j] 
        is given in self.board.matrix[i][j].value.

        After you call `setText()` for each item in self.text_matrix, 
        you should call `self.win.update()`, at the end. 

        Only one call to `self.win.update()` is enough.
        """

        # TASK 1:
        #
        # Your code starts here.
        # ---------------------
        for i in range(len(self.board.matrix)):
            for j in range(len(self.board.matrix)):
                self.text_matrix[i][j].setText(self.board.matrix[i][j].value)
        self.win.update() 
        pass
        
        # ---------------------
        # Your code ends here.


    def get_click_position(self, point):
        """This function returns the row index, and column index
        (both 0-indexed) for the given click position.
        
        Args:
            point: A Point object that stores the click position. Type: graphics.Point.
        Returns:
            A tuple in the form of (i, j):
                i: The row index of the clicked rectangle. Type: Integer.
                j: The column index of the clicked rectangle. Type: Integer.

        HINT: You can use self.cell_width here.
        """

        # TASK 2:
        #
        # Your code starts here.
        # ---------------------
        string = str(self.win.getMouse()).replace('Point(','').replace(')','').split(',')
        i = (float(string[0])//(self.cell_width))
        j = (float(string[1])//(self.cell_width))
        cord = (int(i),int(j))
        return(cord)
        pass
        
        
        # ---------------------
        # Your code ends here.


    def main_loop(self):
        """This function is responsible of the main_loop of the game.

        1. It checks if there is a new mouse click, or a new key press.
        2. If there is a new mouse click:
            a. It makes the necessary updates in the board.
        3. If there is a new key press:
            a. It makes the necessary updates in the board.
        4. It calls `self.update()` function to udpate the window
           with the new values.
        5. After the game is done, it plays the animation.
        """
        while not self.board.done():
            p = self.win.checkMouse()
            key = self.win.checkKey()

            input_is_valid = False
            if p:
                i, j = self.get_click_position(p)
                if i < self.board.n and j < self.board.n:
                    input_is_valid = True
                    
                    self.board.play_click(i, j)
            if key:
                if key in ['Up', 'Right', 'Down', 'Left']:
                    input_is_valid = True

                    self.board.play_key(key)

            if input_is_valid:
                self.update()

                if self.is_started == False:
                    self.is_started = True
                    self.start_time = time.time()

            if self.is_started:
                self.timer_text.setText('%.2f' % (time.time() - self.start_time))

        self.score = time.time() - self.start_time
        self.animation()

    def get_random_color(self):
        """This function returns a random color.
        
        1. Pick three random integer values between 0 and 255 (both inclusive).
        2. Generate the color object using the above three random integers using
           `color_rgb(r, g, b)` function.

        Returns:
            A random color. Type: graphics.color_rgb() function return type.
        """

        # TASK 3:
        #
        # Your code starts here.
        # ---------------------
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return (str(r),str(g),str(b))
        pass
        
        
        # ---------------------
        # Your code ends here.

    def paint_with_random_colors(self):
        """This function paints every rectangle and text in
        self.rect_matrix and self.text_matrix respectively with random colors.
        
        You can use `setFill()` function on each self.rect_matrix[i][j] and 
        self.text_matrix[i][j].

        You can use self.get_random_color() to produce a random color.

        After you call `setFill()` for each item in self.rect_matrix, and
        self.text_matrix, you should call `self.win.update()`, at the end. 

        Only one call to `self.win.update()` is enough.
        """

        # TASK 4:
        #
        # Your code starts here.
        # ---------------------
        for i in range(len(self.board.matrix)):
            for j in range(len(self.board.matrix)):
                l = self.get_random_color()
                self.text_matrix[i][j].setFill(color_rgb(int(l[0]),int(l[1]),int(l[2])))
                l = self.get_random_color()
                self.rect_matrix[i][j].setFill(color_rgb(int(l[0]),int(l[1]),int(l[2])))
        self.win.update() 
        pass
        
        
        # ---------------------
        # Your code ends here.

    def animation(self):
        """This function makes an animation with painting the window with random
        colors repeatedly 100 times.

        Basically write a loop that calls `self.paint_with_random_colors()`
        100 times.
        """

        # TASK 5:
        #
        # Your code starts here.
        # ---------------------
        
        for x in range(0,100):
            self.paint_with_random_colors()
            self.win.update()
        pass
        
        
        # ---------------------
        # Your code ends here.


class Board:
    """This class is responsible for storing the state of the board and also
       has some operations we need to perform over the board.
    """
    def __init__(self, n):
        """This is the constructor method for Board class.
    
        Args:
            n: The value of n to create the board. The board will be n x n.
               Type: Integer.
        """
        self.n = n
        self.matrix = []

        for i in range(n):
            row = []
            for j in range(n):
                c = Cell(str(i*n + j + 1), i, j, self)
                row.append(c)
            self.matrix.append(row)

        self.matrix[-1][-1].value = ''
        
        self.empty_cell = self.matrix[-1][-1]

    def shuffle_one(self):
        """This function is used to shuffle cells to make a random state of the
        game. This function only makes one random move. More specifically:

        1. Get the neighbors of `self.empty_cell`. You can use
           `get_neighbor_cells()` function.
        2. Pick a random neighbor using `random.choice()` function.
        3. Call self.play_click with the given indices of chosen random cell 
           in above step.

        Example:

        Input:

        1 2 3
        4 5 6 
        7 8 
        
        Possible outputs:

        1 2 3       1 2 3
        4 5     or  4 5 6
        7 8 6       7   8

        Input:

        1   6 
        4 3 7  
        8 5 2
    
        Possible outputs:

          1 6       1 6        1 3 6
        4 3 7   or  4 3 7  or  4   7
        8 5 2       8 5 2      8 5 2

        """

        # TASK 6:
        #
        # Your code starts here.
        # ---------------------
        rand = random.choice(self.empty_cell.get_neighbor_cells())
        print(rand)
        self.play_click(rand[1],rand[0])
        pass
        
        
        # ---------------------
        # Your code ends here.

    def play_click(self, i, j):
        """This function is used when a click occurs. 

        You are supposed to:

        1. Check if the empty cell is one of the neighbors of the clicked cell.
           Remember, `self.matrix[i][j].get_neighbor_cells()` gives you
           the neighbors of the `self.matrix[i][j]`.

           Also, `self.empty_cell` is a type Cell object which contains the empty
           cell. For example, `self.empty_cell.i` and `self.empty_cell.j` are the row and
           column indices of the empty cell, respectively.

        2. If there is an empty cell in the neighbors of the clicked cell:
            a. Swap `self.matrix[i][j]` and 
               `self.matrix[self.empty_cell.i][self.empty_cell.j]` in `self.matrix`.
            b. Update the coordinates of `self.empty_cell` and the swapped cell
               using `set_coordinate()` function. Remember, before we do the swapping operation,
               the coordinates of the two swapped cells were: (i, j) and 
               (self.empty_cell.i, self.empty_cell.j) respectively.

        Args:
            i: Row-index for the clicked cell. (0-based index.) Type: Integer
            j: Column-index for the clicked cell. (0-based index.) Type: Integer
        """

        # TASK 7:
        #
        # Your code starts here.
        # ---------------------
        val_empty = (self.matrix[self.empty_cell.i][self.empty_cell.j].value)
        val_click = (self.matrix[i][j].value)
        self.matrix[i][j].value = val_empty
        self.matrix[i][j].set_coordinate(self.empty_cell.i,self.empty_cell.j)
        self.matrix[self.empty_cell.i][self.empty_cell.j].value = val_click
        self.matrix[self.empty_cell.i][self.empty_cell.j].set_coordinate(i,j)
        
        pass
        
        
        # ---------------------
        # Your code ends here.

    def play_key(self, key):
        """This function is used when a key press occurs.

        In addition to playing the game using the mouse with clicking the
        cells, players can also play the game using the keyboard with 'Up', 'Right', 
        'Down' and 'Left' keys.

        When a user presses one arrow key in the keyboard, the logic of the game
        is supposed to be as follows. We push the corresponding cell in the given 
        direction through the empty cell. Examples:

        1   6               1 6 
        4 3 7  + 'Left'  => 4 3 7
        8 5 2               8 5 2

        1   6               1 3 6 
        4 3 7  + 'Up'    => 4   7
        8 5 2               8 5 2

        1   6                 1 6 
        4 3 7  + 'Right' => 4 3 7
        8 5 2               8 5 2

          1 6                 1 6 
        4 3 7  + 'Right' => 4 3 7  (no change)
        8 5 2               8 5 2

        HINT: You can use `self.play_click()` function here. You only
        need to compute the corresponding row and column index that produces
        the same effect with the above logic. For example, in the above first
        example, pressing 'Left' on the keyboard equals to clicking the cell
        contains '6'. More specifically, calling `self.play_click(0, 2)`.
    
        Args:
            key: 'Up' or 'Right' or 'Down' or 'Left'. Type: String
        """

        # TASK 8:
        #
        # Your code starts here.
        # ---------------------
        for i in key:
            if e in score.keys():
                mine = e
                mins = score[e]
        return e
        
        
        pass
        
        
        # ---------------------
        # Your code ends here.

    def done(self):
        """This function checks whether the game is done.

        The game is done if every value is in order. Example:

        1 2 3
        4 5 6
        7 8 

        You are supposed to check every value of self.matrix[i][j].value
        and check they are in order.

        Remember, the values in self.matrix[i][j].value are string values and
        one of them is empty string (''). If you use string comparison, it will
        not be accurate. Because, example: '5' < '13'.

        So, you should convert the values to integer before you compare (sort) them.

        In this particular puzzle game, we expect that the empty string is at the
        very end. (last row and last column.) Some other online puzzle games expect 
        the empty string to be in the beginning, it's just a design choice.
        """

        # TASK 9:
        #
        # Your code starts here.
        # ---------------------
        num = 1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j].value == str(num):
                    num = num + 1
                    if num == 9:
                        return True
        
                else:
                    num = 1
        
        pass
        
        
        # ---------------------
        # Your code ends here.

class Cell:
    """This is the constructor method for Cell class.
    
        Args:
            value: The value for this cell. Type: String.
                   Examples: '3', '5', '13', ''.
            i: The row index for this cell. Type: Integer.
            j: The column index for this cell. Type: Integer.
            board: The board that this cell in. Type: Board.
    """
    def __init__(self, value, i, j, board):
        self.value = value
        self.i = i
        self.j = j
        self.board = board

    def get_neighbor_cells(self):
        """This function returns the neighbors of the cell.

        Neighbors are defined to be on the north, east, south, and west
        of the cell.

        Note that the number of neighbors one cell may have is either two, 
        three or four.

        Example:
    
        1 2 3
        4 5 6
        7 8 
    
        Neighbor cells of 1: 2 and 4.
        Neighbor cells of 2: 1, 3 and 5.
        Neighbor cells of 5: 2, 4, 6 and 8.

        Returns:
            A list of Cell objects which are neighbor to `self`.
        """

        # TASK 10:
        #
        # Your code starts here.
        # ---------------------
        x = self.i
        y = self.j
        neighbor = []
        if x+1 in range(x-1,x+1):
            neighbor.append([x+1,y])
        if x-1 in range(x-1,x+1):
            neighbor.append([x-1,y])
        if y+1 in range(y-1,y+1):
            neighbor.append([x,y+1])
        if y-1 in range(y-1,y+1):
            neighbor.append([x,y-1])
        return neighbor
        pass
        
        
        # ---------------------
        # Your code ends here.

    def set_coordinate(self, i, j):
        """This is a convenience function."""
        self.i = i
        self.j = j

class TopScores:
    """This class contains operations about top scores.
    """
    def __init__(self, file_name, k):
        """This is the constructor method for TopScores class.
        
        Args:
            file_name: The filename of the top scores list. Type: String.
            k: Number of top score entries we want to store. Type: Integer.
        """
        self.file_name = file_name
        self.scores = []
        self.k = k
        with open(self.file_name) as f:
            for line in f:
                name, score = line.split(',')
                score = float(score)
                self.scores.append([name, score])
        self.scores.sort(key=lambda x:x[1])

    def add_score(self, new_name, new_score):
        """This function adds a new score to `self.scores` list.
        
        `self.scores` is a list contains sublists of form: [name, score]
        where name is a string and score is float.

        You should make sure that after you add the new name and score
        to `self.scores`, you should preserve that it is ordered by score,
        in increasing order.
        
        Another import point is that, if there are more then `self.k` sublists
        in `self.scores` list, then, you should only take the first `self.k`
        items which has the smallest scores.

        Args:
            new_name: New name to add in `self.scores` list. Type: String.
            new_score: New score to add in `self.scores` list. Type: Float.
        """

        # TASK 11:
        #
        # Your code starts here.
        # ---------------------
        self.scores.append([new_name, new_score])
        
        pass
        
        
        # ---------------------
        # Your code ends here.

    def write_scores(self):
        """Writes scores to the file `self.file_name`.

        It overrides the previous content of `self.file_name`
        and writes the new scores given in `self.scores` in the following format:

        name_1,score_1
        name_2,score_2
        ...
        name_k,score_k

        Scores should only contain two decimal points. e.g., 9.15, 12.23, etc.
        """

        # TASK 12:
        #
        # Your code starts here.
        # ---------------------
        file = open((self.file_name),'a')
        file.write(str(self.scores[0],self.scores[1]))
        file.close
        
        pass
        
        
        # ---------------------
        # Your code ends here.

    def print_scores(self):
        """Print scores in `self.scores` line by line in the following format:

        Nickname       Score
        --------------------
        george         2.63
        jennifer       9.45
        sait           10.40
        jessica        25.30
        miguel         31.90
    
        Note that the maximum number of characters a nickname
        can have is 15.

        HINT: You can use `ljust()` function.
        Example: 'hello'.ljust(10) returns 'hello     '.
        """

        # TASK 13:
        #
        # Your code starts here.
        # ---------------------
        print('{0:15}{1:6}'.format('Nickname','Score'))
        file = open('top_scores.txt','r')
        readfile = file.read()
        print(readfile.replace(',','     '))
        file.close()
        pass
        
        
        # ---------------------
        # Your code ends here.

def main():
    """The main function for the game."""
    name = input('Your nickname: ')
    print('Please click window to shuffle.')

    b = Board(3)
    w = PuzzleWindow(b, 300, 100)
    w.win.close()

    top_scores = TopScores('top_scores.txt', 5)

    top_scores.add_score(name, w.score)
    top_scores.write_scores()
    top_scores.print_scores()

if __name__ == '__main__':
    main()
