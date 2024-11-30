# -------------------------------------------------- importゾーン --------------------------------------------------

import fontforge # 相変わらず「インポート "fontforge" を解決できませんでした」と言われる日々（？）

# 相対パスだかなんだかの関係で、componentsの前に . を入れないと「そんなモジュールないよ」って言われる　あとで理解しとく
from .components import *

# -------------------------------------------------- ここにグリフをいじる機構をつくる予定、実装できるかは知らない！！！！！ --------------------------------------------------

def lakof_generator(font, weight):

    # フォントの太さは、下の表に対応する値の1/4ってことにする
    # 100 | Thin
    # 200 | ExtraLight
    # 300 | Light
    # 400 | Regular
    # 500 | Medium
    # 600 | SemiBold
    # 700 | Bold
    # 800 | Extrabold
    # 900 | Black
    # 例えばRegularだったら400 * 1/4 = 100
    if weight == "Thin":
        fontweight = 25
    elif weight == "Regular":
        fontweight = 100
    elif weight == "Bold":
        fontweight = 175

    glyph = font.createChar(ord("n"), "n")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fontweight)
    shortRightVerticalBar(pen, fontweight)
    shortForwardslashBar(pen, fontweight)
    bearings(glyph)

    glyph = font.createChar(ord("m"), "m")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fontweight)
    shortRightVerticalBar(pen, fontweight)
    shortForwardslashBar(pen, fontweight)
    bearings(glyph)

    glyph = font.createChar(ord("l"), "l")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fontweight)
    shortHorizontalBar(pen, fontweight)
    bearings(glyph)

    glyph = font.createChar(ord("x"), "x")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fontweight)
    shortBottomHorizontalBar(pen, fontweight)
    bearings(glyph)

    glyph = font.createChar(ord("a"), "a")
    pen = glyph.glyphPen()
    shortLeftCircle(pen, fontweight)
    shortRightCircle(pen, fontweight)
    bearings(glyph)

    glyph = font.createChar(ord("0"), "0")
    pen = glyph.glyphPen()
    shortBackslashBar(pen, fontweight)
    shortForwardslashBar(pen, fontweight)
    bearings(glyph)