import json
import mysql.connector
from hashids import Hashids
import re


from mysql.connector import Error
from mysql.connector import errorcode
from datetime import date
hashids = Hashids(min_length=4, salt='this should be a secret random string')
class Link():
    server_url = "http://127.0.0.1:5000/"
    def __init__(self):
        self.myCon = mysql.connector.connect(
            host="localhost",
            user="root",
            # password="dpass",
            database="test")

    def isValidURL(self,str):
        # Regex to check valid URL
        regex = ("((http|https)://)(www.)?" +
                 "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                 "{2,256}\\.[a-z]" +
                 "{2,6}\\b([-a-zA-Z0-9@:%" +
                 "._\\+~#?&//=]*)")

        # Compile the ReGex
        p = re.compile(regex)

        # If the string is empty
        # return false
        if (str == None):
            return False

        # Return if the string
        # matched the ReGex
        if (re.search(p, str)):
            return True
        else:
            return False

    def AddShortenedUrl(self,original_url,short_url):
        state = False
        try:
            mycursor = self.myCon.cursor()

            today = date.today()
            tdate = today.strftime("%Y/%d/%m")
            # date_time=datetime.datetime.now()
            print(tdate)
            sql_insert_query = f"insert into tbStudent (original_url, short_url, RegDate) values ('{original_url}','{short_url}','{tdate}')";

            mycursor.execute(sql_insert_query)
            self.myCon.commit();
            # print("New URL Added")
            state = True
        except mysql.connector.Error as error:
            state = False
            # print("Failed to insert query into tbStudent table {}".format(error))
        finally:
            mycursor.close()
            if state==True:
                return short_url
            else:
                return "Erorr While adding"

    def GetRowsNumber(self):
        mycursor = self.myCon.cursor()

        mycursor.execute("SELECT Count(*) FROM tbstudent ")

        myRecordset = mycursor.fetchall()
        mycursor.close()
        return myRecordset[0][0]
    def CheckExsistUrl(self,short_url):
        mycursor = self.myCon.cursor()

        mycursor.execute(f"SELECT original_url, short_url FROM tbstudent  WHERE short_url ='{short_url}'")

        myRecordset = mycursor.fetchall()
        if mycursor.rowcount == 0:
            mycursor.close()
            return "no such exissting website"
        else:
            original_url = myRecordset[0][0]
            mycursor.close()
            return original_url
        #
        # for r in myRecordset:
        #
        #     print(r[0], r[1], r[2])

    def ShortenUrl(self,original_url):

        vaild = self.isValidURL(original_url)
        if vaild != True:
            return "The Url Not Valid"
        original_url_id = self.GetRowsNumber() + 1
        url_length = len(original_url)
        url_sum = 0
        for i in range(url_length):
            url_sum += ord(original_url[i])
        print(url_sum)

        hashid = hashids.encode(original_url_id)

        short_url =  hashid
        return self.AddShortenedUrl(original_url,short_url)

    def showUrls(self):
        """
            get all api urls
            """
        mycursor = self.myCon.cursor()
        mycursor.execute("SELECT original_url, short_url, RegDate FROM tbstudent ")
        myRecordset = mycursor.fetchall()
        mycursor.close()
        return str(myRecordset)
    def showUrlsJson(self):
        """
            get all api urls
            """
        mycursor = self.myCon.cursor()

        mycursor.execute("SELECT original_url, short_url, RegDate FROM tbstudent ")

        myRecordset = mycursor.fetchall()
        json_data = []
        row_headers = [x[0] for x in mycursor.description]  # this will extract row headers
        for r in myRecordset:
            json_data.append(dict(zip(row_headers, r)))

        mycursor.close()
        return json.dumps(json_data)



    # Function to validate URL
    # using regular expression
    # def ShortenUrl(self, original_url):
    #     # app.config['SECRET_KEY'] = 'this should be a secret random string'
    #     #
    #     # hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])
    #     # hashids = Hashids(min_length=4, salt= 'this should be a secret random string')
    #     vaild = self.isValidURL(original_url)
    #     if vaild != True:
    #         return "The Url Not Valid"
    #     original_url_id = self.GetRowsNumber() + 1
    #     url_length = len(original_url)
    #     url_sum = 0
    #
    #     for i in range(url_length):
    #         url_sum += ord(original_url[i])
    #     print(url_sum)
    #
    #     # print(url_id)
    #
    #     hashid = hashids.encode(original_url_id)
    #     # print(hashid)
    #     # short_url = "http://127.0.0.1:5000/" + hashid
    #     short_url = hashid
    #     return self.AddShortenedUrl(original_url, short_url)
    #     # print(short_url)