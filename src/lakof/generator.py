import fontforge
from lakof.components import *

def lakof_generator(font, weight):
    if weight == "Thin":
        fontweight = 50
    elif weight == "Regular":
        fontweight = 100
    elif weight == "Bold":
        fontweight = 150
    else:
        fontweight = 100

    width = fontweight + 350
    fw = fontweight
    wd = width

    # -- 小文字 a-z --

    glyph = font.createChar(ord("a"), "a")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    shortHorizontalBar(pen, fw, wd)  # 変更
    shortUpwardTail(pen, fw, wd)     # 追加

    glyph = font.createChar(ord("b"), "b")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortestUpperrightCircle(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("c"), "c")
    pen = glyph.glyphPen()
    downwardDoublecurve(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)

    glyph = font.createChar(ord("d"), "d")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortestUpperleftCircle(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)

    glyph = font.createChar(ord("e"), "e")
    pen = glyph.glyphPen()
    rightCircle(pen, fw, wd)
    shortestLowerrightCircle(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)

    glyph = font.createChar(ord("f"), "f")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("g"), "g")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardDoublecurve(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("h"), "h")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("i"), "i")
    pen = glyph.glyphPen()
    shortestUpperleftCircle(pen, fw, wd)
    shortHorizontalBar(pen, fw, wd)
    iTail(pen, fw, wd)

    glyph = font.createChar(ord("j"), "j")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("k"), "k")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardDoublecurve(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("l"), "l")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("m"), "m")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortForwardslashBar(pen, fw, wd)
    shortRightVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("n"), "n")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortForwardslashBar(pen, fw, wd)
    shortRightVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("o"), "o")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    shortHorizontalBar(pen, fw, wd)
    rightCircle(pen, fw, wd)

    glyph = font.createChar(ord("p"), "p")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("q"), "q")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    longUpwardTail(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    rightDownwardCurve(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("r"), "r")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("s"), "s")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    shortDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("t"), "t")
    pen = glyph.glyphPen()
    upwardDoublecurve(pen, fw, wd)
    shortRightestConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)

    glyph = font.createChar(ord("u"), "u")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    longForwardslashBar(pen, fw, wd)

    glyph = font.createChar(ord("v"), "v")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    longUpwardTail(pen, fw, wd)

    glyph = font.createChar(ord("w"), "w")
    pen = glyph.glyphPen()
    rightCircle(pen, fw, wd)
    shortestUpperleftCircle(pen, fw, wd)
    shortBelowVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("x"), "x")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortBelowHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("y"), "y")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    shortestLowerrightCircle(pen, fw, wd)
    shortAboveVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("z"), "z")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    longDownwardTail(pen, fw, wd)

    # -- 大文字 A-Z --

    glyph = font.createChar(ord("A"), "A")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    shortHorizontalBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)

    glyph = font.createChar(ord("B"), "B")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("C"), "C")
    pen = glyph.glyphPen()
    downwardDoublecurve(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)

    glyph = font.createChar(ord("D"), "D")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortestUpperleftCircle(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)

    glyph = font.createChar(ord("E"), "E")
    pen = glyph.glyphPen()
    rightCircle(pen, fw, wd)
    shortestLowerrightCircle(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)

    glyph = font.createChar(ord("F"), "F")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("G"), "G")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardDoublecurve(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("H"), "H")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("I"), "I")
    pen = glyph.glyphPen()
    shortestUpperleftCircle(pen, fw, wd)
    shortHorizontalBar(pen, fw, wd)
    iTail(pen, fw, wd)

    glyph = font.createChar(ord("J"), "J")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("K"), "K")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardDoublecurve(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("L"), "L")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("M"), "M")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortForwardslashBar(pen, fw, wd)
    shortRightVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("N"), "N")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortForwardslashBar(pen, fw, wd)
    shortRightVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("O"), "O")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    shortHorizontalBar(pen, fw, wd)
    rightCircle(pen, fw, wd)

    glyph = font.createChar(ord("P"), "P")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("Q"), "Q")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    longUpwardTail(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    rightDownwardCurve(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("R"), "R")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("S"), "S")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    shortDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("T"), "T")
    pen = glyph.glyphPen()
    upwardDoublecurve(pen, fw, wd)
    shortRightestConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)

    glyph = font.createChar(ord("U"), "U")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    longForwardslashBar(pen, fw, wd)

    glyph = font.createChar(ord("V"), "V")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    longUpwardTail(pen, fw, wd)

    glyph = font.createChar(ord("W"), "W")
    pen = glyph.glyphPen()
    rightCircle(pen, fw, wd)
    shortestUpperleftCircle(pen, fw, wd)
    shortBelowVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("X"), "X")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortBelowHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("Y"), "Y")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    shortestLowerrightCircle(pen, fw, wd)
    shortAboveVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("Z"), "Z")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    longDownwardTail(pen, fw, wd)

    # -- 記号類 --

    # ! (感嘆符)
    glyph = font.createChar(ord("!"), "exclamation")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortDownwardTail(pen, fw, wd)

    # ? (疑問符)
    glyph = font.createChar(ord("?"), "question")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    upwardCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)

    # , (コンマ)
    glyph = font.createChar(ord(","), "comma")
    pen = glyph.glyphPen()
    shortDownwardTail(pen, fw, wd)

    # . (ピリオド)
    glyph = font.createChar(ord("."), "period")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)

    # : (コロン)
    glyph = font.createChar(ord(":"), "colon")
    pen = glyph.glyphPen()
    # 上の点
    pen.moveTo(wd*0.5, 600)
    pen.lineTo(wd*0.5 + fw, 600)
    pen.lineTo(wd*0.5 + fw, 600 - fw)
    pen.lineTo(wd*0.5, 600 - fw)
    pen.closePath()
    # 下の点
    pen.moveTo(wd*0.5, 300)
    pen.lineTo(wd*0.5 + fw, 300)
    pen.lineTo(wd*0.5 + fw, 300 - fw)
    pen.lineTo(wd*0.5, 300 - fw)
    pen.closePath()

    # ; (セミコロン)
    glyph = font.createChar(ord(";"), "semicolon")
    pen = glyph.glyphPen()
    # 上の点
    pen.moveTo(wd*0.5, 600)
    pen.lineTo(wd*0.5 + fw, 600)
    pen.lineTo(wd*0.5 + fw, 600 - fw)
    pen.lineTo(wd*0.5, 600 - fw)
    pen.closePath()
    # 下の尾
    shortDownwardTail(pen, fw, wd)

    # - (ハイフン)
    glyph = font.createChar(ord("-"), "hyphen")
    pen = glyph.glyphPen()
    shortHorizontalBar(pen, fw, wd)

    # _ (アンダースコア)
    glyph = font.createChar(ord("_"), "underscore")
    pen = glyph.glyphPen()
    pen.moveTo(0, 100)
    pen.lineTo(wd, 100)
    pen.closePath()

    # @ (アットマーク)
    glyph = font.createChar(ord("@"), "at")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)

    # # (シャープ)
    glyph = font.createChar(ord("#"), "numbersign")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortHorizontalBar(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)

    # $ (ドル記号)
    glyph = font.createChar(ord("$"), "dollar")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)

    # % (パーセント)
    glyph = font.createChar(ord("%"), "percent")
    pen = glyph.glyphPen()
    shortForwardslashBar(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    # & (アンパサンド)
    glyph = font.createChar(ord("&"), "ampersand")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardDoublecurve(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    # * (アスタリスク)
    glyph = font.createChar(ord("*"), "asterisk")
    pen = glyph.glyphPen()
    shortRightConnectcurveBar(pen, fw, wd)
    upwardCurve(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)

    # ( (左括弧)
    glyph = font.createChar(ord("("), "parenleft")
    pen = glyph.glyphPen()
    downwardCurve(pen, fw, wd)

    # ) (右括弧)
    glyph = font.createChar(ord(")"), "parenright")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)

    # [ (左角括弧)
    glyph = font.createChar(ord("["), "bracketleft")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)

    # ] (右角括弧)
    glyph = font.createChar(ord("]"), "bracketright")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)

    # { (左波括弧)
    glyph = font.createChar(ord("{"), "braceleft")
    pen = glyph.glyphPen()
    downwardDoublecurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)

    # } (右波括弧)
    glyph = font.createChar(ord("}"), "braceright")
    pen = glyph.glyphPen()
    upwardDoublecurve(pen, fw, wd)
    shortLeftConnectcurveBar(pen, fw, wd)

    # < (小なり)
    glyph = font.createChar(ord("<"), "less")
    pen = glyph.glyphPen()
    shortLeftDownwardTail(pen, fw, wd)

    # > (大なり)
    glyph = font.createChar(ord(">"), "greater")
    pen = glyph.glyphPen()
    shortRightUpwardTail(pen, fw, wd)

    # = (イコール)
    glyph = font.createChar(ord("="), "equal")
    pen = glyph.glyphPen()
    shortHorizontalBar(pen, fw, wd)
    shortBelowHorizontalBar(pen, fw, wd)

    # ^ (キャレット)
    glyph = font.createChar(ord("^"), "circumflex")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)

    # ~ (チルダ)
    glyph = font.createChar(ord("~"), "tilde")
    pen = glyph.glyphPen()
    downwardCurve(pen, fw, wd)

    # | (縦棒)
    glyph = font.createChar(ord("|"), "bar")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)

    # \ (バックスラッシュ)
    glyph = font.createChar(ord("\\"), "backslash")
    pen = glyph.glyphPen()
    shortBackslashBar(pen, fw, wd)

    # / (スラッシュ)
    glyph = font.createChar(ord("/"), "slash")
    pen = glyph.glyphPen()
    shortForwardslashBar(pen, fw, wd)

# フォント生成実行時は
# font = fontforge.font()
# lakof_generator(font, "Regular")
# font.generate("lakof.ttf")
