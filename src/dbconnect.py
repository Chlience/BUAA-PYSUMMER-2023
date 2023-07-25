import json

import pymysql

def findFood(house_name, count_name, food_name):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()
    # 执行 SQL 查询
    query = "SELECT * FROM 学二 WHERE 食堂 = %s AND 档口 = %s AND 菜名 = %s;"
    params = (house_name, count_name, food_name)
    cursor.execute(query, params)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    # 获取查询结果
    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))
    cursor.close()
    cnx.close()
    return result

def findTimeFood(time):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()
    # 执行 SQL 查询
    query = "SELECT * FROM 学二 WHERE 时间 = %s "
    cursor.execute(query, time)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    # 获取查询结果
    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))
    cursor.close()
    cnx.close()
    return result


def findAllFood():
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
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
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()
    # 更新记录
    update_query = "UPDATE 学二 SET times = times + 1 WHERE 食堂 = %s AND 档口 = %s AND 菜名 = %s;"
    update_params = (house_name, count_name, food_name)
    cursor.execute(update_query, update_params)
    cnx.commit()
    # 关闭游标和连接
    cursor.close()
    cnx.close()


def getkindfood(kind):
    # 连接到数据库
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()
    # 查询符合条件的食物数据
    sql_query = "SELECT * FROM 学二 WHERE 类别 = %s"
    values = (kind,)
    cursor.execute(sql_query, values)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    # 获取查询结果
    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))
    # 关闭数据库连接
    cursor.close()
    cnx.close()
    # 返回符合条件的食物数据
    return result


def getplacefood(place):
    # 连接到数据库
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()
    # 查询符合条件的食物数据
    sql_query = "SELECT * FROM 学二 WHERE 食堂 = %s"
    values = (place,)
    cursor.execute(sql_query, values)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    # 获取查询结果
    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))
    # 关闭数据库连接
    cursor.close()
    cnx.close()
    # 返回符合条件的食物数据
    return result


def delafood(food, count, house):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()
    # 删除记录
    delete_query = "DELETE FROM 学二 WHERE 菜名 = %s AND 档口 = %s AND 食堂 = %s;"
    cursor.execute(delete_query, (food, count, house))
    # 提交事务
    cnx.commit()
    # 关闭游标和连接
    result = cursor.rowcount
    cursor.close()
    cnx.close()
    return result


def deldang(tang, dang):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
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
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
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
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()

    # 查询记录
    select_query = "SELECT * FROM 学二 WHERE 菜名 = %s AND 档口 = %s AND 食堂 = %s;"
    cursor.execute(select_query, (cai, dang, tang))

    # 获取查询结果
    records = cursor.fetchall()
    # 关闭游标和连接
    cursor.close()
    cnx.close()
    # 返回记录是否存在
    return len(records) > 0


def gaicai(username, dang, tang, price, cate, time):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()
    # 更新记录
    update_query = "UPDATE 学二 SET 价格 = %s ,类别 = %s, 时间 = %s WHERE 菜名 = %s AND 档口 = %s AND 食堂 = %s;"
    cursor.execute(update_query, (price, cate, time, username, dang, tang))
    # 提交更改
    cnx.commit()
    # 关闭游标和连接
    cursor.close()
    cnx.close()


def jiacai(dict_data):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()

    # 插入记录
    insert_query = "INSERT INTO 学二 (菜名, 价格, 类别, 时间, 食堂, times, 档口, comments) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
    data = (dict_data["username"], dict_data["price"], dict_data["category"],
            dict_data["time"], dict_data["place"], dict_data["times"], dict_data["count"],
            str(dict_data["comment"]))
    cursor.execute(insert_query, data)

    # 提交更改
    cnx.commit()

    # 关闭游标和连接
    cursor.close()
    cnx.close()


def zhuce(dict_data):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()

    # 插入记录
    insert_query = "INSERT INTO user (username, password, star, cost, last, 评分) VALUES (%s, %s, %s, %s, %s, %s);"
    data = (dict_data["username"], dict_data["password"], str(dict_data["star"]),
            dict_data["cost"], str(dict_data["last"]), '{}')
    cursor.execute(insert_query, data)

    # 提交更改
    cnx.commit()

    # 关闭游标和连接
    cursor.close()
    cnx.close()


def hasuser(user):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()

    # 查询记录
    select_query = "SELECT * FROM user WHERE username = %s;"
    cursor.execute(select_query, (user,))

    # 获取查询结果
    records = cursor.fetchall()
    # 关闭游标和连接
    cursor.close()
    cnx.close()
    # 返回记录是否存在
    return len(records) > 0


def getuserdata(username):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()

    # 查询记录
    select_query = "SELECT * FROM user WHERE username = %s;"
    cursor.execute(select_query, (username,))

    # 获取查询结果的列名
    column_names = [column[0] for column in cursor.description]

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


def addstar(username, food,count, house):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()

    # 查询记录
    select_query = "SELECT star FROM user WHERE username = %s;"
    cursor.execute(select_query, (username,))
    result = cursor.fetchall()
    info= house+'-'+count+'-'+food
    # 将查询结果转换为列表形式
    if result:
        star_list = json.loads(result[0][0])
        # 检查食物是否已存在于星级列表中
        if info not in star_list:
            star_list.append(info)
            updated_star = json.dumps(star_list)

            # 更新记录
            update_query = "UPDATE user SET star = %s WHERE username = %s;"
            cursor.execute(update_query, (updated_star, username))
            cnx.commit()
    else:
        # 如果用户记录不存在，则创建新记录
        star_list = [info]
        updated_star = json.dumps(star_list)

        insert_query = "INSERT INTO user (username, star) VALUES (%s, %s);"
        cursor.execute(insert_query, (username, updated_star))
        cnx.commit()

    # 读取查询结果后关闭游标和连接
    cursor.fetchall()
    update_query = "UPDATE 学二 SET 收藏人数 = 收藏人数 + 1 WHERE 食堂 = %s AND 档口 = %s AND 菜名 = %s;"
    update_params = (house, count, food)
    cursor.execute(update_query, update_params)
    cnx.commit()
    cursor.close()
    cnx.close()


def addcost(username, cost):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()

    # 查询记录
    select_query = "SELECT cost FROM user WHERE username = %s;"
    cursor.execute(select_query, (username,))
    result = cursor.fetchone()

    # 更新成本属性
    if result:
        old_cost = result[0]
        new_cost = str(float(old_cost) + float(cost))

        # 更新记录
        update_query = "UPDATE user SET cost = %s WHERE username = %s;"
        cursor.execute(update_query, (new_cost, username))
        cnx.commit()
    else:
        # 如果用户记录不存在，则创建新记录
        insert_query = "INSERT INTO user (username, cost) VALUES (%s, %s);"
        cursor.execute(insert_query, (username, cost))
        cnx.commit()

    # 处理所有结果
    cursor.fetchall()

    # 关闭游标和连接
    cursor.close()
    cnx.close()


def lastchange(username, kind):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()

    # 查询记录
    select_query = "SELECT last FROM user WHERE username = %s;"
    cursor.execute(select_query, (username,))
    result = cursor.fetchone()

    # 更新 last 属性
    if result:
        last_data = json.loads(result[0])
        last_data.append(kind)

        # 如果列表长度大于 5，则移除第一个元素
        if len(last_data) > 5:
            last_data = last_data[1:]

        # 更新记录
        update_query = "UPDATE user SET last = %s WHERE username = %s;"
        cursor.execute(update_query, (json.dumps(last_data), username))
        cnx.commit()
    else:
        # 如果用户记录不存在，则创建新记录
        insert_query = "INSERT INTO user (username, last) VALUES (%s, %s);"
        cursor.execute(insert_query, (username, json.dumps([kind])))
        cnx.commit()

    # 处理所有结果
    cursor.fetchall()

    # 关闭游标和连接
    cursor.close()
    cnx.close()


def getlast(username):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()

    # 查询记录
    select_query = "SELECT last FROM user WHERE username = %s;"
    cursor.execute(select_query, (username,))
    result = cursor.fetchone()
    if result:
        json_list = json.loads(result[0])
    else:
        json_list = []
    cursor.close()
    cnx.close()
    return json_list


def getstar(username):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()

    # 查询记录
    select_query = "SELECT star FROM user WHERE username = %s;"
    cursor.execute(select_query, (username,))
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
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()

    # 更新记录
    update_query = "UPDATE user SET password = %s WHERE username = %s;"
    cursor.execute(update_query, (newmi, user))
    cnx.commit()

    # 获取更新后的数据
    select_query = "SELECT star, last, cost, password FROM user WHERE username = %s;"
    cursor.execute(select_query, (user,))
    result = cursor.fetchone()

    if result is not None:
        star_list = json.loads(result[0])
        last = result[1]
        cost = result[2]
        password = result[3]

        # 关闭游标和连接
        cursor.close()
        cnx.close()

        data = {
            'star': star_list,
            'last': last,
            'cost': cost,
            'password': password
        }
        return data
    else:
        # 关闭游标和连接
        cursor.close()
        cnx.close()
        return None


def changename(username, newname):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()

    # 更新记录
    update_query = "UPDATE user SET username = %s WHERE username = %s;"
    cursor.execute(update_query, (newname, username))
    cnx.commit()

    # 获取更新后的数据
    select_query = "SELECT star, last, cost, password FROM user WHERE username = %s;"
    cursor.execute(select_query, (newname,))
    result = cursor.fetchone()

    if result is not None:
        star_list = json.loads(result[0])
        last = result[1]
        cost = result[2]
        password = result[3]

        # 关闭游标和连接
        cursor.close()
        cnx.close()

        data = {
            'star': star_list,
            'last': last,
            'cost': cost,
            'password': password
        }
        return data
    else:
        # 关闭游标和连接
        cursor.close()
        cnx.close()
        return None


def changestar(username, food):
    list = food.split('-')
    food_name = list[0]
    count_name = list[1]
    house_name = list[2]
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()
    rev_food = house_name+'-'+count_name+'-'+food_name
    # 获取当前记录的星级数据
    select_query = "SELECT star FROM user WHERE username = %s;"
    cursor.execute(select_query, (username,))
    result = cursor.fetchone()

    if result is not None:
        star_list = json.loads(result[0])
        # 从星级数据列表中删除指定项
        if rev_food in star_list:
            star_list.remove(rev_food)

        # 更新记录
        update_query = "UPDATE user SET star = %s WHERE username = %s;"
        cursor.execute(update_query, (json.dumps(star_list), username))
        cnx.commit()
        update_query = "UPDATE 学二 SET 收藏人数 = 收藏人数 - 1 WHERE 食堂 = %s AND 档口 = %s AND 菜名 = %s;"
        update_params = (house_name, count_name, food_name)
        cursor.execute(update_query, update_params)
        cnx.commit()
        # 关闭游标和连接
    cursor.close()
    cnx.close()





def del_comment(canteen, stall, dish, comment_str):
    # 连接到数据库
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()

    # 查询要更新评论的评论项
    sql_query = "SELECT comments FROM 学二 WHERE 食堂 = %s AND 档口 = %s AND 菜名 = %s"
    cursor.execute(sql_query, (canteen, stall, dish))
    result = cursor.fetchone()

    if result:
        # 将数据库中的评论项转换为 Python 对象
        comments = json.loads(result[0])
        print("当前评论项：", comments)

        # 查找并删除列表中第一个匹配的评论字符串
        updated_comments = []
        deleted = False
        for item in comments:
            if item != comment_str or deleted:
                updated_comments.append(item)
            else:
                deleted = True

        if deleted:
            # 更新数据库中的评论项
            updated_comments_json = json.dumps(updated_comments)
            sql_update = "UPDATE 学二 SET comments = %s WHERE 食堂 = %s AND 档口 = %s AND 菜名 = %s"
            cursor.execute(sql_update, (updated_comments_json, canteen, stall, dish))
            cnx.commit()
            print("评论项已成功更新！")
        else:
            print("找不到要删除的评论字符串。")
    else:
        print("找不到符合条件的评论项。")

    # 关闭数据库连接
    cursor.close()
    cnx.close()


def delAll_user():
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()
    sql_query = "GRANT DELETE ON hangeat.user TO 'root'@'chlience.cn';"
    cursor.execute(sql_query)
    cnx.commit()  # 提交事务
    cursor.close()  # 关闭游标
    cnx.close()  # 关闭数据库连接

def addrank(username, food,count, house, score):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat', charset='utf8')
    cursor = cnx.cursor()

    # 查询记录
    select_query = "SELECT 评分 FROM user WHERE username = %s"
    cursor.execute(select_query, (username,))
    result = cursor.fetchone()
    info= house+'-'+count+'-'+food
    score_dict = json.loads(result[0])
    # print(type(score_dict))
    # print(score_dict)
    # print(info)
    # last_score = score_dict.get(info, -1)
    score_dict[info] = score
    new_score_json = json.dumps(score_dict)
    # 将查询结果转换为列表形式
    update_query = "UPDATE user SET 评分=%s WHERE username=%s"
    cursor.execute(update_query, (new_score_json, username))

    select_query = "SELECT 评分人数, 评分 FROM 学二 WHERE 食堂 = %s AND 档口 = %s AND 菜名 = %s"
    cursor.execute(select_query, (house, count, food))
    result = cursor.fetchone()
    if result:
        num_ratings = result[0]
        ave_score = result[1]
        ave_score = (ave_score*num_ratings + score) / (num_ratings+1)
        num_ratings += 1
        ave_score = round(ave_score, 2)
        update_query = "UPDATE 学二 SET 评分人数 = %s, 评分 = %s WHERE 食堂 = %s AND 档口 = %s AND 菜名 = %s"
        cursor.execute(update_query, (num_ratings, ave_score, house, count, food))
    cnx.commit()
    cursor.close()
    cnx.close()

def getrank(user, food, count, house):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()
    select_query = "SELECT 评分 FROM user WHERE username = %s"
    cursor.execute(select_query, (user))
    result = cursor.fetchone()
    info = house + '-' + count + '-' + food
    score_dict = json.loads(result[0])
    result = score_dict.get(info, -1)
    cursor.close()
    cnx.close()
    return result

def add_comment(text, house, count, food):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat', charset='utf8')
    cursor = cnx.cursor()
    # 查询记录
    select_query = "SELECT comments FROM 学二 WHERE 食堂 = %s AND 档口 = %s AND 菜名 = %s"
    cursor.execute(select_query, (house,count,food))
    result = cursor.fetchone()
    score_list = json.loads(result[0])
    score_list.insert(0, text)
    comment_json = json.dumps(score_list)
    # 将查询结果转换为列表形式
    sql_update = "UPDATE 学二 SET comments = %s WHERE 食堂 = %s AND 档口 = %s AND 菜名 = %s"
    update_values = (comment_json, house, count, food)
    cursor.execute(sql_update, update_values)
    cnx.commit()
    cursor.close()
    cnx.close()

def loadcomment(house_name, count_name, food_name):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat', charset='utf8')
    cursor = cnx.cursor()
    # 选择数据库
    sql_query = "SELECT comments FROM 学二 WHERE 食堂 = %s AND 档口 = %s AND 菜名 = %s"
    values = (house_name, count_name, food_name)
    cursor.execute(sql_query, values)
    result = cursor.fetchone()  # 获取查询结果
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
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()

    # 查询数据库中对应项的评论列
    sql_query = "SELECT comments FROM 学二 WHERE 食堂 = %s AND 档口 = %s AND 菜名 = %s"
    values = (house_name, count_name, food_name)

    cursor.execute(sql_query, values)
    result = cursor.fetchone()

    if result is not None and result[0] is not None:
        existing_comments = json.loads(result[0])
        existing_comments += comments
        comments_json = json.dumps(existing_comments)

    # 更新数据库中对应项的评论列
    sql_update = "UPDATE 学二 SET comments = %s WHERE 食堂 = %s AND 档口 = %s AND 菜名 = %s"
    update_values = (comments_json, house_name, count_name, food_name)

    cursor.execute(sql_update, update_values)
    cnx.commit()

    # 关闭数据库连接
    cursor.close()
    cnx.close()

def get_top_scores(user):
    cnx = pymysql.connect(user='hangeat', password='hangeat_mysql',
                          host='chlience.cn', database='hangeat')
    cursor = cnx.cursor()

    select_query = "SELECT 评分 FROM user WHERE username = %s"
    cursor.execute(select_query, (user))
    result = cursor.fetchone()
    st = result[0]
    score_dict = json.loads(result[0])
    scores = list(zip(score_dict.keys(), score_dict.values()))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    top_scores = sorted_scores[:20]

    cursor.close()
    cnx.close()

    return top_scores
