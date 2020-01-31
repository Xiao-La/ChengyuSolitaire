from datas import words,heads,tails
import pypinyin
import random
def isWord(word):
    #判断是否是成语
    if word in words:
        return True
    else:
        return False
def randomWord():
    word = list(words.keys())[random.randint(1,8519)]
    return word
def getNext(word,gw=True,error=True):
    #获得下一个成语
    try:
        for _char in word:
            if '\u4e00' <= _char <= '\u9fa5':
                word_tail = pypinyin.pinyin(word[-1],style=pypinyin.NORMAL)[0][0]
            else:
                word_tail = pypinyin.pinyin(word,style=pypinyin.NORMAL)[0][0]
        next_words = heads[word_tail]
        if gw == True:
            next_words_sort = {}#根据词频排序操作
            for next_word in next_words:
                cipin = words[next_word]
                next_words_sort[next_word] = cipin
            next_word = list(next_words_sort.keys())[0]
        elif gw == False:
            next_word = next_words[random.randint(0,len(next_words)-1)]
        return next_word
    except:
        #错误原因判断
        if isWord(word) == False:
            for _char in word:
                if '\u4e00' <= _char <= '\u9fa5':
                    error = '"'+word+'"'+'不是一个成语/没有收录'
                else:
                    error = '"'+word+'"'+'不能继续接了/输入出错'
        elif isWord(word) == True:
            error = '"'+word+'"'+'不能继续接了'
        else:
            error = '原因不明'
        if error == True:
            print('执行出错：'+error)
        return None
def getSolitaire(fristword=None,lastword=None,long=5,trytimes=5000):
    if lastword == None:
        solitaire = fristword#接龙字符串
        nowword = fristword#等待接龙的成语
        oldwords = []#接龙去重
        for i in range(long-1):
            if nowword != getNext(nowword,True) and getNext(nowword) not in oldwords:
                oldwords.append(nowword)
                nowword = getNext(nowword,True)
                solitaire += '→'+nowword
            else:
                oldwords.append(nowword)
                nowword = getNext(nowword,False)
                solitaire += '→'+nowword
        return solitaire
    else:
        solitaires = []#接龙
        solitaire = fristword
        nowword = fristword#等待接龙的成语
        for WHILE in range(trytimes):
            nowword = fristword
            solitaire = fristword
            for i in range(long-1):
                nowword = getNext(nowword,False,False)
                if nowword != None:
                    solitaire += '→'+nowword
                else:
                    break
            #比对查找
            s_words = solitaire.split('→')[1:]
            for word in s_words:
                if pypinyin.pinyin(s_words[-1][0],style=pypinyin.NORMAL)[0][0] == pypinyin.pinyin(lastword[0],style=pypinyin.NORMAL)[0][0]:
                    s_words = s_words[:-1]
                    s_words.append(lastword)
                    right = solitaire.split('→')[0]+'→'+'→'.join(s_words)
                    solitaires.append(right)
        #去重
        ret = []
        for one in solitaires:
            if not one in ret:
                ret.append(one)
        return ret
def main():
    print('输入"q"退出')
    while True:
        input_word = input('输入成语或拼音:')
        if input_word != 'q':
            next = getNext(input_word)
            if next != None:
                print('接龙结果:'+next)
        else:
            break            
#main()
solitaires = getSolitaire(fristword=randomWord(),lastword='一个顶俩',long=4)
for i in solitaires:
    print(i)