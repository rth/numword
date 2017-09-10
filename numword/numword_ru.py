# coding: utf-8
#This file is part of numword.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

"""numword for Russian language"""

# materials used:
# * http://www.gramota.ru/class/coach/tbgramota/45_110
# * http://www.gramota.ru/spravka/letters/?rub=rubric_92

from .numword_base import NumWordBase
import os, pkg_resources
import pymorphy


_morphs = {}

def get_morph(path, backend='cdb'):
    if not path in _morphs:
        _morphs[path] = pymorphy.get_morph(path, backend)
    return _morphs[path]


class NumWordRU(NumWordBase):
    """NumWord RU"""

    def __init__(self, dictionary=None):
        super(NumWordRU, self).__init__()
        # initializing morphology module for inflecting

        dictionary = dictionary or pkg_resources.resource_filename('numword', 'ru.cdb')

        if not os.path.exists(dictionary):
            raise EnvironmentError(
                'Please put existing dictionaries into "{}" folder or specify your own'.format(dictionary))
        self.morph = get_morph(dictionary)
        self.inflection_case = "им" # todo add gender for the ending of numeral ('жр')

    def _set_high_numwords(self, high):
        """Sets high num words"""
        max_val = 3 + 3 * len(high)
        for word, i in zip(high, list(range(max_val, 3, -3))):
            if 10**i == 1000000000: self.cards[1000000000] = "миллиард"; continue
            self.cards[10**i] = word + "иллион" # Only the short scale of naming numbers is used In Russia


    def _base_setup(self):
        """Base setup"""
        # 10**33..10**6
        lows = ["нон", "окт", "септ", "секст", "квинт", "квадр", "тр",
                "б", "м"] # todo fix ultra-high numwords
        units = ["", "ун", "дуо", "тре", "кваттуор", "квин", "секс",
                "септ", "окто", "новем"]
        tens = ["дец", "вигинт", "тригинт", "квагинт", "квинквагинт",
                "сексагинт", "септагинт", "октогинт", "нонагинт"]
        self.high_numwords = ["cent"] + self._gen_high_numwords(units, tens, lows)


    def _setup(self):
        """
        Setup
        """
        self.negword = "минус "
        self.pointword = ["целая", "десятая", "сотая", "тысячная"]
        self.errmsg_nonnum = "Only numbers may be converted to words."
        self.exclude_title = ["and", "point", "minus"]

        self.mid_numwords = [(1000, "тысяча"), (900, "девятьсот"), (800, "восемьсот"), (700, "семьсот"),
                (600, "шестьсот"), (500, "пятьсот"), (400, "четыреста"),(300, "триста"),(200, "двести"), (100, "сто"),
                (90, "девяносто"), (80, "восемьдесят"), (70, "семьдесят"),
                (60, "шестьдесят"), (50, "пятьдесят"), (40, "сорок"), (30, "тридцать")]
        self.low_numwords = ["двадцать", "девятнадцать", "восемнадцать", "семнадцать",
                "шестнадцать", "пятнадцать", "четырнадцать", "тринадцать", "двенадцать",
                "одиннадцать", "десять", "девять", "восемь", "семь", "шесть", "пять",
                "четыре", "три", "два", "один", "ноль"]
        self.ords = {
                "ноль": "нулевой",
                "один": "первый",
                "два": "второй",
                "три": "третий",
                "четыре": "четвёртый",
                "шесть": "шестой",
                "семь": "седьмой",
                "восемь": "восьмой",
                "восемьдесят": "восьмидесятый",
                "сорок": "сороковой",
                "девяносто": "девяностый",
                "сто": "сотый",
                "двести": "двухсотый",
                "триста": "трёхсотый",
                "четыреста": "четырёхсотый",
                "восемьсот": "восьмисотый",
                "тысяча": "тысячный",
                }


    def _merge(self, curr, next):
        """
        Merge
        """
        curr_text, curr_numb, next_text, next_numb = curr + next
        if curr_numb == 1 and next_numb < 1000:
            #print "merge 1 _ ne", next
            return self._inflect(next_numb,next_text,0),next_numb # all separate numbers should be inflected from the start, that is all mid and low numwords (such as 7, 10, 300)
        elif 1000 > curr_numb > next_numb:
            #print "merge ne _ cu", next_numb, curr_numb # all merging in within 1000 don't change any grammar propeties of the adjacent words
            #return u"%s %s" % (self._inflect(curr_numb,curr_text,next), next_text), curr_numb + next_numb
            return "%s %s" % (curr_text, next_text), curr_numb + next_numb
        elif next_numb > curr_numb:
            # case for number '671000': '1000' > '671'
            # todo make without tam-tams
            if len(curr_text.split(' ')) < 2: whitespace = ''
            else: whitespace = ' '

            if curr_numb == 1: # in Russian if it is only a power of 1000, then we don't need to use 'один' here
                return self._inflect(next_numb,next_text,curr), next_numb
            else:
                return "%s %s" % (' '.join(curr_text.split(' ')[:-1]) + whitespace + self._inflect(curr_numb % 10, curr_text.split(' ')[-1],next), # in Russian only the last digit depends on high numwords
                               self._inflect(next_numb,next_text,curr)), curr_numb * next_numb # we don't need to inflect current because it was or would be already inflected
        else:
            #print "merge_other: ", next_numb, curr_numb
            return "%s %s" % (curr_text, next_text), curr_numb + next_numb

    def _cardinal_float(self, value):
        # todo сделать так, чтобы сами числительные по родам согласовывались: "две сотых, одна целая"
        try:
            assert float(value) == value
        except (ValueError, TypeError, AssertionError):
            raise TypeError(self.errmsg_nonnum % value)
        import math
        if self.precision == -1:
            integer, decimal = str(value).split(".") # -19.98 -> -19
            integer, decimal = int(integer), int(decimal)
        else:
            integer = int(value) # -19.98 -> -19
            decimal = int(round(abs(abs(value) - abs(integer)) * (10**self.precision)))
        out = [self.cardinal(integer)]
        if not self.precision == 0:
            if 11 <= integer % 100 <= 19 or 5 <= integer % 10 or integer % 10 == 0: out.append(self.morph.inflect_ru(self.pointword[0].upper(),"мн,рд").lower())
            else: out.append(self.morph.inflect_ru(self.pointword[0].upper(),"ед,жр" + self.inflection_case).lower())
            out.append(str(self.cardinal(decimal)))
            ending = math.trunc(math.log(decimal,10))+1 # 925 -> trunc(2.91) + 1 = 3
            if 11 <= decimal % 100 <= 19 or 5 <= decimal % 10 or decimal % 10 == 0: out.append(self.morph.inflect_ru(self.pointword[ending].upper(),"мн,рд").lower())
            else: out.append(self.morph.inflect_ru(self.pointword[ending].upper(),"ед,жр" + self.inflection_case).lower())
        return out

    def ordinal(self, value):
        """Convert to ordinal"""
        # first we need the nominativus case
        self._verify_ordinal(value)

        temp_inflection = self.inflection_case
        self.inflection_case = "им"
        outwords = self.cardinal(value).split(" ")
        self.inflection_case = temp_inflection # we put the needed case back
        lastword = outwords[-1].lower()
        try:
            lastword = self.ords[lastword]
        except KeyError:
            import re
            if lastword[-2:] == "ть":
                lastword = lastword[:-2] + "тый"
            elif lastword[-4:] == "ьсот":
                lastword = lastword[:-4] + "исотый"
            elif lastword[-6:] == "ьдесят":
                lastword = lastword[:-6] + "идесятый"
            elif re.search('(иллиона?(ов)?|ллиарда?(ов)?|ысяч(а|и)?)$',lastword):
                wo_zeros = int(re.sub("(000)*$","",str(value))) # 19 250 000 000 -> 19 250
                first = int(wo_zeros / 1000) # 19
                second = wo_zeros % 1000 # 250
                zeroes = int(value / wo_zeros) # 1 000 000
                lastword = re.sub('(иллион|ллиард|ысяч)(ов|а|и)?$','\\1ный',lastword)
                if second != 1:
                    outwords2_str = ""
                    temp_inflection = self.inflection_case
                    self.inflection_case = "им"
                    if first: outwords2_str = self.cardinal(first * zeroes * 1000) + ' '
                    self.inflection_case = temp_inflection # we put the needed case back
                    for sec_part in self.cardinal(second).split(' '):
                        if sec_part.lower() == "один": outwords2_str += "одно"; continue # 51 000 -> пятидесятиоднотысячный
                        outwords2_str += self.morph.inflect_ru(sec_part.upper(),"рд").lower()
                    return outwords2_str + self.morph.inflect_ru(lastword.upper(),self.inflection_case).lower()
        outwords[-1] = self._title(self.morph.inflect_ru(lastword.upper(),self.inflection_case).lower())
        return " ".join(outwords)


    def ordinal_number(self, value):
        """
        Convert to ordinal num
        """
        self._verify_ordinal(value)
        return "%s%s" % (value, self.ordinal(value)[-2:])


    def year(self, value, longval=True):
        """Convert number into year"""
        self._verify_ordinal(value)
        return self.ordinal(value)

    def currency(self, value, longval=True):
        temp_precision, self.precision = self.precision, 2
        return_var = self._split(value, hightxt="доллар", lowtxt="цент",
                                split_precision=0, jointxt="и", longval=longval)
        self.precision = temp_precision
        return return_var

    def _inflect(self, value, text, secondary):
        # @secondary is another tuple(val,text) to have a grammatical agreement with
        if secondary is None:
            return super(NumWordRU,self)._inflect(value, text)
        elif secondary == 0: # initial inflecting of all numbers
            return self.morph.inflect_ru(text.upper(), self.inflection_case).lower()
        sec_text, sec_numb = secondary
        gr_gender = {'мр','жр','ср'}
        gr_number = {'ед','мн'}
        gr_declin = {'им','рд','дт','вн','тв','пр','зв','пр2','рд2'}
        if self.inflection_case == "им" or self.inflection_case == "вн":
            if value < sec_numb:
                # numerals take @gr_gender from thousands, millions etc. (@sec_text)
                intersection = ",".join(list(gr_gender & # here we compute intersection between @gr_gender and set of grammar info of secondary
                                             set(self.morph.get_graminfo(sec_text.upper())[0]['info'].split(',')))) # and return the string again
                if intersection == '':
                    return self.morph.inflect_ru(text.upper(),self.morph.get_graminfo(sec_text.upper())[0]['info']).lower()
                else:
                    return self.morph.inflect_ru(text.upper(), intersection).lower()
            else:
                # thousands, millions etc. take @gr_number from numerals
                if 11<= sec_numb % 100 <= 19 or 5 <= sec_numb % 10 or sec_numb % 10 == 0:
                    return self.morph.inflect_ru(text.upper(), "рд,мн").lower() # [5...9], [11...19], [20,30...] миллион_ов_
                elif sec_numb % 10 == 1:
                    return self.morph.inflect_ru(text.upper(), self.inflection_case + ",ед").lower() # 1 миллион__
                elif 2 <= (sec_numb % 10) <= 4:
                    return self.morph.inflect_ru(text.upper(), "рд,ед").lower() # 3 миллион_а_
                else: quit('DIEEEE!! #1')

        else:
            #print '@ne-imenit@@'
            #print 'value  ', text, value, '\t\t\tsec___', sec_numb
            if False:
                # numerals take @gr_gender from thousands, millions etc. (@sec_text)
                #intersection = ",".join(list(gr_gender & # here we compute intersection between @gr_gender and set of grammar info of secondary
                #                            set(self.morph.get_graminfo(sec_text.upper())[0]['info'].split(',')))) # and return the string again
                #print 'inter',intersection
                #if intersection == '':
                #    print "### intersection void: ",value,sec_text,"___",self.morph.get_graminfo(sec_text.upper())[0]['info'];quit()
                #    return self.morph.inflect_ru(text.upper(),self.inflection_case + self.morph.get_graminfo(sec_text.upper())[0]['info']).lower()

                #else:
                    #print "###res",self.morph.inflect_ru(text.upper(), re.sub(u"(ед)|(мн)","",self.morph.get_graminfo(sec_text.upper())[0]['info'])).lower()
                    #if sec_numb == 1000:
                #print(self.morph.get_graminfo(u'ТРЕМЯ')[0]['info'])
                #quit('!__'+self.morph.inflect_ru(u'ЧЕТЫРЕ', u'пр'))
                return self.morph.inflect_ru(text.upper(), self.inflection_case).lower()# + ',' + intersection).lower()
                #return self.morph.inflect_ru(text.upper(), re.sub(u"(ед)|(мн)","",self.morph.get_graminfo(sec_text.upper())[0]['info'])).lower()
            if value < sec_numb:
                # numerals take @gr_gender from thousands, millions etc. (@sec_text)
                intersection = ",".join(list(gr_gender & # here we compute intersection between @gr_gender and set of grammar info of secondary
                                             set(self.morph.get_graminfo(sec_text.upper())[0]['info'].split(',')))) # and return the string again
                if intersection == '':
                    print("### intersection void: ",value,sec_text,"___",self.morph.get_graminfo(sec_text.upper())[0]['info']);quit()
                    return self.morph.inflect_ru(text.upper(),self.morph.get_graminfo(sec_text.upper())[0]['info']).lower()
                else:
                    return self.morph.inflect_ru(text.upper(), intersection).lower()
                # todo тысяча в творительном падеже склоняется по разному, если существительное и если числительное http://www.gramota.ru/spravka/letters/?rub=rubric_92
                #else: #quit("sec"+str(sec_numb)+self.morph.inflect_ru(text.upper(),self.inflection_case).lower())
                    #quit('DDIEEE!! #2')
                    #return self.morph.inflect_ru(text.upper(),self.inflection_case).lower()
            else: # inflecting high numwords
                if sec_numb % 10 == 1:
                    return self.morph.inflect_ru(text.upper(), self.inflection_case + ",ед").lower()
                else:

                    return self.morph.inflect_ru(text.upper(), self.inflection_case + ",мн").lower()


def cardinal(value):
    """
    Convert to cardinal
    """
    return NumWordRU().cardinal(value)

def ordinal(value):
    """
    Convert to ordinal
    """
    return NumWordRU().ordinal(value)

def ordinal_number(value):
    """
    Convert to ordinal num
    """
    return NumWordRU().ordinal_number(value)

def currency(value, longval=True):
    """
    Convert to currency
    """
    return NumWordRU().currency(value, longval=longval)

def year(value, longval=True):
    """
    Convert to year
    """
    return NumWordRU().year(value, longval=longval)

def main():
    """Main program"""
    _NW = NumWordRU()
    _NW.test_array()
    quit()
    for val in [
             0,''' 4, 12, 21, 31, 33, 71, 80, 81, 91, 99, 100, 101, 102, 120, 155,
             180, 300, 308, 832, 1000, 1001, 1061, 1100, 1120, 1500, 1701, 1800,
             255421650, 420650, 220144, 311671000,2000, 2010, 2099, 2171, 3000, 8280, 8291, 150000, 500000, 1000000,
             2000000, 2000001, -21212121211221211111, -2.121212, -1.0000100,
             1325325436067876801768700107601001012212132143210473207540327057320957032975032975093275093275093270957329057320975093272950730''']:
        _NW.test(val,True)
        #quit()

if __name__ == "__main__":
    main()
