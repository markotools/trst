import sqlite3,json,random
class conect_data:
    def __init__(self,filename):
        self.file_name = filename
    def read(self):
        return json.loads(open(self.file_name).read())
    def list_append(self,user,indent=4):
        file = json.loads(open(self.file_name).read())
        file.append(user)
        new = json.dumps(file,indent=indent)
        open(self.file_name,"w").write(new)
        return True
    def list_remove(self,user,indent=4):
        file = json.loads(open(self.file_name).read())
        file.remove(user)
        new = json.dumps(file,indent=indent)
        open(self.file_name,"w").write(new)
        return True
    def dict_append(self,user,indent=4):
        file = json.loads(open(self.file_name).read())
        file.update(user)
        new = json.dumps(file,indent=indent)
        open(self.file_name,"w").write(new)
        return True
    def dict_remove(self,user,indent=4):
        file = json.loads(open(self.file_name).read())
        file.pop(user)
        new = json.dumps(file,indent=indent)
        open(self.file_name,"w").write(new)
        return True

def denum(coin):
    return str(coin).replace("0","0️⃣").replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣")
le = ["😚😝","🤨😮","😑😁","☺️😋","😣😴","😴😖","😖🤑"]
def text_home(id,name,coin):
    return f"""ـ أهلا بك عزيزي : [{name}](tg://user?id={id})

اجمع النقاط ثم أطلب الأعضاء {random.choice(le)}

  عدد نقاطك  : *{coin}*

🆔 : `{id}`"""

class UserData:
    def __init__(self,id):
        self.id = id
        try:
            info = self.getData()
            self.name = info["name"]
            self.username = info["username"]
            self.coin = info["coin"]
            self.coinpass = info["coinpass"]
            self.isDand = info["isDand"]
            self.isLoginAsia = info["isLoginAsia"]
            self.phone = info["phone"]
            self.access_token = info["access_token"]
            self.gift = info["gift"]
        except:pass
    def verification(self):
        mydb = sqlite3.connect("databeas.db")
        sql = f"SELECT * FROM users WHERE id='{self.id}'"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        file = mycursor.fetchall()
        print(file)
        if len(file) > 0:
            return True
        else:
            return False
    def getData(self):
        mydb = sqlite3.connect("databeas.db")
        sql = f"SELECT * FROM users WHERE id='{self.id}'"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        file = mycursor.fetchall()
        for d in file:
            c = str(d[3]).split(".")[0] +"."
            if len(str(d[3]).split(".")[1]) >4:
                c+=str(d[3]).split(".")[1][:4]
            else:
                c+=str(d[3]).split(".")[1]
            data = {
            "id":d[0],
            "name":d[1],
            "username":d[2],
            "coin":c,
            "coinpass":d[4],
            "isDand":d[5] == "yes",
            "isLoginAsia": d[6] == "yes",
            "phone":d[7],
            "access_token":d[8],
            "gift":d[9]}
            return data
    def addUser(self,name,username,coin,coinpass,isDand,isLoginAsia,phone,access_token):
        mydb = sqlite3.connect("databeas.db")
        req = mydb.cursor()
        sql = f"INSERT INTO users(id,name,username,coin,coinpass,isDand,isLoginAsia,phone,access_token,gift) VALUES('{self.id}','{name}','{username}','{coin}','{coinpass}','{isDand}','{isLoginAsia}','{phone}','{access_token}','')"
        req.execute(sql)
        sql = f"INSERT INTO your_referrals(id,ids) VALUES('{self.id}','')"
        req.execute(sql)
        mydb.commit()
        return True
    def Trind(self):
        b = []
        h = []
        d = []
        mydb = sqlite3.connect("databeas.db")
        sql = f"SELECT * FROM your_referrals"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        data = mycursor.fetchall()
        for i in range(len(data)):
            b.append(int(len(data[i][1].strip().split("-"))))
        for j in range(len(b)):
            bmax = max(b)
            b.remove(bmax)
            h.append(bmax)
        for s in h:
            for k in range(len(data)):
                if int(len(data[k][1].strip().split("-"))) == int(s):
                    d.append({"id":str(data[k][0]),"your_referrals":str(s)})
                    if len(d) == 3:
                        return d
        return d
    def getYour_referrals(self):
        mydb = sqlite3.connect("databeas.db")
        sql = f"SELECT * FROM your_referrals WHERE id='{self.id}'"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return data[0][1]
    
    def updeatDB(self,tabel,key,value,keyIf=None,valueIf=None,isIf=None):
        mydb = sqlite3.connect("databeas.db")
        mycursor = mydb.cursor()
        if isIf:
            mycursor.execute(f"UPDATE {tabel} SET {key}='{value}' WHERE {keyIf}='{valueIf}'")
        else:
            mycursor.execute(f"UPDATE {tabel} SET {key}='{value}' WHERE id='{self.id}'")
        
        mydb.commit()
        return True
        
    def addOrder(self,id,link,cost,times,ranges,name,supplier,idservers):
        mydb = sqlite3.connect("databeas.db")
        req = mydb.cursor()
        idbot = GenPkBot()
        sql = f"INSERT INTO orders(id,idOrders,link,cost,range,name,time,idbot,supplier,idservers) VALUES('{self.id}','{id}','{link}','{cost}','{ranges}','{name}','{times}','{idbot}','{supplier}','{idservers}')"
        req.execute(sql)
        mydb.commit()
        return True
    def getJsonOrders(self):
        orders = []
        mydb = sqlite3.connect("databeas.db")
        sql = f"SELECT * FROM orders WHERE id='{self.id}'"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        data = mycursor.fetchall()
        if data == None or data == "None":
            return orders
        for j in data:
            orders.append(
                {
                    "id":j[0],
                    "idOrders":j[1],
                    "link":j[2],
                    "cost":j[3],
                    "range":j[4],
                    "name":j[5],
                    "time":j[6],
                    "idbot":[7],
                    "supplier":[8],
                    "idservers":[9]
                }
            )
        return orders
def isCode(code):
    mydb = sqlite3.connect("databeas.db")
    sql = f"SELECT * FROM codes WHERE code='{code}'"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    file = mycursor.fetchall()
    if file == []:
        return False
    else:
        return file[0]
def idCodeAdd(code,id):
    s = isCode(code)
    users = s[2]
    users+=f"{id}-"
    number = int(s[4])
    number = number-1
    if number <= 0:
        ok = "no"
    else:
        ok = "ok"
    mydb = sqlite3.connect("databeas.db")
    mycursor = mydb.cursor()
    mycursor.execute(f"UPDATE codes SET users='{users}' WHERE code='{code}'")
    mycursor.execute(f"UPDATE codes SET number='{number}' WHERE code='{code}'")
    mycursor.execute(f"UPDATE codes SET isOk='{ok}' WHERE code='{code}'")
    mydb.commit()
    return True
def addAsia(id,phone,coin,coin_new,times):
    mydb = sqlite3.connect("databeas.db")
    req = mydb.cursor()
    sql = f"INSERT INTO asia(id,phone,coin,coin_new,time) VALUES('{id}','{phone}','{coin}','{coin_new}','{times}')"
    req.execute(sql)
    mydb.commit()
    return True

def AddCodeGift(code,coin,number):
    mydb = sqlite3.connect("databeas.db")
    req = mydb.cursor()
    sql = f"INSERT INTO codes(code,coin,users,isOk,number) VALUES('{code}','{coin}','','ok','{number}')"
    req.execute(sql)
    mydb.commit()
    return True

def DisCodeGift(code):
    mydb = sqlite3.connect("databeas.db")
    mycursor = mydb.cursor()
    mycursor.execute(f"UPDATE codes SET isOk='no' WHERE code='{code}'")
    mydb.commit()
    return True

def getListServers(type,server):
    d = json.loads(open("list.json",encoding='utf-8').read())[type][server]
    return d

def addListServers(type,server,data):
    h = getListServers(type,server)
    h.append(data)
    k = json.loads(open("list.json",encoding='utf-8').read())
    k[type][server] = h
    new = json.dumps(k,indent=4)
    with open("list.json","w",encoding='utf-8') as file:
        file.write(new)
        file.close()
    return True
def getServer(type,server,id):
    d = getListServers(type,server)
    for i in d:
        if str(i["id"]) == str(id):
            return i
    return {}

class getSettingsBotJson:
   def __init__(self):
       s = self._getSettingsBotJson()
       self.payments_phone_number = str(s["payments_phone_number"])
       self.ownerid = str(s["ownerid"])
       self.referral_balance = str(s["referral_balance"])
       self.gift_balance = str(s["gift_balance"])
       self.send_users = s["send_users"]
       self.isbot = s["is_bot"]
   def updeta(self,key,value):
       mydb = sqlite3.connect("databeas.db")
       mycursor = mydb.cursor()
       mycursor.execute(f"UPDATE settings SET {key}='{value}'")
       mydb.commit()
   def _getSettingsBotJson(self):
        mydb = sqlite3.connect("databeas.db")
        sql = f"SELECT * FROM settings"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        file = mycursor.fetchall()
        data = file[0]
        return {
    "payments_phone_number":data[0],
    "ownerid":data[1],
    "referral_balance":data[2],
    "gift_balance":data[3],
    "send_users":str(data[4]) == "1",
    "is_bot":str(data[5]) == "1"
    }



def textnewuser(id,name,username):
    if str(username) == "None":
        user = "لايوجد"
    else:
        user = "@"+str(username)
    mydb = sqlite3.connect("databeas.db")
    sql = f"SELECT * FROM users"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    file = mycursor.fetchall()
    h = len(file)
    return f"""
*٭ تم دخول شخص جديد الى البوت الخاص بك 👾*
            -----------------------
• معلومات العضو الجديد .

• الاسم : [{name}](tg://user?id={id})
• المعرف : {user}
• الايدي : `{id}`
            -----------------------
*• عدد الاعضاء الكلي : {h}*
    """

def getUsersIdsBot():
    ids = []
    mydb = sqlite3.connect("databeas.db")
    sql = f"SELECT * FROM users"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    file = mycursor.fetchall()
    for data in file:
        ids.append(data[0])
    return ids
def getAllServers():
    servers = {}
    d = json.loads(open("list.json",encoding='utf-8').read())
    for i in d:
        for l in d[i]:
            for k in d[i][l]:
                servers.update({k["id"]:k})
    return servers
def getInfoMyBotAll(tim=None):
    lenUsers = str(len(getUsersIdsBot()))
    mydb = sqlite3.connect("databeas.db")
    sql = f"SELECT * FROM orders"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    file = mycursor.fetchall()
    bn = 0
    ssf = getAllServers()
    for i in file:
        if tim == None:
            bn+=(int(ssf[str(i[9])]["profit"])/1000) * int(i[4])
        else:
            if tim in str(i[7]):
                bn+=(int(ssf[str(i[9])]["profit"])/1000) * int(i[4])
    lenOrders = len(file)
    mydb = sqlite3.connect("databeas.db")
    sql = f"SELECT * FROM codes"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    file = mycursor.fetchall()
    lenCodes = len(file)
    mydb = sqlite3.connect("databeas.db")
    sql = f"SELECT * FROM asia"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    file = mycursor.fetchall()
    lenAsia = len(file)
    
    return f"""
عدد المستخدمين : {lenUsers} 👤

عدد الطلبات : {lenOrders} 🔔

عدد أكواد الهدية : {lenCodes} 🎁

عدد الشحن التلقائي (Asiacell) : {lenAsia} 💸

الربح الكلي للبوت : {bn} دينار عراقي 🇮🇶
"""

def GenPkBot():
    while True:
        code = "".join(random.choice("123456789")for _ in range(8))
        mydb = sqlite3.connect("databeas.db")
        sql = f"SELECT * FROM orders WHERE idbot='{code}'"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        file = mycursor.fetchall()
        if len(file) == 0:
            return code


