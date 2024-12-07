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

# 長短斜め棒（／）
def longForwardslashBar(p, fw, wd):
    p.moveTo((0, -ha(he)))
    p.lineTo((wd - fw, he + ha(he)))
    p.lineTo((wd, he + ha(he)))
    p.lineTo((fw, -ha(he)))
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

# 下向きカーブ（右）
def rightDownwardCurve(p, fw, wd):
    p.moveTo((wd, ha(he) + fw))
    p.curveTo((wd, he * 0.55 + fw * 0.9), (wd, he), (wd + ha(wd - fw), he))
    p.curveTo((wd * 2 - fw, he), (wd * 2 - fw, he * 0.55), (wd * 2 - fw, ha(he)))
    p.lineTo((wd * 2 - fw * 2, ha(he)))
    p.curveTo((wd * 2 - fw * 2, ha(he) + (ha(he) - fw) * 0.1), (wd * 2 - fw * 2, he - fw), (ha(wd) - fw + wd, he - fw))
    p.curveTo((wd, he - fw), (wd, ha(he) + (ha(he) - fw) * 0.1), (wd, ha(he)))
    p.closePath()

# 上向きカーブ
def upwardCurve(p, fw, wd):
    p.moveTo((wd - fw, ha(he) - fw))
    p.curveTo((wd - fw, he * 0.45 - fw * 0.9), (wd - fw, 0), (wd - fw - ha(wd - fw), 0))
    p.curveTo((0, 0), (0, he * 0.45), (0, ha(he)))
    p.lineTo((fw, ha(he)))
    p.curveTo((fw, ha(he) - (ha(he) - fw) * 0.1), (fw, fw), (ha(wd), fw))
    p.curveTo((wd - fw, fw), (wd - fw, ha(he) - (ha(he) - fw) * 0.1), (wd - fw, ha(he)))
    p.closePath()

# 短下向きカーブ用しっぽ
def shortDownwardTail(p, fw, wd):
    p.moveTo((wd, ha(he)))
    p.lineTo((wd, 0))
    p.lineTo((wd - fw, 0))
    p.lineTo((wd - fw, ha(he)))
    p.closePath()

# 短下向きカーブ用しっぽ（右）
def shortRightDownwardTail(p, fw, wd):
    p.moveTo((wd * 2 - fw, ha(he)))
    p.lineTo((wd * 2 - fw, 0))
    p.lineTo((wd * 2 - fw * 2, 0))
    p.lineTo((wd * 2 - fw * 2, ha(he)))
    p.closePath()

# 短上向きカーブ用しっぽ
def shortUpwardTail(p, fw, wd):
    p.moveTo((0, ha(he)))
    p.lineTo((0, he))
    p.lineTo((fw, he))
    p.lineTo((fw, ha(he)))
    p.closePath()

# 長下向きカーブ用しっぽ
def longDownwardTail(p, fw, wd):
    p.moveTo((wd, ha(he)))
    p.curveTo((wd, ha(he) - he * 0.15), (wd, -he), (wd + ha(fw), -he))
    p.lineTo((wd - ha(fw), -he))
    p.curveTo((wd - fw, -he), (wd - fw, -he * 0.55), (wd - fw, -ha(he)))
    p.lineTo((wd - fw, ha(he)))
    p.closePath()

# 長下向きカーブ用しっぽ（右）
def longRightDownwardTail(p, fw, wd):
    p.moveTo((wd * 2 - fw, ha(he)))
    p.curveTo((wd * 2 - fw, ha(he) - he * 0.15), (wd * 2 - fw, -he), (wd * 2 - ha(fw), -he))
    p.lineTo((wd * 2 - fw - ha(fw), -he))
    p.curveTo((wd * 2 - fw * 2, -he), (wd * 2 - fw * 2, -he * 0.55), (wd * 2 - fw * 2, -ha(he)))
    p.lineTo((wd * 2 - fw * 2, ha(he)))
    p.closePath()

# 長上向きカーブ用しっぽ
def longUpwardTail(p, fw, wd):
    p.moveTo((0, ha(he)))
    p.curveTo((0, ha(he) + he * 0.15), (0, db(he)), (-ha(fw), db(he)))
    p.lineTo((ha(fw), db(he)))
    p.curveTo((fw, db(he)), (fw, he * 1.55), (fw, he + ha(he)))
    p.lineTo((fw, ha(he)))
    p.closePath()

# 半円（左）
def leftCircle(p, fw, wd):
    # 左上
    p.moveTo((0, ha(he)))
    p.curveTo((0, he * 0.55), (0, he), (ha(wd), he))
    p.lineTo((ha(wd), he - fw * 0.8))
    p.curveTo((fw, he - fw * 0.8), (fw, ha(he) + (ha(he) - fw * 0.8) * 0.1), (fw, ha(he)))
    p.closePath()
    # 左下
    p.moveTo((0, ha(he)))
    p.curveTo((0, he * 0.45), (0, 0), (ha(wd), 0))
    p.lineTo((ha(wd), fw * 0.8))
    p.curveTo((fw, fw * 0.8), (fw, ha(he) - (ha(he) - fw * 0.8) * 0.1), (fw, ha(he)))
    p.closePath()

# 半円（右）
def rightCircle(p, fw, wd):
    # 右上
    p.moveTo((wd, ha(he)))
    p.curveTo((wd, he * 0.55), (wd, he), (ha(wd), he))
    p.lineTo((ha(wd), he - fw * 0.8))
    p.curveTo((wd - fw, he - fw * 0.8), (wd - fw, ha(he) + (he - fw * 0.8) * 0.1), (wd - fw, ha(he)))
    p.closePath()
    # 右下
    p.moveTo((wd, ha(he)))
    p.curveTo((wd, he * 0.45), (wd, 0), (ha(wd), 0))
    p.lineTo((ha(wd), fw * 0.8))
    p.curveTo((wd - fw, fw * 0.8), (wd - fw, ha(he) - (ha(he) - fw * 0.8) * 0.1), (wd - fw, ha(he)))
    p.closePath()

# 丸の端（上）
def upperrightShortestCircle(p, fw, wd):
    p.moveTo((ha(wd), he))
    p.curveTo((wd, he), (wd, he * 0.64), (wd, he * 0.6))
    p.lineTo((wd - fw, he * 0.6))
    p.curveTo((wd - fw, he * 0.6 + (he - fw * 0.8 - he * 0.6) * 0.1), (wd - fw, he - fw * 0.8), (ha(wd), he - fw * 0.8))
    p.closePath()

# 丸の端（下）
def lowerrightShortestCircle(p, fw, wd):
    p.moveTo((ha(wd), 0))
    p.curveTo((wd, 0), (wd, he * 0.36), (wd, he * 0.4))
    p.lineTo((wd - fw, he * 0.4))
    p.curveTo((wd - fw, he * 0.4 - (he * 0.4 - fw * 0.8) * 0.1), (wd - fw, fw * 0.8), (ha(wd), fw * 0.8))
    p.closePath()

# セミコロン
def semicolon(p, fw, wd):
    p.moveTo((0, he + ha(he)))
    p.lineTo((0, -ha(he)))
    p.lineTo((fw, -ha(he)))
    p.lineTo((fw, he + ha(he)))
    p.closePath()
    p.moveTo((fw + 100, he + ha(he)))
    p.lineTo((fw + 100, -ha(he)))
    p.lineTo((fw * 2 + 100, -ha(he)))
    p.lineTo((fw * 2 + 100, he + ha(he)))
    p.closePath()

# アポストロフィ
def apostrophe(p, fw, wd):
    p.moveTo((0, db(he)))
    p.lineTo((0, he * 1.5))
    p.lineTo((fw, he * 1.6))
    p.lineTo((fw, db(he)))
    p.closePath()

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

# （……u、円と斜線が合わさって大変なことになってる？）