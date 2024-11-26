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
    
    def ttf_path(self):
        ttf_path = "out/ttf/" + self.name + "-" + self.weight.lower() + ".ttf"
        return ttf_path
    
    def woff_path(self):
        woff_path = "out/woff/" + self.name + "-" + self.weight.lower() + ".woff"
        return woff_path

# -------------------------------------------------- インスタンスを作る！ --------------------------------------------------

# フォントの種類
ex = "example"

# フォントの太さ
t = "Thin"
r = "Regular"
b = "Bold"

ext = font_info(ex, t)
exr = font_info(ex, r)
exb = font_info(ex, b)

fontfamily_list = [ext, exr, exb]