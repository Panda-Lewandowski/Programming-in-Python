from tkinter import *

s = 4  # МАСШТАБ
ivory = '#FFFFF0'
lavender = '#E6E6FA'
b = 'black'

root = Tk()
cnv = Canvas(root, height=170 * s, width=180 * s, background=lavender)


# рисуем котика
# тело
# хвост
cnv.create_polygon([40 * s, 95 * s],
                   [44 * s, 105 * s],
                   [39 * s, 120 * s],
                   [55 * s, 145 * s],
                   [30 * s, 135 * s],
                   [23 * s, 110 * s], fill=ivory, outline=b, smooth=1, width=3)

cnv.create_polygon([53 * s, 106 * s],
                   [70 * s, 90 * s],
                   [90 * s, 97 * s],
                   [110 * s, 94 * s],
                   [128 * s, 106 * s],
                   [115 * s, 120 * s],
                   [90 * s, 115 * s],
                   [64 * s, 120 * s], fill=ivory, smooth=1, outline=b, width=3)  # верхняя часть тела


cnv.create_polygon([25 * s, 70 * s],
                   [44 * s, -5 * s],
                   [80 * s, 50 * s], fill=ivory, outline=b, smooth=1, width=3)  # левое ухо
cnv.create_polygon([40 * s, 17 * s],
                   [46 * s, 7 * s],
                   [56 * s, 15 * s], fill=ivory, outline=b, width=3)  # кончик левого уха
cnv.create_polygon([100 * s, 50 * s],
                   [129 * s, -5 * s],
                   [145 * s, 70 * s], fill=ivory, outline=b, smooth=1, width=3)  # правое ухо
cnv.create_polygon([118 * s, 17 * s],
                   [126 * s, 7 * s],
                   [131 * s, 15 * s], fill=ivory, outline=b, width=3)  # кончик правого уха

cnv.create_oval([30 * s, 20 * s],
                [140 * s, 105 * s], fill=ivory, outline=b, width=3)  # голова

# задние лапки
cnv.create_polygon([40 * s, 161 * s],
                   [53 * s, 153 * s],
                   [64 * s, 155 * s],
                   [98 * s, 150 * s],
                   [53 * s, 163 * s], fill=ivory, outline=b, smooth=1, width=3)  # левая

cnv.create_polygon([97 * s, 137 * s],
                   [120 * s, 148 * s],
                   [143 * s, 159 * s],
                   [110 * s, 160 * s], fill=ivory, outline=b, smooth=1, width=3)  # правая

cnv.create_polygon([43 * s, 135 * s],
                   [60 * s, 107 * s],
                   [90 * s, 112 * s],
                   [132 * s, 107 * s],
                   [140 * s, 135 * s],
                   [120 * s, 162 * s],
                   [98 * s, 147 * s],
                   [64 * s, 162 * s], fill=ivory, smooth=1, outline=b, width=3)  # нижняя часть тела

# передние лапки
cnv.create_polygon([98 * s, 140 * s],
                   [95 * s, 125 * s],
                   [118 * s, 120 * s],
                   [115 * s, 140 * s],
                   [104 * s, 160 * s],
                   [80 * s, 169 * s], fill=ivory, outline=b, smooth=1, width=3)  # правая

cnv.create_oval([95 * s, 119 * s],
                [117 * s, 134 * s], fill=ivory, outline=ivory)  # заглушка лишних линий


cnv.create_polygon([53 * s, 106 * s],
                   [65 * s, 95 * s],
                   [75 * s, 99 * s],
                   [96 * s, 88 * s],
                   [80 * s, 113 * s],
                   [64 * s, 120 * s], fill=ivory, outline=b, smooth=1, width=3)

cnv.create_polygon([86 * s, 94 * s],
                   [91 * s, 90 * s],
                   [95 * s, 100 * s],
                   [93 * s, 105 * s], fill=ivory, outline=b, smooth=1, width=3)


# заглушки
cnv.create_oval([40 * s, 14 * s],
                [56 * s, 24 * s], fill=ivory, outline=ivory)

cnv.create_oval([42 * s, 14 * s],
                [58 * s, 24 * s], fill=ivory, outline=ivory)


cnv.create_oval([118 * s, 14 * s],
                [128 * s, 24 * s], fill=ivory, outline=ivory)

cnv.create_oval([121 * s, 13 * s],
                [132 * s, 24 * s], fill=ivory, outline=ivory)

cnv.create_oval([34 * s, 60 * s],
                [77 * s, 25 * s], fill=ivory, outline=ivory)

cnv.create_oval([94 * s, 63 * s],
                [137 * s, 28 * s], fill=ivory, outline=ivory)

cnv.create_oval([79 * s, 121 * s],
                [126 * s, 106 * s], fill=ivory, outline=ivory)

cnv.create_oval([86 * s, 93 * s],
                [92 * s, 97 * s], fill=ivory, outline=ivory)

cnv.create_oval([57 * s, 154 * s],
                [73 * s, 158 * s], fill=ivory, outline=ivory)

cnv.create_oval([113 * s, 154 * s],
                [123 * s, 158 * s], fill=ivory, outline=ivory)


cnv.create_oval([118 * s, 151 * s],
                [128 * s, 156 * s], fill=ivory, outline=ivory)
cnv.pack()
root.mainloop()
