# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 15:28:44 2017

@author: daniel
"""

import csv, configparser, datetime, os, glob

#Where am I running?
dir_path = os.path.dirname(os.path.realpath(__file__))


#Create a config object, in the event we use it later
configobject = configparser.ConfigParser()
configobject.read('{}\\Widoc_KofaxAssembler_Config.ini'.format(dir_path))
headers = 'OFFENDER_ID,LAST_NAME,FIRST_NAME,MIDDLE_NAME,OHR_DATE,OHR_LOCATION,FORM_NUMBER,SCAN_IMPORT_DATE,FILE_NAME'





#Local paths
widoc_dir = 'E:\\Kofax_Widoc\\WIDOC'
img_source = widoc_dir + '\\IMAGES'
data_source = widoc_dir + '\\DATA'
output_dir = widoc_dir + '\\DELIVERED'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)



#Our main list
current_count = 0
datastream = []
textfile = glob.glob(os.path.join(data_source,"*.txt"))


def write_widocdata(output_dir):
    with open(output_dir + 'ay.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(headers)
        spamwriter.writerow


#Reads INDEX.txt and parses it to a list
def read_kofaxdata(data_source):
    for datafile in textfile:
        with open(datafile, newline='') as csvfile:
            #datastream.append(headers)
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                ohr_docnumber = row[3]
                
                #First lets zerofill the DOC Numbers so they're 8 long
                if ohr_docnumber != '':
                    if ohr_docnumber != None:
                        ohr_docnumber = ohr_docnumber.zfill(8)
                        
                #last, first, and middle names stay as they are
                last_name = row[5].upper()
                first_name = row[7].upper()
                middle_name = row[9].upper()
                
                #Convert ohr_date to unix stamp
                ohr_date = row[11]
                if ohr_date != '':
                    if ohr_date != None:
                        ohr_date = datetime.datetime.strptime(ohr_date, '%m/%d/%y').strftime('%Y-%m-%d')
                
                
                ohr_location = row[13]
                doc_type = row[15]
                
                #Convert batch_date to unix stamp
                batch_date = row[17]
                if batch_date != '':
                    if batch_date != None:
                        batch_date = datetime.datetime.strptime(batch_date, '%m/%d/%Y').strftime('%Y-%m-%d')
                        
                batch_name = row[19]
                
                img_path = row[20]
                img_name = os.path.basename(img_path)
                internal_file_name = img_name
                global current_count
                current_count += 1
                external_file_name = batch_name + '_DOC' +  (str(current_count) + '.pdf')
                
                the_text = '{}","{}","{}","{}","{}","{}","{}","{}","{}","{}"'.format(ohr_docnumber, last_name, first_name, middle_name, ohr_date, ohr_location, doc_type, batch_date, internal_file_name, external_file_name)
                datastream.append(the_text)
        return(datastream)
    
    
    

datastream = read_kofaxdata(data_source)

