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

# 平均値の計算 ←なくてもいい……？
def av(number1, number2):
    av = (number1 + number2) / 2
    return av

# -------------------------------------------------- 部品をつくって、グリフいじりの効率を上げる！ --------------------------------------------------

# 名前は、「長さ, 位置, 形状, 種類」の順に統一！
# とにかく時計回りに描く！

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

# 短縦棒（中）
def shortCenterVerticalBar(p, fw, wd):
    p.moveTo((ha(wd) - ha(fw), 0))
    p.lineTo((ha(wd) - ha(fw), he))
    p.lineTo((ha(wd) + ha(fw), he))
    p.lineTo((ha(wd) + ha(fw), 0))
    p.closePath()

# 短縦棒（上）
def shortAboveVerticalBar(p, fw, wd):
    p.moveTo((ha(wd) - ha(fw), he - fw * 0.8))
    p.lineTo((ha(wd) - ha(fw), db(he)))
    p.lineTo((ha(wd) + ha(fw), db(he)))
    p.lineTo((ha(wd) + ha(fw), he - fw * 0.8))
    p.closePath()

# 短縦棒（下）
def shortBelowVerticalBar(p, fw, wd):
    p.moveTo((ha(wd) - ha(fw), -he))
    p.lineTo((ha(wd) - ha(fw), fw * 0.8))
    p.lineTo((ha(wd) + ha(fw), fw * 0.8))
    p.lineTo((ha(wd) + ha(fw), -he))

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
    p.moveTo((wd - fw * 0.9, 0))
    p.lineTo((wd - fw, ha(he) - fw))
    p.lineTo((wd - fw, he))
    p.lineTo((wd, he))
    p.lineTo((wd, 0))
    p.closePath()

# 短両カーブ接続用縦棒
def shortRightConnectcurvesBar(p, fw, wd):
    p.moveTo((wd - fw * 0.9, 0))
    p.lineTo((wd - fw, ha(he) - fw))
    p.lineTo((wd - fw, he))
    p.lineTo((wd - fw * 0.1, he))
    p.lineTo((wd, ha(he) + fw))
    p.lineTo((wd, 0))
    p.closePath()

# 短カーブ接続用縦棒（超右）
def shortRightestConnectcurveBar(p, fw, wd):
    p.moveTo((wd * 2 - fw * 1.9, 0))
    p.lineTo((wd * 2 - fw * 2, ha(he) - fw))
    p.lineTo((wd * 2 - fw * 2, he))
    p.lineTo((wd * 2 - fw, he))
    p.lineTo((wd * 2 - fw, 0))
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

# 短横棒（中）
def shortCenterHorizontalBar(p, fw, wd):
    p.moveTo((0, ha(he) - ha(fw)))
    p.lineTo((0, ha(he) + ha(fw)))
    p.lineTo((wd, ha(he) + ha(fw)))
    p.lineTo((wd, ha(he) - ha(fw)))
    p.closePath()

# 超短横棒（中）
def shortestCenterHorizontalBar(p, fw, wd):
    p.moveTo((ha(fw), ha(he) - ha(fw)))
    p.lineTo((ha(fw), ha(he) + ha(fw)))
    p.lineTo((wd - ha(fw), ha(he) + ha(fw)))
    p.lineTo((wd - ha(fw), ha(he) - ha(fw)))
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

# ダブル下向きカーブ
def downwardDoublecurve(p, fw, wd):
    # 最初は下向きカーブ
    p.moveTo((fw, ha(he) + fw))
    p.curveTo((fw, he * 0.55 + fw * 0.9), (fw, he), (fw + ha(wd - fw), he))
    p.curveTo((wd - fw * 0.2, he), (wd - fw * 0.2, ha(he) + fw + (ha(he) - fw) * 0.1), (wd - fw * 0.2, ha(he) + fw))
    # 途中から下向きカーブ（右）
    p.curveTo((wd - fw * 0.2, he * 0.55 + fw * 0.9), (wd - fw * 0.2, he), (wd + ha(wd - fw), he))
    p.curveTo((wd * 2 - fw, he), (wd * 2 - fw, he * 0.55), (wd * 2 - fw, ha(he)))
    p.lineTo((wd * 2 - fw * 2, ha(he)))
    p.curveTo((wd * 2 - fw * 2, ha(he) + (ha(he) - fw) * 0.1), (wd * 2 - fw * 2, he - fw), (ha(wd) - fw + wd, he - fw))
    p.curveTo((wd, he - fw), (wd, ha(he) + (ha(he) - fw) * 0.1), (wd, ha(he)))
    # 短下向きカーブ用しっぽを経由
    p.lineTo((wd, 0))
    p.lineTo((wd - fw, 0))
    p.lineTo((wd - fw, ha(he)))
    # 下向きカーブに戻る
    p.curveTo((wd - fw, ha(he) + (ha(he) - fw) * 0.1), (wd - fw, he - fw), (ha(wd), he - fw))
    p.curveTo((fw, he - fw), (fw, ha(he) + (ha(he) - fw) * 0.1), (fw, ha(he)))
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

# ダブル上向きカーブ
def upwardDoublecurve(p, fw, wd):
    # 最初は上向きカーブ（右）
    p.moveTo((wd * 2 - fw * 2, ha(he) - fw))
    p.curveTo((wd * 2 - fw * 2, he * 0.45 - fw * 0.9), (wd * 2 - fw * 2, 0), (wd * 2 - fw * 2 - ha(wd - fw), 0))
    p.curveTo((wd - fw * 0.8, 0), (wd - fw * 0.8, ha(he) - fw - (ha(he) - fw) * 0.1), (wd - fw * 0.8, ha(he) - fw))
    # 途中から上向きカーブ
    p.curveTo((wd - fw * 0.8, he * 0.45 - fw * 0.9), (wd - fw * 0.8, 0), (wd - fw - ha(wd - fw), 0))
    p.curveTo((0, 0), (0, he * 0.45), (0, ha(he)))
    p.lineTo((fw, ha(he)))
    p.curveTo((fw, ha(he) - (ha(he) - fw) * 0.1), (fw, fw), (ha(wd), fw))
    p.curveTo((wd - fw, fw), (wd - fw, ha(he) - (ha(he) - fw) * 0.1), (wd - fw, ha(he)))
    # 短上向きカーブ用しっぽ（右）を経由
    p.lineTo((wd - fw, he))
    p.lineTo((wd, he))
    p.lineTo((wd, ha(he)))
    # 上向きカーブに戻る（右）
    p.curveTo((wd, ha(he) - (ha(he) - fw) * 0.1), (wd, fw), (wd + ha(wd) - fw, fw))
    p.curveTo((wd * 2 - fw * 2, fw), (wd * 2 - fw * 2, ha(he) - (ha(he) - fw) * 0.1), (wd * 2 -  fw * 2, ha(he)))
    p.closePath()

# シンメトリー上向きカーブ
def symmetricalCurve(p, fw, wd):
    p.moveTo((wd - fw, ha(he) - fw))
    p.curveTo((wd - fw, (ha(he) - fw) * 0.9), (wd - fw, 0), (ha(wd), 0))
    p.curveTo((fw, 0), (fw, (ha(he) - fw) * 0.9), (fw, ha(he) - fw))
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

# 短下向きカーブ用しっぽ（左）
def shortLeftDownwardTail(p, fw, wd):
    p.moveTo((fw, ha(he)))
    p.lineTo((fw, 0))
    p.lineTo((0, 0))
    p.lineTo((0, ha(he)))
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

# 長下向きカーブ用しっぽ（左）
def longLeftDownwardTail(p, fw, wd):
    p.moveTo((fw, ha(he)))
    p.lineTo((fw, -ha(he)))
    p.curveTo((fw, -he * 0.55), (fw, -he), (ha(fw), -he))
    p.lineTo((-ha(fw), -he))
    p.curveTo((0, -he), (0, ha(he) - he * 0.15), (0, ha(he)))
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

# i用しっぽ
def iTail(p, fw, wd):
    # 左側（cみたいな形の部分）
    p.moveTo((ha(wd), 0))
    p.curveTo((0, 0), (0, (he / 4 + fw * 0.2) * 0.9), (0, he / 4 + fw * 0.2))
    p.curveTo((0, (he / 4 + fw * 0.2)), (0, ha(he) + fw * 0.4), (ha(wd), ha(he) + fw * 0.4))
    p.lineTo((ha(wd), ha(he) - fw * 0.4))
    p.curveTo((fw, ha(he) - fw * 0.4), (fw, he / 4 + fw * 0.2 + (he / 4 - fw * 0.6) * 0.1), (fw, he / 4 + fw * 0.2))
    p.curveTo((fw, he / 4 + fw * 0.2 - (he / 4 - fw * 0.6) * 0.1), (fw, fw * 0.8), (ha(wd), fw * 0.8))
    p.closePath()
    # 右側（zみたいな形の部分）
    p.moveTo((ha(wd), ha(he) + fw * 0.4))
    p.curveTo((wd * 0.9, ha(he) + fw * 0.4), (wd * 0.8, fw), (wd * 1.1, fw))
    p.lineTo((wd * 1.1, 0))
    p.curveTo((wd * 0.8, 0), (wd * 0.9, ha(he) - fw * 0.4), (ha(wd), ha(he) - fw * 0.4))
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
    p.moveTo((fw, ha(he)))
    p.curveTo((fw, ha(he) - (ha(he) - fw * 0.8) * 0.1), (fw, fw * 0.8), (ha(wd), fw * 0.8))
    p.lineTo((ha(wd), 0))
    p.curveTo((0, 0), (0, he * 0.45), (0, ha(he)))
    p.closePath()

# 半円（右）
def rightCircle(p, fw, wd):
    # 右上
    p.moveTo((wd - fw, ha(he)))
    p.curveTo((wd - fw, ha(he) + (he - fw * 0.8) * 0.1), (wd - fw, he - fw * 0.8), (ha(wd), he - fw * 0.8))
    p.lineTo((ha(wd), he))
    p.curveTo((wd, he), (wd, he * 0.55), (wd, ha(he)))
    p.closePath()
    # 右下
    p.moveTo((wd, ha(he)))
    p.curveTo((wd, he * 0.45), (wd, 0), (ha(wd), 0))
    p.lineTo((ha(wd), fw * 0.8))
    p.curveTo((wd - fw, fw * 0.8), (wd - fw, ha(he) - (ha(he) - fw * 0.8) * 0.1), (wd - fw, ha(he)))
    p.closePath()

# 丸の端（左上）
def shortestUpperleftCircle(p, fw, wd):
    p.moveTo((0, he * 0.6))
    p.curveTo((0, he * 0.64), (0, he), (ha(wd), he))
    p.lineTo((ha(wd), he - fw * 0.8))
    p.curveTo((fw, he - fw * 0.8), (fw, he * 0.6 + (he - fw * 0.8 - he * 0.6) * 0.1), (fw, he * 0.6))
    p.closePath()

# 丸の端（右上）
def shortestUpperrightCircle(p, fw, wd):
    p.moveTo((wd - fw, he * 0.6))
    p.curveTo((wd - fw, he * 0.6 + (he - fw * 0.8 - he * 0.6) * 0.1), (wd - fw, he - fw * 0.8), (ha(wd), he - fw * 0.8))
    p.lineTo((ha(wd), he))
    p.curveTo((wd, he), (wd, he * 0.64), (wd, he * 0.6))
    p.closePath()

# 丸の端（右下）
def shortestLowerrightCircle(p, fw, wd):
    p.moveTo((wd, he * 0.4))
    p.curveTo((wd, he * 0.36), (wd, 0), (ha(wd), 0))
    p.lineTo((ha(wd), fw * 0.8))
    p.curveTo((wd - fw, fw * 0.8), (wd - fw, he * 0.4 - (he * 0.4 - fw * 0.8) * 0.1), (wd - fw, he * 0.4))
    p.closePath()

# セミコロン
def semicolon(p, fw, wd):
    p.moveTo((0, -ha(he)))
    p.lineTo((0, he + ha(he)))
    p.lineTo((fw, he + ha(he)))
    p.lineTo((fw, -ha(he)))
    p.closePath()
    p.moveTo((fw + 100, -ha(he)))
    p.lineTo((fw + 100, he + ha(he)))
    p.lineTo((fw * 2 + 100, he + ha(he)))
    p.lineTo((fw * 2 + 100, -ha(he)))
    p.closePath()

# 不等号
def inequalitysign(p, fw, wd):
    p.moveTo((0, he * 1.5))
    p.lineTo((fw + 50, db(he)))
    p.lineTo((fw * 2 + 100, he * 1.5))
    p.lineTo((fw * 1.2 + 100, he * 1.5))
    p.lineTo((fw + 50, db(he) - fw * 0.8))
    p.lineTo((fw * 0.8, he * 1.5))
    p.closePath()

# アポストロフィ
def apostrophe(p, fw, wd):
    p.moveTo((0, he * 1.5))
    p.lineTo((0, db(he)))
    p.lineTo((fw, db(he)))
    p.lineTo((fw, he * 1.6))
    p.closePath()