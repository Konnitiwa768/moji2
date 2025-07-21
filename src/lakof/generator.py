import fontforge
from lakof.components import *

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

    def draw_char(code, name, *shapes):
        glyph = font.createChar(ord(code), name)
        pen = glyph.glyphPen()
        for shape in shapes:
            shape(pen, fw, wd)

    # -- 小文字 a-z --
    draw_char("a", "a", leftCircle, rightCircle)
    draw_char("b", "b", symmetricalCurve, shortRightConnectcurveBar, shortUpwardTail, longLeftDownwardTail)
    draw_char("c", "c", upwardCurve, shortUpwardTail, shortRightConnectcurveBar, rightDownwardCurve, shortRightDownwardTail)
    draw_char("d", "d", upwardDoublecurve, longUpwardTail, shortRightestConnectcurveBar)
    draw_char("e", "e", leftCircle, shortestUpperrightCircle, shortestLowerrightCircle)
    draw_char("f", "f", upwardCurve, shortRightConnectcurveBar, shortUpwardTail)
    draw_char("g", "g", shortConnectcurveBar, downwardDoublecurve, longRightDownwardTail)
    draw_char("h", "h", longVerticalBar, shortRightConnectcurveBar, shortUpwardTail)
    draw_char("i", "i", shortestUpperleftCircle, rightCircle, iTail)
    draw_char("j", "j", shortVerticalBar, shortRightConnectcurveBar, longRightDownwardTail)
    draw_char("k", "k", shortConnectcurveBar, downwardDoublecurve, shortRightDownwardTail)
    draw_char("l", "l", shortVerticalBar, shortHorizontalBar)
    draw_char("m", "m", longVerticalBar, shortForwardslashBar, shortRightVerticalBar)
    draw_char("n", "n", shortVerticalBar, shortForwardslashBar, shortRightVerticalBar)
    draw_char("o", "o", leftCircle, rightCircle, shortHorizontalBar)
    draw_char("p", "p", symmetricalCurve, shortRightConnectcurveBar, shortUpwardTail, shortLeftDownwardTail)
    draw_char("q", "q", upwardCurve, longUpwardTail, shortRightConnectcurveBar, rightDownwardCurve, longRightDownwardTail)
    draw_char("r", "r", shortVerticalBar, shortRightConnectcurveBar, shortUpwardTail)
    draw_char("s", "s", shortConnectcurveBar, downwardCurve, shortDownwardTail)
    draw_char("t", "t", upwardDoublecurve, shortUpwardTail, shortRightestConnectcurveBar)
    draw_char("u", "u", leftCircle, rightCircle, longForwardslashBar)
    draw_char("v", "v", upwardCurve, shortRightConnectcurveBar, longUpwardTail)
    draw_char("w", "w", rightCircle, shortestUpperleftCircle, shortBelowVerticalBar)
    draw_char("x", "x", longVerticalBar, shortBelowHorizontalBar)
    draw_char("y", "y", leftCircle, shortestLowerrightCircle, shortAboveVerticalBar)
    draw_char("z", "z", shortConnectcurveBar, downwardCurve, longDownwardTail)

    # -- 大文字 A-Z --
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        draw_char(ch, ch, *font[ord(ch.lower())].foreground.references)

    # -- 記号類 --
    draw_char("!", "exclamation", shortVerticalBar, shortDownwardTail)
    draw_char("?", "question", shortConnectcurveBar, upwardCurve, shortRightConnectcurveBar)
    draw_char(",", "comma", shortDownwardTail)
    draw_char(".", "period", shortVerticalBar)
    draw_char("-", "hyphen", shortHorizontalBar)
    draw_char("_", "underscore", lambda pen, fw, wd: (pen.moveTo((0,100)), pen.lineTo((wd,100)), pen.closePath()))
    draw_char("@", "at", leftCircle, rightCircle, shortRightConnectcurveBar, shortUpwardTail)
    draw_char("#", "numbersign", shortVerticalBar, shortHorizontalBar, shortRightConnectcurveBar)
    draw_char("$", "dollar", shortVerticalBar, downwardCurve, shortRightConnectcurveBar)
    draw_char("%", "percent", shortForwardslashBar, shortRightDownwardTail)
    draw_char("&", "ampersand", shortConnectcurveBar, downwardDoublecurve, shortRightDownwardTail)
    draw_char("*", "asterisk", shortRightConnectcurveBar, upwardCurve, shortUpwardTail)
    draw_char("(", "parenleft", upwardCurve, shortLeftDownwardTail)
    draw_char(")", "parenright", downwardCurve, shortRightDownwardTail)
    draw_char("[", "bracketleft", shortVerticalBar, shortHorizontalBar)
    draw_char("]", "bracketright", shortVerticalBar, shortHorizontalBar)
    draw_char("{", "braceleft", upwardDoublecurve, downwardDoublecurve)
    draw_char("}", "braceright", downwardDoublecurve, upwardDoublecurve)
    draw_char("<", "less", shortForwardslashBar, shortRightDownwardTail)
    draw_char(">", "greater", shortRightConnectcurveBar, shortLeftDownwardTail)
    draw_char("=", "equal", shortHorizontalBar, lambda pen, fw, wd: (pen.moveTo((0,300)), pen.lineTo((wd,300)), pen.closePath()))

    # -- コロン・セミコロン --
    def colon(pen, fw, wd):
        pen.moveTo((wd*0.5, 600))
        pen.lineTo((wd*0.5 + fw, 600))
        pen.lineTo((wd*0.5 + fw, 600 - fw))
        pen.lineTo((wd*0.5, 600 - fw))
        pen.closePath()
        pen.moveTo((wd*0.5, 300))
        pen.lineTo((wd*0.5 + fw, 300))
        pen.lineTo((wd*0.5 + fw, 300 - fw))
        pen.lineTo((wd*0.5, 300 - fw))
        pen.closePath()

    draw_char(":", "colon", colon)
    draw_char(";", "semicolon", colon, shortDownwardTail)

    return font
