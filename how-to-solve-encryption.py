"""暗号化&解読ツールplus_ver2.0.6"""
import urllib.parse as urp
# rot13
def rot13(x):
    a0 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", ",", " ", "_", ":", "/", ";", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "*", "+", "%"]
    a13 = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", ".", ",", " ", "_", ":", "/", ";", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "*", "+", "%"]
    ls = [c for c in x]
    l1 = []
    for i in range(len(ls)):
        l1.append(a13[a0.index(ls[i])])
    return("".join(l1))
# マイナスキー値
def keym(x):
    return(x - 10868) # 10868はキー値
# プラスキー値
def keyp(x):
    return(x + 10868) # 10868はキー値
# 10進数→36進数
def fix10_36(x):
    dgt = 0
    num = x
    while num >= (36 ** dgt):
        dgt += 1
    a = []
    for i in sorted(list(range(dgt)), reverse=True):
        d = num // (36 ** i)
        a.append(d)
        num -= d * (36 ** i)
    def fix(v):
        l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        return(l[v])
    return("".join(list(map(fix, a))))
# 36進数→10進数
def fix36_10(x):
    def dec(w):
        l01 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        return(l01.index(w))
    xl = [c for c in x]
    dgt = len(xl)
    ans = 0
    for i in sorted(list(range(dgt)), reverse=True):
        ans += dec(xl[(dgt - 1) - i]) * (36 ** (i))
    return(ans)
# Unicode変換
def enu(x):
    return(ord(x))
# Unicode復号
def deu(x):
    return(chr(x))
# URL変換
def urle(x):
    return(urp.quote(x))
# URL復号
def urld(x):
    return(urp.unquote(x))
# 大文字小文字変換
def fixchr(x):
    l = [c for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    for i in range(len(x)):
        try:
            int(x[i])
        except:
            try:
                l.index(x[i])
            except:
                return(x[i])
            else:
                a = l.index(x[i]) + 26
                if a >= 52:
                    return(l[a - 52])
                else:
                    return(l[a])
        else:
            return(int(x[i]))
# 文字列2文字区切り
def split2(x):
    return(list(map(str, [x[i: i+2] for i in range(0, len(x), 2)])))
# 文字列5文字区切り
def split5(x):
    return(list(map(str, [x[i: i+5] for i in range(0, len(x), 5)])))
