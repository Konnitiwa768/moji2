# -------------------------------------------------- importゾーン --------------------------------------------------

import fontforge # 相変わらず「インポート "fontforge" を解決できませんでした」と言われる日々（？）

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

    glyph = font.createChar(ord("l"), "l")
    pen = glyph.glyphPen()
    
    pen.moveTo((0, 0))
    pen.lineTo((0, 500))
    pen.lineTo((fontweight, 500))
    pen.lineTo((fontweight, 0))
    pen.closePath()

    pen.moveTo((0, 0))
    pen.lineTo((0, fontweight))
    pen.lineTo((400, fontweight))
    pen.lineTo((400, 0))
    pen.closePath()

    glyph.left_side_bearing = 50
    glyph.right_side_bearing = 50