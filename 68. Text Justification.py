class Solution:
    def fullJustify(self, words, maxWidth):
        temp = []
        tempSentence = ""
        prev = ""
        result = []

        for word in words:
            tempSentence = "{} %s".format(tempSentence) % word
            if len(tempSentence) > maxWidth:
                tempSentence = ""
                size = maxWidth - len(prev)
                tempRes = ""
                step = len(temp)
                for i in temp:
                    tempRes = "{}%s".format(tempRes) % i
                    if len(temp) == 1:
                        for j in range(size):
                            tempRes = "{}%s".format(tempRes) % ' '
                    else:
                        if step-1 == 0:
                            break
                        if size % (step-1) != 0:
                            nk = round(size // (step-1))
                            for j in range(nk):
                                tempRes = "{}%s".format(tempRes) % ' '
                            size -= nk
                            step -= 1
                        else:
                            nk = size // (step-1)
                            for j in range(nk):
                                tempRes = "{}%s".format(tempRes) % ' '
                            size -= nk
                            step -= 1

                result.append(tempRes)
                temp.clear()
                tempSentence = "{}%s".format(tempSentence) % word
                prev = word
                temp.append(word)
            else:
                temp.append(word)
                prev = tempSentence

        print(temp, prev, tempRes)
        if temp:
            size = maxWidth - len(prev)
            tempRes = ""
            step = len(temp)
            for i in temp:
                tempRes = "{}%s ".format(tempRes) % i
                size -= 1

            for i in range(size):
                tempRes = "{}%s".format(tempRes) % ' '
            result.append(tempRes)

        return result

sol = Solution()
print(sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
