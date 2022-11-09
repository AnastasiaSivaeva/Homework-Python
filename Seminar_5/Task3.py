#Создайте программу для игры в ""Крестики-нолики""

board = list(range(1,10))

def draw(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)


valid = False
player_choice = "X" or "O"
while not valid:
    player_pos = input("Куда поставим " + player_choice+"? ")
    try:
        player_pos = int(player_pos)
    except:
        print("Введите корректное число")
        continue
    if player_pos >= 1 and player_pos <= 9:
        if(str(board[player_pos-1]) not in "XO"):
            board[player_pos-1] = player_choice
            valid = True
        else:
            print("Эта клетка уже занята, выберите другую")
    else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def Exam(board):
   options = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in options:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    count = 0
    win = False
    while not win:
        draw(board)
        if count % 2 == 0:
           Exam("X")
        else:
           Exam("O")
        count += 1
        if count > 4:
           tmp = Exam(board)
           if tmp:
              print(tmp, "выиграл")
              win = True
              break
        
draw(board)
main(board)