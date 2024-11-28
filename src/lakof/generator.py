# -------------------------------------------------- importゾーン --------------------------------------------------

import fontforge # 相変わらず「インポート "fontforge" を解決できませんでした」と言われる日々（？）

# -------------------------------------------------- ここにグリフをいじる機構をつくる予定、実装できるかは知らない！！！！！ --------------------------------------------------

def lakof_generator(font, weight):

    glyph = font.createChar(ord("a"), "a")
    pen = glyph.glyphPen()
    pen.moveTo((100, 100))  # 最初の点
    pen.curveTo((150, 50), (200, 150), (150, 200))  # ベジエ曲線でカーブを描く
    pen.curveTo((100, 250), (50, 150), (100, 100))  # もう一つのカーブを描いて閉じる
    pen.closePath()

    glyph = font.createChar(ord("b"), "b")
    pen = glyph.glyphPen()
    pen.moveTo((100, 100))
    pen.curveTo((150, 50), (200, 150), (150, 200))  # 第1曲線
    pen.curveTo((100, 250), (50, 150), (100, 100))  # 第2曲線
    pen.curveTo((150, 300), (200, 200), (150, 250))  # 第3曲線
    pen.closePath()

    glyph.width = weight