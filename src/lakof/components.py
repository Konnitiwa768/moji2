# -------------------------------------------------- importゾーン --------------------------------------------------

import fontforge # 「インポート "fontforge" を解決できませんでした」って言われるのそろそろなんとかしたい、けど面倒だからしない

# -------------------------------------------------- グリフの設定項目 --------------------------------------------------

# ココをいじるだけで見た目を改善できるようにする
short_height = 500
short_width = 400
under_height = -300

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

# 半円（左）
def shortLeftCircle(p, w):
    p.moveTo((hW, 0))
    p.curveTo((hW / 2, 0), (0, hH / 2), (0, hH))
    p.curveTo((0, (hH + sH) / 2), (hW / 2, sH), (hW, sH))
    p.lineTo((hW, sH - w))
    p.curveTo(((hW + w) / 2, sH - w), (w, (sH - w + hH) / 2), (w , hH))
    p.curveTo((w, (hH + w) / 2), ((w + hW) / 2, w), (hW, w))
    p.closePath()

# 半円（右）
def shortRightCircle(p, w):
    p.moveTo((hW, 0))
    p.curveTo(((hW + sW) / 2, 0), (sW, hH / 2), (sW, hH))
    p.curveTo((sW, (hH + sH) / 2), ((sW + hW) / 2, sH), (hW, sH))
    p.lineTo((hW, sH - w))
    p.curveTo(((sW - w + hW) / 2, sH - w), (sW - w, (sH - w + hH) / 2), (sW - w, hH))
    p.curveTo((sW - w, (hH + w) / 2), ((sW - w + hW) / 2, w), (hW, w))
    p.closePath()

# sとかの2画目とかにある「7」みたいなやつ
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

# （……a、なんかスリムじゃない…………？）
# （……Widthの W とweightの w が入り混じって大変なことになってるな…………）