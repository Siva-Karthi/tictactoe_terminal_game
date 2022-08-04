class TicTacToe2():
    holded = {
    }
    Board = [["" for _ in range(3) ] for _ in range(3)]
    user = False
    user_0_mark = "O"
    user_1_mark = "X"
    winner = None
    def __int__(self):
        pass

    def get_input(self, user):
        r = int(input(" User " + str(int(self.user)) + "select the row "))
        c = int(input(" User " + str(int(self.user)) + "select the column "))
        return r, c

    def play(self):
        self.select_key()
        self.print_board()
        while not self.validate_success() and not self.validate_filled():
            r,c = self.get_input(self.user)
            if (r,c) in self.holded:
                print("Invalid selection", r, c , " is already selected")
                continue
            # lock position
            self.holded[r, c] = True
            # set key
            if self.user:
                self.Board[r][c] = self.user_0_mark
            else:
                self.Board[r][c] = self.user_1_mark
            # show board
            self.print_board()
            if self.validate_success():
                # self.winner = self.user
                print(int(self.user), " Won the game :)")
                # break
            elif self.validate_filled():
                print("Game ended :(")
            else:
                # change user
                self.user = not self.user

    # return true if anyone success
    def validate_success(self):
        # validate rows
        if self.Board[0][0] == self.Board[0][1] == self.Board[0][2] and self.Board[0][0] != "":
            return True
        elif self.Board[1][0] == self.Board[1][1] == self.Board[1][2] and self.Board[1][0] !="":
            return True
        elif self.Board[2][0] == self.Board[2][1] == self.Board[2][2] and self.Board[2][0] !="":
            print("here")
            return True

        # any column is filled
        if self.Board[0][0] == self.Board[1][0] == self.Board[2][0] and self.Board[0][0] !="":
            return True
        elif self.Board[0][1] == self.Board[1][1] == self.Board[2][1] and  self.Board[0][1] != "":
            print("here")
            return True
        elif self.Board[0][2] == self.Board[1][2] == self.Board[2][2] and  self.Board[0][2] != "":
            return True

            # any diagonal filled
        if self.Board[0][0] == self.Board[1][1] == self.Board[2][2] and self.Board[0][0] != "" :
            return True
        elif self.Board[0][2] ==  self.Board[1][1] ==  self.Board[2][0] and self.Board[0][2] != "":
            return True

    # return true if filled
    def validate_filled(self):
        if len(self.holded) == 9:
            return True

    def print_board(self):
        print("---------", end="\n")
        for i in self.Board:
            for j in i:
                print(j, "|", end=" ")
            print("\n")
            print("---------", end="\n")

    def select_key(self):
        while True:
            inp = input("User " + str(int(self.user)) + " Please select X or O : ")
            if inp not in ["X", "O"]:
                print("Invalid selection")
                continue
            self.user_0_mark = inp
            if self.user_0_mark == "X":
                self.user_1_mark = "O"
            else:
                self.user_1_mark = "X"
            print("User 1 yours key coin is ", self.user_1_mark)
            break
        return

if __name__ == '__main__':
    obj = TicTacToe2()
    obj.play()
