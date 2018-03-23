import pymysql
import logging
import json

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S %p"
)


def insert(values, env):
    """
    将数据插入到mysql
    :return:
    """
    with open("./conf/" + env + ".conf") as f:
        config = json.loads(f.read())
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    try:
        sql = "replace into odps_tasks values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
              "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        res = cur.executemany(sql, values)
        print(res)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    value_list = json.load(open("value_list.txt", encoding="utf-8"))
    insert(value_list, 'test')
