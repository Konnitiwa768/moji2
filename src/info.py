# -------------------------------------------------- importゾーン --------------------------------------------------

from lakof.generator import lakof_generator

# -------------------------------------------------- フォントの情報をまとめるためにクラスを作る！ --------------------------------------------------

class font_info:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def fullname(self):
        fullname = self.name + " " + self.weight
        return fullname
    
    def fontname(self):
        fontname = self.name + "-" + self.weight.lower()
        return fontname
    
    # フォントの種類に対応する関数を引っぱってくる
    def edit_glyph(self, font):
        if self.name == lk:
            if self.weight == t:
                lakof_generator(font, "Thin")
            
            if self.weight == n:
                lakof_generator(font, "Normal")

            if self.weight == r:
                lakof_generator(font, "Regular")

            if self.weight == b:
                lakof_generator(font, "Bold")
    
    def ttf_path(self):
        ttf_path = "out/ttf/" + self.name + "-" + self.weight.lower() + ".ttf"
        return ttf_path
    
    def woff_path(self):
        woff_path = "out/woff/" + self.name + "-" + self.weight.lower() + ".woff"
        return woff_path

# -------------------------------------------------- インスタンスを作る！ --------------------------------------------------

# フォントの種類
lk = "lakof"

# フォントの太さ
t = "Thin"
n = "Normal"
r = "Regular"
b = "Bold"

lkt = font_info(lk, t)
lkr = font_info(lk, r)
lkb = font_info(lk, b)
lkn = font_info(lk, n)
fontfamily_list = [lkt, lkr, lkb, lkn]
