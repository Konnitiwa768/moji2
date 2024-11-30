# -------------------------------------------------- importゾーン --------------------------------------------------

import fontforge # 「インポート "fontforge" を解決できませんでした」って言われるのそろそろなんとかしたい、けど面倒だからしない

# -------------------------------------------------- 部品をつくって、グリフいじりの効率を上げる！ --------------------------------------------------

# 短縦棒
def shortVerticalBar(pen, fontweight):
    pen.moveTo((0, 0))
    pen.lineTo((0, 500))
    pen.lineTo((fontweight, 500))
    pen.lineTo((fontweight, 0))
    pen.closePath()

# 短横棒
def shortHorizontalBar(pen, fontweight):
    pen.moveTo((0, 0))
    pen.lineTo((0, fontweight))
    pen.lineTo((400, fontweight))
    pen.lineTo((400, 0))
    pen.closePath()