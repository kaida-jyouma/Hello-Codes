"""暗号化ツールplus_ver2.0.9"""
import urllib.parse as urp
# rot13
def rot13(x):
    x = str(x)
    a0 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    a13 = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    ls = [c for c in x]
    for i in range(len(ls)):
        if ls[i] in a0:
            ls[i] = a13[a0.index(ls[i])]
    t = "".join(ls)
    print(t)
# マイナスキー値
def keym(x, k):
    return(x  - k)
# プラスキー値
def keyp(x, k):
    return(x + k)
# 2進数→10進数
def fix2_10(x):
    try:
        int(x)
    except:
        return(x)
    else:
        n = 0
        x = str(x)
        for i in range(len(x)):
            n += (2 ** i) * int(x[len(x) - (i + 1)])
        return(n)
# 3進数→10進数
def fix3_10(x):
    try:
        int(x)
    except:
        return(x)
    else:
        n = 0
        for i in range(len(str(x))):
            n += (3 ** i) * int(str(x)[len(str(x)) - (i + 1)])
        return(n)
# 10進数→2進数
def fix10_2(x):
    try:
        int(x)
    except:
        return(x)
    else:
        n = 0
        strx = str(x)
        l = []
        while True:
            if x % 2**(n + 1) == 2 ** n:
                l.insert(0, 1)
                x -= 2 ** n
            else:
                l.insert(0, 0)
            n += 1
            if 2 ** n > x:
                break
        return("".join([str(k) for k in l]))
# 10進数→3進数
# def 
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
        l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        l.extend(list(map(chr, list(range(97, 123)))))
        return(l[v])
    return("".join(list(map(fix, a))))
# 36進数→10進数
def fix36_10(x):
    def dec(w):
        l01 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        l01.extend(list(map(chr, list(range(97, 123)))))
        return(l01.index(w))
    xl = [c for c in x]
    dgt = len(xl)
    ans = 0
    for i in sorted(list(range(dgt)), reverse=True):
        ans += dec(xl[(dgt - 1) - i]) * (36 ** (i))
    return(ans)
def unic(string, rev=False):
    if not rev:
        return(ord(x))
    else:
        return(chr(x))
# URL変換
def urle(x):
    return(urp.quote(x))
# URL復号
def urld(x):
    return(urp.unquote(x))
# 大文字小文字変換
def fixchr(letter, capital=False):
    l = [c for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    try:
        int(letter)
    except:
        try:
            l.index(letter)
        except:
            return(letter)
        else:
            a = l.index(letter) + 26
            if a > 51 and not capital:
                a -= 52
            elif a > 51:
                a -= 26
            elif a > 25 and not capital:
                a -= 26
        return(l[a])
    else:
        return(letter)
# エニグマもどき
def engmself(string, key=False, rot=0):
    import datetime, time
    # 時間生成
    now = str(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('%y.%m.%d %H.%M.%S'))
    # IP生成
    ip = None
    c1 = []
    for i in range(4):
        c1.append(str(fix2_10("".join([str(randbin(x)) for x in range(8)]))))
    ip = ".".join(c1)
    print(ip)
    if key:
        nout = ip
    else:
        nout = now + "." + str(time.time()).split(".")[1]
    text = [c for c in nout]
    for i in range(text.count(".")):
        text.remove(".")
    noutim = "".join("".join(text).split())
    ct0 = ct1 = ct2 = 0
    for i in list(map(int, [c for c in noutim])):
        if i % 3 == 0:
            ct0 += 1
        elif i % 3 == 1:
            ct1 += 1
        elif i % 3 == 2:
            ct2 += 1
    lstr = [c for c in string]
    alpb = [chr(c) for c in range(97, 123)]
    alpb.extend(list(map(chr, list(range(65, 91)))))
    alpb.extend(list(map(chr, [32, 33, 44, 45, 46, 47, 58, 61, 63, 95])))
    alpb.extend(list(map(chr, list(range(48, 58)))))
    if rot != 0:
        als1 = alpb[-rot:]
        als1.extend(alpb[:len(alpb) - rot])
        alpb = als1
    ansls = []
    for i in range(len(lstr)):
        if i % 3 == 0:
            ind = alpb.index(lstr[i]) + ct0 - ct1 + ct2
            if ind >= len(alpb):
                ind -= len(alpb)
        elif i % 3 == 1:
            ind = alpb.index(lstr[i]) - ct1 + ct2 - ct0
            if ind < 0:
                ind += len(alpb)
        elif i % 3 == 2:
            ind = alpb.index(lstr[i]) + ct2 - ct0 + ct1
            if ind >= len(alpb):
                ind -= len(alpb)
        ansls.append(ind)
    ret = []
    # print(ansls)
    for i in range(len(ansls)):
        ret.append(alpb[ansls[i]])
    if key:
        nout = ip
        return(["".join(ret), nout])
    else:
        return(["".join(ret), nout])
# エニグマもどきの解法
def solvengm(string, keydate, rot=0):
    alpb = [chr(c) for c in range(97, 123)]
    alpb.extend(list(map(chr, list(range(65, 91)))))
    alpb.extend(list(map(chr, [32, 33, 44, 45, 46, 47, 58, 61, 63, 95])))
    alpb.extend(list(map(chr, list(range(48, 58)))))
    nout = keydate
    text = [c for c in nout]
    for i in range(text.count(".")):
        text.remove(".")
    noutim = "".join("".join(text).split())
    ct0 = ct1 = ct2 = 0
    for i in list(map(int, [c for c in noutim])):
        if i % 3 == 0:
            ct0 += 1
        elif i % 3 == 1:
            ct1 += 1
        elif i % 3 == 2:
            ct2 += 1
    lstr = [c for c in string]
    if rot != 0:
        rot = abs(rot)
        als1 = alpb[-rot:]
        als1.extend(alpb[:len(alpb) - rot])
        alpb = als1
    ansls = []
    for i in range(len(lstr)):
        if i % 3 == 0:
            ind = alpb.index(lstr[i]) - ct0 + ct1 - ct2
            if ind < 0:
                ind += len(alpb)
        elif i % 3 == 1:
            ind = alpb.index(lstr[i]) + ct1 - ct2 + ct0
            if ind >= 0:
                ind -= len(alpb)
        elif i % 3 == 2:
            ind = alpb.index(lstr[i]) - ct2 + ct0 - ct1
            if ind < 0:
                ind += len(alpb)
        ansls.append(ind)
    ret = []
    for i in range(len(ansls)):
        ret.append(alpb[ansls[i]])
    return("".join(ret))
# 強化版エニグマもどき
def engmpow(string, key=False, rot=0):
    import datetime, time
    now = str(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('%y.%m.%d-%H.%M.%S'))
    nout = now + "." + str(time.time()).split(".")[1]
    text = [c for c in nout]
    for i in range(text.count(".")):
        text.remove(".")
    noutim = "".join("".join(text).split())
    ct0 = ct1 = ct2 = ct3 = ct4 = ct5 = ct6 = 0
    for i in list(map(int, [c for c in noutim])):
        if i % 7 == 0:
            ct0 += 1
        elif i % 7 == 1:
            ct1 += 1
        elif i % 7 == 2:
            ct2 += 1
        elif i % 7 == 3:
            ct3 += 1
        elif i % 7 == 4:
            ct4 += 1
        elif i % 7 == 5:
            ct5 += 1
        elif i % 7 == 6:
            ct6 += 1
    lstr = [c for c in string]
    alpb = [chr(c) for c in range(97, 123)]
    alpb.extend(list(map(chr, list(range(65, 91)))))
    alpb.extend(list(map(chr, [32, 33, 44, 45, 46, 47, 58, 61, 63, 95])))
    alpb.extend(list(map(chr, list(range(48, 58)))))
    if rot != 0:
        als1 = alpb[-rot:]
        als1.extend(alpb[:len(alpb) - rot])
        alpb = als1
    ansls = []
    for i in range(len(lstr)):
        if i % 7 == 0:
            ind = alpb.index(lstr[i]) - ct0 + ct1 - ct2 + ct3 - ct4 + ct5 - ct6
            if ind < 0:
                ind += len(alpb)
        elif i % 7 == 1:
            ind = alpb.index(lstr[i]) + ct1 - ct2 + ct3 - ct4 + ct5 - ct6 + ct0
            if ind >= len(alpb):
                ind -= len(alpb)
        elif i % 7 == 2:
            ind = alpb.index(lstr[i])
            if ind < 0:
                ind += len(alpb)
        elif i % 7 == 3:
            ind = alpb.index(lstr[i])
            if ind >= len(alpb):
                ind -= len(alpb)
        elif i % 7 == 4:
            ind = alpb.index(lstr[i])
            if ind < 0:
                ind += len(alpb)
        elif i % 7 == 5:
            ind = alpb.index(lstr[i])
            if ind >= len(alpb):
                ind -= len(alpb)
        elif i % 7 == 6:
            ind = alpb.index(lstr[i])
            if ind < 0:
                ind += len(alpb)
        ansls.append(ind)
    ret = []
    # print(ansls)
    for i in range(len(ansls)):
        ret.append(alpb[ansls[i]])
    if key:
        nout = ip
        return(["".join(ret), nout])
    else:
        return(["".join(ret), nout])
def splitn(x, num=1):
    try:
        int(num)
    except:
        return(num)
    else:
        return(list(map(str, [x[i: i+int(num)] for i in range(0, len(x), int(num))])))
import random as rdm
def fixchr(letter, capital=False):
    l = [c for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    if type(letter) != str:
        return(letter)
    else:
        a = l.index(letter) + 26
        if a > 51 and not capital:
            a -= 52
        elif a > 51:
            a -= 26
        elif a > 25 and not capital:
            a -= 26
    return(l[a])
def reverce(txt):
    n = []
    for i in range(len(txt)):
        n.append(txt[-(i + 1)])
    if type(txt) == list:
        return(n)
    else:
        return("".join(n))
    return("".join(n))
def pairbase(dna):
    dnac = ([fixchr(c, True) for c in dna])
    base = {"A": "T", "T": "A", "G": "C", "C": "G"}
    for i in range(len(dnac)):
        if (dnac[i] in base):
            dnac[i] = base[dnac[i]]
        else:
            break
    return("".join(dnac))
def exrnamino(rna, rev=False):
    prot = []
    aminocdn = {
        "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
        "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
        "UAU": "Tyr", "UAC": "Tyr", "UAA": "END", "UAG": "END",
        "UGU": "Cys", "UGC": "Cys", "UGA": "END", "UGG": "Trp",
        "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
        "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
        "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
        "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
        "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
        "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
        "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
        "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
        "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
        "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
        "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
        "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
    }
    if not rev:
        # 開始コドン探す
        rna = ''.join([fixchr(c, True) for c in rna])
        b1 = False
        for i in range(len(rna) - 2):
            if rna[i:i+3] == "AUG":
                transl = splitn(rna[i:], 3)
                b1 = True
                break
        if not b1:
            transl = splitn(rna[0:], 3)
        for i in transl:
            prot.append(aminocdn[i])
            if aminocdn[i] == "END":
                break
        return(prot)
    elif rev:
        for i in rna:
            n = [k for k, v in aminocdn.items() if v == i]
            if len(n) > 1:
                prot.append(n[rdm.randrange(0, len(n), 1)])
            else:
                prot.append(n[0])
        return(''.join(prot))

def shortamino(aminos, rev=False):
    alamin = {
        'Ala': 'A', 'Cys': 'C', 'Asp': 'D', 'Glu': 'E',
        'Phe': 'F', 'Gly': 'G', 'His': 'H', 'Ile': 'I',
        'Lys': 'K', 'Leu': 'L', 'Met': 'M', 'Asn': 'N',
        'Pro': 'P', 'Gln': 'Q', 'Arg': 'R', 'Ser': 'S',
        'Thr': 'T', 'Val': 'V', 'Trp': 'W', 'Tyr': 'Y',
        "END": ""
    }
    l = []
    if not rev:
        for i in aminos:
            l.append(alamin[i])
        return(''.join(l))
    elif rev:
        aminos = ''.join([fixchr(c, True) for c in aminos])
        aminos = [c for c in aminos]
        for i in aminos:
            l.append([k for k, v in alamin.items() if v == i][0])
        return(l)
    return(prot)
def dnatorna(dna):
    dna = [c for c in dna]
    for i in range(len(dna)):
        if dna[i] == "T":
            dna[i] = "U"
    return("".join(dna))
def repl(string, bf=None, af=None):
    string = [c for c in str(string)]
    if bf == None or (type(bf) != str and type(bf) != tuple):
        bf = string[0]
    if af == None or (type(af) != str and type(bf) != tuple):
        af = bf
    for i in range(len(string)):
        if string[i] in bf:
            string[i] = af[bf.index(string[i])]
    return(''.join(string))
def join_s(l):
    return(''.join(l))
def mkmrna(string):
    return('AUG' + exrnamino(shortamino(repl(string, ('o', 'u', 'b'), ('q', 'v', 'l')), True), True) + 'UGA')
def trlrna(string):
    return(repl(join_s([fixchr(c) for c in (shortamino(exrnamino(string)))]), ('q', 'v', 'l'), ('o', 'u', 'b')))
def alpbnum(string, rev=False):
    al = [c for c in "abcdefghijklmnopqrstuvwxyz"]
    if not rev:
        s = [c for c in [fixchr(d) for d in string]]
        a = []
        for i in s:
            a.append(str(al.index(i) + 1).zfill(2))
        return("0a" + "".join(a))
    else:
        s = splitn(string, 2)[1:]
        n = []
        for i in s:
            n.append(al[int(i) - 1])
        return("".join(n))
