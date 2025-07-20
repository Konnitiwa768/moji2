# -------------------------------------------------- importゾーン --------------------------------------------------

import fontforge  # fontforge標準インポート
from lakof.components import *  # components内の全パーツ関数をインポート

# -------------------------------------------------- グリフ生成関数 --------------------------------------------------

def lakof_generator(font, weight):

    if weight == "Thin":
        fontweight = 50
    elif weight == "Regular":
        fontweight = 100
    elif weight == "Bold":
        fontweight = 150
    else:
        fontweight = 100

    width = fontweight + 350
    fw = fontweight
    wd = width

    # -- 小文字 a-z --

    glyph = font.createChar(ord("a"), "a")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)

    glyph = font.createChar(ord("b"), "b")
    pen = glyph.glyphPen()
    symmetricalCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    longLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("c"), "c")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    shortRightConnectcurvesBar(pen, fw, wd)
    rightDownwardCurve(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("d"), "d")
    pen = glyph.glyphPen()
    upwardDoublecurve(pen, fw, wd)
    longUpwardTail(pen, fw, wd)
    shortRightestConnectcurveBar(pen, fw, wd)

    glyph = font.createChar(ord("e"), "e")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    shortestUpperrightCircle(pen, fw, wd)
    shortestLowerrightCircle(pen, fw, wd)

    glyph = font.createChar(ord("f"), "f")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)

    glyph = font.createChar(ord("g"), "g")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardDoublecurve(pen, fw, wd)
    longRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("h"), "h")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)

    glyph = font.createChar(ord("i"), "i")
    pen = glyph.glyphPen()
    shortestUpperleftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    iTail(pen, fw, wd)

    glyph = font.createChar(ord("j"), "j")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    longRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("k"), "k")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardDoublecurve(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("l"), "l")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("m"), "m")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortForwardslashBar(pen, fw, wd)
    shortRightVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("n"), "n")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortForwardslashBar(pen, fw, wd)
    shortRightVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("o"), "o")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    shortestCenterHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("p"), "p")
    pen = glyph.glyphPen()
    symmetricalCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("q"), "q")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    longUpwardTail(pen, fw, wd)
    shortRightConnectcurvesBar(pen, fw, wd)
    rightDownwardCurve(pen, fw, wd)
    longRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("r"), "r")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)

    glyph = font.createChar(ord("s"), "s")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    shortDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("t"), "t")
    pen = glyph.glyphPen()
    upwardDoublecurve(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    shortRightestConnectcurveBar(pen, fw, wd)

    glyph = font.createChar(ord("u"), "u")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    longForwardslashBar(pen, fw, wd)

    glyph = font.createChar(ord("v"), "v")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    longUpwardTail(pen, fw, wd)

    glyph = font.createChar(ord("w"), "w")
    pen = glyph.glyphPen()
    rightCircle(pen, fw, wd)
    shortestUpperleftCircle(pen, fw, wd)
    shortBelowVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("x"), "x")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortBelowHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("y"), "y")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    shortestLowerrightCircle(pen, fw, wd)
    shortAboveVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("z"), "z")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    longDownwardTail(pen, fw, wd)

    # -- 大文字 A-Z （小文字の複製） --

    for c in range(ord('A'), ord('Z') + 1):
        lowercase = chr(c + 32)
        glyph_upper = font.createChar(c, chr(c))
        glyph_lower = font[lowercase]
        glyph_upper.clear()  # 既存のアウトラインを消去
        for contour in glyph_lower.foreground:
            glyph_upper.foreground.appendContour(contour)
        glyph_upper.width = glyph_lower.width

    # -- 記号類 --

    # ! (感嘆符)
    glyph = font.createChar(ord("!"), "exclamation")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortDownwardTail(pen, fw, wd)

    # ? (疑問符)
    glyph = font.createChar(ord("?"), "question")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    upwardCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)

    # , (コンマ)
    glyph = font.createChar(ord(","), "comma")
    pen = glyph.glyphPen()
    shortDownwardTail(pen, fw, wd)

    # . (ピリオド)
    glyph = font.createChar(ord("."), "period")
    pen = glyph.glyphPen()
    circleBar(pen, fw, wd)

    # : (コロン) → ピリオド2つ縦に
    glyph = font.createChar(ord(":"), "colon")
    pen = glyph.glyphPen()
    pen.moveTo(wd*0.5, 600)
    circleBar(pen, fw, wd)
    pen.moveTo(wd*0.5, 300)
    circleBar(pen, fw, wd)

    # ; (セミコロン) → コロン+コンマっぽく
    glyph = font.createChar(ord(";"), "semicolon")
    pen = glyph.glyphPen()
    pen.moveTo(wd*0.5, 600)
    circleBar(pen, fw, wd)
    pen.moveTo(wd*0.5, 300)
    shortDownwardTail(pen, fw, wd)

    # - (ハイフン)
    glyph = font.createChar(ord("-"), "hyphen")
    pen = glyph.glyphPen()
    shortHorizontalBar(pen, fw, wd)

    # _ (アンダースコア)
    glyph = font.createChar(ord("_"), "underscore")
    pen = glyph.glyphPen()
    pen.moveTo(0, 100)
    pen.lineTo(wd, 100)
    pen.closePath()

    # @ (アットマーク)
    glyph = font.createChar(ord("@"), "at")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)

    # # (シャープ)
    glyph = font.createChar(ord("#"), "numbersign")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortHorizontalBar(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)

    # $ (ドル記号)
    glyph = font.createChar(ord("$"), "dollar")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)

    # % (パーセント)
    glyph = font.createChar(ord("%"), "percent")
    pen = glyph.glyphPen()
    shortForwardslashBar(pen, fw, wd)
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)

    # & (アンパサンド)
    glyph = font.createChar(ord("&"), "ampersand")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    # * (アスタリスク)
    glyph = font.createChar(ord("*"), "asterisk")
    pen = glyph.glyphPen()
    shortHorizontalBar(pen, fw, wd)
    shortVerticalBar(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)

    # ( (左括弧)
    glyph = font.createChar(ord("("), "parenleft")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)

    # ) (右括弧)
    glyph = font.createChar(ord(")"), "parenright")
    pen = glyph.glyphPen()
    downwardCurve(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    # [ (左角括弧)
    glyph = font.createChar(ord("["), "bracketleft")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortHorizontalBar(pen, fw, wd)

    # ] (右角括弧)
    glyph = font.createChar(ord("]"), "bracketright")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortHorizontalBar(pen, fw, wd)

    # { (左波括弧)
    glyph = font.createChar(ord("{"), "braceleft")
    pen = glyph.glyphPen()
    upwardDoublecurve(pen, fw, wd)
    downwardDoublecurve(pen, fw, wd)

    # } (右波括弧)
    glyph = font.createChar(ord("}"), "braceright")
    pen = glyph.glyphPen()
    downwardDoublecurve(pen, fw, wd)
    upwardDoublecurve(pen, fw, wd)

    # < (左不等号)
    glyph = font.createChar(ord("<"), "less")
    pen = glyph.glyphPen()
    shortForwardslashBar(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    # > (右不等号)
    glyph = font.createChar(ord(">"), "greater")
    pen = glyph.glyphPen()
    shortRightConnectcurveBar(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)

    # = (等号)
    glyph = font.createChar(ord("="), "equal")
    pen = glyph.glyphPen()
    shortHorizontalBar(pen, fw, wd)
    pen.moveTo(0, 300)
    pen.lineTo(wd, 300)
    pen.closePath()
