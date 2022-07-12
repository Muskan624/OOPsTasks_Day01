import logging
logging.basicConfig(filename="Task1.log",level=logging.INFO,format='%(asctime)s,%(name)s,%(levelname)s,%(message)s')
logging.info("This is my task for basics of string operations")

class String_basic_tasks():

# Extract string based on index

        def index_jump(self,extracted_str):
            logging.info("WE are about to extact string from index 1 to index 30 with a jump of 3")
            self.ext_string = extracted_str
            try:
                indexed_str=extracted_str[1:30:3]
                logging.info("Extracted string is - %s",indexed_str)

            except Exception as e:
                logging.exception(e)

obj_str = String_basic_tasks()
output_str =obj_str.index_jump("this is My First Python programming class and i am learNING python string and its function")
print(output_str)

#Reverse of string

class ReverseString():

     def reverse_string(self,s):
         logging.info("We are reversing a string ")
         self.s=s
         try:
             str=s[::-1]
             logging.info("reversed string is - %s: ",str)
             return str
         except Exception as e:
             logging.exception(e)

obj_rev= ReverseString()
output_rev=obj_rev.reverse_string("This is my first python programm")
print(output_rev)

##Try to split a string after conversion of entire string in uppercase

class Split_str():
    def upperCase(self,s):
        logging.info("We are converting the string in upper case and splitting the string")
        self.s=s
        try:
            s1=s.upper().split(' ')
          ##  str1=s1.split()
            logging.info("splitted string is - %s",s1)
            return s1
        except Exception as e:
            logging.exception(e)
obj_upp=Split_str()
str2=obj_upp.upperCase("Muskan Sinha")
print(str2)

##try to convert the whole string into lower case

class LowerString():
    def str_low(self,s):
        logging.info("We are converting string to lower case")
        self.s=s
        try:
            s2=s.lower()
            logging.info("Lower case string is - %s",s2)
            return s2
        except Exception as e:
            logging.exception(e)
obj3=LowerString()
print(obj3.str_low("MUSKAN"))

##Try to capitalize the whole string

class Capitalze():
    def Captilize(self,s):
        logging.info("WE are capitalizing a string")
        self.s=s
        try:
            s1=s.capitalize()
            logging.info("Capitalized string is - %s",s1)
            return s1
        except Exception as e:
            logging.exception(e)

obj=Capitalze()
print(obj.Captilize("this is my first string python programm"))

##Try to give an example of expand tab

class Expand():
    def expand_tab(self,s):
        logging.info("We are giving an example of expand tab")
        self.s=s
        try:
            s1=s.expandtabs()
            logging.info("expandstab string is - %s",s1)
            return s1
        except Exception as e:
            logging.exception(e)

obj_expand=Expand()
print(obj_expand.expand_tab("xyzyu\t12345\tabc"))

##Give an example of strip , lstrip and rstrip
class Strip():
    def strip(self,s):
        logging.info("We are doing strip operation for string")
        self.s=s
        try:
            s1=s.strip()
            logging.info("strip string is - %s",s1)
            return s1
        except Exception as e:
            logging.exception(e)

    def lstrip(self,s):
        logging.info("We are doing  left strip operation for string")
        self.s=s
        try:
            lstrip=s.strip()
            logging.info("left strip string is - %s",lstrip)
            return lstrip
        except Exception as e:
            logging.exception(e)

    def rstrip(self,s):
        logging.info("We are doing  right strip operation for string")
        self.s=s
        try:
            rstrip=s.strip()
            logging.info(" right strip string is - %s",rstrip)
            return rstrip
        except Exception as e:
            logging.exception(e)

obj_strip=Strip()
print(obj_strip.strip("     Muskan       "))
print(obj_strip.lstrip("        Muskan       "))
print(obj_strip.rstrip("     Muskan       "))

##Replace a string charecter by another charector by taking your own example "sudhanshu"

class Replace():
    def replaceee(self,s):
        logging.info("We are replacing a string")
        self.s=s
        try:
            s1=s.replace("sudhanshu","Muskan")
            logging.info("Replaced string is - %s",s1)
            return s1
        except Exception as e:
            logging.exception(e)

obj_rep=Replace()
print(obj_rep.replaceee("sudhanshu Sinha"))

##Try  to give a defination of string center function with and exmple

class Center():
    def cen(self,s):
        logging.info("We are trying to user center operation on string")
        self.s=s
        try:
            s1=s.center(20,"&")
            logging.info("String is - %s",s1)
            return s1
        except Exception as e:
            logging.exception(e)
obj_cen=Center()
print(obj_cen.cen("Muskan"))















