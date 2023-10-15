# Write a program to perform File handling concept by create, read & write operation in text, csv file

import csv
from os import path

class FileHandeling:

    # defaulf text file is created
    def __init__(self,filename):
        if not path.exists(filename):
            self.textFile = filename;
        else:
            print("File already exists");

    def createTextFile(self,filename):
        if not path.exists(filename):
            self.textFile = filename;
        else:
            print("File already exists");

    def readTextFile(self):
        content=""
        if path.exists(self.textFile):
            rd = open(f"{self.textFile}.txt",'r');
            content = rd.read();
            rd.close();
            return content;
        else:
            return "File does not exist";


    def writeTextFile(self,content):
        if path.exists(self.textFile):
            wr = open(f"{self.textFile}.txt",'a');
            wr.write(content);
            wr.close();
        else:
            wr = open(f"{self.textFile}.txt",'w');
            wr.write(content);
            wr.close();

    def createCsvFile(self,filename):
        if not path.exists(filename):
            self.csvFile = filename;
        else:
            print("File already exists");

    def setCsvSchema(self,obj):
        if path.exists(self.csvFile):
            fields = obj;
            f = open(self.csvFile,'w+',newline='');
            writer = csv.DictWriter(self.csvFile,fieldnames=fields);
            writer.writeheader();
            writer.writerow({
                
            })
            f.close();

        else:
            print("File already exists");

    def readCsvFile(self,filename):
        if path.exists(filename):
            f = open(self.csvFile,'r');
            print(f.read());
        else:
            print("File already exists");

    def writeCsvFile(self,filename):
        if not path.exists(filename):
            self.file = open(f"{filename}.csv",'x');
        else:
            print("File already exists");


f = not open("file.txt",'x');
f.write("hello world");
f.close();

f = open("file.txt",'r');
print(f.read());