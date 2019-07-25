# !/bin/python
# **coding=utf-8**

import sqlite3


def creatDB():

    """
    for generate DataBase
    """
    # createDB in Local directory
    conn = sqlite3.connect("botHistory.sqlite3")
    c = conn.cursor()

    # create tables
    sql = '''
    create table IF NOT EXISTS chat_history
(
    id         INTEGER
        constraint chat_history_pk
            primary key autoincrement,
    user_id    VARCHAR(45),
    human      TEXT,
    bot        TEXT,
    session_id VARCHAR(45),
    creat_time DATETIME default (DATETIME(CURRENT_TIMESTAMP ,'localtime')) not null
);

    '''
    c.execute(sql)

    # save the changes
    conn.commit()

    # close the connection with the database
    conn.close()

def InsertDB(user, ask , answer):
    conn = sqlite3.connect("DataBase/botHistory.sqlite3")
    c = conn.cursor()

    # create tables
    sql = '''
        INSERT INTO chat_history (user_id, human, bot, session_id) VALUES ('%s','%s','%s',NULL)

        ''' % (user, ask, answer)
    c.execute(sql)

    # save the changes
    conn.commit()

    # close the connection with the database
    conn.close()



if __name__ == '__main__':
    creatDB()
    InsertDB('007', '哈哈哈哈哈哈号', '你好啊')
