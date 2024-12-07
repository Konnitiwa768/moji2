# -------------------------------------------------- importゾーン --------------------------------------------------

import fontforge # 「インポート "fontforge" を解決できませんでした」って言われるのそろそろなんとかしたい、けど面倒だからしない

# -------------------------------------------------- グリフの設定項目 --------------------------------------------------

# 高さ
height = 500

# 略称
he = height

# -------------------------------------------------- 計算系の関数（意味ある……？） --------------------------------------------------

# 2倍の計算
def db(number):
    db = number * 2
    return db

# 半分の計算
def ha(number):
    ha = number / 2
    return ha

# 平均値の計算
def av(number1, number2):
    av = (number1 + number2) / 2
    return av

# -------------------------------------------------- 部品をつくって、グリフいじりの効率を上げる！ --------------------------------------------------

# 名前は、「長さ, 位置, 形状, 種類」の順に統一！

# 短縦棒
def shortVerticalBar(p, fw, wd):
    p.moveTo((0, 0))
    p.lineTo((0, he))
    p.lineTo((fw, he))
    p.lineTo((fw, 0))
    p.closePath()

# 短縦棒（右）
def shortRightVerticalBar(p, fw, wd):
    p.moveTo((wd - fw, 0))
    p.lineTo((wd - fw, he))
    p.lineTo((wd, he))
    p.lineTo((wd, 0))
    p.closePath()

# 短カーブ接続用縦棒
def shortConnectcurveBar(p, fw, wd):
    p.moveTo((0, 0))
    p.lineTo((0, he))
    p.lineTo((fw * 0.9, he))
    p.lineTo((fw, ha(he) + fw))
    p.lineTo((fw, 0))
    p.closePath()

# 短カーブ接続用縦棒（右）
def shortRightConnectcurveBar(p, fw, wd):
    p.moveTo((wd - fw, he))
    p.lineTo((wd - fw, ha(he) - fw))
    p.lineTo((wd - fw * 0.9, 0))
    p.lineTo((wd, 0))
    p.lineTo((wd, he))
    p.closePath()

# 短両カーブ接続用縦棒
def shortRightConnectcurvesBar(p, fw, wd):
    p.moveTo((wd - fw, he))
    p.lineTo((wd - fw, ha(he) - fw))
    p.lineTo((wd - fw * 0.9, 0))
    p.lineTo((wd, 0))
    p.lineTo((wd, ha(he) + fw))
    p.lineTo((wd - fw * 0.1, he))
    p.closePath()

# 短カーブ接続用縦棒（超右）
def shortRightestConnectcurveBar(p, fw, wd):
    p.moveTo((100, 100))
    p.lineTo((100, 200))
    p.lineTo((200, 200))
    p.lineTo((200, 100))
    p.closePath()

# 長縦棒
def longVerticalBar(p, fw, wd):
    p.moveTo((0, -he))
    p.lineTo((0, he))
    p.lineTo((fw, he))
    p.lineTo((fw, -he))
    p.closePath()

# 短横棒
def shortHorizontalBar(p, fw, wd):
    p.moveTo((0, 0))
    p.lineTo((0, fw))
    p.lineTo((wd, fw))
    p.lineTo((wd, 0))
    p.closePath()

# 短横棒（下）
def shortBottomHorizontalBar(p, fw, wd):
    p.moveTo((0, -he))
    p.lineTo((0, -he + fw))
    p.lineTo((wd, -he + fw))
    p.lineTo((wd, -he))
    p.closePath()

# 短斜め棒（＼）
def shortBackslashBar(p, fw, wd):
    p.moveTo((0, he))
    p.lineTo((fw, he))
    p.lineTo((wd, 0))
    p.lineTo((wd - fw, 0))
    p.closePath()

# 短斜め棒（／）
def shortForwardslashBar(p, fw, wd):
    p.moveTo((0, 0))
    p.lineTo((wd - fw, he))
    p.lineTo((wd, he))
    p.lineTo((fw, 0))
    p.closePath()

# 超長斜め棒（／）
def longestForwardslashBar(p, fw, wd):
    p.moveTo((0, -he))
    p.lineTo((wd - fw, db(he)))
    p.lineTo((wd, db(he)))
    p.lineTo((fw, -he))
    p.closePath()

# 下向きカーブ
def downwardCurve(p, fw, wd):
    p.moveTo((fw, ha(he) + fw))
    p.curveTo((fw, he * 0.55 + fw * 0.9), (fw, he), (fw + ha(wd - fw), he))
    p.curveTo((wd, he), (wd, he * 0.55), (wd, ha(he)))
    p.lineTo((wd - fw, ha(he)))
    p.curveTo((wd - fw, ha(he) + (ha(he) - fw) * 0.1), (wd - fw, he - fw), (ha(wd), he - fw))
    p.curveTo((fw, he - fw), (fw, ha(he) + (ha(he) - fw) * 0.1), (fw, ha(he)))
    p.closePath()

# 上向きカーブ
def upwardCurve(p, fw, wd):
    p.moveTo((100, 100))
    p.lineTo((100, 200))
    p.lineTo((200, 200))
    p.lineTo((200, 100))
    p.closePath()

# 短下向きカーブ用しっぽ
def shortDownwardTail(p, fw, wd):
    p.moveTo((wd, ha(he)))
    p.lineTo((wd, 0))
    p.lineTo((wd - fw, 0))
    p.lineTo((wd - fw, ha(he)))
    p.closePath()

# 長下向きカーブ用しっぽ
def longDownwardTail(p, fw, wd):
    p.moveTo((wd, ha(he)))
    p.lineTo((wd, -he))
    p.lineTo((wd - fw, -he))
    p.lineTo((wd - fw, ha(he)))
    p.closePath()

# アポストロフィ
def apostrophe(p, fw, wd):
    p.moveTo((0, db(he)))
    p.lineTo((0, he * 1.5))
    p.lineTo((fw, he * 1.8))
    p.lineTo((fw, db(he)))

# # 短縦棒（超右）
# def shortRightestVerticalBar(p, w):
#     p.moveTo(((sW - w) * 2, 0))
#     p.lineTo(((sW - w) * 2, sH))
#     p.lineTo((sW * 2 - w, sH))
#     p.lineTo((sW * 2 - w, 0))
#     p.closePath()

# # 長縦棒
# def longVerticalBar(p, w):
#     p.moveTo((0, uH))
#     p.lineTo((0, sH))
#     p.lineTo((w, sH))
#     p.lineTo((w, uH))
#     p.closePath()

# # 短横棒
# def shortHorizontalBar(p, w):
#     p.moveTo((0, 0))
#     p.lineTo((0, w))
#     p.lineTo((sW, w))
#     p.lineTo((sW, 0))
#     p.closePath()

# # 短横棒（下）
# def shortBottomHorizontalBar(p, w):
#     p.moveTo((0, uH))
#     p.lineTo((0, uH + w))
#     p.lineTo((sW, uH + w))
#     p.lineTo((sW, uH))
#     p.closePath()

# # 短斜め棒（＼）
# def shortBackslashBar(p, w):
#     p.moveTo((0, sH))
#     p.lineTo((w, sH))
#     p.lineTo((sW, 0))
#     p.lineTo((sW - w, 0))
#     p.closePath()

# # 短斜め棒（／）
# def shortForwardslashBar(p, w):
#     p.moveTo((0, 0))
#     p.lineTo((sW - w, sH))
#     p.lineTo((sW, sH))
#     p.lineTo((w, 0))
#     p.closePath()

# # 長斜め棒（／）
# def longForwardslashBar(p, w):
#     p.moveTo((0, uH / 2))
#     p.lineTo((sW - w, (sH + lH) / 2))
#     p.lineTo((sW, (sH + lH) / 2))
#     p.lineTo((w, uH / 2))
#     p.closePath()

# # 超長斜め棒（／）
# def longestForwardslashBar(p, w):
#     p.moveTo((0, uH))
#     p.lineTo((sW - w, lH))
#     p.lineTo((sW, lH))
#     p.lineTo((w, uH))
#     p.closePath()

# # 半円（左）
# def leftCircle(p, w):
#     p.moveTo((hW, 0))
#     p.curveTo((hW / 2, 0), (0, hH / 2), (0, hH))
#     p.curveTo((0, (hH + sH) / 2), (hW / 2, sH), (hW, sH))
#     p.lineTo((hW, sH - w))
#     p.curveTo(((hW + w) / 2, sH - w), (w, (sH - w + hH) / 2), (w , hH))
#     p.curveTo((w, (hH + w) / 2), ((w + hW) / 2, w), (hW, w))
#     p.closePath()

# # 半円（右）
# def rightCircle(p, w):
#     p.moveTo((hW, 0))
#     p.curveTo(((hW + sW) / 2, 0), (sW, hH / 2), (sW, hH))
#     p.curveTo((sW, (hH + sH) / 2), ((sW + hW) / 2, sH), (hW, sH))
#     p.lineTo((hW, sH - w))
#     p.curveTo(((sW - w + hW) / 2, sH - w), (sW - w, (sH - w + hH) / 2), (sW - w, hH))
#     p.curveTo((sW - w, (hH + w) / 2), ((sW - w + hW) / 2, w), (hW, w))
#     p.closePath()

# # 短下カーブ
# def shortDownwardCurve(p, w):
#     p.moveTo((w, sH * 0.9))
#     p.curveTo((hW, sH * 1.1), (sW, sH), (sW, sH * 0.9))
#     p.lineTo((sW - w, sH * 0.9 - w))
#     p.curveTo((sW - w, sH * 0.9), (hW, sH), (w, sH * 0.9 - w))
#     p.closePath()
#     p.moveTo((sW - w, 0))
#     p.lineTo((sW - w, sH * 0.9 - w))
#     p.lineTo((sW, sH * 0.9))
#     p.lineTo((sW, 0))
#     p.closePath()

# # 長下カーブ
# def longDownwardCurve(p, w):
#     p.moveTo((w, sH * 0.9))
#     p.curveTo(((hW + sW) / 2, sH * 1.1), (sW, sH), (sW, sH * 0.9))
#     p.lineTo((sW - w, sH * 0.9 - w))
#     p.curveTo((sW - w, sH * 0.9), (hW, sH), (w, sH * 0.9 - w))
#     p.closePath()
#     p.moveTo((sW, uH))
#     p.curveTo((sW - w, uH), (sW - w, 0), (sW - w, sH * 0.9 - w))
#     p.lineTo((sW, sH * 0.9))
#     p.curveTo((sW, 0), (sW, uH), (sW + w, uH))
#     p.closePath()

# # 短下カーブ（右）
# def shortRightDownwardCurve(p, w):
#     p.moveTo((sW, sH * 0.9))
#     p.curveTo(((hW + sW) / 2 - w + sW, sH * 1.1), (sW * 2 - w, sH), (sW * 2 - w, sH * 0.9))
#     p.lineTo(((sW - w) * 2, sH * 0.9 - w))
#     p.curveTo(((sW - w) * 2, sH * 0.9), (hW - w + sW, sH), (sW, sH * 0.9 - w))
#     p.closePath()
#     p.moveTo(((sW - w) * 2, 0))
#     p.lineTo(((sW - w) * 2, sH * 0.9 - w))
#     p.lineTo((sW * 2 - w, sH * 0.9))
#     p.lineTo((sW * 2 - w, 0))
#     p.closePath()

# # 長下カーブ（右）
# def longRightDownwardCurve(p, w):
#     p.moveTo((sW, sH * 0.9))
#     p.curveTo(((hW + sW) / 2 - w + sW, sH * 1.1), (sW * 2 - w, sH), (sW * 2 - w, sH * 0.9))
#     p.lineTo(((sW - w) * 2, sH * 0.9 - w))
#     p.curveTo(((sW - w) * 2, sH * 0.9), (hW - w + sW, sH), (sW, sH * 0.9 - w))
#     p.closePath()
#     p.moveTo((sW * 2 - w, uH))
#     p.curveTo(((sW - w) * 2, uH), ((sW - w) * 2, 0), ((sW - w) * 2, sH * 0.9 - w))
#     p.lineTo((sW * 2 - w, sH * 0.9))
#     p.curveTo((sW * 2 - w, 0), (sW * 2 - w, uH), (sW * 2, uH))
#     p.closePath()

# # 短上カーブ
# def shortUpwardCurve(p, w):
#     p.moveTo((sW - w, sH * 0.1))
#     p.curveTo((hW / 2, sH * -0.1), (0, 0), (0, sH * 0.1))
#     p.lineTo((w, sH * 0.1 + w))
#     p.curveTo((w, sH * 0.1), (hW, 0), (sW - w, sH * 0.1 + w))
#     p.closePath()
#     p.moveTo((w, sH))
#     p.lineTo((w, sH * 0.1 + w))
#     p.lineTo((0, sH * 0.1))
#     p.lineTo((0, sH))
#     p.closePath()

# # 長上カーブ
# def longUpwardCurve(p, w):
#     p.moveTo((sW - w, sH * 0.1))
#     p.curveTo((hW / 2, sH * -0.1), (0, 0), (0, sH * 0.1))
#     p.lineTo((w, sH * 0.1 + w))
#     p.curveTo((w, sH * 0.1), (hW, 0), (sW - w, sH * 0.1 + w))
#     p.closePath()
#     p.moveTo((0, lH))
#     p.curveTo((w, lH), (w, sH), (w, sH * 0.1 + w))
#     p.lineTo((0, sH * 0.1))
#     p.curveTo((0, sH), (0, lH), (-w, lH))
#     p.closePath()

# # 短上カーブ（右）
# def shortRightUpwardCurve(p, w):
#     p.moveTo(((sW - w) * 2, sH * 0.1))
#     p.curveTo((hW / 2 - w + sW, sH * -0.1), (sW - w, 0), (sW - w, sH * 0.1))
#     p.lineTo((sW, sH * 0.1 + w))
#     p.curveTo((sW, sH * 0.1), (hW - w + sW, 0), ((sW - w) * 2, sH * 0.1 + w))
#     p.closePath()
#     p.moveTo((sW, sH))
#     p.lineTo((sW, sH * 0.1 + w))
#     p.lineTo((sW - w, sH * 0.1))
#     p.lineTo((sW - w, sH))
#     p.closePath()

# # p用のしっぽ
# def shortPtail(p, w):
#     p.moveTo((0, 0))
#     p.curveTo((w, 0), (sW - w, hH), (sW - w, sH))
#     p.lineTo(sW, sH)
#     p.curveTo((sW, hH), (w * 2, 0), (w, 0))
#     p.closePath()

# # b用のしっぽ
# def shortBtail(p, w):
#     p.moveTo((0, uH))
#     p.curveTo((w, uH), (sW - w, 0), (sW - w, sH))
#     p.lineTo(sW, sH)
#     p.curveTo((sW, 0), (w * 2, uH), (w, uH))
#     p.closePath()

# # アポストロフィ
# def apostrophe(p, w):
#     p.moveTo(0, lH)
#     p.lineTo(0, (sH + lH) / 2)
#     p.lineTo(w, lH * 0.8)
#     p.lineTo(w, lH)

# （……a、左右でぶった切られてるしなんかスリムじゃない…………？）
# （……u、円と斜線が合わさって大変なことになってる？）