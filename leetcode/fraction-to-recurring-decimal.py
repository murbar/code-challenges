# https://leetcode.com/problems/fraction-to-recurring-decimal/


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        num, den = numerator, denominator
        if not den:  # denominator is 0
            return
        if not num:  # numerator is 0
            return "0"

        res = []
        if (num < 0) ^ (den < 0):
            res.append("-")  # add the sign
        num, den = abs(num), abs(den)
        res.append(str(num//den))
        rmd = num % den
        if not rmd:
            return "".join(res)  # only has integral part
        res.append(".")  # has frational part
        dic = {}
        while rmd:
            if rmd in dic:   # the remainder recurs
                res.insert(dic[rmd], "(")
                res.append(")")
                break
            dic[rmd] = len(res)
            div, rmd = divmod(rmd*10, den)
            res.append(str(div))
        return "".join(res)

    def fractionToDecimal2(self, numerator, denominator):
        sign = '-' if numerator * denominator < 0 else ''
        head, remainder = divmod(abs(numerator), abs(denominator))
        tail, seen = '', {}
        while remainder != 0:
            if remainder in seen:
                tail = tail[: seen[remainder]] + \
                    '(' + tail[seen[remainder]:] + ')'
                break
            seen[remainder] = len(tail)
            digit, remainder = divmod(remainder*10, abs(denominator))
            tail += str(digit)
        return sign + str(head) + (tail and '.' + tail)
