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

    glyph = font.createChar(ord("s"), "s")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fontweight)
    shortDownwardCurve(pen, fontweight)

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
    shortLeftCircle(pen, fontweight)
    shortRightCircle(pen, fontweight)

    glyph = font.createChar(ord("0"), "0")
    pen = glyph.glyphPen()
    shortBackslashBar(pen, fontweight)
    shortForwardslashBar(pen, fontweight)

    # 縦の余白
    font.ascent = 1050

    # 横の余白
    for glyph in font.glyphs():
        glyph.left_side_bearing = 50
        glyph.right_side_bearing = 50