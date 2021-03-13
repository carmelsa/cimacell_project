"""
Run this file to upload the csv files to the remote db
"""
import csv
import glob

from db_handler import DBHandler


def upload_csv_dir_to_db():
    file_names = glob.glob("resources/*.csv")
    for file_name in file_names:
        upload_csv_to_db(file_name)


def upload_csv_to_db(file_name):
    db_handler = DBHandler()
    conn = db_handler.connect()
    with open(file_name, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        list_to_inset = []
        for index, row in enumerate(reader):
            if index == 0:
                continue
            if index % 100 == 0:
                db_handler.insert_list(conn, tuple(list_to_inset))
                print(index)
                list_to_inset.clear()
            list_to_inset.append(tuple(row))
        db_handler.insert_list(conn, list_to_inset)
    conn.close()


# upload_csv_dir_to_db()
