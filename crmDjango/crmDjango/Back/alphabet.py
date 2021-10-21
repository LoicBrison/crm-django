from enum import Enum

class Alphabet(Enum):
    A ="abcdefghijklmnopqrstuvwxyz"
    B ="bcdefghijklmnopqrstuvwxyza"
    C ="cdefghijklmnopqrstuvwxyzab"
    D ="defghijklmnopqrstuvwxyzabc"
    E ="efghijklmnopqrstuvwxyzabcd"
    F ="fghijklmnopqrstuvwxyzabcde"
    G ="ghijklmnopqrstuvwxyzabcdef"
    H ="hijklmnopqrstuvwxyzabcdefg"
    I ="ijklmnopqrstuvwxyzabcdefgh"
    J ="jklmnopqrstuvwxyzabcdefghi"
    K ="klmnopqrstuvwxyzabcdefghij"
    L ="lmnopqrstuvwxyzabcdefghijk"
    M ="mnopqrstuvwxyzabcdefghijkl"
    N ="nopqrstuvwxyzabcdefghijklm"
    O ="opqrstuvwxyzabcdefghijklmn"
    P ="pqrstuvwxyzabcdefghijklmno"
    Q ="qrstuvwxyzabcdefghijklmnop"
    R ="rstuvwxyzabcdefghijklmnopq"
    S ="stuvwxyzabcdefghijklmnopqr"
    T ="tuvwxyzabcdefghijklmnopqrs"
    U ="uvwxyzabcdefghijklmnopqrst"
    V ="vwxyzabcdefghijklmnopqrstu"
    W ="wxyzabcdefghijklmnopqrstuv"
    X ="xyzabcdefghijklmnopqrstuvw"
    Y ="yzabcdefghijklmnopqrstuvwx"
    Z ="zabcdefghijklmnopqrstuvwxy"

    
    def get(c):
        switcher={
                'A' :"abcdefghijklmnopqrstuvwxyz",
                'B' :"bcdefghijklmnopqrstuvwxyza",
                'C' :"cdefghijklmnopqrstuvwxyzab",
                'D' :"defghijklmnopqrstuvwxyzabc",
                'E' :"efghijklmnopqrstuvwxyzabcd",
                'F' :"fghijklmnopqrstuvwxyzabcde",
                'G' :"ghijklmnopqrstuvwxyzabcdef",
                'H' :"hijklmnopqrstuvwxyzabcdefg",
                'I' :"ijklmnopqrstuvwxyzabcdefgh",
                'J' :"jklmnopqrstuvwxyzabcdefghi",
                'K' :"klmnopqrstuvwxyzabcdefghij",
                'L' :"lmnopqrstuvwxyzabcdefghijk",
                'M' :"mnopqrstuvwxyzabcdefghijkl",
                'N' :"nopqrstuvwxyzabcdefghijklm",
                'O' :"opqrstuvwxyzabcdefghijklmn",
                'P' :"pqrstuvwxyzabcdefghijklmno",
                'Q' :"qrstuvwxyzabcdefghijklmnop",
                'R' :"rstuvwxyzabcdefghijklmnopq",
                'S' :"stuvwxyzabcdefghijklmnopqr",
                'T' :"tuvwxyzabcdefghijklmnopqrs",
                'U' :"uvwxyzabcdefghijklmnopqrst",
                'V' :"vwxyzabcdefghijklmnopqrstu",
                'W' :"wxyzabcdefghijklmnopqrstuv",
                'X' :"xyzabcdefghijklmnopqrstuvw",
                'Y' :"yzabcdefghijklmnopqrstuvwx",
                'Z' :"zabcdefghijklmnopqrstuvwxy"
                }
        return switcher.get(c,"Invalid char")