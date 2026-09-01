class PieceType:
    PAWN = 'Pawn'
    ROOK = 'Rook'
    KNIGHT = 'Knight'
    BISHOP = 'Bishop'
    QUEEN = 'Queen'
    KING = 'King'

class Piece:
    def __init__(self, piece_type: PieceType, color, position):
        if not isinstance(piece_type, PieceType):
            raise ValueError("Invalid piece type")

        self.piece_type = piece_type
        self.color = color
        self.position = position

class Square: 
    def __init__(self, position):
        self.position = position
        self.piece = None

class Chessboard:
    def __init__(self):
        self.squares = [[Square((row, col)) for col in range(8)] for row in range(8)]
        self.setup_pieces()
    
    def setup_pieces(self):
        # Set up pawns
        for col in range(8):
            self.squares[1][col].piece = Piece(PieceType.PAWN, 'black', (1, col))
            self.squares[6][col].piece = Piece(PieceType.PAWN, 'white', (6, col))

        # Set up rooks
        self.squares[0][0].piece = Piece(PieceType.ROOK, 'black', (0, 0))
        self.squares[0][7].piece = Piece(PieceType.ROOK, 'black', (0, 7))
        self.squares[7][0].piece = Piece(PieceType.ROOK, 'white', (7, 0))
        self.squares[7][7].piece = Piece(PieceType.ROOK, 'white', (7, 7))

        # Set up knights
        self.squares[0][1].piece = Piece(PieceType.KNIGHT, 'black', (0, 1))
        self.squares[0][6].piece = Piece(PieceType.KNIGHT, 'black', (0, 6))
        self.squares[7][1].piece = Piece(PieceType.KNIGHT, 'white', (7, 1))
        self.squares[7][6].piece = Piece(PieceType.KNIGHT, 'white', (7, 6))

        # Set up bishops
        self.squares[0][2].piece = Piece(PieceType.BISHOP, 'black', (0, 2))
        self.squares[0][5].piece = Piece(PieceType.BISHOP, 'black', (0, 5))
        self.squares[7][2].piece = Piece(PieceType.BISHOP, 'white', (7, 2))
        self.squares[7][5].piece = Piece(PieceType.BISHOP, 'white', (7, 5))

        # Set up queens
        self.squares[0][3].piece = Piece(PieceType.QUEEN, 'black', (0, 3))
        self.squares[7][3].piece = Piece(PieceType.QUEEN, 'white', (7, 3))

        # Set up kings
        self.squares[0][4].piece = Piece
