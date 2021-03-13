"""
Util for managing the DB
"""
import json

import psycopg2

from queries import *

FORECAST_TIME = "forecastTime"

PRECIPITATION = "Precipitation"

TEMPERATURE = "Temperature"


class DBHandler:

    def __init__(self):
        self.table_name = "WeatherByLocation"

    @staticmethod
    def connect():
        auth_path = "auth.json"
        with open(auth_path, "r") as f:
            params = json.load(f)
        conn = psycopg2.connect(**params)
        return conn

    @staticmethod
    def insert_list(conn, values):
        cur = conn.cursor()
        sql = SQL_INSERT_QUERY
        cur.executemany(sql, values)
        conn.commit()
        cur.close()

    @staticmethod
    def create_table(conn):
        cur = conn.cursor()
        sql = SQL_CREATE_TABLE_QUERY
        cur.execute(sql)
        conn.commit()
        cur.close()
        print("table created successfully")

    @staticmethod
    def drop_table(conn):
        cur = conn.cursor()
        sql = SQL_DROP_TABLE
        cur.execute(sql)
        conn.commit()
        cur.close()
        print("table was dropped")

    @staticmethod
    def create_index(conn):
        cur = conn.cursor()
        sql = SQL_CREATE_INDEX
        cur.execute(sql)
        conn.commit()
        cur.close()
        print("index created successfully")

    @staticmethod
    def get_from_db(conn, sql):
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        return result

    def get_weather_by_location(self, lon, lat):
        conn = self.connect()
        sql = SQL_SELECT_WITH_LON_LAT.format(lon, lat)
        result = self.get_from_db(conn, sql)
        conn.close()
        result_dict = []
        for row in result:
            row_as_json = {
                TEMPERATURE: row[3],
                PRECIPITATION: row[4],
                FORECAST_TIME: row[2].strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            }
            result_dict.append(row_as_json)
        return result_dict

    def get_max_from_db(self, lon, lat):
        conn = self.connect()
        sql = SQL_SELECT_WITH_OPERATOR.format(lon, lat)
        result = self.get_from_db(conn, sql)
        conn.close()
        result_json = {"max": {TEMPERATURE: result[0][0], PRECIPITATION: result[0][1]},
                       "min": {TEMPERATURE: result[0][2], PRECIPITATION: result[0][3]},
                       "avg": {TEMPERATURE: result[0][4], PRECIPITATION: result[0][5]}}
        return result_json

    def setup_db(self):
        """
        apply this method for creating the table for the first time and setting the indexes
        """
        conn = self.connect()
        self.drop_table(conn)
        self.create_table(conn)
        self.create_index(conn)
