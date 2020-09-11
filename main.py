import random
import pypinyin
import time
from datas import words, heads, tails

isWord = lambda word: True if word in words else False
randomWord = lambda: list(words.keys())[random.randint(0, len(words))]

# def randomWord():
#     return list(words.keys())[random.randint(0, len(words))]


def getNext(word, israndom=False):
    tail_pinyin = pypinyin.pinyin(word, style=pypinyin.NORMAL)[-1][0]
    try:
        next_words = heads[tail_pinyin]
    except:
        return None
    if israndom:
        next_word = next_words[random.randint(0, len(next_words)-1)]
    else:
        next_word = next_words[0]

    return next_word if next_word else False


def getSolitaire(firstword=None, lastword=None, long=5, trytimes=5000):
    if firstword == None and lastword == None:
        return None
    elif lastword == None:
        solitaire = firstword
        nowword = firstword
        oldwords = []
        if not getNext(nowword, True):
            return None
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
        solitaires = []
        solitaire = firstword
        nowword = firstword
        for WHILE in range(trytimes):
            nowword = firstword
            solitaire = firstword
            for i in range(long - 1):
                nowword = getNext(nowword)
                if nowword != None:
                    solitaire += '→' + nowword
                else:
                    break
            s_words = solitaire.split('→')[1:]
            for word in s_words:
                if pypinyin.pinyin(s_words[-1][0], style=pypinyin.NORMAL)[0][0] == pypinyin.pinyin(lastword[0], style=pypinyin.NORMAL)[0][0]:
                    s_words = s_words[:-1]
                    s_words.append(lastword)
                    right = solitaire.split('→')[0] + '→' + '→'.join(s_words)
                    return right
                    solitaires.append(right)
    return None


def isChinese(str):
    for _char in str:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True


def main():
    print('Input "q" to quit, input "tip" to get next word')
    lastword = randomWord()
    # play solitaire, the first word is random
    while True:
        # time.sleep(0.5)
        lastpinyin = pypinyin.pinyin(lastword, style=pypinyin.NORMAL)[-1][0]

        print('\nNow word: {} ({})'.format(lastword, lastpinyin))
        input_word = input('Input: ')
        if input_word == "":
            break
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
            if getNext(lastword, israndom=True):
                print("Tip: Next word is %s or %s maybe." % (getNext(lastword, israndom=True), getNext(lastword, israndom=True)))
            else:
                print('Game Over.')
                break   

        elif input_word == 'q':
            break

        else:
            if isWord(input_word) == True:
                print('The last pinyin is "%s",but NOT "%s".' % (lastpinyin, input_pinyin))
            elif isChinese(input_word) == False:
                print("Please ALL input CHINESE.")
            else:
                print("Please try again.")

if __name__ == '__main__':
    main()
