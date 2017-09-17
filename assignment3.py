from __future__ import division
import argparse
import urllib2
import urllib
import csv
from StringIO import StringIO
import re
from datetime import datetime

def read_url(weburl):
    req = urllib2.Request(weburl)
    response = urllib2.urlopen(weburl)
    return response.read()

def parse_csv(csvdata):
    count_image = 0
    count_jpg = 0
    count_gif = 0
    count_png = 0
    count_rows = 0
    reader = csv.reader(StringIO(csvdata))
    for row in reader:
        count_rows += 1
        if row[0].lower().find('jpg') != -1:
            count_jpg += 1
        if row[0].lower().find('gif') != -1:
            count_gif += 1
        if row[0].lower().find('png') != -1:
            count_png += 1
        count_image = count_jpg+count_gif+count_png
    print "Image requests account for {}% of all requests".format(100 * count_image/count_rows)

def popular_browser(csvdata):
    count_browser = 0
    count_firefox = 0
    count_chrome = 0
    count_safari = 0
    count_ie = 0
    reader = csv.reader(StringIO(csvdata))
    for row in reader:
        if row[2].find('Firefox') != - 1:
            count_firefox += 1
        if row[2].find('Chrome') != - 1:
            count_chrome += 1
        if row[2].find('Safari') != - 1:
            count_safari += 1
        if row[2].find('Internet Explorer') != - 1:
            count_ie += 1
    data = {'Firefox': count_firefox, 'Chrome': count_chrome, 'Safari': count_safari, 'Internet Explorer': count_ie}
    key, value = max(data.iteritems(), key=lambda x: x[1])
    print "The most popular browser is " + str(key) + " with " + str(value) + " hits"

def hour_hits(csvdata):
    reader = csv.reader(StringIO(csvdata))
    mylist = []
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    count_7 = 0
    count_8 = 0
    count_9 = 0
    count_10 = 0
    count_11 = 0
    count_12 = 0
    count_13 = 0
    count_14 = 0
    count_15 = 0
    count_16 = 0
    count_17 = 0
    count_18 = 0
    count_19 = 0
    count_20 = 0
    count_21 = 0
    count_22 = 0
    count_23 = 0
    count_24 = 0
    for row in reader:
        mylist.append(datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S').time())
    for line in mylist:
         if re.match('^01', str(line)):
            count_1+=1
    for line in mylist:
         if re.match('^02', str(line)):
            count_2+=1
    for line in mylist:
         if re.match('^03', str(line)):
            count_3+=1
    for line in mylist:
         if re.match('^04', str(line)):
            count_4+=1
    for line in mylist:
         if re.match('^05', str(line)):
            count_5+=1
    for line in mylist:
         if re.match('^06', str(line)):
            count_6+=1
    for line in mylist:
         if re.match('^07', str(line)):
            count_7+=1
    for line in mylist:
         if re.match('^08', str(line)):
            count_8+=1
    for line in mylist:
         if re.match('^09', str(line)):
            count_9+=1
    for line in mylist:
         if re.match('^10', str(line)):
            count_10+=1
    for line in mylist:
         if re.match('^11', str(line)):
            count_11+=1
    for line in mylist:
         if re.match('^12', str(line)):
            count_12+=1
    for line in mylist:
         if re.match('^13', str(line)):
            count_13+=1
    for line in mylist:
         if re.match('^14', str(line)):
            count_14+=1
    for line in mylist:
         if re.match('^15', str(line)):
            count_15+=1
    for line in mylist:
         if re.match('^16', str(line)):
            count_16+=1
    for line in mylist:
         if re.match('^17', str(line)):
            count_17+=1
    for line in mylist:
         if re.match('^18', str(line)):
            count_18+=1
    for line in mylist:
         if re.match('^19', str(line)):
            count_19+=1
    for line in mylist:
         if re.match('^20', str(line)):
            count_20+=1
    for line in mylist:
         if re.match('^21', str(line)):
            count_21+=1
    for line in mylist:
         if re.match('^22', str(line)):
            count_22+=1
    for line in mylist:
         if re.match('^23', str(line)):
            count_23+=1
    for line in mylist:
         if re.match('^00', str(line)):
            count_24+=1
    print 'Hour 1 has ' + str(count_1) + ' hits'
    print 'Hour 2 has ' + str(count_2) + ' hits'
    print 'Hour 3 has ' + str(count_3) + ' hits'
    print 'Hour 4 has ' + str(count_4) + ' hits'
    print 'Hour 5 has ' + str(count_5) + ' hits'
    print 'Hour 6 has ' + str(count_6) + ' hits'
    print 'Hour 7 has ' + str(count_7) + ' hits'
    print 'Hour 8 has ' + str(count_8) + ' hits'
    print 'Hour 9 has ' + str(count_9) + ' hits'
    print 'Hour 10 has ' + str(count_10) + ' hits'
    print 'Hour 11 has ' + str(count_11) + ' hits'
    print 'Hour 12 has ' + str(count_12) + ' hits'   
    print 'Hour 13 has ' + str(count_13) + ' hits'
    print 'Hour 14 has ' + str(count_14) + ' hits'
    print 'Hour 15 has ' + str(count_15) + ' hits'
    print 'Hour 16 has ' + str(count_16) + ' hits'
    print 'Hour 17 has ' + str(count_17) + ' hits'
    print 'Hour 18 has ' + str(count_18) + ' hits'
    print 'Hour 19 has ' + str(count_19) + ' hits'
    print 'Hour 20 has ' + str(count_20) + ' hits'
    print 'Hour 21 has ' + str(count_21) + ' hits'
    print 'Hour 22 has ' + str(count_22) + ' hits'
    print 'Hour 23 has ' + str(count_23) + ' hits'
    print 'Hour 24 has ' + str(count_24) + ' hits'

            
if __name__ == "__main__":
    weburl = raw_input("enter url: ")
    parser = argparse.ArgumentParser(description='download data from csv file')
    parser.add_argument('--url', action="store", dest="weburl")
    args = parser.parse_args()
    csvdata = read_url(weburl)
    parse_csv(csvdata)
    popular_browser(csvdata)
    hour_hits(csvdata)
