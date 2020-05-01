import random
import pypinyin
import time
from datas import words, heads, tails


def isWord(word):
    return True if word in words else False


def randomWord():
    return list(words.keys())[random.randint(0, len(words))]


def getNext(word, israndom=False):
    tail_pinyin = pypinyin.pinyin(word, style=pypinyin.NORMAL)[-1][0]
    try:
        next_words = heads[tail_pinyin]
    except:
        return None
    if israndom:
        next_word = next_words[random.randint(0, len(next_words))]
    else:
        next_word = next_words[0]

    return next_word if next_word else False


def getSolitaire(fristword=None, lastword=None, long=5, trytimes=5000):
    if lastword == None:
        solitaire = fristword  # 接龙字符串
        nowword = fristword  # 等待接龙的成语
        oldwords = []  # 接龙去重
        for i in range(long - 1):
            if nowword != getNext(nowword, True) and getNext(nowword) not in oldwords:
                oldwords.append(nowword)
                nowword = getNext(nowword, True)
                solitaire += '→' + nowword
            else:
                oldwords.append(nowword)
                nowword = getNext(nowword, False)
                solitaire += '→' + nowword
        return solitaire
    else:
        solitaires = []  # 接龙
        solitaire = fristword
        nowword = fristword  # 等待接龙的成语
        for WHILE in range(trytimes):
            nowword = fristword
            solitaire = fristword
            for i in range(long - 1):
                nowword = getNext(nowword)
                if nowword != None:
                    solitaire += '→' + nowword
                else:
                    break
            # 比对查找
            s_words = solitaire.split('→')[1:]
            for word in s_words:
                if pypinyin.pinyin(s_words[-1][0], style=pypinyin.NORMAL)[0][0] == pypinyin.pinyin(lastword[0], style=pypinyin.NORMAL)[0][0]:
                    s_words = s_words[:-1]
                    s_words.append(lastword)
                    right = solitaire.split('→')[0] + '→' + '→'.join(s_words)
                    solitaires.append(right)
        # 去重
        ret = []
        ret = list(set(solitaires))
        return ret
    return None


def isChinese(str):
    for _char in str:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True


def main():
    print('Input "q" to quit, input "tip" to get next word')
    lastword = randomWord()
    # play solitaire, the frist word is random
    while True:
        # time.sleep(0.5)
        lastpinyin = pypinyin.pinyin(lastword, style=pypinyin.NORMAL)[-1][0]

        print('\nNow word: {} ({})'.format(lastword, lastpinyin))
        input_word = input('Input: ')
        input_pinyin = pypinyin.pinyin(
            input_word, style=pypinyin.NORMAL)[0][0]

        if input_pinyin == lastpinyin and isWord(input_word) == True:
            next = getNext(input_word)
            if getNext(next) == None:
                next = getNext(input_word)
            elif next != None:
                lastword = next
            else:
                print('Game Over.')
                break

        elif input_word == 'tip':
            print("Tip: Next word is %s or %s maybe." % (getNext(lastword, israndom=True), getNext(lastword, israndom=True)))

        elif input_word == 'q':
            break

        elif input_word == 'h2w':
            print("You can try to input %s" % getSolitaire(fristword=lastword, lastword="一个顶俩"))

        else:
            if isWord(input_word) == True:
                print('The last pinyin is "%s",but NOT "%s".' % (lastpinyin, input_pinyin))
            elif isChinese(input_word) == False:
                print("Please ALL input CHINESE.")
            else:
                print("Please try again.")

if __name__ == '__main__':
    main()
