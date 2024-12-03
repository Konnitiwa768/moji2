# -------------------------------------------------- importゾーン --------------------------------------------------

import fontforge # 「インポート "fontforge" を解決できませんでした」って言われるのそろそろなんとかしたい、けど面倒だからしない

# -------------------------------------------------- グリフの設定項目 --------------------------------------------------

# ココをいじるだけで見た目を改善できるようにする
short_height = 500
short_width = 400
under_height = -500

# 上のルールを受けて定義する部分
long_height = short_height * 2
long_width = short_width * 2
half_height = short_height / 2
half_width = short_width / 2

# コードをラクに書くための略称（ただし非常にわかりづらい！）
hH = half_height
sH = short_height
lH = long_height
uH = under_height
hW = half_width
sW = short_width
lW = long_width

# -------------------------------------------------- 部品をつくって、グリフいじりの効率を上げる！ --------------------------------------------------

# 名前は、「長さ, 位置, 形状, 種類」の順に統一！

# 短縦棒
def shortVerticalBar(p, w):
    p.moveTo((0, 0))
    p.lineTo((0, sH))
    p.lineTo((w, sH))
    p.lineTo((w, 0))
    p.closePath()

# 短縦棒（右）
def shortRightVerticalBar(p, w):
    p.moveTo((sW - w, 0))
    p.lineTo((sW - w, sH))
    p.lineTo((sW, sH))
    p.lineTo((sW, 0))
    p.closePath()

# 短縦棒（超右）
def shortRightestVerticalBar(p, w):
    p.moveTo(((sW - w) * 2, 0))
    p.lineTo(((sW - w) * 2, sH))
    p.lineTo((sW * 2 - w, sH))
    p.lineTo((sW * 2 - w, 0))
    p.closePath()

# 長縦棒
def longVerticalBar(p, w):
    p.moveTo((0, uH))
    p.lineTo((0, sH))
    p.lineTo((w, sH))
    p.lineTo((w, uH))
    p.closePath()

# 短横棒
def shortHorizontalBar(p, w):
    p.moveTo((0, 0))
    p.lineTo((0, w))
    p.lineTo((sW, w))
    p.lineTo((sW, 0))
    p.closePath()

# 短横棒（下）
def shortBottomHorizontalBar(p, w):
    p.moveTo((0, uH))
    p.lineTo((0, uH + w))
    p.lineTo((sW, uH + w))
    p.lineTo((sW, uH))
    p.closePath()

# 短斜め棒（＼）
def shortBackslashBar(p, w):
    p.moveTo((0, sH))
    p.lineTo((w, sH))
    p.lineTo((sW, 0))
    p.lineTo((sW - w, 0))
    p.closePath()

# 短斜め棒（／）
def shortForwardslashBar(p, w):
    p.moveTo((0, 0))
    p.lineTo((sW - w, sH))
    p.lineTo((sW, sH))
    p.lineTo((w, 0))
    p.closePath()

# 長斜め棒（／）
def longForwardslashBar(p, w):
    p.moveTo((0, uH / 2))
    p.lineTo((sW - w, (sH + lH) / 2))
    p.lineTo((sW, (sH + lH) / 2))
    p.lineTo((w, uH / 2))
    p.closePath()

# 超長斜め棒（／）
def longestForwardslashBar(p, w):
    p.moveTo((0, uH))
    p.lineTo((sW - w, lH))
    p.lineTo((sW, lH))
    p.lineTo((w, uH))
    p.closePath()

# 半円（左）
def leftCircle(p, w):
    p.moveTo((hW, 0))
    p.curveTo((hW / 2, 0), (0, hH / 2), (0, hH))
    p.curveTo((0, (hH + sH) / 2), (hW / 2, sH), (hW, sH))
    p.lineTo((hW, sH - w))
    p.curveTo(((hW + w) / 2, sH - w), (w, (sH - w + hH) / 2), (w , hH))
    p.curveTo((w, (hH + w) / 2), ((w + hW) / 2, w), (hW, w))
    p.closePath()

# 半円（右）
def rightCircle(p, w):
    p.moveTo((hW, 0))
    p.curveTo(((hW + sW) / 2, 0), (sW, hH / 2), (sW, hH))
    p.curveTo((sW, (hH + sH) / 2), ((sW + hW) / 2, sH), (hW, sH))
    p.lineTo((hW, sH - w))
    p.curveTo(((sW - w + hW) / 2, sH - w), (sW - w, (sH - w + hH) / 2), (sW - w, hH))
    p.curveTo((sW - w, (hH + w) / 2), ((sW - w + hW) / 2, w), (hW, w))
    p.closePath()

# 短下カーブ
def shortDownwardCurve(p, w):
    p.moveTo((w, sH * 0.9))
    p.curveTo(((hW + sW) / 2, sH * 1.2), (sW, sH), (sW, sH * 0.9))
    p.lineTo((sW - w, sH * 0.9 - w))
    p.curveTo((sW - w, sH * 0.9), (hW, sH), (w, sH * 0.9 - w))
    p.closePath()
    p.moveTo((sW - w, 0))
    p.lineTo((sW - w, sH * 0.9 - w))
    p.lineTo((sW, sH * 0.9))
    p.lineTo((sW, 0))
    p.closePath()

# 長下カーブ
def longDownwardCurve(p, w):
    p.moveTo((w, sH * 0.9))
    p.curveTo(((hW + sW) / 2, sH * 1.2), (sW, sH), (sW, sH * 0.9))
    p.lineTo((sW - w, sH * 0.9 - w))
    p.curveTo((sW - w, sH * 0.9), (hW, sH), (w, sH * 0.9 - w))
    p.closePath()
    p.moveTo((sW, uH))
    p.curveTo((sW - w, uH), (sW - w, 0), (sW - w, sH * 0.9 - w))
    p.lineTo((sW, sH * 0.9))
    p.curveTo((sW, 0), (sW, uH), (sW + w, uH))
    p.closePath()

# 短下カーブ（右）
def shortRightDownwardCurve(p, w):
    p.moveTo((sW, sH * 0.9))
    p.curveTo(((hW + sW) / 2 - w + sW, sH * 1.2), (sW * 2 - w, sH), (sW * 2 - w, sH * 0.9))
    p.lineTo(((sW - w) * 2, sH * 0.9 - w))
    p.curveTo(((sW - w) * 2, sH * 0.9), (hW - w + sW, sH), (sW, sH * 0.9 - w))
    p.closePath()
    p.moveTo(((sW - w) * 2, 0))
    p.lineTo(((sW - w) * 2, sH * 0.9 - w))
    p.lineTo((sW * 2 - w, sH * 0.9))
    p.lineTo((sW * 2 - w, 0))
    p.closePath()

# 長下カーブ（右）
def longRightDownwardCurve(p, w):
    p.moveTo((sW, sH * 0.9))
    p.curveTo(((hW + sW) / 2 - w + sW, sH * 1.2), (sW * 2 - w, sH), (sW * 2 - w, sH * 0.9))
    p.lineTo(((sW - w) * 2, sH * 0.9 - w))
    p.curveTo(((sW - w) * 2, sH * 0.9), (hW - w + sW, sH), (sW, sH * 0.9 - w))
    p.closePath()
    p.moveTo((sW * 2 - w, uH))
    p.curveTo(((sW - w) * 2, uH), ((sW - w) * 2, 0), ((sW - w) * 2, sH * 0.9 - w))
    p.lineTo((sW * 2 - w, sH * 0.9))
    p.curveTo((sW * 2 - w, 0), (sW * 2 - w, uH), (sW * 2, uH))
    p.closePath()

# 短上カーブ
def shortUpwardCurve(p, w):
    p.moveTo((sW - w, sH * 0.1))
    p.curveTo((hW / 2, sH * -0.2), (0, 0), (0, sH * 0.1))
    p.lineTo((w, sH * 0.1 + w))
    p.curveTo((w, sH * 0.1), (hW, 0), (sW - w, sH * 0.1 + w))
    p.closePath()
    p.moveTo((w, sH))
    p.lineTo((w, sH * 0.1 + w))
    p.lineTo((0, sH * 0.1))
    p.lineTo((0, sH))
    p.closePath()

# 長上カーブ
def longUpwardCurve(p, w):
    p.moveTo((sW - w, sH * 0.1))
    p.curveTo((hW / 2, sH * -0.2), (0, 0), (0, sH * 0.1))
    p.lineTo((w, sH * 0.1 + w))
    p.curveTo((w, sH * 0.1), (hW, 0), (sW - w, sH * 0.1 + w))
    p.closePath()
    p.moveTo((0, lH))
    p.curveTo((w, lH), (w, sH), (w, sH * 0.1 + w))
    p.lineTo((0, sH * 0.1))
    p.curveTo((0, sH), (0, lH), (-w, lH))
    p.closePath()

# 短上カーブ（右）
def shortRightUpwardCurve(p, w):
    p.moveTo(((sW - w) * 2, sH * 0.1))
    p.curveTo((hW / 2 - w + sW, sH * -0.2), (sW - w, 0), (sW - w, sH * 0.1))
    p.lineTo((sW, sH * 0.1 + w))
    p.curveTo((sW, sH * 0.1), (hW - w + sW, 0), ((sW - w) * 2, sH * 0.1 + w))
    p.closePath()
    p.moveTo((sW, sH))
    p.lineTo((sW, sH * 0.1 + w))
    p.lineTo((sW - w, sH * 0.1))
    p.lineTo((sW - w, sH))
    p.closePath()

# p用のしっぽ
def shortPtail(p, w):
    p.moveTo((0, 0))
    p.curveTo((w, 0), (sW - w, hH), (sW - w, sH))
    p.lineTo(sW, sH)
    p.curveTo((sW, hH), (w * 2, 0), (w, 0))
    p.closePath()

# b用のしっぽ
def shortBtail(p, w):
    p.moveTo((0, uH))
    p.curveTo((w, uH), (sW - w, 0), (sW - w, sH))
    p.lineTo(sW, sH)
    p.curveTo((sW, 0), (w * 2, uH), (w, uH))
    p.closePath()

# アポストロフィ
def apostrophe(p, w):
    p.moveTo(0, lH)
    p.lineTo(0, (sH + lH) / 2)
    p.lineTo(w, lH * 0.8)
    p.lineTo(w, lH)

# （……a、左右でぶった切られてるしなんかスリムじゃない…………？）
# （……u、円と斜線が合わさって大変なことになってる？）
# （……Widthの W とweightの w が入り混じって大変なことになってるな…………）