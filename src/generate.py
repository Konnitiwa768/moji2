# -------------------------------------------------- importゾーン --------------------------------------------------

import fontforge # 「インポート "fontforge" を解決できませんでした」って言われる……
import os

from info import fontfamily_list

# -------------------------------------------------- フォントを生成するぞー！（オー！） --------------------------------------------------

fontfamily = fontfamily_list

# for文で、フォントの種類の数だけフォントを生成する
for fontfamily in fontfamily:

    font = fontforge.font()

    fontfamily.edit_glyph(font)

    # フォントの情報のいろいろ
    font.familyname = fontfamily.name
    font.fullname = fontfamily.fullname()
    font.fontname = fontfamily.fontname()
    font.weight = fontfamily.weight
    font.copyright = "©2024 hakuxna"

    # フォントを生成する先のフォルダをつくっておく
    if not os.path.isdir("out"):
        os.mkdir("out")
    if not os.path.isdir("out/ttf"):
        os.mkdir("out/ttf")
    if not os.path.isdir("out/woff"):
        os.mkdir("out/woff")

    # いざ生成！
    font.generate(fontfamily.ttf_path())
    font.generate(fontfamily.woff_path())
    font.close()