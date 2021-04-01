import sqlite3
import sys
from datetime import datetime, timedelta
import calendar

def month_name (number):
    if number == 1:
        return "Jan"
    elif number == 2:
        return "Feb"
    elif number == 3:
        return "Mar"
    elif number == 4:
        return "Apr"
    elif number == 5:
        return "May"
    elif number == 6:
        return "June"
    elif number == 7:
        return "July"
    elif number == 8:
        return "August"
    elif number == 9:
        return "Sep"
    elif number == 10:
        return "Oct"
    elif number == 11:
        return "Nov"
    elif number == 12:
        return "Dec"
try:
    db = sys.argv[1]
    if db:
        connection = sqlite3.connect(db)
        c = connection.cursor()
        try:
            print("Source File:", db)
            c.execute("SELECT id FROM downloads")
            print("Total Downloads:", len(c.fetchall()))
            

            c.execute("PRAGMA table_info(urls)")
            #print("url col names")
            #print(c.fetchall()) #columns names

            c.execute("PRAGMA table_info(keyword_search_terms)")
            #print("keyword col names")
            #print(c.fetchall()) #columns names
            c.execute("PRAGMA table_info(urls)")
            #print("keyword col names")
            #print(c.fetchall()) #columns names
            c.execute("PRAGMA table_info(visits)")
            #print("keyword col names")
            #print(c.fetchall()) #columns names

            c.execute("SELECT keyword_id, url_id, term FROM keyword_search_terms")
            #print("all search")
            #print(c.fetchall()) #columns names

            c.execute("SELECT visit_time, url FROM visits ORDER BY visit_time DESC")
            #print(c.fetchall())
            #print("all search")
            #print(c.fetchall()) #columns names


            #c.execute("SELECT id, url FROM urls WHERE url LIKE '%library%'")
            #print("all search")
            #print(c.fetchall()) #columns names

            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            #print(c.fetchall()) #all tables

         


            num_of_downloads = c.execute("SELECT term FROM keyword_search_terms")
            num_of_downloads.fetchall()

            max_time = c.execute ("SELECT max(end_time - start_time), current_path FROM downloads")
            max_time = c.fetchone()
            max_time = max_time[1]
            max_time = max_time.split("\\")[-1]
            print("File Name:", max_time)

            file_size = c.execute ("SELECT max(end_time - start_time), received_bytes FROM downloads")
            file_size = c.fetchone()
            print("File Size:", file_size [1])

            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            #print(c.fetchall()) #all tables


            uniuqe_searchs = c.execute("SELECT DISTINCT term FROM keyword_search_terms")
            uniuqe_searchs = uniuqe_searchs.fetchall()
            print("Unique Search Terms:", len(uniuqe_searchs))

            join = c.execute("SELECT term, url_id FROM keyword_search_terms INNER JOIN urls on urls.id = keyword_search_terms.url_id ORDER BY last_visit_time DESC")
            join = join.fetchall()
            #print(join)
            print("Most Recent Search:", join[0][0])

            id = join[0][1]
            join_time = c.execute("SELECT last_visit_time FROM urls WHERE id = ?", (id,))
            join_time = join_time.fetchall()
            #print(join_time)
          
            most_recent_time = c.execute("SELECT datetime(visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime') FROM visits WHERE url = ?", (id,))
            most_recent_time = most_recent_time.fetchall()
            temp = most_recent_time[0][0]
            num_of_momth = temp [6:7]
            print(num_of_momth)
            x = month_name(int(num_of_momth))
            year = temp[0:5]
            day = temp[7:10]
            secs = temp[10:]
        
            print("Most Recent Search Date/Time: {}{}{}{}".format(year,x,day,secs))

            
      

        except sqlite3.OperationalError:
            print("Error! - File Not Found!")


except:
        print("Error! - No History File Specified!")

