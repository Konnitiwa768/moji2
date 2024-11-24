# -------------------------------------------------- importゾーン --------------------------------------------------

import fontforge # 「インポート "fontforge" を解決できませんでした」って言われる……
import os

# -------------------------------------------------- フォントを生成するぞー！（オー！） --------------------------------------------------

font = fontforge.font()

# aのグリフを適当にいじる
glyph = font.createChar(ord("a"), "a")
pen = glyph.glyphPen()
pen.moveTo((100, 100))
pen.lineTo((200, 100))
pen.lineTo((200, 200))
pen.lineTo((100, 200)) # ちっちゃい正方形
pen.closePath()

# フォントを生成する先のフォルダをつくっておく
if os.path.isdir("out") == False:
    os.mkdir("out")
if os.path.isdir("out/ttf") == False:
    os.mkdir("out/ttf")
if os.path.isdir("out/woff") == False:
    os.mkdir("out/woff")

# いざ生成！
font.generate("out/ttf/example.ttf")
font.generate("out/woff/example.woff")
font.close()