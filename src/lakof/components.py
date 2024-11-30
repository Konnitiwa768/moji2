# -------------------------------------------------- importゾーン --------------------------------------------------

import fontforge # 「インポート "fontforge" を解決できませんでした」って言われるのそろそろなんとかしたい、けど面倒だからしない

# -------------------------------------------------- 部品をつくって、グリフいじりの効率を上げる！ --------------------------------------------------

# 関数名は、「長さ, 位置, 種類」の順に統一！

# 短縦棒
def shortVerticalBar(p, w):
    p.moveTo((0, 0))
    p.lineTo((0, 500))
    p.lineTo((w, 500))
    p.lineTo((w, 0))
    p.closePath()

# 短縦棒（右）
def shortRightVerticalBar(p, w):
    p.moveTo((400 - w, 0))
    p.lineTo((400 - w, 500))
    p.lineTo((400, 500))
    p.lineTo((400, 0))
    p.closePath()

# 長縦棒
def longVerticalBar(p, w):
    p.moveTo((0, -300))
    p.lineTo((0, 500))
    p.lineTo((w, 500))
    p.lineTo((w, -300))
    p.closePath()

# 短横棒
def shortHorizontalBar(p, w):
    p.moveTo((0, 0))
    p.lineTo((0, w))
    p.lineTo((400, w))
    p.lineTo((400, 0))
    p.closePath()

# 短横棒（下）
def shortBottomHorizontalBar(p, w):
    p.moveTo((0, -300))
    p.lineTo((0, -300 + w))
    p.lineTo((400, -300 + w))
    p.lineTo((400, -300))
    p.closePath()

# 短斜め棒（＼）
def shortBackslashBar(p, w):
    p.moveTo((0, 0))
    p.lineTo((400 - w, 500))
    p.lineTo((400, 500))
    p.lineTo((w, 0))
    p.closePath()

# 短斜め棒（／）
def shortForwardslashBar(p, w):
    p.moveTo((0, 500))
    p.lineTo((w, 500))
    p.lineTo((400, 0))
    p.lineTo((400 - w, 0))
    p.closePath()

# 半円（左）
def shortLeftCircle(p, w):
    p.moveTo((200, 0))
    p.curveTo((100, 0), (0, 125), (0, 250))
    p.curveTo((0, 375), (100, 500), (200, 500))
    p.lineTo((200, 500 - w))
    p.curveTo(((200  + w) / 2, 500 - w), (w, (500 - w + 250) / 2), (w , 250))
    p.curveTo((w, (250 + w) / 2), ((w + 200) / 2, w), (200, w))
    p.closePath()

# 半円（右）
def shortRightCircle(p, w):
    p.moveTo((200, 0))
    p.curveTo((300, 0), (400, 125), (400, 250))
    p.curveTo((400, 375), (300, 500), (200, 500))
    p.lineTo((200, 500 - w))
    p.curveTo(((400 - w + 200) / 2, 500 - w), (400 - w, (500 - w + 250) / 2), (400 - w, 250))
    p.curveTo((400 - w, (250 + w) / 2), ((400 - w + 200) / 2, w), (200, w))
    p.closePath()

# 余白を設定する
def bearings(glyph):
    glyph.left_side_bearing = 50
    glyph.right_side_bearing = 50