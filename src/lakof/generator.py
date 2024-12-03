# -------------------------------------------------- importゾーン --------------------------------------------------

import fontforge # 相変わらず「インポート "fontforge" を解決できませんでした」と言われる日々（？）

# 相対パスだかなんだかの関係で、componentsの前に . を入れないと「そんなモジュールないよ」って言われる　あとで理解しとく
from .components import *

# -------------------------------------------------- ここにグリフをいじる機構をつくる予定、実装できるかは知らない！！！！！ --------------------------------------------------

def lakof_generator(font, weight):

    # 太さの設定
    if weight == "Thin":
        fontweight = 50
    elif weight == "Regular":
        fontweight = 100
    elif weight == "Bold":
        fontweight = 150

    glyph = font.createChar(ord("p"), "p")
    pen = glyph.glyphPen()
    shortPtail(pen, fontweight)
    shortRightUpwardCurve(pen, fontweight)
    shortRightestVerticalBar(pen, fontweight)

    glyph = font.createChar(ord("b"), "b")
    pen = glyph.glyphPen()
    shortBtail(pen, fontweight)
    shortRightUpwardCurve(pen, fontweight)
    shortRightestVerticalBar(pen, fontweight)

    glyph = font.createChar(ord("k"), "k")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fontweight)
    shortDownwardCurve(pen, fontweight)
    shortRightDownwardCurve(pen, fontweight)

    glyph = font.createChar(ord("g"), "g")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fontweight)
    shortDownwardCurve(pen, fontweight)
    longRightDownwardCurve(pen, fontweight)

    glyph = font.createChar(ord("t"), "t")
    pen = glyph.glyphPen()
    shortUpwardCurve(pen, fontweight)
    shortRightUpwardCurve(pen, fontweight)
    shortRightestVerticalBar(pen, fontweight)

    glyph = font.createChar(ord("d"), "d")
    pen = glyph.glyphPen()
    longUpwardCurve(pen, fontweight)
    shortRightUpwardCurve(pen, fontweight)
    shortRightestVerticalBar(pen, fontweight)

    glyph = font.createChar(ord("s"), "s")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fontweight)
    shortDownwardCurve(pen, fontweight)

    glyph = font.createChar(ord("z"), "z")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fontweight)
    longDownwardCurve(pen, fontweight)

    glyph = font.createChar(ord("f"), "f")
    pen = glyph.glyphPen()
    shortUpwardCurve(pen, fontweight)
    shortRightVerticalBar(pen, fontweight)

    glyph = font.createChar(ord("v"), "v")
    pen = glyph.glyphPen()
    longUpwardCurve(pen, fontweight)
    shortRightVerticalBar(pen, fontweight)

    glyph = font.createChar(ord("c"), "c")
    pen = glyph.glyphPen()
    shortUpwardCurve(pen, fontweight)
    shortRightVerticalBar(pen, fontweight)
    shortRightDownwardCurve(pen, fontweight)

    glyph = font.createChar(ord("q"), "q")
    pen = glyph.glyphPen()
    longUpwardCurve(pen, fontweight)
    shortRightVerticalBar(pen, fontweight)
    longRightDownwardCurve(pen, fontweight)

    glyph = font.createChar(ord("n"), "n")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fontweight)
    shortRightVerticalBar(pen, fontweight)
    shortForwardslashBar(pen, fontweight)

    glyph = font.createChar(ord("m"), "m")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fontweight)
    shortRightVerticalBar(pen, fontweight)
    shortForwardslashBar(pen, fontweight)

    glyph = font.createChar(ord("l"), "l")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fontweight)
    shortHorizontalBar(pen, fontweight)

    glyph = font.createChar(ord("x"), "x")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fontweight)
    shortBottomHorizontalBar(pen, fontweight)

    glyph = font.createChar(ord("a"), "a")
    pen = glyph.glyphPen()
    leftCircle(pen, fontweight)
    rightCircle(pen, fontweight)

    glyph = font.createChar(ord("u"), "u")
    pen = glyph.glyphPen()
    leftCircle(pen, fontweight)
    rightCircle(pen, fontweight)
    longForwardslashBar(pen, fontweight)

    glyph = font.createChar(ord("0"), "0")
    pen = glyph.glyphPen()
    shortBackslashBar(pen, fontweight)
    shortForwardslashBar(pen, fontweight)

    glyph = font.createChar(ord("."), ".")
    pen = glyph.glyphPen()
    longestForwardslashBar(pen, fontweight)

    glyph = font.createChar(ord("!"), "!")
    pen = glyph.glyphPen()
    longestForwardslashBar(pen, fontweight)
    shortBackslashBar(pen, fontweight)

    glyph = font.createChar(ord("'"), "'")
    pen = glyph.glyphPen()
    apostrophe(pen, fontweight)

    # 縦の余白
    font.ascent = 1050

    # 横の余白
    for glyph in font.glyphs():
        glyph.left_side_bearing = 50
        glyph.right_side_bearing = 50