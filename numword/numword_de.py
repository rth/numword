# coding: utf-8
#This file is part of numword.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

"""numword for German language"""

from .numword_eu import NumWordEU

#//TODO: Use German error messages
class NumWordDE(NumWordEU):
    """
    NumWord DE
    """
    def _set_high_numwords(self, high):
        """
        Set high num words
        """
        max = 3 + 6*len(high)

        for word, n in zip(high, list(range(max, 3, -6))):
            self.cards[10**n] = word + "illiarde"
            self.cards[10**(n-3)] = word + "illion"

    def _setup(self):
        """
        Setup
        """
        self.negword = "minus "
        self.pointword = "Komma"
        self.errmsg_nonnum = "Nur Zahlen koennen in Worte konvertiert werden."
        self.errmsg_toobig = "Zahl ist zu gross um in Worte konvertiert zu werden."
        self.exclude_title = []
        lows = ["Non", "Okt", "Sept", "Sext", "Quint", "Quadr", "Tr",
                "B", "M"]
        units = ["", "Un", "Do", "Tre", "Quattuor", "Quin", "Sex",
                "Septem", "Okto", "Novem"]
        tens = ["Dezi", "Vigint", "Trigint", "Quadragint", "Quinquagint",
                "Sexagint", "Septuagint", "Oktogint", "Nonagint"]
        self.high_numwords = ["zent"] + self._gen_high_numwords(units, tens, lows)
        self.mid_numwords = [(1000, "tausend"), (100, "hundert"),
                (90, "neunzig"), (80, "achtzig"), (70, "siebzig"),
                (60, "sechzig"), (50, "fünfzig"), (40, "vierzig"),
                (30, "dreißig"), (20, "zwanzig"), (19, "neunzehn"),
                (18, "achtzehn"), (17, "siebzehn"), (16, "sechzehn"),
                (15, "fünfzehn"), (14, "vierzehn"), (13, "dreizehn"),
                (12, "zwölf"), (11, "elf"), (10, "zehn")]
        self.low_numwords = ["neun", "acht", "sieben", "sechs", "fünf",
                "vier", "drei", "zwei", "eins", "null"]
        self.ords = {
                "eins": "ers",
                "drei": "drit",
                "acht": "ach",
                "sieben": "sieb",
                "hundert": "hunderts",
                "tausend": "tausends",
                "million": "millionens",
                "ig": "igs",
                }
        self.ordflag = False

    def _cardinal_float(self, value):
        """
        Convert float to cardinal
        """
        try:
            assert float(value) == value
        except (ValueError, TypeError, AssertionError):
            raise TypeError(self.errmsg_nonnum % value)
        pre = int(round(value))
        post = abs(value - pre)
        out = [self.cardinal(pre)]
        if self.precision:
            out.append(self._title(self.pointword))

            decimal = int(round(post * (10**self.precision)))
            for digit in tuple([x for x in str(decimal)]):
                out.append(str(self.cardinal(int(digit))))
                number = " ".join(out)
        return number

    def _merge(self, curr, next):
        """
        Merge
        """
        ctext, cnum, ntext, nnum = curr + next
        if cnum == 1:
            if nnum == 100 or nnum == 10**3 :
                return "ein" + ntext, nnum
            if nnum >= 10**6 and not (nnum % 10**3):
                return "eine " + ntext.capitalize(), nnum
            return next
        if nnum > cnum:
            if nnum >= 10**6:
                if ntext[-1] == "e":
                    ntext = ntext[:-1]
                if cnum > 1:
                    ntext += "en"
                ctext += " "
            val = cnum * nnum
        else:
            if nnum < 10 < cnum < 100:
                if nnum == 1:
                    ntext = "ein"
                ntext, ctext =  ctext, ntext + "und"
            elif nnum < 10 < cnum < 1000:
                if nnum == 1:
                    ntext = "eins"
                ntext, ctext =  ntext, ctext
            if cnum >= 10**6 and nnum != 0:
                ctext += " "
            val = cnum + nnum

        word = ctext + ntext
        return (word.strip(), val)

    def ordinal(self, value):
        """
        Convert to ordinal
        """
        self._verify_ordinal(value)
        self.ordflag = True
        outword = self.cardinal(value)
        self.ordflag = False
        for key in self.ords:
            if outword.endswith(key):
                outword = outword[:len(outword) - len(key)] + self.ords[key]
                break
        return outword + "te"

    def ordinal_number(self, value):
        """
        Convert to ordinal number
        """
        self._verify_ordinal(value)
        return str(value) + "te"

    def currency(self, val, longval=True, old=False, hightxt=False, lowtxt=False, space=True):
        """
        Convert to currency
        """
        self.precision = 2
        if old:
            return self._split(val, hightxt="Mark", lowtxt="Pfennig(e)",
                                split_precision=0,jointxt="und",longval=longval)
        curr = super(NumWordDE, self).currency(val, jointxt="und", hightxt="Euro",
                        lowtxt="Cent", longval=longval, space=space)
        return curr.replace("eins", "ein")

    def cardinal(self, value):
        # catch floats and parse decimalplaces
        if isinstance(value, float):
            prefix, suffix = str(value).split(".")
            pre_card = super(NumWordDE, self).cardinal(int(prefix))
            suf_card = self._cardinal_float(float("." + suffix))
            suf_card = suf_card.replace("null %s" % _NW.pointword,_NW.pointword)
            cardinal = pre_card + " " + suf_card
            return cardinal
        else:
            return super(NumWordDE, self).cardinal(value)

    def year(self, value, longval=True):
        self._verify_ordinal(value)
        if not (value//100)%10:
            return self.cardinal(value)
        year = self._split(value, hightxt="hundert", longval=longval, space=False)
        if not year.count(self.negword) == 0:
            year = year.replace(self.negword, "").strip()
            year = year + " v. Chr."
        return year.replace("eins", "ein")

_NW = NumWordDE()

def cardinal(value):
    """
    Convert to cardinal
    """
    return _NW.cardinal(value)

def ordinal(value):
    """
    Convert to ordinal
    """
    return _NW.ordinal(value)

def ordinal_number(value):
    """
    Convert to ordinal number
    """
    return _NW.ordinal_number(value)

def currency(value, longval=True, old=False):
    """
    Convert to currency
    """
    return _NW.currency(value, longval=longval, old=old)

def year(value):
    """
    Convert to year
    """
    return _NW.year(value)

def main():
    pass

if __name__ == "__main__":
    main()

