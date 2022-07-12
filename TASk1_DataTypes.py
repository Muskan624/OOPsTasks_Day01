import logging
logging.basicConfig(filename="Task1DataTypes.log",level=logging.INFO,format='%(asctime)s,%(name)s,%(levelname)s,%(message)s')
logging.info("This is my task for various Datatypes Operations")

input_list = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7),
                  set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                  {"k1": "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8},
                  ["ineuron", "data science "]]

class list_task():
#Try to extract all the list entity
    def extract_lst(self):
      logging.info("WE are about to extact list from the given collection")

      try:
          output_list = []
          for i in input_list:
              if type(i)== list:
                  output_list.append(i)
                  logging.info("List are extracted - %s",output_list)

                  print(output_list)

      except Exception as e:
          logging.exception(e)

lst = list_task()
print(lst.extract_lst())

 #Try to extract all the dict entities
class Dict_ext():
    def extract_dic(self):
        logging.info("We are extracting dictionary from the given collection")
        try:
            for i in input_list:
                if type(i) == dict:
                    print(i)
                    logging.info("Extracted dic is - %s",i)
        except Exception as e:
            logging.exception(e)

obj=Dict_ext()
print(obj.extract_dic())

##Try to extract all the tuples entities

class Tuple_ext():
    def extract_tup(self):
        logging.info("Trying to extract tuple from the given collection")
        try:
            for i in input_list:
                if type(i)==tuple:
                    print(i)
                    logging.info("Extracted tuple is - %s",i)
        except Exception as e:
            logging.exception(e)

obj1=Tuple_ext()
print(obj1.extract_tup())
##Try to give summation of all the numeric data

class sum_num():
    def numer_sum(self):
        logging.info("trying to get the sum of the numerical data from the collection")
        try:
           sum=0
           for i in input_list:

                if type(i)== list or type(i)==set or type(i)==tuple:
                    for j in i:
                        if type(j)==int:
                           sum +=j
                if type(i) == dict:
                    for k,v in i.items():
                        if type(k)==int or type(v)==int:
                                sum +=k
                                sum+=v
                        logging.info("sum of numerical data is - %s",sum)

           print(sum)

        except Exception as e:
            logging.exception(e)

obj3=sum_num()
print(obj3.numer_sum())

#Try to filter out all the odd values out all numeric data which is a part of a list

class Odd_val():
    def oddvalue(self):
        logging.info("trying to get the odd values from the numerical data which is part of List:")
        try:
            l1=[]
            for i in input_list:
                if type(i)==list:
                    for j in i:
                        if type(j)==int:
                            if j%2==1:
                                l1.append(j)
                                logging.info("Odd value - %s",l1)
            print(l1)

        except Exception as e:
            logging.exception(e)
obj4=Odd_val()
print(obj4.oddvalue())

##Try to extract "ineruon" out of this data

class Ineuron():
    def ext_ineuron(self):
        logging.info("Trying to extract Ineuron from the collection")
        try:
            l1=[]
            for i in input_list:
                if type(i)==list or type(i)==set or type(j)==tuple:
                    for j in i:
                        if j == "ineuron":
                            l1.append(j)
                if type(i)==dict:
                    for k in i.items():
                        for g in k:
                            if g=="ineuron":

                                l1.append(g)

                            logging.info("extracted list is - %s",l1)
            print(l1)

        except Exception as e:
            logging.exception(e)
obj5=Ineuron()
print(obj5.ext_ineuron())
##Try to find out a number of occurances of all the data

class occurence():
    def NoOfOcur(self):
        l1=[]
        logging.info("Trying to find out number of ocurrences of the data in the given collecton")
        try:
            for i in input_list:
                if type(i)==list or type(i)==set or type(i)==tuple:
                    for j in i:
                        l1.append(j)
                if type(i)==dict:
                    for k,v in i.items():
                        l1.append(k)
                        l1.append(v)

            for i in l1:
             print(i,":",l1.count(i))

            logging.info("Successfully get the ocurrencs ")

        except Exception as e:
         logging.exception(e)

obj6=occurence()
abc=obj6.NoOfOcur()
print(abc)

##Try to find out number of keys in dict element

class keys_dic():
    def keys_dic(self):
        logging.info("trying to get the no of keys in dic element")
        try:
            for i in input_list:
                if type(i)==dict:
                   print(len(i))
                   logging.info("length of dict elemnent is - %s",len(i))
        except Exception as e:
            logging.error(e)
obj7=keys_dic()
print(obj7.keys_dic())

#Try to filter out all the string data

class str_data():
    def str_fil(self):
        logging.info("Trying to filter out all the string data from the given collection")
        try:
            l1=[]
            for i in input_list:

                if type(i)==list or type(i)==set or type(i)==tuple:
                    for j in i:
                        if j==str:
                            l1.append(j)
                if type(i)==dict:
                    for k,v in i.items():
                        if type(k)== str or type(v)==str:
                         l1.append(k)
                         l1.append(v)
                    logging.info("string data from the collection are: - %s",l1)
        except Exception as e:
            logging.error(e)

obj8=str_data()
print(obj8.str_fil())

##Try to Find  out alphanum in data

class AlphaNum():
    def alpha_num(self):
        logging.info("trying to find out the alpha numerical data from the given collection")
        try:
            for i in input_list:
                if type(i)==str:
                    if i.isalnum() == True:
                        print(i)
                        logging.info("alpha numeric data is - %s",i)
        except Exception as e:
            logging.error(e)
obj9=AlphaNum()
print(obj9.alpha_num())

##Try to find out multiplication of all numeric value in the individual collection inside dataset

class Multiply():
    def multi(self):
        lst = 1
        tup = 1
        s = 1
        d = 1
        res = 1

        for i in input_list:
            if type(i) == list:
                for j in i:
                    if type(j) == int:
                        lst = lst * j
        logging.info("The multiplication result for all list elements is - %s ", lst)

        for i in input_list:
            if type(i) == tuple:
                for j in i:
                    if type(j) == int:
                        tup = tup * j
        logging.info("The multiplication result for all tuple elements is - %s ", tup)

        for i in input_list:
            if type(i) == set:
                for j in i:
                    if type(j) == int:
                        s = s * j
        logging.info("The multiplication result for all set elements is - %s", s)

        for i in input_list:
            if type(i) == dict:
                for k, v in i.items():
                    if type(k) == int or type(v) == int:
                        d = d * k
                        d = d * v
        logging.info("The multiplication result for all dict elements is - %s ", d)

        res = res * lst * tup * s * d
        print("The multiplication result for all int elements is - %s ", res)

obj10=Multiply()
print(obj10.multi())

##Try to unwrape all the collection inside collection and create a flat list.

class unwrape():
    def unwrap(self):
        lst=[]
        logging.info("trying to unwrap all the collection")
        try:
            for i in input_list:
                if type(i)==list or type(i)==set or type(i)==tuple:
                    for j in i:
                        lst.append(j)
                if type(i)==dict:
                    for k,v in i.items():
                        lst.append(k)
                        lst.append(v)
            print(lst)
            logging.info("flat list is - %s",lst)

        except Exception as e:
            logging.error(e)
obj11=unwrape()
print(obj11.unwrap())



















