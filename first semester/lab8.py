text = ['За окном шел дождь. Но ',
        'небо было чистым. hkj hjkh hkjhkj hkjhkjh hjkhkjh hklhj kllkjkljlkjkljl. Оно окрасилось ',
        'в алый цвет. Пахло землей, ',
        'лавандой и пряным. jhjhgj jgjghg jhgjhgjhg hhggff hghghg hghg ggg  g  g g g rrrrrrrrrrrrrrrrrrrrrrr.']

itr = 0  # кол-во итераций
for i in range(len(text)):
    itr += text[i].count('.')
for i in range(itr):
    _str_ = ''
    flag = 0
    for h in range(len(text)):
        for t in range(len(text[h])):
            if text[h][t] == '.':
                flag = 1
                m = t + 2
                break
            else:
                _str_ += text[h][t]
        if flag == 1:
            n = h
            _str_ += '.'
            break
    print(_str_)
    text = text[n:]
    text[0] = text[0][m:]



