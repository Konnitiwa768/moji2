from lakof.components import (
    symmetricalCurve, shortRightConnectcurveBar, leftCircle, verticalBar, 
    longRightConnectcurveBar, shortMiddleCurve, wideOval, downwardCurve, 
    shortLeftConnectcurveBar, circleBar, middleCurve, doubleVerticalBar, 
    wideCircle, middleUpCurve, shortBar, longBar, upwardCurve, 
    shortMiddleConnectcurveBar, longLeftConnectcurveBar, rightConnectcurveBar, 
    middleConnectcurveBar, leftDownwardCurve, rightDownwardCurve, 
    shortSymmetricalCurve, horizontalShortBar
)

def lakof_generator(font, weight):
    if weight == "Thin":
        fontweight = 50
    elif weight == "Regular":
        fontweight = 100
    elif weight == "Bold":
        fontweight = 150
    else:
        raise ValueError("weight must be 'Thin', 'Regular', or 'Bold'")

    width = fontweight + 350
    fw = fontweight
    wd = width

    def draw(char, *parts):
        glyph = font.createChar(ord(char), char)
        pen = glyph.glyphPen()
        for part in parts:
            part(pen, fw, wd)

    char_parts_map = {
        'a': (leftCircle, shortRightConnectcurveBar, shortMiddleCurve),
        'b': (verticalBar, wideOval, shortBar),
        'c': (symmetricalCurve, downwardCurve, shortBar),
        'd': (verticalBar, rightConnectcurveBar, middleCurve),
        'e': (middleCurve, horizontalShortBar, shortLeftConnectcurveBar),
        'f': (longLeftConnectcurveBar, shortMiddleCurve, verticalBar),
        'g': (wideCircle, downwardCurve, shortRightConnectcurveBar),
        'h': (doubleVerticalBar, shortBar, middleUpCurve),
        'i': (shortBar, verticalBar, shortMiddleCurve),
        'j': (longRightConnectcurveBar, shortBar, leftDownwardCurve),
        'k': (verticalBar, rightDownwardCurve, shortSymmetricalCurve),
        'l': (verticalBar, longBar, shortBar),
        'm': (symmetricalCurve, verticalBar, middleConnectcurveBar),
        'n': (verticalBar, middleCurve, rightConnectcurveBar),
        'o': (wideOval, circleBar, shortBar),
        'p': (verticalBar, leftCircle, shortMiddleCurve),
        'q': (wideCircle, shortRightConnectcurveBar, downwardCurve),
        'r': (verticalBar, shortMiddleConnectcurveBar, rightDownwardCurve),
        's': (symmetricalCurve, shortBar, horizontalShortBar),
        't': (shortBar, longBar, verticalBar),
        'u': (leftDownwardCurve, verticalBar, rightDownwardCurve),
        'v': (leftDownwardCurve, rightDownwardCurve, shortBar),
        'w': (symmetricalCurve, middleUpCurve, rightConnectcurveBar),
        'x': (shortSymmetricalCurve, rightDownwardCurve, leftDownwardCurve),
        'y': (shortBar, verticalBar, shortMiddleCurve),
        'z': (horizontalShortBar, downwardCurve, shortRightConnectcurveBar),

        '0': (wideOval, verticalBar, circleBar),
        '1': (verticalBar, shortBar, rightConnectcurveBar),
        '2': (shortBar, middleCurve, downwardCurve),
        '3': (symmetricalCurve, shortBar, horizontalShortBar),
        '4': (verticalBar, shortRightConnectcurveBar, shortBar),
        '5': (shortLeftConnectcurveBar, downwardCurve, horizontalShortBar),
        '6': (wideCircle, leftDownwardCurve, shortBar),
        '7': (shortBar, rightDownwardCurve, verticalBar),
        '8': (doubleVerticalBar, circleBar, symmetricalCurve),
        '9': (wideOval, shortRightConnectcurveBar, shortBar),

        '.': (shortBar,),
        ',': (shortRightConnectcurveBar,),
        '!': (verticalBar, shortBar),
        '?': (symmetricalCurve, shortBar, rightConnectcurveBar),
        ':': (shortBar, shortBar),
        ';': (shortBar, shortRightConnectcurveBar),
        '-': (horizontalShortBar,),
        '_': (longBar,),
        '(': (leftCircle, downwardCurve),
        ')': (rightConnectcurveBar, downwardCurve),
        '[': (verticalBar, shortBar, downwardCurve),
        ']': (verticalBar, shortBar, downwardCurve),
        '{': (symmetricalCurve, leftDownwardCurve, rightDownwardCurve),
        '}': (symmetricalCurve, rightDownwardCurve, leftDownwardCurve),
        '@': (circleBar, verticalBar, horizontalShortBar),
        '#': (doubleVerticalBar, horizontalShortBar, shortBar),
        '$': (verticalBar, circleBar, horizontalShortBar),
        '%': (symmetricalCurve, shortBar, rightConnectcurveBar),
        '&': (leftCircle, rightConnectcurveBar, shortBar),
        '*': (shortBar, verticalBar, horizontalShortBar),
        '+': (verticalBar, horizontalShortBar),
        '=': (horizontalShortBar, horizontalShortBar),
        '/': (rightDownwardCurve, shortBar),
        '\\': (leftDownwardCurve, shortBar),
        '|': (verticalBar,),
        '<': (leftDownwardCurve, shortBar),
        '>': (rightDownwardCurve, shortBar),
        '"': (shortBar, shortBar),
        "'": (shortBar,),
    }

    for char, parts in char_parts_map.items():
        draw(char, *parts)
