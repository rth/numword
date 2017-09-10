# coding: utf-8
"""This script is for testing numword. Please provide 2-letter language code"""
__author__ = 'soshial'
import unittest

class NumwordTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_cardinal(self):
        cardinals = {
            'de':[
                [-1.0000100, "minus eins Komma null"],
                [1.11, "eins Komma eins eins"],
                [1, "eins"],
                [11, "elf"],
                [12, "zwölf"],
                [21, "einundzwanzig"],
                [29, "neunundzwanzig"],
                [30, "dreißig"],
                [31, "einunddreißig"],
                [33, "dreiunddreißig"],
                [71, "einundsiebzig"],
                [80, "achtzig"],
                [81, "einundachtzig"],
                [91, "einundneunzig"],
                [99, "neunundneunzig"],
                [100, "einhundert"],
                [101, "einhunderteins"],
                [102, "einhundertzwei"],
                [151, "einhunderteinundfünfzig"],
                [155, "einhundertfünfundfünfzig"],
                [161, "einhunderteinundsechzig"],
                [180, "einhundertachtzig"],
                [300, "dreihundert"],
                [301, "dreihunderteins"],
                [308, "dreihundertacht"],
                [832, "achthundertzweiunddreißig"],
                [1000, "eintausend"],
                [1001, "eintausendeins"],
                [1061, "eintausendeinundsechzig"],
                [1100, "eintausendeinhundert"],
                [1111, "eintausendeinhundertelf"],
                [1500, "eintausendfünfhundert"],
                [1701, "eintausendsiebenhunderteins"],
                [3000, "dreitausend"],
                [8280, "achttausendzweihundertachtzig"],
                [8291, "achttausendzweihunderteinundneunzig"],
                [10100, "zehntausendeinhundert"],
                [10101, "zehntausendeinhunderteins"],
                [10099, "zehntausendneunundneunzig"],
                [12000, "zwölftausend"],
                [150000, "einhundertfünfzigtausend"],
                [500000, "fünfhunderttausend"],
                [1000000, "eine Million"],
                [1000100, "eine Million einhundert"],
                [1000199, "eine Million einhundertneunundneunzig"],
                [2000000, "zwei Millionen"],
                [2000001, "zwei Millionen eins"],
                [1000000000, "eine Milliarde"],
                [2147483647, "zwei Milliarden einhundertsiebenundvierzig"
                 " Millionen vierhundertdreiundachtzigtausend"
                 "sechshundertsiebenundvierzig"],
                [23000000000, "dreiundzwanzig Milliarden"],
                [126000000000001, "einhundertsechsundzwanzig Billionen eins"],
                [-121211221211111 , "minus einhunderteinundzwanzig Billionen "
                "zweihundertelf Milliarden zweihunderteinundzwanzig Millionen "
                "zweihundertelftausendeinhundertelf"],
                [1000000000000000, "eine Billiarde"],
                [256000000000000000, "zweihundertsechsundfünfzig Billiarden"],
                # I know the next is wrong! but what to do?
                [-2.12, "minus zwei Komma eins zwei"],
                [7401196841564901869874093974498574336000000000, "sieben Septil"
                 "liarden vierhunderteins Septillionen einhundertsechsundneunzig S"
                 "extilliarden achthunderteinundvierzig Sextillionen fünfhundertvi"
                 "erundsechzig Quintilliarden neunhunderteins Quintillionen achthu"
                 "ndertneunundsechzig Quadrilliarden achthundertvierundsiebzig Qua"
                 "drillionen dreiundneunzig Trilliarden neunhundertvierundsiebzig "
                 "Trillionen vierhundertachtundneunzig Billiarden fünfhundertvieru"
                 "ndsiebzig Billionen dreihundertsechsunddreißig Milliarden"],
                ],
            'en':[
                [0,'zero'],
                [4,'four'],
                [12,'twelve'],
                [-45,'minus forty-five'],
                [-2.12,'minus two point twelve'],
                [-19.98,'minus nineteen point ninety-eight'],
                [5.980,'five point ninety-eight'],
                [22000001,'twenty-two million and one'],
                [399670900,'three hundred and ninety-nine million, six hundred and seventy thousand, nine hundred'],
                [90311671002,'ninety billion, three hundred and eleven million, six hundred and seventy-one thousand and two'],
            ],
            'es':[],
            'fr':[],
            'pl':[],
            'ru':[
                [0,'ноль'],
                [4,'четыре'],
                [12,'двенадцать'],
                [21,'двадцать один'],
                [33,'тридцать три'],
                [71,'семьдесят один'],
                [-80,'минус восемьдесят'],
                [81,'восемьдесят один'],
                [91,'девяносто один'],
                [99,'девяносто девять'],
                [100,'сто'],
                [101,'сто один'],
                [102,'сто два'],
                [113,'сто тринадцать'],
                [120,'сто двадцать'],
                [155,'сто пятьдесят пять'],
                [280,'двести восемьдесят'],
                [300,'триста'],
                [308,'триста восемь'],
                [832,'восемьсот тридцать два'],
                [1000,'тысяча'],
                [1001,'тысяча один'],
                [1065,'тысяча шестьдесят пять'],
                [1100,'тысяча сто'],
                [1120,'тысяча сто двадцать'],
                [1500,'тысяча пятьсот'],
                [1701,'тысяча семьсот один'],
                [1800,'тысяча восемьсот'],
                [2000,'две тысячи'],
                [2010,'две тысячи десять'],
                [2099,'две тысячи девяносто девять'],
                [2171,'две тысячи сто семьдесят один'],
                [3000,'три тысячи'],
                [8280,'восемь тысяч двести восемьдесят'],
                [8291,'восемь тысяч двести девяносто один'],
                [150000,'сто пятьдесят тысяч'],
                [220144,'двести двадцать тысяч сто сорок четыре'],
                [420650,'четыреста двадцать тысяч шестьсот пятьдесят'],
                [500000,'пятьсот тысяч'],
                [1000000,'миллион'],
                [2000000,'два миллиона'],
                [20000001,'двадцать миллионов один'],
                [255421650,'двести пятьдесят пять миллионов четыреста двадцать одна тысяча шестьсот пятьдесят'],
                [399670900,'триста девяносто девять миллионов шестьсот семьдесят тысяч девятьсот'],
                [90311671002,'девяносто миллиардов триста одиннадцать миллионов шестьсот семьдесят одна тысяча два'],
#                [10**63,u'вигинтиллион'],
#                [10**81,u'сексвигинтиллион'],
#                [10**99,u'дуотригинтиллион'],
#                [10**108,u'октодециллиард'],
#                [10**144,u'кватторвигинтиллиард'],
#                [10**336,u'ундецицентиллион'],
#                [10**402,u'третригинтацентиллион'],
#                [-21212121211221211111,u'минус двадцать один квинтиллион двести двенадцать квадриллионов сто двадцать один триллион двести одиннадцать миллиардиллионов двести двадцать один миллион двести одиннадцать тысяч сто одиннадцать'],
                [-2.121212,'минус два целых и двенадцать'],
                [-1.00001,'минус один целых и ноль'],
            ]
        }
        for number, word in cardinals[language]:
            self.assertEqual(word,numword.cardinal(number))

    def test_ordinal(self):
        ordinals =  {
            'de':[
                [1, "erste"],
                [3, "dritte"],
                [11, "elfte"],
                [12, "zwölfte"],
                [21, "einundzwanzigste"],
                [29, "neunundzwanzigste"],
                [30, "dreißigste"],
                [31, "einunddreißigste"],
                [33, "dreiunddreißigste"],
                [71, "einundsiebzigste"],
                [80, "achtzigste"],
                [81, "einundachtzigste"],
                [91, "einundneunzigste"],
                [99, "neunundneunzigste"],
                [100, "einhundertste"],
                [101, "einhunderterste"],
                [102, "einhundertzweite"],
                [151, "einhunderteinundfünfzigste"],
                [155, "einhundertfünfundfünfzigste"],
                [161, "einhunderteinundsechzigste"],
                [180, "einhundertachtzigste"],
                [300, "dreihundertste"],
                [301, "dreihunderterste"],
                [308, "dreihundertachte"],
                [832, "achthundertzweiunddreißigste"],
                [1000, "eintausendste"],
                [1001, "eintausenderste"],
                [1061, "eintausendeinundsechzigste"],
                [2000001, "zwei Millionen erste"],
                # The following is broken
                #[1000000000, "eine Milliardeste"],
                [2147483647, "zwei Milliarden einhundertsiebenundvierzig"
                 " Millionen vierhundertdreiundachtzigtausend"
                 "sechshundertsiebenundvierzigste"],
            ],
            'en':[],
            'es':[],
            'fr':[],
            'pl':[],
            'ru':[ # todo implemet inflection testing
                #[256,u"ДВЕСТИ ПЯТЬДЕСЯТ ШЕСТОЙ".lower()],
                #[900,u"ДЕВЯТИСОТЫЙ".lower()],
                #[3000,u"трёхтысячный"],
                #[150000,u"стапятидесятитысячный"],
                #[5000000,u"пятимиллионный"],
                #[51000000,u"пятидесятиодногомиллионный"], # todo 51000000й - как правильно?
                [0,'нулевого'],
                [1,'первого'],
                [2,'второго'],
                [3,'третьего'],
                [4,'четвёртого'],
                [5,'пятого'],
                [6,'шестого'],
                [7,'седьмого'],
                [8,'восьмого'],
                [9,'девятого'],
                [10,'десятого'],
                [12,'двенадцатого'],
                [20,'двадцатого'],
                [21,'двадцать первого'],
                [30,'тридцатого'],
                [31,'тридцать первого'],
                [33,'тридцать третьего'],
                [40,'сорокового'],
                [50,'пятидесятого'],
                [60,'шестидесятого'],
                [70,'семидесятого'],
                [71,'семьдесят первого'],
                [80,'восьмидесятого'],
                [81,'восемьдесят первого'],
                [90,'девяностого'],
                [91,'девяносто первого'],
                [99,'девяносто девятого'],
                [100,'сотого'],
                [200,'двухсотого'],
                [300,'трёхсотого'],
                [400,'четырёхсотого'],
                [500,'пятисотого'],
                [600,'шестисотого'],
                [700,'семисотого'],
                [800,'восьмисотого'],
                [900,'девятисотого'],
                [78,'семьдесят восьмого'],
                [180,'сто восьмидесятого'],
                [300,'трёхсотого'],
                [308,'триста восьмого'],
                [832,'восемьсот тридцать второго'],
                [1000,'тысячного'],
                [1001,'тысяча первого'],
                [1061,'тысяча шестьдесят первого'],
                [1100,'тысяча сотого'],
                [1120,'тысяча сто двадцатого'],
                [1500,'тысяча пятисотого'],
                [1701,'тысяча семьсот первого'],
                [1800,'тысяча восьмисотого'],
                [1051000000,'миллиард пятидесятиодногомиллионного'],
                [2000,'двухтысячного'],
                [2010,'две тысячи десятого'],
                [2099,'две тысячи девяносто девятого'],
                [2171,'две тысячи сто семьдесят первого'],
                [4000,'четырехтысячного'],
                [8280,'восемь тысяч двести восьмидесятого'],
                [8291,'восемь тысяч двести девяносто первого'],
                [150000,'стапятидесятитысячного'],
                [220144,'двести двадцать тысяч сто сорок четвёртого'],
                [420650,'четыреста двадцать тысяч шестьсот пятидесятого'],
                [500000,'пятисоттысячного'],
                [1000000,'миллионного'],
                [2000000,'двухмиллионного'],
                [20000001,'двадцать миллионов первого'],
                [255421650,'двести пятьдесят пять миллионов четыреста двадцать одна тысяча шестьсот пятидесятого'],
                [399670900,'триста девяносто девять миллионов шестьсот семьдесят тысяч девятисотого'],
                [90311671002,'девяносто миллиардов триста одиннадцать миллионов шестьсот семьдесят одна тысяча второго'],
            ],
        }
        for number, word in ordinals[language]:
            print(word," = ",numword.ordinal(number))
            self.assertEqual(word,numword.ordinal(number))

    def test_year(self):
        years = {
            'de':[
                # Watch out, negative years are broken!
                [0, "null"],
                [33, "dreiunddreißig"],
                [150, "einhundertfünfzig"],
                [160, "einhundertsechzig"],
                [1130, "elfhundertdreißig"],
                [1999, "neunzehnhundertneunundneunzig"],
                [1984, "neunzehnhundertvierundachtzig"],
                [2000, "zweitausend"],
                [2001, "zweitausendeins"],
                [2010, "zweitausendzehn"],
                [2012, "zweitausendzwölf"],
            ],
            'en':[[0,'zero'],[33,'thirty-three']],
            'es':[],
            'fr':[],
            'pl':[],
            'ru':[],
        }
        for number, word in years[language]:
            self.assertEqual(word,numword.year(number))

    def test_currency(self):
        currencies =  {
            'de':[
                [12222, "einhundertzweiundzwanzig Euro und zweiundzwanzig Cent"],
                [123322, "eintausendzweihundertdreiunddreißig Euro und zweiundzwanzig Cent"],
                [686412, "sechstausendachthundertvierundsechzig Euro und zwölf Cent"],
                [84, "vierundachtzig Cent"],
                [1, "ein Cent"],
            ],
            'en':[],
            'es':[],
            'fr':[],
            'pl':[],
            'ru':[],
        }
        for number, word in currencies[language]:
            self.assertEqual(word,numword.currency(number))

if __name__ == '__main__':
    # todo make possible to give the script parameters 'en','de','ru'...
    '''import sys
    arguments = sys.argv
    if len(arguments) < 2: quit("Please specify the language as a parameter!")
    language = arguments[1]'''
    language = 'en'
    if language == 'de': from . import numword_de as numword
    elif language == 'en': from . import numword_en as numword
    elif language == 'es': from . import numword_es as numword
    elif language == 'fr': from . import numword_fr as numword
    elif language == 'ru': from . import numword_ru as numword
    elif language == 'pl': import numword_pl as numword
    else: quit("Please specify the language as a parameter!")
    unittest.main()

def simple_manual_test(self, value):
     """Test function for manual testing in output; very simple"""
     try:
         _card = self.cardinal(value)
     except:
         _card = "invalid"
     try:
         _ord = self.ordinal(value)
     except:
         _ord = "invalid"
     try:
         _ordnum = self.ordinal_number(value)
     except:
         _ordnum = "invalid"
     try:
         _curr = self.currency(value)
     except:
         _curr = "invalid"
     try:
         _year = self.year(value)
     except:
         _year = "invalid"
     print(("For %s, cardinal is %s;\n\tordinal is %s;\n\tordinal number is %s;\n\tcurrency is %s;\n\tyear is %s." %
                 (value, _card, _ord, _ordnum, _curr, _year)))