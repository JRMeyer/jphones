#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

# original code from https://github.com/Greatdane/Convert-Numbers-to-Japanese

# Japanese Number Converter
# Works only up to sen man for now.




class Converter:
    def __init__(self):
        self.kanaDict = {'0': u'ゼロ',
                         '1': u'いち',
                         '2': u'に',
                         '3': u'さん',
                         '4': u'よん',
                         '5': u'ご',
                         '6': u'ろく',
                         '7': u'なな',
                         '8': u'はち',
                         '9': u'きゅう',
                         '10': u'じゅう',
                         '100': u'ひゃく',
                         '1000': u'せん',
                         '10000': u'まん',
                         '100000000': u'おく',
                         '300': u'さんびゃく',
                         '600': u'ろっぴゃく',
                         '800': u'はっぴゃく',
                         '3000': u'さんぜん',
                         '8000': u'はっせん' }
        self.num=''

        
    def len_one(self, num=None):
        # Returns single digit conversion, 0-9
        if num == None:
            result = self.kanaDict[self.num]
        else:
            result = self.kanaDict[num]
            
        return result

    
    def len_two(self, num=None):
        # Returns the conversion, when number is of length two (10-99)

        if num == None:
            num = self.num
        else:
            pass
        
        if num == "10":
            # Exception, if number is 10, simple return 10
            result = self.kanaDict["10"]
            
        # When first number is 1, use ten plus second number
        elif num[0] == "1":

            result = self.kanaDict["10"] + " " + self.len_one(num[1])

        # If ending number is zero, give first number plus 10
        elif num[1] == "0": 
            result = self.len_one(num[0]) + " " + self.kanaDict["10"]
            
        else:
            num_list = []
            for i in num:
                num_list.append(self.kanaDict[i])
                
            num_list.insert(1, self.kanaDict["10"])

            result = ''.join(num_list)

        return result
    

    def len_three(self, num=None):
        # Returns the conversion, when number is of length three (101-999)

        if num == None:
            num = self.num
        else:
            pass
        
        num_list = []
        if num[0] == "1":
            num_list.append(self.kanaDict["100"])
        elif num[0] == "3":
            num_list.append(self.kanaDict["300"])
        elif num[0] == "6":
            num_list.append(self.kanaDict["600"])
        elif num[0] == "8":
            num_list.append(self.kanaDict["800"])
        else:
            num_list.append(self.kanaDict[num[0]])
            num_list.append(self.kanaDict["100"])
            
        if num[1:] == "00" and len(num) == 3:
            pass
        else:
            if num[1] == "0":
                num_list.append(self.kanaDict[num[2]])
            else:
                num_list.append(self.len_two(num[1:]))


        result = ''.join(num_list)
        
        return result
            

    def len_four(self, num=None):
        # Returns the conversion, when number is of length four (1001-9999)

        if num == None:
            num=self.num
        else:
            pass
        
        num_list = []

        if num[0] == "1":
            num_list.append(self.kanaDict["1000"])
        elif num[0] == "3":
            num_list.append(self.kanaDict["3000"])
        elif num[0] == "8":
            num_list.append(self.kanaDict["8000"])
        else:
            num_list.append(self.kanaDict[num[0]])
            num_list.append(self.kanaDict["1000"])
        if num[1:] == "000":
            pass
        else:
            if num[1] == "0":
                num_list.append(self.len_two(num[2:]))
            else:
                num_list.append(self.len_three(num[1:]))

        result = "".join(num_list)
        
        return result
        
    
        
    def do(self, num):
        #Check lengths and convert accordingly
        self.num=str(num)
        
        if len(self.num) == 1:
            result = self.len_one()
            
        elif len(self.num) == 2:
            result = self.len_two()
            
        elif len(self.num) == 3:
            result = self.len_three()
            
        elif len(self.num) == 4:
            result = self.len_four()

        else:
            result='NUM-TOO-LARGE'

        return result


    def conv(self,num):
        result = self.do(num)
        return result


def demo():
    n2j=Converter()
    for num in [9134,234,76,0]:
        print( str(num) +' == '+ str(n2j.conv(str(num))))

if __name__ == "__main__":
    demo()
