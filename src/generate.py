# -------------------------------------------------- importゾーン --------------------------------------------------

import fontforge # 「インポート "fontforge" を解決できませんでした」って言われる……
import os

# -------------------------------------------------- フォントを生成するぞー！（オー！） --------------------------------------------------

fontfamily = [ext, exr, exb]

# for文で、フォントの種類の数だけフォントを生成する
for fontfamily in fontfamily:

    font = fontforge.font()

    font.familyname = "???"
    font.fullname = "???"
    font.fontname = "???"
    font.weight = "???"
    font.copyright = "©2024 hakuxna"

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
    font.generate("out/ttf/???.ttf")
    font.generate("out/woff/???.woff")
    font.close()