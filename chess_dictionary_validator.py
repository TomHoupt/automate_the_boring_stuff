## chess_dictionary_validator.py

# Write a function named is_valid_chess_board() that takes a dictionary argument and returns True or False
# depending on if the board is valid.
# A valid board will have exactly one black king and exactly one white king. Each player can only have
# at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h';
# that is, a piece can’t be on space '9z'. The piece names begin with either a 'w' or 'b' to represent
# white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
# This function should detect when a bug has resulted in an improper chess board.

import pprint

## DEFINE THE BOARD SET UP FOR WHITE AND BLACK USING A DICTIONARY
chess_board = {
'1a': 'wrook',
'1b': 'wknight',
'1c': 'wbishop',
'1d': 'wqueen',
'1e': 'wking',
'1f': 'wbishop',
'1g': 'wknight',
'1h': 'wrook',
'2a': 'wpawn',
'2b': 'wpawn',
'2c': 'wpawn',
'2d': 'wpawn',
'2e': 'wpawn',
'2f': 'wpawn',
'2g': 'wpawn',
'2h': 'wpawn',
'8a': 'brook',
'8b': 'bknight',
'8c': 'bbishop',
'8d': 'bqueen',
'8e': 'bking',
'8f': 'bbishop',
'8g': 'bknight',
'8h': 'brook',
'7a': 'bpawn',
'7b': 'bpawn',
'7c': 'bpawn',
'7d': 'bpawn',
'7e': 'bpawn',
'7f': 'bpawn',
'7g': 'bpawn',
'7h': 'bpawn'}

##A FUNCTION TO CHECK IF THE PIECES IN THE DICTIONARY ARE ALL IN A VALID SPOT ON THE BOARD
def pieces_in_valid_place():
    for k in chess_board.keys():
        key_first_char = str(k[0])
        key_int = int(key_first_char)
        key_second_char = str(k[1])
    if key_int < 9 and key_second_char < 'i':
        global valid_spots
        valid_spots = True
    else:
        print('The places the pieces exists are NOT valid')

pieces_in_valid_place()

#now you need to check to see if each player has only 16 pieces (that there is only 16 'b' or 'w' pieces)
##A FUNCTION TO CHECK IF BOTH WHITE AND BLACK HAVE 16 PIECES
def number_of_pieces_per_player():
    pieces_values_list = list(chess_board.values())
    first_characters = [item[0] for item in pieces_values_list]
    individual_chars = ''.join(first_characters)

    count = {}
    for char in individual_chars:
        count.setdefault(char, 0)
        count[char] = count[char] + 1

    piece_number = list(count.values())
    w = piece_number[0]
    b = piece_number[1]

    if w == 16 and b == 16:
        global pieces_per_player
        pieces_per_player = True
    else:
        print("Incorrect number of pieces for each player")

number_of_pieces_per_player()

##A FUNCTION TO SEE IF BOTH BLACK AND WHITE HAVE 8 PAWNS EACH AND 1 KING EACH
def correct_pawn_and_king_amount_for_each_player():
    type_of_piece = list(chess_board.values())

    count = {}
    for i in type_of_piece:
        count.setdefault(i, 0)
        count[i] = count[i] + 1

    wpawn_amount = count.get('wpawn')
    bpawn_amount = count.get('bpawn')
    wking_amount = count.get('wking')
    bking_amount = count.get('bking')

    if wpawn_amount <= 8 and bpawn_amount <= 8 and wking_amount == 1 and bking_amount ==1:
        global correct_pawn_and_king_amount
        correct_pawn_and_king_amount = True
    else:
        print("Invalid board. Too many pawns for one player")


correct_pawn_and_king_amount_for_each_player()

##A FUNCTION THAT CHECKS TO SEE IF THE OTHER FUNCTIONS RESULT IN TRUE. IF THEY DO, PRINT TRUE
def is_valid_chess_board():
    if valid_spots == True and pieces_per_player == True and correct_pawn_and_king_amount == True:
        print(True)
        print('This is a valid board setup')

is_valid_chess_board()
