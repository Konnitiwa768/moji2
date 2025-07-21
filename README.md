# xefasic-dabeka-pado-tofxolfe
https://github.com
i

https://konnitiwa768.github.io/Astedmm/A.html

i


https://konnitiwa768.github.io/xefasic-dabeka-pado-tofxolfe/Hi.html
https://gemini.google.com
い
https://github.com/konnitiwa768/astedmm
https://scratch.mit.edu
live at https://konnitiwa768.github.io/xefasic-dabeka-pado-tofxolfe/out/ttf/lakof-regular.ttf
https://konnitiwa768.github.io/xefasic-dabeka-pado-tofxolfe/A.html

https://konnitiwa768.github.io/xefasic-dabeka-pado-tolxolfe/out/ttf/lakof-regular.ttf
xefasic neda sadabek tofxolfe;. tofxolfe; de'dabeka nedo sagek nef "lakof".
# -------------------------------------------------- importゾーン --------------------------------------------------
https://chatgpt.com
import fontforge # 相変わらず「インポート "fontforge" を解決できませんでした」と言われる日々（？）

# 相対パスだかなんだかの関係で、componentsの前に . を入れないと「そんなモジュールないよ」って言われる　あとで理解しとく
from .components import *

# -------------------------------------------------- グリフいじり（？）をする！ --------------------------------------------------

def lakof_generator(font, weight):

    # 太さの設定
    if weight == "Thin":
        fontweight = 50
    elif weight == "Regular":
        fontweight = 100
    elif weight == "Bold":
        fontweight = 150

    width = fontweight + 350

    fw = fontweight
    wd = width

    # -------------------------------------------------- 小文字 --------------------------------------------------
    glyph = font.createChar(ord("p"), "p")
    pen = glyph.glyphPen()
    symmetricalCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("b"), "b")
    pen = glyph.glyphPen()
    symmetricalCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    longLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("k"), "k")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardDoublecurve(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("g"), "g")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardDoublecurve(pen, fw, wd)
    longRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("t"), "t")
    pen = glyph.glyphPen()
    upwardDoublecurve(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    shortRightestConnectcurveBar(pen, fw, wd)

    glyph = font.createChar(ord("d"), "d")
    pen = glyph.glyphPen()
    upwardDoublecurve(pen, fw, wd)
    longUpwardTail(pen, fw, wd)
    shortRightestConnectcurveBar(pen, fw, wd)

    glyph = font.createChar(ord("s"), "s")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    shortDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("z"), "z")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    longDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("f"), "f")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)

    glyph = font.createChar(ord("v"), "v")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    longUpwardTail(pen, fw, wd)

    glyph = font.createChar(ord("c"), "c")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    shortRightConnectcurvesBar(pen, fw, wd)
    rightDownwardCurve(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("q"), "q")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    longUpwardTail(pen, fw, wd)
    shortRightConnectcurvesBar(pen, fw, wd)
    rightDownwardCurve(pen, fw, wd)
    longRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("n"), "n")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortForwardslashBar(pen, fw, wd)
    shortRightVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("m"), "m")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortForwardslashBar(pen, fw, wd)
    shortRightVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("l"), "l")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("x"), "x")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortBelowHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("y"), "y")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    shortestLowerrightCircle(pen, fw, wd)
    shortAboveVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("w"), "w")
    pen = glyph.glyphPen()
    rightCircle(pen, fw, wd)
    shortestUpperleftCircle(pen, fw, wd)
    shortBelowVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("a"), "a")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)

    glyph = font.createChar(ord("e"), "e")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    shortestUpperrightCircle(pen, fw, wd)
    shortestLowerrightCircle(pen, fw, wd)

    glyph = font.createChar(ord("i"), "i")
    pen = glyph.glyphPen()
    shortestUpperleftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    iTail(pen, fw, wd)

    glyph = font.createChar(ord("o"), "o")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    shortestCenterHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("u"), "u")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    longForwardslashBar(pen, fw, wd)

    # -------------------------------------------------- 一応大文字も --------------------------------------------------
    glyph = font.createChar(ord("P"), "P")
    pen = glyph.glyphPen()
    symmetricalCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    shortLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("B"), "B")
    pen = glyph.glyphPen()
    symmetricalCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    longLeftDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("K"), "K")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardDoublecurve(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("G"), "G")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardDoublecurve(pen, fw, wd)
    longRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("T"), "T")
    pen = glyph.glyphPen()
    upwardDoublecurve(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    shortRightestConnectcurveBar(pen, fw, wd)

    glyph = font.createChar(ord("D"), "D")
    pen = glyph.glyphPen()
    upwardDoublecurve(pen, fw, wd)
    longUpwardTail(pen, fw, wd)
    shortRightestConnectcurveBar(pen, fw, wd)

    glyph = font.createChar(ord("S"), "S")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    shortDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("Z"), "Z")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    longDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("F"), "F")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)

    glyph = font.createChar(ord("V"), "V")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    longUpwardTail(pen, fw, wd)

    glyph = font.createChar(ord("C"), "C")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    shortRightConnectcurvesBar(pen, fw, wd)
    rightDownwardCurve(pen, fw, wd)
    shortRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("Q"), "Q")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    longUpwardTail(pen, fw, wd)
    shortRightConnectcurvesBar(pen, fw, wd)
    rightDownwardCurve(pen, fw, wd)
    longRightDownwardTail(pen, fw, wd)

    glyph = font.createChar(ord("N"), "N")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortForwardslashBar(pen, fw, wd)
    shortRightVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("M"), "M")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortForwardslashBar(pen, fw, wd)
    shortRightVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("L"), "L")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    shortHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("X"), "X")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortBelowHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("Y"), "Y")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    shortestLowerrightCircle(pen, fw, wd)
    shortAboveVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("W"), "W")
    pen = glyph.glyphPen()
    rightCircle(pen, fw, wd)
    shortestUpperleftCircle(pen, fw, wd)
    shortBelowVerticalBar(pen, fw, wd)

    glyph = font.createChar(ord("A"), "A")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)

    glyph = font.createChar(ord("E"), "E")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    shortestUpperrightCircle(pen, fw, wd)
    shortestLowerrightCircle(pen, fw, wd)

    glyph = font.createChar(ord("I"), "I")
    pen = glyph.glyphPen()
    shortestUpperleftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    iTail(pen, fw, wd)

    glyph = font.createChar(ord("O"), "O")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    shortestCenterHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("U"), "U")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    longForwardslashBar(pen, fw, wd)

    # -------------------------------------------------- 数字 --------------------------------------------------
    glyph = font.createChar(ord("0"), "0")
    pen = glyph.glyphPen()
    shortBackslashBar(pen, fw, wd)
    shortForwardslashBar(pen, fw, wd)

    glyph = font.createChar(ord("1"), "1")
    pen = glyph.glyphPen()
    shortRightVerticalBar(pen, fw, wd)
    belowNumberTail(pen, fw, wd)

    glyph = font.createChar(ord("2"), "2")
    pen = glyph.glyphPen()
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    shortRightVerticalBar(pen, fw, wd)
    belowNumberTail(pen, fw, wd)

    glyph = font.createChar(ord("3"), "3")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    shortRightVerticalBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    belowNumberTail(pen, fw, wd)

    glyph = font.createChar(ord("4"), "4")
    pen = glyph.glyphPen()
    shortConnectcurveBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    shortDownwardTail(pen, fw, wd)
    belowNumberTail(pen, fw, wd)

    glyph = font.createChar(ord("5"), "5")
    pen = glyph.glyphPen()
    triangle(pen, fw, wd)

    glyph = font.createChar(ord("6"), "6")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    aboveNumberTail(pen, fw, wd)

    glyph = font.createChar(ord("7"), "7")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    leftCircle(pen, fw, wd)
    rightCircle(pen, fw, wd)
    aboveNumberTail(pen, fw, wd)

    glyph = font.createChar(ord("8"), "8")
    pen = glyph.glyphPen()
    shortVerticalBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    shortDownwardTail(pen, fw, wd)
    aboveNumberTail(pen, fw, wd)

    glyph = font.createChar(ord("9"), "9")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortUpwardTail(pen, fw, wd)
    aboveNumberTail(pen, fw, wd)

    # -------------------------------------------------- 約物 --------------------------------------------------
    glyph = font.createChar(ord(" "), " ")
    pen = glyph.glyphPen()
    empty(pen, fw, wd)

    glyph = font.createChar(ord(","), ",")
    pen = glyph.glyphPen()
    comma(pen, fw, wd)

    glyph = font.createChar(ord("."), ".")
    pen = glyph.glyphPen()
    longestForwardslashBar(pen, fw, wd)

    glyph = font.createChar(ord("!"), "!")
    pen = glyph.glyphPen()
    longestForwardslashBar(pen, fw, wd)
    shortBackslashBar(pen, fw, wd)

    glyph = font.createChar(ord("?"), "?")
    pen = glyph.glyphPen()
    shortCenterVerticalBar(pen, fw, wd)
    shortCenterHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("-"), "-")
    pen = glyph.glyphPen()
    shortCenterHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord(";"), ";")
    pen = glyph.glyphPen()
    semicolon(pen, fw, wd)

    glyph = font.createChar(ord("<"), "<")
    pen = glyph.glyphPen()
    inequalitysign(pen, fw, wd)

    glyph = font.createChar(ord(">"), ">")
    pen = glyph.glyphPen()
    inequalitysign(pen, fw, wd)

    glyph = font.createChar(ord("“"), "“")
    pen = glyph.glyphPen()
    shortUpperleftVerticalBar(pen, fw, wd)
    shortAboveHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("”"), "”")
    pen = glyph.glyphPen()
    shortUpperrightVerticalBar(pen, fw, wd)
    shortAboveHorizontalBar(pen, fw, wd)

    glyph = font.createChar(ord("'"), "'")
    pen = glyph.glyphPen()
    apostrophe(pen, fw, wd)

    # -------------------------------------------------- 余白とかの設定 --------------------------------------------------
    # 縦の余白
    font.ascent = 1050

    # 横の余白
    for glyph in font.glyphs():
        glyph.left_side_bearing = 50
        glyph.right_side_bearing = 50

    # -------------------------------------------------- 絶望のカーニング設定 --------------------------------------------------
    font.addLookup("wipit", "gpos_pair", None, (("wpt",(("latn",("dflt")),)),))

    # xとのカーニングを調整する文字たち
    nedus_safakesa_x = ["other", "p", "P", "k", "K", "g", "G", "t", "T", "d", "D", "s", "S", "z", "Z", "f", "F", "v", "V", "c", "C", "q", "Q", "n", "N", "l", "L", \
                            "a", "A", "e", "E", "i", "I", "o", "O", "u", "U", \
                            "0", "5", "6", "7", "8", "9", \
                            ",", "?", "-", ";", "<", ">", "“", "”", "'"]
    
    wipit_xet = []
    for i in range(104):
        wipit_xet.append(-fw)

    wipit_xet[0] = 0
    wipit_xet[52] = 0

    font.addKerningClass("wipit", "x_nedus", ["x", "X"], nedus_safakesa_x, wipit_xet)

    # ,とのカーニングを調整する文字たち
    nedus_safakesa_comma = ["y", "Y", "w", "W", \
                                "a", "A", "e", "E", "o", "O", "u", "U", \
                                "6", \
                                ".", "?", "-", "<", ">", "“", "”", "'"]

    wipit_commat = []
    for i in range(42):
        wipit_commat.append(-fw)

    ledixonu = range(42)
    even_safakesa_comma = []

    for i in ledixonu:
        if i % 2 == 0:
            even_safakesa_comma.append(i) #ledixonuから偶数を取り出す

    for i in even_safakesa_comma:
        wipit_commat[i] = 0

    font.addKerningClass("wipit", "nedus_comma", nedus_safakesa_comma, ["other", ","], wipit_commat)
