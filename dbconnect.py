import json

import mysql.connector

global cnx


def searchtest():
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    # 建立数据库连接
    # 创建游标对象
    cursor = cnx.cursor()
    # 执行 SQL 查询
    query = "SELECT * FROM 学二"
    cursor.execute(query)
    # 获取查询结果
    result = cursor.fetchall()
    # 遍历结果并进行处理
    for row in result:
        # 对每一行数据进行操作
        print(type(row))
    # 关闭游标和连接
    cursor.close()
    cnx.close()


def findFood(house_name, count_name, food_name):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()
    # 执行 SQL 查询
    query = "SELECT * FROM 学二 WHERE 食堂 = 'house_name' AND 档口 = 'count_name' AND 菜名 = 'food_name';"
    cursor.execute(query)
    # 获取查询结果
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return result


def findAllFood():
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()
    # 执行 SQL 查询
    query = "SELECT * FROM 学二 "
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    # 获取查询结果
    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))
    cursor.close()
    cnx.close()
    return result


def eatchange(house_name, count_name, food_name):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()
    # 更新记录
    update_query = "UPDATE 学二 SET times = times + 1 WHERE 食堂 = %s AND 档口 = %s AND 菜名 = %s;"
    update_params = (house_name, count_name, food_name)
    print(update_params)
    cursor.execute(update_query, update_params)
    cnx.commit()
    print(cursor.rowcount)
    # 关闭游标和连接
    cursor.close()
    cnx.close()


def loadcomment(house_name, count_name, food_name):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()
    # 选择数据库
    sql_query = "SELECT comments FROM 学二 WHERE 食堂 = %s AND 档口 = %s AND 菜名 = %s"
    values = (house_name, count_name, food_name)
    print(values)
    cursor.execute(sql_query, values)
    result = cursor.fetchone()  # 获取查询结果
    print(type(result))
    cursor.close()
    cnx.close()
    if result is not None:
        comments_json = result[0]
        comments = json.loads(comments_json)  # 解析 JSON
        return comments
    else:
        return None


def savecomments(house_name, count_name, food_name, comments):
    # 将评论列表转换为 JSON 字符串
    comments_json = json.dumps(comments)

    # 连接到数据库
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()

    # 更新数据库中对应项的评论列
    sql_query = "UPDATE 学二 SET comments = %s WHERE 食堂 = %s AND 档口 = %s AND 菜名 = %s"
    values = (comments_json, house_name, count_name, food_name)

    cursor.execute(sql_query, values)
    cnx.commit()

    # 关闭数据库连接
    cursor.close()
    cnx.close()


def getkindfood(kind):
    # 连接到数据库
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()
    # 查询符合条件的食物数据
    print(kind)
    sql_query = "SELECT * FROM 学二 WHERE 类别 = %s"
    values = (kind,)
    cursor.execute(sql_query, values)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    # 获取查询结果
    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))
    print(result)
    # 关闭数据库连接
    cursor.close()
    cnx.close()
    # 返回符合条件的食物数据
    return result


def getplacefood(place):
    # 连接到数据库
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()
    # 查询符合条件的食物数据
    print(place)
    sql_query = "SELECT * FROM 学二 WHERE 食堂 = %s"
    values = (place,)
    cursor.execute(sql_query, values)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    # 获取查询结果
    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))
    print(result)
    # 关闭数据库连接
    cursor.close()
    cnx.close()
    # 返回符合条件的食物数据
    return result


def delafood(name):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()
    # 删除记录
    delete_query = "DELETE FROM 学二 WHERE 菜名 = %s;"
    cursor.execute(delete_query, (name,))
    # 提交事务
    cnx.commit()
    # 关闭游标和连接
    result = cursor.rowcount
    cursor.close()
    cnx.close()
    return result


def deldang(tang, dang):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()
    # 删除记录
    delete_query = "DELETE FROM 学二 WHERE 食堂 = %s AND 档口 = %s;"
    cursor.execute(delete_query, (tang, dang))
    # 提交事务
    cnx.commit()
    # 关闭游标和连接
    result = cursor.rowcount
    cursor.close()
    cnx.close()


def gaidang(yuan, xian, tang):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()

    # 更新记录
    update_query = "UPDATE 学二 SET 档口 = %s WHERE 档口 = %s AND 食堂 = %s;"
    cursor.execute(update_query, (xian, yuan, tang))

    # 提交事务
    cnx.commit()

    # 关闭游标和连接
    cursor.close()
    cnx.close()


def hasthis(cai, dang, tang):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()

    # 查询记录
    select_query = "SELECT * FROM 学二 WHERE 菜名 = %s AND 档口 = %s AND 食堂 = %s;"
    cursor.execute(select_query, (cai, dang, tang))

    # 获取查询结果
    records = cursor.fetchall()
    print(records)
    # 关闭游标和连接
    cursor.close()
    cnx.close()
    print(len(records))
    # 返回记录是否存在
    return len(records) > 0


def gaicai(name, dang, tang, price, cate, time):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()
    # 更新记录
    update_query = "UPDATE 学二 SET 价格 = %s ,类别 = %s, 时间 = %s WHERE 菜名 = %s AND 档口 = %s AND 食堂 = %s;"
    cursor.execute(update_query, (price, cate, time, name, dang, tang))
    # 提交更改
    cnx.commit()
    # 关闭游标和连接
    cursor.close()
    cnx.close()


def jiacai(dict_data):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()

    # 插入记录
    insert_query = "INSERT INTO 学二 (菜名, 价格, 类别, 时间, 食堂, times, 档口, comments) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
    data = (dict_data["name"], dict_data["price"], dict_data["category"],
            dict_data["time"], dict_data["place"], dict_data["times"], dict_data["count"],
            str(dict_data["comment"]))
    cursor.execute(insert_query, data)

    # 提交更改
    cnx.commit()

    # 关闭游标和连接
    cursor.close()
    cnx.close()


def zhuce(dict_data):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()

    # 插入记录
    insert_query = "INSERT INTO 用户示例 (name, mi, star, cost, last) VALUES (%s, %s, %s, %s, %s);"
    data = (dict_data["name"], dict_data["mi"], str(dict_data["star"]),
            dict_data["cost"], str(dict_data["last"]))
    cursor.execute(insert_query, data)

    # 提交更改
    cnx.commit()

    # 关闭游标和连接
    cursor.close()
    cnx.close()


def hasuser(user):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()

    # 查询记录
    select_query = "SELECT * FROM 用户示例 WHERE name = %s;"
    cursor.execute(select_query, (user,))

    # 获取查询结果
    records = cursor.fetchall()
    print(records)
    # 关闭游标和连接
    cursor.close()
    cnx.close()
    print(len(records))
    # 返回记录是否存在
    return len(records) > 0


def getuserdata(name):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()

    # 查询记录
    select_query = "SELECT * FROM 用户示例 WHERE name = %s;"
    cursor.execute(select_query, (name,))

    # 获取查询结果的列名
    column_names = cursor.column_names

    # 获取查询结果
    records = cursor.fetchall()

    # 关闭游标和连接
    cursor.close()
    cnx.close()

    # 将查询结果转换为字典
    user_data = {}
    if len(records) > 0:
        for i, column_name in enumerate(column_names):
            if column_name == "star" or column_name == "last":
                user_data[column_name] = json.loads(records[0][i])
            else:
                user_data[column_name] = records[0][i]

    return user_data


def addstar(name, food):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()

    # 查询记录
    select_query = "SELECT star FROM 用户示例 WHERE name = %s;"
    cursor.execute(select_query, (name,))
    result = cursor.fetchall()

    # 将查询结果转换为列表形式
    if result:
        star_list = json.loads(result[0][0])
        # 检查食物是否已存在于星级列表中
        if food not in star_list:
            star_list.append(food)
            updated_star = json.dumps(star_list)

            # 更新记录
            update_query = "UPDATE 用户示例 SET star = %s WHERE name = %s;"
            cursor.execute(update_query, (updated_star, name))
            cnx.commit()
    else:
        # 如果用户记录不存在，则创建新记录
        star_list = [food]
        updated_star = json.dumps(star_list)

        insert_query = "INSERT INTO 用户示例 (name, star) VALUES (%s, %s);"
        cursor.execute(insert_query, (name, updated_star))
        cnx.commit()

    # 读取查询结果后关闭游标和连接
    cursor.fetchall()
    cursor.close()
    cnx.close()


def addcost(name, cost):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()

    # 查询记录
    select_query = "SELECT cost FROM 用户示例 WHERE name = %s;"
    cursor.execute(select_query, (name,))
    result = cursor.fetchone()

    # 更新成本属性
    if result:
        old_cost = result[0]
        new_cost = str(float(old_cost) + float(cost))

        # 更新记录
        update_query = "UPDATE 用户示例 SET cost = %s WHERE name = %s;"
        cursor.execute(update_query, (new_cost, name))
        cnx.commit()
    else:
        # 如果用户记录不存在，则创建新记录
        insert_query = "INSERT INTO 用户示例 (name, cost) VALUES (%s, %s);"
        cursor.execute(insert_query, (name, cost))
        cnx.commit()

    # 处理所有结果
    cursor.fetchall()

    # 关闭游标和连接
    cursor.close()
    cnx.close()


def lastchange(name, kind):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()

    # 查询记录
    select_query = "SELECT last FROM 用户示例 WHERE name = %s;"
    cursor.execute(select_query, (name,))
    result = cursor.fetchone()

    # 更新 last 属性
    if result:
        last_data = json.loads(result[0])
        last_data.append(kind)

        # 如果列表长度大于 5，则移除第一个元素
        if len(last_data) > 5:
            last_data = last_data[1:]

        # 更新记录
        update_query = "UPDATE 用户示例 SET last = %s WHERE name = %s;"
        cursor.execute(update_query, (json.dumps(last_data), name))
        cnx.commit()
    else:
        # 如果用户记录不存在，则创建新记录
        insert_query = "INSERT INTO 用户示例 (name, last) VALUES (%s, %s);"
        cursor.execute(insert_query, (name, json.dumps([kind])))
        cnx.commit()

    # 处理所有结果
    cursor.fetchall()

    # 关闭游标和连接
    cursor.close()
    cnx.close()


def getlast(name):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()

    # 查询记录
    select_query = "SELECT last FROM 用户示例 WHERE name = %s;"
    cursor.execute(select_query, (name,))
    result = cursor.fetchone()
    if result:
        json_list = json.loads(result[0])
    else:
        json_list = []
    cursor.close()
    cnx.close()
    return json_list


def getstar(name):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()

    # 查询记录
    select_query = "SELECT star FROM 用户示例 WHERE name = %s;"
    cursor.execute(select_query, (name,))
    result = cursor.fetchone()

    if result is not None:
        star_list = json.loads(result[0])
        # 关闭游标和连接
        cursor.close()
        cnx.close()
        return star_list
    else:
        # 关闭游标和连接
        cursor.close()
        cnx.close()
        return []

def changemi(user, newmi):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()

    # 更新记录
    update_query = "UPDATE 用户示例 SET mi = %s WHERE name = %s;"
    cursor.execute(update_query, (newmi, user))
    cnx.commit()

    # 获取更新后的数据
    select_query = "SELECT star, last, cost, mi FROM 用户示例 WHERE name = %s;"
    cursor.execute(select_query, (user,))
    result = cursor.fetchone()

    if result is not None:
        star_list = json.loads(result[0])
        last = result[1]
        cost = result[2]
        mi = result[3]

        # 关闭游标和连接
        cursor.close()
        cnx.close()

        data = {
            'star': star_list,
            'last': last,
            'cost': cost,
            'mi': mi
        }
        return data
    else:
        # 关闭游标和连接
        cursor.close()
        cnx.close()
        return None

def changename(name, newname):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()

    # 更新记录
    update_query = "UPDATE 用户示例 SET name = %s WHERE name = %s;"
    cursor.execute(update_query, (newname, name))
    cnx.commit()

    # 获取更新后的数据
    select_query = "SELECT star, last, cost, mi FROM 用户示例 WHERE name = %s;"
    cursor.execute(select_query, (newname,))
    result = cursor.fetchone()

    if result is not None:
        star_list = json.loads(result[0])
        last = result[1]
        cost = result[2]
        mi = result[3]

        # 关闭游标和连接
        cursor.close()
        cnx.close()

        data = {
            'star': star_list,
            'last': last,
            'cost': cost,
            'mi': mi
        }
        return data
    else:
        # 关闭游标和连接
        cursor.close()
        cnx.close()
        return None

def changestar(name, star):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='localhost', database='hangeat')
    cursor = cnx.cursor()

    # 更新记录
    update_query = "UPDATE 用户示例 SET star = %s WHERE name = %s;"
    cursor.execute(update_query, (json.dumps(star), name))
    cnx.commit()

    # 获取更新后的数据
    select_query = "SELECT star, last, cost, mi FROM 用户示例 WHERE name = %s;"
    cursor.execute(select_query, (name,))
    result = cursor.fetchone()

    if result is not None:
        star_list = json.loads(result[0])
        last = result[1]
        cost = result[2]
        mi = result[3]

        # 关闭游标和连接
        cursor.close()
        cnx.close()

        data = {
            'star': star_list,
            'last': last,
            'cost': cost,
            'mi': mi
        }
        return data
    else:
        # 关闭游标和连接
        cursor.close()
        cnx.close()
        return None