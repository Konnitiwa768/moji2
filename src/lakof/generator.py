# -------------------------------------------------- importゾーン --------------------------------------------------

import fontforge # 相変わらず「インポート "fontforge" を解決できませんでした」と言われる日々（？）

# 相対パスだかなんだかの関係で、componentsの前に . を入れないと「そんなモジュールないよ」って言われる　あとで理解しとく
from .components import *

# -------------------------------------------------- グリフいじり（？）をする！ --------------------------------------------------

def lakof_generator(font, weight):

    # 太さの設定
    if weight == "Thin":
        fontweight = 50
    elif weight == "Regular":
        fontweight = 100
    elif weight == "Bold":
        fontweight = 150

    width = fontweight + 350

    fw = fontweight
    wd = width

    # lakof/componentsの部品を使ってグリフをいじる！
    glyph = font.createChar(ord("p"), "p")
    pen = glyph.glyphPen()

    glyph = font.createChar(ord("b"), "b")
    pen = glyph.glyphPen()

    glyph = font.createChar(ord("k"), "k")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardDoublecurve(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("g"), "g")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardDoublecurve(pen, fw, wd)
    longRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("t"), "t")
    pen = glyph.glyphPen()
    upwardDoublecurve(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    shortRightestConnectcurveBar(pen, fw, wd)

    glyph = font.createChar(ord("d"), "d")
    pen = glyph.glyphPen()
    upwardDoublecurve(pen, fw, wd)
    longUpwardTail(pen, fw, wd)
    shortRightestConnectcurveBar(pen, fw, wd)

    glyph = font.createChar(ord("s"), "s")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    shortDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("z"), "z")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    longDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("f"), "f")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)

    glyph = font.createChar(ord("v"), "v")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    longUpwardTail(pen, fw, wd)

    glyph = font.createChar(ord("c"), "c")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    shortRightConnectcurvesBar(pen, fw, wd)
    rightDownwardCurve(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("q"), "q")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    longUpwardTail(pen, fw, wd)
    shortRightConnectcurvesBar(pen, fw, wd)
    rightDownwardCurve(pen, fw, wd)
    longRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("n"), "n")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortForwardslashBar(pen, fw, wd)
    shortRightVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("m"), "m")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortForwardslashBar(pen, fw, wd)
    shortRightVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("l"), "l")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("x"), "x")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortBottomHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("y"), "y")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    shortestLowerrightCircle(pen, fw, wd)
    shortAboveVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("w"), "w")
    pen = glyph.glyphPen()
    rightCircle(pen, fw, wd)
    shortestUpperleftCircle(pen, fw, wd)
    shortBelowVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("a"), "a")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)

    glyph = font.createChar(ord("e"), "e")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    shortestUpperrightCircle(pen, fw, wd)
    shortestLowerrightCircle(pen, fw, wd)

    glyph = font.createChar(ord("i"), "i")
    pen = glyph.glyphPen()
    shortestUpperleftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    iTail(pen, fw, wd)

    glyph = font.createChar(ord("o"), "o")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    shortestCenterHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("u"), "u")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    longForwardslashBar(pen, fw, wd)

    glyph = font.createChar(ord("0"), "0")
    pen = glyph.glyphPen()
    shortBackslashBar(pen, fw, wd)
    shortForwardslashBar(pen, fw, wd)

    glyph = font.createChar(ord("1"), "1")
    pen = glyph.glyphPen()

    glyph = font.createChar(ord("2"), "2")
    pen = glyph.glyphPen()

    glyph = font.createChar(ord("3"), "3")
    pen = glyph.glyphPen()

    glyph = font.createChar(ord("4"), "4")
    pen = glyph.glyphPen()

    glyph = font.createChar(ord("5"), "5")
    pen = glyph.glyphPen()

    glyph = font.createChar(ord("6"), "6")
    pen = glyph.glyphPen()

    glyph = font.createChar(ord("7"), "7")
    pen = glyph.glyphPen()

    glyph = font.createChar(ord("8"), "8")
    pen = glyph.glyphPen()

    glyph = font.createChar(ord("9"), "9")
    pen = glyph.glyphPen()

    glyph = font.createChar(ord(","), ",")
    pen = glyph.glyphPen()

    glyph = font.createChar(ord("."), ".")
    pen = glyph.glyphPen()
    longestForwardslashBar(pen, fw, wd)

    glyph = font.createChar(ord("!"), "!")
    pen = glyph.glyphPen()
    longestForwardslashBar(pen, fw, wd)
    shortBackslashBar(pen, fw, wd)

    glyph = font.createChar(ord("?"), "?")
    pen = glyph.glyphPen()
    shortCenterVerticalBar(pen, fw, wd)
    shortCenterHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("-"), "-")
    pen = glyph.glyphPen()
    shortCenterHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord(";"), ";")
    pen = glyph.glyphPen()
    semicolon(pen, fw, wd)

    glyph = font.createChar(ord("<"), "<")
    pen = glyph.glyphPen()
    inequalitysign(pen, fw, wd)

    glyph = font.createChar(ord(">"), ">")
    pen = glyph.glyphPen()
    inequalitysign(pen, fw, wd)

    glyph = font.createChar(ord("\""), "\"")
    pen = glyph.glyphPen()

    glyph = font.createChar(ord("'"), "'")
    pen = glyph.glyphPen()
    apostrophe(pen, fw, wd)

    # 縦の余白
    font.ascent = 1050

    # 横の余白
    for glyph in font.glyphs():
        glyph.left_side_bearing = 50
        glyph.right_side_bearing = 50