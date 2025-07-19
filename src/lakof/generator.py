from lakof.components import *
import fontforge


def lakof_generator(font, weight):
    if weight == "Thin":
        fontweight = 50
    elif weight == "Regular":
        fontweight = 100
    elif weight == "Bold":
        fontweight = 150

    width = fontweight + 350
    fw = fontweight
    wd = width

    # --- a ---
    glyph = font.createChar(ord("a"), "a")
    pen = glyph.glyphPen()
    symmetricalCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    leftCircle(pen, fw, wd)

    # --- b ---
    glyph = font.createChar(ord("b"), "b")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    longRightConnectcurveBar(pen, fw, wd)
    shortMiddleCurve(pen, fw, wd)

    # --- c ---
    glyph = font.createChar(ord("c"), "c")
    pen = glyph.glyphPen()
    wideOval(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    shortLeftConnectcurveBar(pen, fw, wd)

    # --- d ---
    glyph = font.createChar(ord("d"), "d")
    pen = glyph.glyphPen()
    circleBar(pen, fw, wd)
    middleCurve(pen, fw, wd)
    doubleVerticalBar(pen, fw, wd)

    # --- e ---
    glyph = font.createChar(ord("e"), "e")
    pen = glyph.glyphPen()
    wideCircle(pen, fw, wd)
    middleUpCurve(pen, fw, wd)
    shortBar(pen, fw, wd)

    # --- f ---
    glyph = font.createChar(ord("f"), "f")
    pen = glyph.glyphPen()
    longBar(pen, fw, wd)
    upwardCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)

    # --- g ---
    glyph = font.createChar(ord("g"), "g")
    pen = glyph.glyphPen()
    shortMiddleConnectcurveBar(pen, fw, wd)
    longLeftConnectcurveBar(pen, fw, wd)
    middleDownCurve(pen, fw, wd)

    # --- h ---
    glyph = font.createChar(ord("h"), "h")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    rightConnectcurveBar(pen, fw, wd)
    middleConnectcurveBar(pen, fw, wd)

    # --- i ---
    glyph = font.createChar(ord("i"), "i")
    pen = glyph.glyphPen()
    doubleVerticalBar(pen, fw, wd)
    shortBar(pen, fw, wd)

    # --- j ---
    glyph = font.createChar(ord("j"), "j")
    pen = glyph.glyphPen()
    leftDownwardCurve(pen, fw, wd)
    shortLeftConnectcurveBar(pen, fw, wd)
    wideCircle(pen, fw, wd)

    # --- k ---
    glyph = font.createChar(ord("k"), "k")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    rightDownwardCurve(pen, fw, wd)
    upwardCurve(pen, fw, wd)

    # --- l ---
    glyph = font.createChar(ord("l"), "l")
    pen = glyph.glyphPen()
    longBar(pen, fw, wd)
    shortBar(pen, fw, wd)

    # --- m ---
    glyph = font.createChar(ord("m"), "m")
    pen = glyph.glyphPen()
    middleConnectcurveBar(pen, fw, wd)
    shortMiddleCurve(pen, fw, wd)
    shortLeftConnectcurveBar(pen, fw, wd)

    # --- n ---
    glyph = font.createChar(ord("n"), "n")
    pen = glyph.glyphPen()
    shortRightConnectcurveBar(pen, fw, wd)
    shortMiddleConnectcurveBar(pen, fw, wd)
    longVerticalBar(pen, fw, wd)

    # --- o ---
    glyph = font.createChar(ord("o"), "o")
    pen = glyph.glyphPen()
    wideOval(pen, fw, wd)
    leftCircle(pen, fw, wd)

    # --- p ---
    glyph = font.createChar(ord("p"), "p")
    pen = glyph.glyphPen()
    longLeftConnectcurveBar(pen, fw, wd)
    middleCurve(pen, fw, wd)
    shortBar(pen, fw, wd)

    # --- q ---
    glyph = font.createChar(ord("q"), "q")
    pen = glyph.glyphPen()
    rightConnectcurveBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    circleBar(pen, fw, wd)

    # --- r ---
    glyph = font.createChar(ord("r"), "r")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    shortSymmetricalCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)

    # --- s ---
    glyph = font.createChar(ord("s"), "s")
    pen = glyph.glyphPen()
    wideCircle(pen, fw, wd)
    shortMiddleCurve(pen, fw, wd)
    downwardCurve(pen, fw, wd)

    # --- t ---
    glyph = font.createChar(ord("t"), "t")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)
    horizontalShortBar(pen, fw, wd)

    # --- u ---
    glyph = font.createChar(ord("u"), "u")
    pen = glyph.glyphPen()
    shortLeftConnectcurveBar(pen, fw, wd)
    middleConnectcurveBar(pen, fw, wd)
    longRightConnectcurveBar(pen, fw, wd)

    # --- v ---
    glyph = font.createChar(ord("v"), "v")
    pen = glyph.glyphPen()
    shortSymmetricalCurve(pen, fw, wd)
    shortBar(pen, fw, wd)

    # --- w ---
    glyph = font.createChar(ord("w"), "w")
    pen = glyph.glyphPen()
    wideCircle(pen, fw, wd)
    leftCircle(pen, fw, wd)
    rightConnectcurveBar(pen, fw, wd)

    # --- x ---
    glyph = font.createChar(ord("x"), "x")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    downwardCurve(pen, fw, wd)

    # --- y ---
    glyph = font.createChar(ord("y"), "y")
    pen = glyph.glyphPen()
    leftDownwardCurve(pen, fw, wd)
    shortMiddleConnectcurveBar(pen, fw, wd)
    doubleVerticalBar(pen, fw, wd)

    # --- z ---
    glyph = font.createChar(ord("z"), "z")
    pen = glyph.glyphPen()
    middleDownCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    longBar(pen, fw, wd)

    # --- 0 ---
    glyph = font.createChar(ord("0"), "0")
    pen = glyph.glyphPen()
    wideOval(pen, fw, wd)
    circleBar(pen, fw, wd)

    # --- 1 ---
    glyph = font.createChar(ord("1"), "1")
    pen = glyph.glyphPen()
    longVerticalBar(pen, fw, wd)

    # --- 2 ---
    glyph = font.createChar(ord("2"), "2")
    pen = glyph.glyphPen()
    rightConnectcurveBar(pen, fw, wd)
    downwardCurve(pen, fw, wd)
    shortBar(pen, fw, wd)

    # --- 3 ---
    glyph = font.createChar(ord("3"), "3")
    pen = glyph.glyphPen()
    middleCurve(pen, fw, wd)
    shortRightConnectcurveBar(pen, fw, wd)
    shortBar(pen, fw, wd)

    # --- 4 ---
    glyph = font.createChar(ord("4"), "4")
    pen = glyph.glyphPen()
    doubleVerticalBar(pen, fw, wd)
    shortLeftConnectcurveBar(pen, fw, wd)

    # --- 5 ---
    glyph = font.createChar(ord("5"), "5")
    pen = glyph.glyphPen()
    shortRightConnectcurveBar(pen, fw, wd)
    middleDownCurve(pen, fw, wd)
    circleBar(pen, fw, wd)

    # --- 6 ---
    glyph = font.createChar(ord("6"), "6")
    pen = glyph.glyphPen()
    leftDownwardCurve(pen, fw, wd)
    shortMiddleConnectcurveBar(pen, fw, wd)
    wideCircle(pen, fw, wd)

    # --- 7 ---
    glyph = font.createChar(ord("7"), "7")
    pen = glyph.glyphPen()
    upwardCurve(pen, fw, wd)
    longRightConnectcurveBar(pen, fw, wd)

    # --- 8 ---
    glyph = font.createChar(ord("8"), "8")
    pen = glyph.glyphPen()
    wideCircle(pen, fw, wd)
    wideOval(pen, fw, wd)

    # --- 9 ---
    glyph = font.createChar(ord("9"), "9")
    pen = glyph.glyphPen()
    rightDownwardCurve(pen, fw, wd)
    middleCurve(pen, fw, wd)
    longVerticalBar(pen, fw, wd)

    # --- 記号 ---
    def g(c): return font.createChar(ord(c), c).glyphPen()
    g("."); shortBar(g("."), fw, wd)
    g(","); shortBar(g(","), fw, wd); downwardCurve(g(","), fw, wd)
    g("!"); verticalBar(g("!"), fw, wd); shortBar(g("!"), fw, wd)
    g("?"); upwardCurve(g("?"), fw, wd); circleBar(g("?"), fw, wd)
    g(":"); shortBar(g(":"), fw, wd); middleConnectcurveBar(g(":"), fw, wd)
    g(";"); shortBar(g(";"), fw, wd); downwardCurve(g(";"), fw, wd)
    g("-"); horizontalShortBar(g("-"), fw, wd)
    g("_"); horizontalShortBar(g("_"), fw, wd); shortBar(g("_"), fw, wd)
    g("("); leftCircle(g("("), fw, wd)
    g(")"); rightConnectcurveBar(g(")"), fw, wd)
    g("["); longVerticalBar(g("["), fw, wd); shortBar(g("["), fw, wd)
    g("]"); longVerticalBar(g("]"), fw, wd); shortRightConnectcurveBar(g("]"), fw, wd)
    g("{"); leftDownwardCurve(g("{"), fw, wd); upwardCurve(g("{"), fw, wd)
    g("}"); rightDownwardCurve(g("}"), fw, wd); upwardCurve(g("}"), fw, wd)
    g("@"); wideOval(g("@"), fw, wd); shortBar(g("@"), fw, wd); shortLeftConnectcurveBar(g("@"), fw, wd)
    g("#"); longVerticalBar(g("#"), fw, wd); horizontalShortBar(g("#"), fw, wd); doubleVerticalBar(g("#"), fw, wd)
    g("$"); shortMiddleConnectcurveBar(g("$"), fw, wd); longBar(g("$"), fw, wd); shortBar(g("$"), fw, wd)
    g("%"); shortBar(g("%"), fw, wd); shortRightConnectcurveBar(g("%"), fw, wd); downwardCurve(g("%"), fw, wd)
    g("&"); wideCircle(g("&"), fw, wd); upwardCurve(g("&"), fw, wd); shortLeftConnectcurveBar(g("&"), fw, wd)
    g("*"); upwardCurve(g("*"), fw, wd); downwardCurve(g("*"), fw, wd); shortBar(g("*"), fw, wd)
    g("+"); longVerticalBar(g("+"), fw, wd); horizontalShortBar(g("+"), fw, wd)
    g("="); horizontalShortBar(g("="), fw, wd); shortBar(g("="), fw, wd)
    g("/"); rightDownwardCurve(g("/"), fw, wd)
    g("\\"); leftDownwardCurve(g("\\"), fw, wd)
    g("|"); longVerticalBar(g("|"), fw, wd)
    g("<"); longLeftConnectcurveBar(g("<"), fw, wd)
    g(">"); longRightConnectcurveBar(g(">"), fw, wd)
    g("\""); shortBar(g("\""), fw, wd); shortBar(g("\""), fw, wd)
    g("'"); shortBar(g("'"), fw, wd)
