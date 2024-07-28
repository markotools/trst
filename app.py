from telebot import TeleBot
from telebot.types import InlineKeyboardButton as Button
from telebot.types import InlineKeyboardMarkup as Markup
import time,os,json,requests,random
import sqlite3,json,random
from threading import Thread
import datetime
from concurrent.futures import ThreadPoolExecutor
from captcha.image import ImageCaptcha
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
  return "<b> hello</b>"

def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()


def GenImageCaptcha():
    token = "token="
    token+= ''.join(random.choice('0123456789') for _ in range(4))
    token+="-"
    token+= ''.join(random.choice('0123456789') for _ in range(4))
    token+="-"
    token+= ''.join(random.choice('0123456789') for _ in range(4))
    token+="-"
    token+= ''.join(random.choice('0123456789') for _ in range(4))
    captcha_text = ''.join(random.choice('0123456789') for _ in range(4))
    image = ImageCaptcha()
    data = image.generate(captcha_text)
    image.write(captcha_text, f'tokens/{token}.png')
    mydb = sqlite3.connect("databeas.db")
    reqdb = mydb.cursor()
    sql = f"INSERT INTO tokens(token,code) VALUES('{token}','{captcha_text}')"
    reqdb.execute(sql)
    mydb.commit()
    return str(token)


class getSettingsBotJson:
   def __init__(self):
       s = self._getSettingsBotJson()
       self.payments_phone_number = str(s["payments_phone_number"])
       self.ownerid = str(s["ownerid"])
       self.referral_balance = str(s["referral_balance"])
       self.gift_balance = str(s["gift_balance"])
       self.send_users = s["send_users"]
       self.isbot = s["is_bot"]
       self.subscription_points = int(s["subscription_points"])
       self.finance_points = int(s["finance_points"])
       self.sunday_points_finance = int(s["sunday_points_finance"])
       self.isproofs = int(s["isproofs"])
       self.proofs = int(s["proofs"])
       self.price_points = int(s["price_points"])
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
    "is_bot":str(data[5]) == "1",
    "subscription_points":data[6],
    "finance_points":data[7],
    "sunday_points_finance":data[8],
    "isproofs":data[9],
    "proofs":data[10],
    "price_points":data[11]
    
    }



token = "1998437062:AAEtpjoOWfuDdZVGmDh8VRPGZMrJM1a7KvI"
settings = getSettingsBotJson()
usernamebot = "QHObot"
linkCanelGiftCode = "https://t.me/FlachChannel"
LinkMe = "https://t.me/QQQQQQ2"
bot = TeleBot(token=token)
Flash = "https://t.me/FlachChannel"







class conect_data:
    def __init__(self,filename):
        self.file_name = filename
    def read(self):
        return json.loads(open(self.file_name,encoding='utf-8').read())
    def list_append(self,user,indent=4):
        file = json.loads(open(self.file_name,encoding='utf-8').read())
        file.append(user)
        new = json.dumps(file,indent=indent)
        open(self.file_name,"w",encoding='utf-8').write(new)
        return True
    def list_remove(self,user,indent=4):
        file = json.loads(open(self.file_name,encoding='utf-8').read())
        file.remove(user)
        new = json.dumps(file,indent=indent)
        open(self.file_name,"w",encoding='utf-8').write(new)
        return True
    def dict_append(self,user,indent=4):
        file = json.loads(open(self.file_name,encoding='utf-8').read())
        file.update(user)
        new = json.dumps(file,indent=indent)
        open(self.file_name,"w",encoding='utf-8').write(new)
        return True
    def dict_remove(self,user,indent=4):
        file = json.loads(open(self.file_name,encoding='utf-8').read())
        file.pop(user)
        new = json.dumps(file,indent=indent)
        open(self.file_name,"w",encoding='utf-8').write(new)
        return True

def IsTokenFromID(id):
    mydb = sqlite3.connect("databeas.db")
    sql = f"SELECT * FROM istoken WHERE id='{id}'"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    file = mycursor.fetchall()
    return len(file) > 0

def GetCodeFromToken(Token):
    mydb = sqlite3.connect("databeas.db")
    sql = f"SELECT * FROM tokens WHERE token='{Token}'"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    file = mycursor.fetchall()
    return str(file[0][1])
def UpdeatCaptchaLogin(id):
    mydb = sqlite3.connect("databeas.db")
    reqdb = mydb.cursor()
    sql = f"INSERT INTO istoken(id,iss) VALUES('{id}','1')"
    reqdb.execute(sql)
    mydb.commit()
def DeletImageCaptach(token):
    mydb = sqlite3.connect("databeas.db")
    req = mydb.cursor()
    sql = f"DELETE FROM tokens WHERE token='{token}' "
    req.execute(sql)
    mydb.commit()
    try:os.remove(f"tokens/{token}.png")
    except:pass 

class UserData:
    def __init__(self,id):
        self.id = str(id)
        try:
            info = self.getData()
            self.name = info["name"]
            self.username = info["username"]
            self.coin = int(str(info["coin"]))
            self.coinpass = int(str(info["coinpass"]))
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
            c = str(d[3])
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
    def addUser(self,id,name,username,coin,coinpass,isDand,isLoginAsia,phone,access_token):
        mydb = sqlite3.connect("databeas.db")
        req = mydb.cursor()
        sql = f"INSERT INTO users(id,name,username,coin,coinpass,isDand,isLoginAsia,phone,access_token,gift) VALUES('{id}','{name}','{username}','{coin}','{coinpass}','{isDand}','{isLoginAsia}','{phone}','{access_token}','')"
        req.execute(sql)
        sql = f"INSERT INTO your_referrals(id,ids) VALUES('{id}','')"
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
                    "idbot":j[7],
                    "supplier":j[8],
                    "idservers":j[9]
                }
            )
        return orders
    def AddRequest(self,data):
        mydb = sqlite3.connect("databeas.db")
        req = mydb.cursor()
        idbot = GenPkBot()
        sql = f"INSERT INTO requests(user_id,id,username,name,link,required_number,remaining_number,condition,order_date,expiry_date,fixed) VALUES('{self.id}','{data['id']}','{data['username']}','{data['name']}','{data['link']}','{data['required_number']}','{data['remaining_number']}','{data['condition']}','{data['order_date']}','{data['expiry_date']}','{data['fixed']}')"
        req.execute(sql)
        mydb.commit()
        return True
    def GetAccountsFollow(self):
        lists = []
        mydb = sqlite3.connect("databeas.db")
        sql = f"SELECT * FROM subscribers WHERE id='{self.id}'"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        file = mycursor.fetchall()
        for i in file:
            lists.append(str(i[1]))
        return lists
    def GetSkipChannels(self):
        lists = []
        mydb = sqlite3.connect("databeas.db")
        sql = f"SELECT * FROM skip_channels WHERE user_id='{self.id}'"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        file = mycursor.fetchall()
        for i in file:
            lists.append(str(i[1]))
        return lists
    def GetReportingChannels(self):
        lists = []
        mydb = sqlite3.connect("databeas.db")
        sql = f"SELECT * FROM reporting_channels WHERE user_id='{self.id}'"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        file = mycursor.fetchall()
        for i in file:
            lists.append(str(i[1]))
        return lists
    def GetRequestsChannels(self):
        lists = []
        mydb = sqlite3.connect("databeas.db")
        sql = f"SELECT * FROM requests WHERE user_id='{self.id}'"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        file = mycursor.fetchall()
        for i in file:
            lists.append({
            "user_id":str(i[0]),
            "id":str(i[1]),
            "username":str(i[2]),
            "name":str(i[3]),
            "link":str(i[4]),
            "required_number":str(i[5]),
            "remaining_number":str(i[6]),
            "condition":str(i[7]),
            "order_date":str(i[8]),
            "expiry_date":str(i[9]),
            "fixed":str(i[10])
            })
        return lists
    
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
def denum(coin):
    return str(coin).replace("0","0️⃣").replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣")
le = ["😚😝","🤨😮","😑😁","☺️😋","😣😴","😴😖","😖🤑"]
def text_home(id,name,coin):
    return f"""*ـ أهلا بك عزيزي :* [{name}](tg://user?id={id})

*اجمع النقاط ثم أطلب الأعضاء {random.choice(le)}*

*يمكنك التمتع بكافة الخدمات الموجودة في البوت بأسعار مميزة ومنافسة للسوق مع ضمان الجودة والسرعة*

- عدد نقاطك  : *{coin}* ⭐

🆔 : `{id}`"""

def text_send_follw_done(db):
    info = db
    name_ch = info["name"]
    link = info["link"]
    required_number = info["required_number"]
    remaining_number = info["remaining_number"]
    return f"""
*• شترك شخص جديد في قناتك :* [{name_ch}]({link})
*- العدد المطلوب* {required_number} *عضو*
*- العدد المتبقي* {remaining_number} *عضو* 🚸
"""

def text_done_sned(link,r):
    return f"""
• تم نتهاء تمويل قناة : 
{link}

العدد المطلوب : {r}
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
            bn+=(float(str(i[9]).split("/")[1])/1000) * int(i[4])
        else:
            if tim == str(i[6]):
                bn+=(float(str(i[9]).split("/")[1])/1000) * int(i[4])
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
    
    return f"""*عدد المستخدمين : {lenUsers} 👤

عدد الطلبات : {lenOrders} 🔔

عدد أكواد الهدية : {lenCodes} 🎁

عدد الشحن التلقائي (Asiacell) : {lenAsia} 💸

الربح الكلي للبوت : {bn} دينار عراقي 🇮🇶
*"""

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



def text_send_follw(coin):
    coin = int(coin)
    f = int(settings.finance_points)
    return f"""*لديك : {coin} نقطة 💰

سعر العضو : {f} نقطة ⭐

يمكنك تمويل : {int(coin/f)} عضو 👥

او أرسال العدد المطلوب 📩
    *"""

def text_send_follw_else(coin):
    coin = int(coin)
    r = settings.sunday_points_finance
    return f"""*لديك : {coin} نقطة 💰

يجب عليك تجميع اكثر من {r} نقطة  حتى تستطيع تمويل أعضاء 👥➕
    *"""



def text_send_order_coin(coin):
    coin = int(coin)
    f = settings.finance_points
    return f"""*لديك : {coin} نقطة 🌱

سعر العضو : {f} نقطة ⭐

يجب أن يكون العدد أقل من {int(coin/f)} عضو 👥

أرسل العدد ألمطلوب لبدء التمويل 📩
    *"""
def text_get_send_order_coin():
    return """*❇️  خطوات تمويل  ❇️

1- يجب عليك رفع البوت ادمن في القناة المراد تمويله ⚙️ 🤖

2 - يجب عليك أرسل توجيه من القناة المراد تمويله 🔄 
 
 ملاحضة 
أذا لم تعطي البوت صلاحية الادمن سوفة يمهل تمويلك وتخصم نقاطك
 *"""
def text_get_num_send(coin,num,e):
    return f"""*جاري تمويل قناتك بنجاح 👥✅

عدد المتابعين المطلوب : {num} 👥

تم أستقطاع : {e} نقطة 💰

أصبح عدد نقاطك : {int(coin)-e} نقطة 💰

للمزيد أضغط على طلباتي 🔔

اذا حذفت البوت من قائمة المدراء سوفة يمهل تمويلك وتخصم نقاطك ⚓
    *"""

def GetAllRequests(ids=False,target=False):
    lists = []
    ids = []
    mydb = sqlite3.connect("databeas.db")
    sql = f"SELECT * FROM requests"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    file = mycursor.fetchall()
    for i in file:
        dt = {
                "user_id":str(i[0]),
                "id":str(i[1]),
                "username":str(i[2]),
                "name":str(i[3]),
                "link":"{}".format(str(i[4])),
                "required_number":"{}".format(str(i[5])),
                "remaining_number":"{}".format(str(i[6])),
                "condition":str(i[7]),
                "order_date":str(i[8]),
                "expiry_date":str(i[9]),
                "fixed":str(i[10])
        }
        if str(i[1]) == target and str(i[7]) == "1" and int(i[6]) > 0:
            return dt
        lists.append(dt)
        ids.append(str(i[1]))
    if target == None:
        if ids == False:
            return lists
        else:
            return ids 
    return {}
def get_send_order_coin(message):
    id = str(message.chat.id)
    info = UserData(id)
    coin = int(info.coin)
    try:
        num = int(message.text)
        if  not num > 49:
            main = Markup()
            main.add(Button(text="رجوع ⬅️",callback_data="add-folowers"))
            bot.send_message(chat_id=id,text="عزيزي أقل تمويل يمكنك البدء به هو 50 عضو ⁉️",reply_markup=main,parse_mode="markdown")
            return False
        if num > int(int(coin)/int(settings.finance_points)):
            main = Markup()
            main.add(Button(text="رجوع ⬅️",callback_data="add-folowers"))
            bot.send_message(chat_id=id,text="عزيزي عدد نقاطك لايكفي ⁉️",reply_markup=main,parse_mode="markdown")
        else:
            main = Markup()
            main.add(Button(text="رجوع ⬅️",callback_data="add-folowers"))
            c = bot.send_message(chat_id=id,text=text_get_send_order_coin(),parse_mode="markdown",reply_markup=main)
            bot.register_next_step_handler(c,get_num_send,num)
    except Exception:
        main = Markup()
        main.add(Button(text="رجوع ⬅️",callback_data="add-folowers"))
        bot.send_message(chat_id=id,text="يجب أرسال ارقام فقط ⁉️",reply_markup=main,parse_mode="markdown")

def get_num_send(message,num):
    id = str(message.chat.id)
    info = UserData(id)
    coin = int(info.coin)
    jj = 0
    if not (message.forward_from_chat) == None:
        forward_from_chat = message.forward_from_chat
        if forward_from_chat.type == "channel":
            channel_id = str(forward_from_chat.id)
            r = requests.get("https://api.telegram.org/bot{}/getChatAdministrators?chat_id={}".format(token,channel_id)).json()["ok"]
            if r:
                pass
            else:
                main = Markup()
                main.add(Button(text="رجوع ⬅️",callback_data="add-folowers"))
                bot.send_message(chat_id=id,text="يجب رفع البوت ادمن في القناة ⁉️",reply_markup=main,parse_mode="markdown")
                return False
            if channel_id in GetAllRequests(True):
                if GetAllRequests(target=channel_id)["condition"] == "1" :
                    main = Markup()
                    main.add(Button(text="رجوع ⬅️",callback_data="add-folowers"))
                    bot.send_message(chat_id=id,text="القناة موجودة في تمويل \n أنتضر التمويل الاول يكتمل وبعده يمكنك تمويله مرة اخرة \n/start",reply_markup=main,parse_mode="markdown")
                    return True
            if True:
                channel_name = str(forward_from_chat.title)
                channel_username = forward_from_chat.username
                if channel_username == None:
                    channel_username = "لا يوجد"
                invite_link = str(bot.get_chat(chat_id=channel_id).invite_link)
                dt ={
                "id_send":id,
                "id":str(channel_id),
                "username":str(channel_username),
                "name":channel_name,
                "link":invite_link,
                "required_number":"{}".format(int(num)),
                "remaining_number":"{}".format(int(num)),
                "condition":"1",
                "order_date":time.strftime("%Y-%m-%d-%H:%M:%S"),
                "expiry_date":"لا يوجد",
                "fixed":"0"
                }
                e = int(num) * int(settings.finance_points)
                if coin >= e:
                    info.updeatDB(tabel="users",key="coin",value=str(int(coin)-int(e)))
                    info.AddRequest(dt)
                    main = Markup()
                    main.add(Button(text="🔔  طلباتي  🔔",callback_data="orders-server"))
                    main.add(Button(text="❇️  صفحة رئيسية  ❇️",callback_data="back"))
                    bot.reply_to(message=message,text=text_get_num_send(coin,num,e),parse_mode="markdown",reply_markup=main)
                else:
                    main = Markup()
                    main.add(Button(text="رجوع ⬅️",callback_data="add-folowers"))
                    bot.send_message(chat_id=id,text="عزيزي عدد نقاطك لايكفي ⁉️",reply_markup=main,parse_mode="markdown")
        else:
            main = Markup()
            main.add(Button(text="رجوع ⬅️",callback_data="add-folowers"))
            bot.send_message(chat_id=id,text="يجب ان يكون التمويل لقناة فقط ⁉️",reply_markup=main,parse_mode="markdown")
    else:
        main = Markup()
        main.add(Button(text="رجوع ⬅️",callback_data="add-folowers"))
        bot.send_message(chat_id=id,text="يجب أن يكون توجيه من قناة فقط ⁉️",reply_markup=main,parse_mode="markdown")

def AddChnalFixed(message):
    id = str(message.chat.id)
    jj = 0
    if not (message.forward_from_chat) == None:
        forward_from_chat = message.forward_from_chat
        if forward_from_chat.type == "channel":
            channel_id = str(forward_from_chat.id)
            r = requests.get("https://api.telegram.org/bot{}/getChatAdministrators?chat_id={}".format(token,channel_id)).json()["ok"]
            if r:
                pass
            else:
                main = Markup()
                main.add(Button(text="رجوع ⬅️",callback_data="adminall"))
                bot.send_message(chat_id=id,text="يجب رفع البوت ادمن في القناة ⁉️",reply_markup=main,parse_mode="markdown")
                return False
            try:
                fiex = GetAllRequests(target=channel_id)["fixed"]
                print(fiex)
                if fiex == "1" :
                    main = Markup()
                    main.add(Button(text="رجوع ⬅️",callback_data="adminall"))
                    bot.send_message(chat_id=id,text="القناة موجودة في تمويل \n أنتضر التمويل الاول يكتمل وبعده يمكنك تمويله مرة اخرة \n/start",reply_markup=main,parse_mode="markdown")
                    return True
            except:
                pass
            if True:
                channel_name = str(forward_from_chat.title)
                channel_username = forward_from_chat.username
                if channel_username == None:
                    channel_username = "لا يوجد"
                invite_link = str(bot.get_chat(chat_id=channel_id).invite_link)
                dt ={
                "id_send":id,
                "id":str(channel_id),
                "username":str(channel_username),
                "name":channel_name,
                "link":invite_link,
                "required_number":"1",
                "remaining_number":"1",
                "condition":"1",
                "order_date":time.strftime("%Y-%m-%d-%H:%M:%S"),
                "expiry_date":"لا يوجد",
                "fixed":"1"
                }
                info = UserData(id)
                info.AddRequest(dt)
                main = Markup()
                main.add(Button(text="رجوع ⬅️",callback_data="adminall"))
                bot.reply_to(message=message,text="*تم أضافة القناة في الاشتراك الاجباري ✅*",parse_mode="markdown",reply_markup=main)
                
        else:
            main = Markup()
            main.add(Button(text="رجوع ⬅️",callback_data="adminall"))
            bot.send_message(chat_id=id,text="يجب ان يكون التمويل لقناة فقط ⁉️",reply_markup=main,parse_mode="markdown")
    else:
        main = Markup()
        main.add(Button(text="رجوع ⬅️",callback_data="adminall"))
        bot.send_message(chat_id=id,text="يجب أن يكون توجيه من قناة فقط ⁉️",reply_markup=main,parse_mode="markdown")



def GetRequestChannel(id):
    id = str(id)
    db = UserData(id)
    acList = db.GetAccountsFollow()
    Skips = db.GetSkipChannels()
    Rps = db.GetReportingChannels()
    mydb = sqlite3.connect("databeas.db")
    sql = f"SELECT * FROM requests"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    file = mycursor.fetchall()
    for i in file:
        dt = {
                "user_id":str(i[0]),
                "id":str(i[1]),
                "username":str(i[2]),
                "name":str(i[3]),
                "link":"{}".format(str(i[4])),
                "required_number":"{}".format(str(i[5])),
                "remaining_number":"{}".format(str(i[6])),
                "condition":str(i[7]),
                "order_date":str(i[8]),
                "expiry_date":str(i[9]),
                "fixed":str(i[10])
        }
        if (int(dt["condition"]) == 1
            and not str(dt["id"]) in acList
            and not str(dt["id"]) in Skips
            and not str(dt["id"]) in Rps
            and int(dt["fixed"]) == 0
        ):
            js = requests.get("https://api.telegram.org/bot{}/getChatMember?chat_id={}&user_id={}".format(token,dt["id"],id)).json()
            if js["ok"]:
                status = js["result"]["status"]
                if not status in ["member","administrator","creator"]:
                    return dt
        if (int(dt["condition"]) == 1
            and not str(dt["id"]) in acList
            and not str(dt["id"]) in Skips
            and not str(dt["id"]) in Rps
            and int(dt["fixed"]) == 1
        ):
            js = requests.get("https://api.telegram.org/bot{}/getChatMember?chat_id={}&user_id={}".format(token,dt["id"],id)).json()
            if js["ok"]:
                status = js["result"]["status"]
                if not status in ["member","administrator","creator"]:
                    return dt
        pass


def get_50Data(data,ko=None):
    r = 0
    rt = []
    m = []
    for i in data:
        m.append(data.index(i))
    d = []
    for i in range(len(m)):
        f = max(m)
        d.append(f)
        m.remove(f)
    for n in d:
        rt.append(data[n])
        r+=1
        if ko == None:
            if r == 50:
                return rt
        else:
            if r == ko:
                return rt
    return rt


def GetKeyFromApi(api):
    mydb = sqlite3.connect("databeas.db")
    sql = f"SELECT * FROM apis WHERE api='{api}'"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    file = mycursor.fetchall()
    return str(file[0][1])

def GetLenAllServers():
    api = "https://smmgen.com/"
    #r = requests.get(api).text
    return '465889'

ListsRamCheack = []
@bot.message_handler(commands=["admin"])
def add(m):
    id = str(m.chat.id)
    settings = getSettingsBotJson()
    if id == settings.ownerid:
        m = Markup()
        if settings.isbot:t="حالة البوت : ✅"
        else:t="حالة البوت : ❌"
        if settings.send_users:s="اشعارات الدخول : ✅"
        else:s="اشعارات الدخول : ❌"
        A = Button(text=t,callback_data="adminisbot")
        B = Button(text=s,callback_data="adminissend")
        m.add(A,B)
        C = Button(text="قسم الاشتراك الاجباري",callback_data="adminchnel")
        D = Button(text="قسم الادمنية",callback_data="adminadmins")
        m.add(C,D)
        E = Button(text="قسم الاذاعة",callback_data="adminhi")
        F = Button(text="قسم الاحصائيات",callback_data="adminusers")
        m.add(E,F)
        G = Button(text="• اعدادات بوت الرشق •",callback_data="adminall")
        m.add(G)
        text = "• اهلا بك في لوحه الأدمن الخاصه بالبوت 🤖\n- يمكنك التحكم في البوت الخاص بك من هنا\n~~~~~~~~~~~~~~~~~"
        bot.send_message(chat_id=settings.ownerid,text=text,reply_markup=m)
        


@bot.message_handler(commands=["start"])
def start(message):
    try:bot.clear_step_handler(message=message)
    except:pass
    settings = getSettingsBotJson()
    id = str(message.chat.id)
    if settings.isbot == False and not id == settings.ownerid:
        bot.send_message(chat_id=id,text="البوت مغلق للصيانة")
        return 
    name = str(message.chat.first_name)
    username = str(message.chat.username)
    text = str(message.text)
    UserDB = UserData(id)
    for chn in json.loads(open("channel.json",encoding='utf-8').read()):
        js = requests.get("https://api.telegram.org/bot{}/getChatMember?chat_id={}&user_id={}".format(token,chn["id"],id)).json()
        if js["ok"]:
            status = js["result"]["status"]
            print(status)
            if not status in ["member","administrator","creator"]:
                main = Markup()
                main.add(Button(text="الدخول الى القناة ✅",url=chn["url"]))
                main.add(Button(text="تحقق من الاشتراك ♻️",callback_data="back"))
                text = "يرجى الاشتراك في القناة لكي يعمل البوت \n\n1 - اضغط على دخول الى القناة \n2- قم بلشتراك في القناة \n3 - اضغط على تحقق من الاشتراك \n\n وسوفة يعمل لبوت"
                bot.send_message(chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
                return False
    if UserDB.verification():
        coin = UserDB.coin
        text = text_home(id,name,coin)
        if UserDB.isDand:
            bot.send_message(chat_id=id,text="تم حظرك من لبوت بسبب مخالفة الشروط 🚷")
            return False 
        main = Markup()
        A = Button(text="تجميع نقاط ➕",callback_data="add-coin")
        B = Button(text="قسم الطلبات 🔔",callback_data="orders")
        C = Button(text="💎 قسم الخدمات 💎",callback_data="server")
        D = Button(text="تحويل نقاط 📤",callback_data="send-coin")
        E = Button(text="معلومات حسابي 💳",callback_data="info-my")
        F = Button(text="💰 شحن حسابي تلقائي 💰",callback_data="asiacell")
        G = Button(text="تمويل قناة حقيقي 👤",callback_data="add-folowers")
        main.add(C)
        main.add(A,B)
        main.add(G)
        main.add(D,E)
        main.add(F)
        main.add(Button(text="- قناة بوت فلاش الرسمية ⚡",url=Flash))
        bot.send_message(chat_id=id,text=text,parse_mode="markdown",reply_markup=main)
    else:
        if IsTokenFromID(id) == False:
            Token = GenImageCaptcha()
            m = bot.send_photo(chat_id=id,photo=open(f"tokens/{Token}.png","rb"),caption="يرجى كتابة الكود الموجود في ألاعلى 👆\nوقم بأرسله ألى البوت ليتحقق من أنك أنسان",parse_mode="markdown")
            bot.register_next_step_handler(m,DefCheckCaptcha,Token,text)
            return 
        if "ref" in text:
            kk = settings.referral_balance
            try:
                idT = text.replace("/start ref","").strip()
                target = UserData(idT)
                me = str(target.getYour_referrals()).strip()
                if True:
                    me+=f"{id}-"
                    new = str(int(target.coin)+int(kk))
                    Lt = len(me.strip().split("-"))-1
                    target.updeatDB(tabel="your_referrals",key="ids",value=me)
                    target.updeatDB(tabel="users",key="coin",value=new)
                    text = f"*لقد دعوت : *[{name}](tg://user?id={id})\n*اصبح رصيدك : {new} 💰\nعدد دعواتك : {Lt} 👤*"
                    bot.send_message(chat_id=idT,text=text,parse_mode="markdown")
            except Exception as e:
                print(e)
        add = UserDB.addUser(id=id,name=name,username=username,coin="0",coinpass="0",isDand="no",isLoginAsia="no",phone="",access_token="")
        UserDB = UserData(id)
        coin = UserDB.coin
        text = text_home(id,name,coin)
        if settings.send_users:
            bot.send_message(chat_id=settings.ownerid,text=textnewuser(id,name,username),parse_mode="markdown")
        main = Markup()
        A = Button(text="تجميع نقاط ➕",callback_data="add-coin")
        B = Button(text="قسم الطلبات 🔔",callback_data="orders")
        C = Button(text="💎 قسم الخدمات 💎",callback_data="server")
        D = Button(text="تحويل نقاط 📤",callback_data="send-coin")
        E = Button(text="معلومات حسابي 💳",callback_data="info-my")
        F = Button(text="💰 شحن حسابي تلقائي 💰",callback_data="asiacell")
        G = Button(text="تمويل قناة حقيقي 👤",callback_data="add-folowers")
        main.add(C)
        main.add(A,B)
        main.add(G)
        main.add(D,E)
        main.add(F)
        main.add(Button(text="- قناة بوت فلاش الرسمية ⚡",url=Flash))
        bot.send_message(chat_id=id,text=text,parse_mode="markdown",reply_markup=main)


def DefCheckCaptcha(m,Token,text):
    id = str(m.chat.id)
    code = str(m.text)
    if code == GetCodeFromToken(Token):
        DeletImageCaptach(Token)
        UpdeatCaptchaLogin(str(m.chat.id))
        bot.send_message(chat_id=m.chat.id,text= "تم تحقق من أنك أنسان حقيقي … ✅")
        m.text = text
        start(message=m)
        return 
    else:
        DeletImageCaptach(Token)
        Token = GenImageCaptcha()
        msg = bot.send_photo(chat_id=id,photo=open(f"tokens/{Token}.png","rb"),caption="يرجى كتابة الكود الموجود في ألاعلى 👆\nوقم بأرسله ألى البوت ليتحقق من أنك أنسان",parse_mode="markdown")
        bot.register_next_step_handler(msg,DefCheckCaptcha,Token,text)
        return 
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    message = call.message
    try:bot.clear_step_handler(message=message)
    except:pass
    data = call.data
    print(f"✅ [{time.strftime('%Y-%m-%d-%H:%M:%S')}] ({str(message.chat.first_name)}) => {data}")
    settings = getSettingsBotJson()
    call_id = call.id
    id = str(message.chat.id)
    if settings.isbot == False and not id == settings.ownerid:
        bot.send_message(chat_id=id,text="البوت مغلق للصيانة")
        return
    for chn in json.loads(open("channel.json",encoding='utf-8').read()):
        js = requests.get("https://api.telegram.org/bot{}/getChatMember?chat_id={}&user_id={}".format(token,chn["id"],id)).json()
        if js["ok"]:
            status = js["result"]["status"]
            print(status)
            if not status in ["member","administrator","creator"]:
                main = Markup()
                main.add(Button(text="الدخول الى القناة ✅",url=chn["url"]))
                main.add(Button(text="تحقق من الاشتراك ♻️",callback_data="back"))
                text = "يرجى الاشتراك في القناة لكي يعمل البوت \n\n1 - اضغط على دخول الى القناة \n2- قم بلشتراك في القناة \n3 - اضغط على تحقق من الاشتراك \n\n وسوفة يعمل لبوت"
                bot.send_message(chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
                return False
    name = str(message.chat.first_name)
    username = str(message.chat.username)
    UserDB = UserData(id)
    if UserDB.isDand:
        bot.send_message(chat_id=id,text="تم حظرك من لبوت بسبب مخالفة الشروط 🚷")
        return False
    if data == "add-coin":
        bot.clear_step_handler(message=message)
        main = Markup()
        A = Button(text="🌀 مشاركة رابط الدعوة 🌀",callback_data="frinds")
        B = Button(text="ستخدام كود 🎫",callback_data="code")
        C = Button(text="الهدية يومية 🎁",callback_data="gift")
        D = Button(text="كودات هداية 😍",url=str(linkCanelGiftCode))
        E = Button(text="➕ الانضمام في القنوات ➕",callback_data="ch-add")
        F = Button(text="رجوع ⬅️",callback_data="back")
        G = Button(text="شحن حسابي 💸",callback_data="asiacell-add")
        main.add(A)
        main.add(B,C)
        main.add(E)
        main.add(D,G)
        main.add(F)
        text=f"""
نقاطك : *{UserDB.coin}*

🔦 انضمام بقنــوات : ( {settings.subscription_points} )
🌀 مشاركة رابط الدعوة : ( {settings.referral_balance} )
🎁 الهدية اليـوميــة : ( {settings.gift_balance} )
💸 شراء نقاط : ( 💲💲 )
        """
        bot.edit_message_text(chat_id=id,message_id=message.id,text=text,parse_mode="markdown",reply_markup=main)
    elif data == "add-folowers":
        main = Markup()
        num_add = int(int(UserDB.coin)/int(settings.finance_points))
        if int(UserDB.coin) >= int(settings.sunday_points_finance):
            main.add(Button(text=f"تمويل {num_add} عضو 👤",callback_data="send_all"))
            main.add(Button(text="ارسال العدد المطلوب ❇️",callback_data="send_order_coin"))
            main.add(Button(text="رجوع ⬅️",callback_data="back"))
            bot.edit_message_text(text=text_send_follw(UserDB.coin),chat_id=id,message_id=message.message_id,reply_markup=main,parse_mode="markdown")
        else:
            main = Markup()
            main.add(Button(text="تجميع نقاط ⚓",callback_data="add-coin"))
            main.add(Button(text="رجوع ⬅️",callback_data="back"))
            bot.edit_message_text(text=text_send_follw_else(UserDB.coin),chat_id=id,message_id=message.message_id,reply_markup=main,parse_mode="markdown")
    elif data == "send_order_coin":
        main = Markup()
        main.add(Button(text="رجوع ⬅️",callback_data="add-folowers"))
        c = bot.edit_message_text(text=text_send_order_coin(UserDB.coin),chat_id=id,message_id=message.message_id,reply_markup=main,parse_mode="markdown")
        bot.register_next_step_handler(c,get_send_order_coin)
        
    elif data == "send_all":
        f = int(settings.finance_points)
        num = int(int(UserDB.coin)/f)
        main = Markup()
        main.add(Button(text="رجوع ⬅️",callback_data="add-folowers"))
        if not num > 49:
            bot.send_message(chat_id=id,text="عزيزي أقل تمويل يمكنك البدء به هو 50 عضو ⁉️",reply_markup=main,parse_mode="markdown")
            return False
        c = bot.edit_message_text(text=text_get_send_order_coin(),chat_id=id,message_id=message.message_id,reply_markup=main,parse_mode="markdown")
        bot.register_next_step_handler(c,get_num_send,num)
    elif data == "ch-add":
        dbChannel = GetRequestChannel(id)
        if dbChannel == None:
            main = Markup()
            main.add(Button(text="رجوع ⬅️",callback_data="add-coin"))
            bot.edit_message_text(chat_id=id,message_id=message.id,text="لاتوجد قنوات حالين يرجى الرجوع بعد ساعة",reply_markup=main,parse_mode="markdown")
            return 
        main = Markup()
        A = Button(text="تحقق",callback_data=f"IS?@{dbChannel['id']}")
        B = Button(text="تخطي ♻️",callback_data=f"SKIP&@{dbChannel['id']}")
        C = Button(text="أبلاغ ⚠️",callback_data=f"RP#@{dbChannel['id']}")
        main.add(A)
        main.add(Button(text="دخول ألى القناة ↖️",url=dbChannel["link"]))
        main.add(B,C)
        main.add(Button(text="رجوع ⬅️",callback_data="add-coin"))
        name_ch = dbChannel["name"]
        link = dbChannel["link"]
        co = str(settings.subscription_points)
        coin = UserData(id).coin
        bot.edit_message_text(chat_id=id,message_id=message.message_id,text=f"""
• اشترك في القناة : [{name_ch}]({link})

 من ثم اضغط على تحقق لكي تحصل على {co} نقطة ⭐✳️

 نقاطك الحاليه : *{coin}*
""",reply_markup=main,parse_mode="markdown",disable_web_page_preview=True)
    elif "SKIP&@" in data:
        cid = str(data).replace("SKIP&@","").strip()
        mydb = sqlite3.connect("databeas.db")
        req = mydb.cursor()
        sql = f"INSERT INTO skip_channels(user_id,idSkip) VALUES('{id}','{cid}')"
        req.execute(sql)
        mydb.commit()
        dbChannel = GetRequestChannel(id)
        print(dbChannel)
        if dbChannel == None:
            main = Markup()
            main.add(Button(text="رجوع ⬅️",callback_data="add-coin"))
            bot.edit_message_text(chat_id=id,message_id=message.id,text="لاتوجد قنوات حالين يرجى الرجوع بعد ساعة",reply_markup=main,parse_mode="markdown")
            return 
        main = Markup()
        A = Button(text="تحقق",callback_data=f"IS?@{dbChannel['id']}")
        B = Button(text="تخطي ♻️",callback_data=f"SKIP&@{dbChannel['id']}")
        C = Button(text="أبلاغ ⚠️",callback_data=f"RP#@{dbChannel['id']}")
        main.add(A)
        main.add(Button(text="دخول ألى القناة ↖️",url=dbChannel["link"]))
        main.add(B,C)
        main.add(Button(text="رجوع ⬅️",callback_data="add-coin"))
        name_ch = dbChannel["name"]
        link = dbChannel["link"]
        co = str(settings.subscription_points)
        coin = UserData(id).coin
        bot.edit_message_text(chat_id=id,message_id=message.message_id,text=f"""
• اشترك في القناة : [{name_ch}]({link})

 من ثم اضغط على تحقق لكي تحصل على {co} نقطة ⭐✳️

 نقاطك الحاليه : *{coin}*
""",reply_markup=main,parse_mode="markdown",disable_web_page_preview=True)
    
    elif "RP#@" in data:
        cid = str(data).replace("RP#@","").strip()
        mydb = sqlite3.connect("databeas.db")
        req = mydb.cursor()
        sql = f"INSERT INTO reporting_channels(user_id,idReporting) VALUES('{id}','{cid}')"
        req.execute(sql)
        mydb.commit()
        dbCid = GetAllRequests(target=cid)
        linkcid = dbCid["link"]
        
        main = Markup()
        main.add(Button(text="عرض القناة",url=linkcid))
        hhe = f"المبلغ : [{id}](tg://openmessage?user_id={id})\nمعرف لقناة : {cid}"
        bot.send_message(chat_id=settings.ownerid,text=hhe,parse_mode="markdown",reply_markup=main,disable_web_page_preview=True)
        dbChannel = GetRequestChannel(id)
        if dbChannel == None:
            main = Markup()
            main.add(Button(text="رجوع ⬅️",callback_data="add-coin"))
            bot.edit_message_text(chat_id=id,message_id=message.id,text="لاتوجد قنوات حالين يرجى الرجوع بعد ساعة",reply_markup=main,parse_mode="markdown")
            return 
        main = Markup()
        A = Button(text="تحقق",callback_data=f"IS?@{dbChannel['id']}")
        B = Button(text="تخطي ♻️",callback_data=f"SKIP&@{dbChannel['id']}")
        C = Button(text="أبلاغ ⚠️",callback_data=f"RP#@{dbChannel['id']}")
        main.add(A)
        main.add(Button(text="دخول ألى القناة ↖️",url=dbChannel["link"]))
        main.add(B,C)
        main.add(Button(text="رجوع ⬅️",callback_data="add-coin"))
        name_ch = dbChannel["name"]
        link = dbChannel["link"]
        co = str(settings.subscription_points)
        coin = UserData(id).coin
        bot.edit_message_text(chat_id=id,message_id=message.message_id,text=f"""
• اشترك في القناة : [{name_ch}]({link})

 من ثم اضغط على تحقق لكي تحصل على {co} نقطة ⭐✳️

 نقاطك الحاليه : *{coin}*
""",reply_markup=main,parse_mode="markdown",disable_web_page_preview=True)
    elif "IS?@" in data:
        cid = str(data).replace("IS?@","").strip()
        js = requests.get("https://api.telegram.org/bot{}/getChatMember?chat_id={}&user_id={}".format(token,cid,id)).json()
        dbCid = GetAllRequests(target=cid)
        if js["ok"]:
            status = js["result"]["status"]
            if status in ["member","administrator","creator"]:
                dbCid = GetAllRequests(target=cid)
                try:
                    if cid in UserData(id).GetAccountsFollow():
                        return False
                    mydb = sqlite3.connect("databeas.db")
                    req = mydb.cursor()
                    sql = f"INSERT INTO subscribers(id,idSubscribers) VALUES('{id}','{cid}')"
                    req.execute(sql)
                    mydb.commit()
                    dbUser = UserData(id)
                    newMin = int(int(dbCid["remaining_number"]))
                    newMin = (newMin)-1
                    if dbCid["fixed"] == "0":
                        dbUser.updeatDB(tabel="requests",key="remaining_number",value=str(newMin),keyIf="id",valueIf=cid,isIf=True)
                        if newMin <= 0:
                            dbUser.updeatDB(tabel="requests",key="condition",value="0",keyIf="id",valueIf=cid,isIf=True)
                            dbUser.updeatDB(tabel="requests",key="expiry_date",value=time.strftime("%Y-%m-%d-%H:%M:%S"),keyIf="id",valueIf=cid,isIf=True)
                            main = Markup()
                            link = dbCid["link"]
                            name_ch = dbCid["name"]
                            username_bot = usernamebot
                            required_number = dbCid["required_number"]
                            textu = f"*تم انتهاء تمويل قناة جديدة ✅*\n\n*القناة :* [{name_ch}]({link})\n\n*العدد المطلوب : {required_number}*"
                            main.add(Button(text="ذهاب الى البوت ✅",url="t.me/{}".format(usernamebot.replace("@",""))))
                            bot.send_message(chat_id=settings.proofs,text=textu,parse_mode="markdown",reply_markup=main,disable_web_page_preview=True)
                        bot.send_message(chat_id=dbCid["user_id"],text=text_send_follw_done(dbCid),parse_mode="markdown",disable_web_page_preview=True)
                    newCoin = int(dbUser.coin) + int(settings.subscription_points)
                    dbUser.updeatDB(tabel="users",key="coin",value=str(newCoin))
                except Exception as e:
                    print(e)
            else:
                bot.answer_callback_query(callback_query_id=call_id,text=f"عليك ألاشتراك في القناة اولا ⁉️",show_alert=True)
                return 
        else:
            link = dbCid["link"]
            bot.send_message(chat_id=dbCid["user_id"],text=f"لقد أنزلت البوت من الادمنية وتم توقيف تمويلك وسحب النقاط ⁉ \nرابط القناة : {link}️")
            dbUser.updeatDB(tabel="requests",key="condition",value="0",keyIf="id",valueIf=cid)
            mydb = sqlite3.connect("databeas.db")
            req = mydb.cursor()
            sql = f"INSERT INTO skip_channels(user_id,idSkip) VALUES('{id}','{cid}')"
            req.execute(sql)
        dbChannel = GetRequestChannel(id)
        if dbChannel == None:
            main = Markup()
            main.add(Button(text="رجوع ⬅️",callback_data="add-coin"))
            bot.edit_message_text(chat_id=id,message_id=message.id,text="لاتوجد قنوات حالين يرجى الرجوع بعد ساعة",reply_markup=main,parse_mode="markdown")
            return 
        main = Markup()
        A = Button(text="تحقق",callback_data=f"IS?@{dbChannel['id']}")
        B = Button(text="تخطي ♻️",callback_data=f"SKIP&@{dbChannel['id']}")
        C = Button(text="أبلاغ ⚠️",callback_data=f"RP#@{dbChannel['id']}")
        main.add(A)
        main.add(Button(text="دخول ألى القناة ↖️",url=dbChannel["link"]))
        main.add(B,C)
        main.add(Button(text="رجوع ⬅️",callback_data="add-coin"))
        name_ch = dbChannel["name"]
        link = dbChannel["link"]
        co = str(settings.subscription_points)
        coin = UserData(id).coin
        bot.answer_callback_query(callback_query_id=call_id,text="تم التحقق بنجاح ⚓ ")
        bot.edit_message_text(chat_id=id,message_id=message.message_id,text=f"""
• اشترك في القناة : [{name_ch}]({link})

 من ثم اضغط على تحقق لكي تحصل على {co} نقطة ⭐✳️

 نقاطك الحاليه : *{coin}*
""",reply_markup=main,parse_mode="markdown",disable_web_page_preview=True)
    elif data == "frinds":
        main = Markup()
        link = f"https://t.me/{usernamebot}?start=ref{id}"
        isCoin = settings.referral_balance
        ids = UserDB.getYour_referrals().strip().split("-")
        Lids = len(ids)-1
        text = f"* عندما تقوم بدعوة شخص من خلال الرابط : {link}\n\n ستحصل على : {isCoin} 💰\nعدد دعواتك : {Lids} 👤\n\nقائمة أكثر الاشخاص شاركو رابط الدعوة ❤️‍🔥\n*"
        i = UserDB.Trind()
        Tid = i[0]["id"]
        Lt = int(i[0]["your_referrals"])-1
        text+=f"\n🥇) {Lt} : [{Tid}](tg://user?id={Tid})\n"
        Tid = i[1]["id"]
        Lt = int(i[1]["your_referrals"])-1
        text+=f"🥈) {Lt} : [{Tid}](tg://user?id={Tid})\n"
        Tid = i[2]["id"]
        Lt = int(i[2]["your_referrals"])-1
        text+=f"🥉) {Lt} : [{Tid}](tg://user?id={Tid})\n"
        main.add(Button(text="رجوع ⬅️",callback_data="add-coin"))
        bot.edit_message_text(chat_id=id,message_id=message.id,text=text,parse_mode="markdown",reply_markup=main,disable_web_page_preview=True)
    elif data == "back":
        bot.clear_step_handler(message=message)
        coin = UserDB.coin
        text = text_home(id,name,coin)
        
        main = Markup()
        A = Button(text="تجميع نقاط ➕",callback_data="add-coin")
        B = Button(text="قسم الطلبات 🔔",callback_data="orders")
        C = Button(text="💎 قسم الخدمات 💎",callback_data="server")
        D = Button(text="تحويل نقاط 📤",callback_data="send-coin")
        E = Button(text="معلومات حسابي 💳",callback_data="info-my")
        F = Button(text="💰 شحن حسابي تلقائي 💰",callback_data="asiacell")
        G = Button(text="تمويل قناة حقيقي 👤",callback_data="add-folowers")
        main.add(C)
        main.add(A,B)
        main.add(G)
        main.add(D,E)
        main.add(F)
        main.add(Button(text="- قناة بوت فلاش الرسمية ⚡",url=Flash))
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,parse_mode="markdown",reply_markup=main)
        
    elif data == "gift":
        g = settings.gift_balance
        if UserDB.gift == time.strftime("%Y-%m-%d"):
            bot.answer_callback_query(callback_query_id=call_id,text=f"لقد حصلت على الهدية مسبقا , انتظر يوم واعد المحاولة !",show_alert=True)
        else:
            UserDB.updeatDB(
            tabel="users",
            key="coin",
            value=str(int(UserDB.coin)+int(g))
            )
            UserDB.updeatDB(
            tabel="users",
            key="gift",
            value=time.strftime("%Y-%m-%d")
            )
            bot.answer_callback_query(callback_query_id=call_id,text=f"• لقد حصلت على {g} نقاط هدية يومية 🎁",show_alert=True)
            bot.send_message(chat_id=settings.ownerid,text=f"قام المستخدم : {id}\nبجمع رصيد الهدية 🎁")
            

    elif data == "server":
        main = Markup()
        A = Button(text="💎 خدمات انستغرام 💎",callback_data="root#instagram")
        B = Button(text="💎 خدمات فيسبوك 💎",callback_data="root#facebook")
        
        C = Button(text="💎 خدمات تلجرام 💎",callback_data="root#telegram")
        D = Button(text="💎 خدمات تيك توك 💎",callback_data="root#tiktok")
        
        E = Button(text="💎 خدمات يوتيوب 💎",callback_data="root#tube")
        F = Button(text="💎 خدمات تويتر 💎",callback_data="root#X")
        
        G = Button(text="رجوع ⬅️",callback_data="back")
        
        main.add(A,D)
        main.add(B,E)
        main.add(C,F)
        main.add(Button(text="- الشروط ⁉️",callback_data="TheConditions"))
        main.add(G)
        slen = GetLenAllServers()
        text = "*يمكنك من هذا القسم اختار نوع الخدمات 💎*\n\n"
        text+=f"*يمكنك التمتع بكافة الخدمات الموجودة في البوت بأسعار مميزة ومنافسة للسوق مع صمان الجودة والسرعة*"
        text+="\n\n"
        text+=f"*عدد الطلبات : {slen} طلب مكتمل ✅*"
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
    elif data == "TheConditions":
        text = open("TheConditions.txt",encoding="utf-8").read()
        main = Markup()
        main.add(Button(text="رجوع ⬅️",callback_data="server"))
        msg = bot.edit_message_text(parse_mode="markdown",reply_markup=main,message_id=message.id,chat_id=id,text=text)
    elif data == "send-coin":
        main = Markup()
        main.add(Button(text="رجوع ⬅️",callback_data="back"))
        msg = bot.edit_message_text(parse_mode="markdown",reply_markup=main,message_id=message.id,chat_id=id,text="*أرسل ايدي الشخص المستلم للنقاط 📤🆔*")
        bot.register_next_step_handler(msg,sendCoingetId)
        
    elif data == "code":
        main = Markup()
        main.add(Button(text="رجوع ⬅️",callback_data="add-coin"))
        msg = bot.edit_message_text(parse_mode="markdown",reply_markup=main,message_id=message.id,chat_id=id,text="*قم بأرسال كود الهدية او كود شحن 🎫*")
        bot.register_next_step_handler(msg,getcodeuser)
        
        
    elif data == "asiacell":
        main = Markup()
        text = f"*يمكنك شحن حسابك تلقائي من خطوط الاسياسيل فقط واذا كنت تريد شحن عن طريق الزينكاش او طرق اخره يمكنك مراسلة المالك للشحن اليدوي عبر الزينكاش ~ أختر من الاسفل ماذا تريد 👇*"
        main.add(Button(text="شحن تلقائي عبر الاسياسيل 💰",callback_data="asiacell-done"))
        main.add(Button(text="مراسلة المالك للشحن اليدوي ♻️👤",url=LinkMe))
        main.add(Button(text="رجوع ⬅️",callback_data="back"))
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
    
    elif data == "asiacell-add":
        main = Markup()
        text = f"*يمكنك شحن حسابك تلقائي من خطوط الاسياسيل فقط واذا كنت تريد شحن عن طريق الزينكاش او طرق اخره يمكنك مراسلة المالك للشحن اليدوي عبر الزينكاش ~ أختر من الاسفل ماذا تريد 👇*"
        main.add(Button(text="شحن تلقائي عبر الاسياسيل 💰",callback_data="asiacell-done"))
        main.add(Button(text="مراسلة المالك للشحن اليدوي ♻️👤",url=LinkMe))
        main.add(Button(text="رجوع ⬅️",callback_data="add-coin"))
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
    
    elif data == "asiacell-done":
        if UserDB.isLoginAsia:
            main = Markup()
            j = 60
            k = []
            op = settings.price_points
            for i in range(20):
                main.add(
                Button(text=f"{j}$",callback_data=f"asiacell-coin{j}000.0"),
                Button(text=f"{j-1}$",callback_data=f"asiacell-coin{j-1}000.0"),
                Button(text=f"{j-2}$",callback_data=f"asiacell-coin{j-2}000.0"),
                )
                j-=3
            main.add(Button(text="يرجى أختيار الكمية لشحن حسابك بها 👆💰",callback_data="kop6899ij78j"))
            main.add(Button(text="رجوع ⬅️",callback_data="asiacell"))
            text = "*يرجى اختيار كمية شحن حسابك من الاسفل 👇*"
            bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
        else:
            text = "حسناً، قم بأرسال رقم الهاتف بهذهِ الصيغة:\n\n077********"
            main = Markup()
            main.add(Button(text="رجوع ⬅️",callback_data="back"))
            msg = bot.edit_message_text(reply_markup=main,message_id=message.id,chat_id=id,text=text)
            bot.register_next_step_handler(msg,getPhoneAsia)
            
    elif "asiacell-coin" in data:
        f = str(data).replace("asiacell-coin","")
        j = float(f)
        l = f.replace("000.0","")
        op = int(settings.price_points)*int(l)
        text = f"سيتم شحن حسابك بقيمة : {l} اسياسيل ➕\nما يعادل : {op} نقطة في البوت 💰\n\n * ~ أضغط على (تأكيد) لتأكيد طلبك 💪*"
        main = Markup()
        main.add(Button(text="تأكيد 🟢",callback_data=f"root@done{f}"))
        main.add(Button(text="رجوع ⬅️",callback_data="asiacell-done"))
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
    elif "root@done" in data:
        k = str(data).replace("root@done","").strip()
        h = float(k)
        l = k.replace("000.0","")
        op = int(settings.price_points)*int(l)
        target = settings.payments_phone_number 
        access_token = UserDB.access_token
        url = "https://odpapp.asiacell.com/api/v1/credit-transfer/start?lang=ar"
        headers ={
        "X-ODP-API-KEY": "1ccbc4c913bc4ce785a0a2de444aa0d6",
        "DeviceID": UserDB.phone,
        "Authorization": f"Bearer {access_token}",
        "X-OS-Version": "11",
        "X-Device-Type": "[Android][realme][RMX2001 11] [Q]",
        "X-ODP-APP-VERSION": "3.4.1",
        "X-FROM-APP": "odp",
        "X-ODP-CHANNEL": "mobile",
        "X-SCREEN-TYPE": "MOBILE",
        "Cache-Control": "private, max-age=240",
        "Content-Type": "application/json; charset=UTF-8",
        "Content-Length": "43",
        "Host": "odpapp.asiacell.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/5.0.0-alpha.2"}
        data = {"amount":f"{h}","receiverMsisdn":str(target)}
        r = requests.post(url,headers=headers,json=data).json()
        try:
            if r["success"]:
                sid = UserDB.phone
                coin = str(op)
                pid = str(r["PID"])
                main = Markup()
                main.add(Button(text="ألغاء العملية 🚫",callback_data="back"))
                msg = bot.edit_message_text(message_id=message.id,parse_mode="markdown",reply_markup=main,chat_id=message.chat.id,text="*سوف يصلك كود على رقمك مكون من 6 ارقام يرجى ارسالة*")
                bot.register_next_step_handler(msg,getCodeSmsTrans,pid,sid,access_token,coin)
            else:
                UserDB.updeatDB(tabel="users",key="isLoginAsia",value="no")
                main = Markup()
                main.add(Button(text="تسجيل دخول في أسياسيل",callback_data="asiacell-done"))
                bot.edit_message_text(message_id=message.id,chat_id=message.chat.id,text="*يجب عليك تسجيل دخول الى رقمك في اسيا سيل لتتمكن من شحن حسابك*",parse_mode="markdown",reply_markup=main)
                return 
        except:
            UserDB.updeatDB(tabel="users",key="isLoginAsia",value="no")
            main = Markup()
            main.add(Button(text="تسجيل دخول في أسياسيل",callback_data="asiacell-done"))
            bot.edit_message_text(message_id=message.id,chat_id=message.chat.id,text="*يجب عليك تسجيل دخول الى رقمك في اسيا سيل لتتمكن من شحن حسابك*",parse_mode="markdown",reply_markup=main)
            return 
    elif data == "orders":
        texts = f"*قسم طلبات التمويل :* \n - يضهر لك اخر 5 قنوات قمت بتمويلها 👤 \n\n*قسم طلبات خدماتي :* \n - يضهر لك اخر 5 خدمات قمت بشرائها 💎"
        main = Markup()
        main.add(Button(text="قسم طلبات التمويل 👤",callback_data="requests-chanel"))
        main.add(Button(text="قسم طلبات الخدمات 💎",callback_data="orders-server"))
        main.add(Button(text="رجوع ⬅️",callback_data="back"))
        bot.edit_message_text(message_id=message.id,chat_id=message.chat.id,text=texts,parse_mode="markdown",reply_markup=main)
    elif data == "orders-server":
        od = UserDB.getJsonOrders()
        od5 = get_50Data(od,ko=5)
        main = Markup()
        if len(od) == 0:
            text = "*ليس لديك طلبات في الوقت الحالي 🔔*"
        else:
            text = f"* عدد طلباتك : {len(od)} 🔔➕\nأنقر على رقم الطلب لأضهار المعلومات 📇*"
            for s in od5:
                idO = str(s["idbot"])
                indx = od.index(s)+1
                main.add(Button(text=f"رقم طلب : {indx} - المعرف : {idO} 👀",callback_data=f"INFO?ORDER={idO}"))
        main.add(Button(text="رجوع ⬅️",callback_data="orders"))
        bot.edit_message_text(message_id=message.id,chat_id=message.chat.id,text=text,reply_markup=main,parse_mode="markdown")
    elif data == "requests-chanel":
        od = UserDB.GetRequestsChannels()
        od5 = get_50Data(od,ko=5)
        main = Markup()
        if len(od) == 0:
            text = "*ليس لديك طلبات في الوقت الحالي 🔔*"
        else:
            text = f"* عدد طلباتك : {len(od)} 🔔➕\nأنقر على اسم القناة لأضهار المعلومات 📇*"
            for s in od5:
                namech = str(s["name"])
                idO = s["id"]
                indx = od.index(s)+1
                main.add(Button(text=f"رقم طلب : {indx} - {namech} 👀",callback_data=f"INFO?REQUESTS={idO}=INDEX={indx}"))
        main.add(Button(text="رجوع ⬅️",callback_data="orders"))
        bot.edit_message_text(message_id=message.id,chat_id=message.chat.id,text=text,reply_markup=main,parse_mode="markdown")
    elif "INFO?REQUESTS=" in data:
        ind = str(data).split("INDEX=")[1]
        orderid = str(data).split("=")[1]
        od = UserDB.GetRequestsChannels()
        for Ord in od:
            if str(Ord["id"]) == orderid and int(od.index(Ord)+1) == int(ind):
                nameod = Ord["name"]
                required_number = Ord["required_number"]
                remaining_number = Ord["remaining_number"]
                condition = Ord["condition"]
                order_date = Ord["order_date"]
                expiry_date = Ord["expiry_date"]
                if condition == "1":
                    condition = "قيد التمويل"
                else:
                    condition = "تم نتهاء التمويل" 
                text = f"*معلومات طلبك رقم : {ind}*\n"
                text+=f"-"*50 + "\n"
                text+=f"*أسم القناة : {nameod} 🌱* \n"
                text+=f"*ايدي القناة :* `{orderid}` 🆔\n"
                text+=f"*العدد المطلوب : {required_number} 👀 *\n"
                text+=f"*العدد المتبقي : {remaining_number} 🌀*\n"
                text+=f"*الحالة : {condition} 🔎*\n"
                text+=f"*تاريخ بدء التمويل : {order_date} 📅*\n"
                text+=f"*تاريخ أنتهاء التمويل : {expiry_date} 📆*"
                main = Markup()
                main.add(Button(text="- الرابط ↖️",url=Ord["link"]))
                main.add(Button(text="رجوع ⬅️",callback_data="requests-chanel"))
                bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
    elif "INFO?ORDER=" in data:
        orderid = str(data).replace("INFO?ORDER=","").strip()
        od = UserDB.getJsonOrders()
        for Ord in od:
            if str(Ord["idbot"]) == orderid:
                nameod = Ord["name"]
                api = Ord["supplier"]
                mydb = sqlite3.connect("databeas.db")
                sql = f"SELECT * FROM apis WHERE api='{api}'"
                mycursor = mydb.cursor()
                mycursor.execute(sql)
                key = str(mycursor.fetchall()[0][1])
                isA = requests.post(api,data={"key":key,"action":"status","order":Ord["idOrders"]}).json()["status"]
                rng = Ord["range"]
                cost = Ord["cost"]
                text = f"*معلومات طلبك رقم : {orderid}*\n"
                text+=f"-"*50 + "\n"
                text+=f"*حالة الطلب : {isA} 🔎* \n"
                text+=f"*ايدي الطلب :* `{orderid}` 🆔\n"
                text+=f"*العدد المطلوب : {rng} 👀 *\n"
                text+=f"*التكلفة : {cost} 💸*\n"
                text+=f"*أسم الخدمة : {nameod}*\n"
                main = Markup()
                main.add(Button(text="- الرابط ↖️",url=Ord["link"]))
                main.add(Button(text="رجوع ⬅️",callback_data="orders-server"))
                try:
                    bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
                except:
                    text+=f"*الرابط : {Ord['link']} 🧬*\n"
                    main = Markup()
                    main.add(Button(text="رجوع ⬅️",callback_data="orders-server"))
                    bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
    elif data == "info-my":
        main = Markup()
        ref = len(str(UserDB.getYour_referrals).split("-"))
        od = len(UserDB.getJsonOrders())
        ot = len(UserDB.GetRequestsChannels())
        clen = len(UserDB.GetAccountsFollow())
        text = f"*اهلا بك في قسم معلوماتك 👤🎫*\n\n"
        text+=f"* ايدي : *`{id}` 🆔\n\n"
        text+=f"*عدد مشاركات رابط الدعوة : {ref} 🔄*\n"
        text+=f"*عدد طلبات الخدمات : {od} 💎*\n"
        text+=f"*عدد طلبات التمويل : {ot} 👤*\n"
        text+=f"*عدد القنوات التي شتركت بها : {clen} ♻️*\n\n"
        text+=f"*رصيد حسابك : {UserDB.coin} 💰*\n"
        main.add(Button(text="رجوع ⬅️",callback_data="back"))
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
    
    elif "root$" in data:
        main = Markup()
        type = str(data).replace("root#","").strip()
        main.add(Button(text="👍 قسم لايكات 👍",callback_data=f"root${type}/like"),Button(text="👁️‍🗨️ قسم المشاهدات 👁️‍🗨️️",callback_data=f"root${type}/view"))
        main.add(Button(text="👤 قسم المتابعين👤",callback_data=f"root${type}/followers"))
        main.add(Button(text="رجوع ⬅️",callback_data="server"))
        text = "*اختار قسم نوع الخدمات التي تريدها 👇*"
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
        
    elif "root#" in data:
        type = str(data).replace("root#","").strip()
        servers = ["followers","like","view"]
        callback_data = f"server"
        main = Markup()
        for server in servers:
            for i in getListServers(type=type,server=server):
                main.add(Button(text=i["name"],callback_data=f"getServerid#{i['id']}/{type}/{server}"))
        main.add(Button(text="رجوع ⬅️",callback_data=callback_data))
        text = "*اختر الخدمة التي تناسبك لعرض محتواها 👇*"
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
        
    elif "getServerid#" in data:
        dt = str(data).replace("getServerid#","").strip()
        id_order = dt.split("/")[0]
        type = dt.split("/")[1]
        server = dt.split("/")[2]
        info_order = getServer(type,server,id_order)
        name = info_order["name"]
        dis = info_order["dis"]
        pis = info_order["pis"]
        pisone = str(int(pis)/1000)
        ma = info_order["max"]
        mi = info_order["min"]
        main = Markup()
        main.add(Button(text="رجوع ⬅️",callback_data=f"root#{type}"))
        text = f"*اسم لخدمة : {name} \nوصف لخدمة : {dis} \n\nالحد الادنى : {mi} \nالحد الاعلى : {ma} \n\n سعر لكل الف : {pis} 💰\nسعر المفرد : {pisone} ✨\n\n للشراء أرسل العدد المطلوب 🎭*"
        msg = bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
        bot.register_next_step_handler(msg,getRangeForOrder,id_order,type,server)
    
    elif data == "adminisbot" and id==settings.ownerid:
        if settings.isbot:
            v = "0"
        else:
            v = "1"
        settings.updeta(key="isbot",value=v)
        m = Markup()
        settings = getSettingsBotJson()
        if settings.isbot:t="حالة البوت : ✅"
        else:t="حالة البوت : ❌"
        if settings.send_users:s="اشعارات الدخول : ✅"
        else:s="اشعارات الدخول : ❌"
        A = Button(text=t,callback_data="adminisbot")
        B = Button(text=s,callback_data="adminissend")
        m.add(A,B)
        C = Button(text="قسم الاشتراك الاجباري",callback_data="adminchnel")
        D = Button(text="قسم الادمنية",callback_data="adminadmins")
        m.add(C,D)
        E = Button(text="قسم الاذاعة",callback_data="adminhi")
        F = Button(text="قسم الاحصائيات",callback_data="adminusers")
        m.add(E,F)
        G = Button(text="• اعدادات بوت الرشق •",callback_data="adminall")
        m.add(G)
        text = "• اهلا بك في لوحه الأدمن الخاصه بالبوت 🤖\n- يمكنك التحكم في البوت الخاص بك من هنا\n~~~~~~~~~~~~~~~~~"
        bot.edit_message_text(message_id=message.id,chat_id=settings.ownerid,text=text,reply_markup=m)
    
    elif data == "adminissend" and id==settings.ownerid:
        if settings.send_users:
            v = "0"
        else:
            v = "1"
        settings.updeta(key="send_users",value=v)
        m = Markup()
        settings = getSettingsBotJson()
        if settings.isbot:t="حالة البوت : ✅"
        else:t="حالة البوت : ❌"
        if settings.send_users:s="اشعارات الدخول : ✅"
        else:s="اشعارات الدخول : ❌"
        A = Button(text=t,callback_data="adminisbot")
        B = Button(text=s,callback_data="adminissend")
        m.add(A,B)
        C = Button(text="قسم الاشتراك الاجباري",callback_data="adminchnel")
        D = Button(text="قسم الادمنية",callback_data="adminadmins")
        m.add(C,D)
        E = Button(text="قسم الاذاعة",callback_data="adminhi")
        F = Button(text="قسم الاحصائيات",callback_data="adminusers")
        m.add(E,F)
        G = Button(text="• اعدادات بوت الرشق •",callback_data="adminall")
        m.add(G)
        text = "• اهلا بك في لوحه الأدمن الخاصه بالبوت 🤖\n- يمكنك التحكم في البوت الخاص بك من هنا\n~~~~~~~~~~~~~~~~~"
        bot.edit_message_text(message_id=message.id,chat_id=settings.ownerid,text=text,reply_markup=m)
    elif data == "adminhi" and id==settings.ownerid:
        main = Markup()
        main.add(Button(text="رجوع",callback_data="back-admin"))
        text = "*قم بأرسال النص الذي تريد أذاعته 📣*"
        msg = bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
        bot.register_next_step_handler(msg,allHiAdmin)
    elif data == "back-admin" and id==settings.ownerid:
        bot.clear_step_handler(message=message)
        m = Markup()
        settings = getSettingsBotJson()
        if settings.isbot:t="حالة البوت : ✅"
        else:t="حالة البوت : ❌"
        if settings.send_users:s="اشعارات الدخول : ✅"
        else:s="اشعارات الدخول : ❌"
        A = Button(text=t,callback_data="adminisbot")
        B = Button(text=s,callback_data="adminissend")
        m.add(A,B)
        C = Button(text="قسم الاشتراك الاجباري",callback_data="adminchnel")
        D = Button(text="قسم الادمنية",callback_data="adminadmins")
        m.add(C,D)
        E = Button(text="قسم الاذاعة",callback_data="adminhi")
        F = Button(text="قسم الاحصائيات",callback_data="adminusers")
        m.add(E,F)
        G = Button(text="• اعدادات بوت الرشق •",callback_data="adminall")
        m.add(G)
        text = "• اهلا بك في لوحه الأدمن الخاصه بالبوت 🤖\n- يمكنك التحكم في البوت الخاص بك من هنا\n~~~~~~~~~~~~~~~~~"
        bot.edit_message_text(message_id=message.id,chat_id=settings.ownerid,text=text,reply_markup=m)
    elif data == "adminusers" and id==settings.ownerid:
        main = Markup()
        main.add(Button(text="تحديد تاريخ معين",callback_data="order-time-admin"))
        main.add(Button(text="رجوع",callback_data="back-admin"))
        text = getInfoMyBotAll()
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
    elif data == "order-time-admin":
        main = Markup(row_width=3)
        text ="يرجى تحديد السنة"
        for i in range(2024,2033):
            main.add(Button(text=str(i),callback_data=f"Tyear=>{str(i)}"))
        main.add(Button(text="رجوع",callback_data="adminusers"))
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
    elif "Tyear=>" in data:
        year = str(data).split("=>")[1]
        main = Markup()
        text ="يرجى تحديد الشهر"
        for i in range(1,13):
            if not i > 9:
                i = f"0{i}"
            main.add(Button(text=str(i),callback_data=f"Tmonth=>{year}-{str(i)}"))
        main.add(Button(text="رجوع",callback_data="order-time-admin"))
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
    elif "Tmonth=>" in data:
        year = str(data).split("=>")[1]
        main = Markup()
        text ="يرجى تحديد اليوم"
        for i in range(1,32):
            if not i > 9:
                i = f"0{i}"
            main.add(Button(text=str(i),callback_data=f"Tday=>{year}-{str(i)}"))
        main.add(Button(text="رجوع",callback_data=f"order-time-admin"))
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
    elif "Tday=>" in data:
        year = str(data).split("=>")[1]
        main = Markup()
        text = getInfoMyBotAll(tim=str(year))
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
        main.add(Button(text="رجوع",callback_data=f"order-time-admin"))
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
    
    elif data == "adminchnel" and id==settings.ownerid:
        main = Markup()
        lists = json.loads(open("channel.json",encoding='utf-8').read())
        for i in lists:
            main.add(
            Button(text=i['name'],url=i['url']),
            Button(text="حذف القناة 🚫",callback_data=f"(deletchannel){i['id']}"))
        
        main.add(Button(text="رجوع",callback_data="back-admin"))
        text="سوفة تضهر جميع قنوات الاشتراك الاجباري \n\nاذا كنت تريد أضافة قناة شتراك أجباري جديدة قم برفع البوت ادمن في القناة وأرسل توجيه من القناة الى البوت"
        msg = bot.edit_message_text(message_id=message.id,chat_id=settings.ownerid,text=text,reply_markup=main,parse_mode="markdown")
        bot.register_next_step_handler(msg,getAddCaneel)
    elif "(deletchannel)" in data and id==settings.ownerid:
        id_ = str(data).replace("(deletchannel)","")
        for j in json.loads(open("channel.json",encoding='utf-8').read()):
            if j["id"] == id_:
                g = json.loads(open("channel.json",encoding='utf-8').read())
                g.remove(j)
                open("channel.json","w",encoding='utf-8').write(json.dumps(g,indent=4))
                break
        main = Markup()
        lists = json.loads(open("channel.json",encoding='utf-8').read())
        for i in lists:
            main.add(
            Button(text=i['name'],url=i['url']),
            Button(text="حذف القناة 🚫",callback_data=f"(deletchannel){i['id']}"))
        
        main.add(Button(text="رجوع",callback_data="back-admin"))
        text="سوفة تضهر جميع قنوات الاشتراك الاجباري \n\nاذا كنت تريد أضافة قناة شتراك أجباري جديدة قم برفع البوت ادمن في القناة وأرسل توجيه من القناة الى البوت"
        msg = bot.edit_message_text(message_id=message.id,chat_id=settings.ownerid,text=text,reply_markup=main)
        bot.register_next_step_handler(msg,getAddCaneel)

    elif data == "adminall" and id==settings.ownerid:
        bot.clear_step_handler(message=message)
        main = Markup()
        A = Button(text="اضافة رصيد ➕",callback_data="admins-coinadd")
        B = Button(text="خصم رصيد ➖",callback_data="admins-coindis")
        main.add(A,B)
        main.add(Button(text="أضافة خدمات 🛒",callback_data="admins-serveradd"))
        D = Button(text="حظر مستخدم 🚷",callback_data="admins-bandadd")
        E = Button(text="فك حظر 🚹",callback_data="admins-banddis")
        main.add(D,E)
        main.add(Button(text="حذف خدمات ⁉️",callback_data="admins-serverdis"))
        F = Button(text="اضافة هدية 🎁",callback_data="admins-giftadd")
        G = Button(text="تعطيل هدية 🚫",callback_data="admins-giftdis")
        main.add(F,G)
        main.add(Button("اضافة قناة ثابتة في التمويل 👤",callback_data="admins-addFixed"))
        J = Button(text="تعديل خدمة 🔄",callback_data="admins-editservers")
        K	= Button(text="أعدادات متقدمة ♻️",callback_data="admins-edit-sting")
        main.add(J,K)
        main.add(Button(text="رجوع",callback_data="back-admin"))
        text = "من هنا يمكنك تحديد نوع الاعدادات"
        bot.edit_message_text(message_id=message.id,chat_id=settings.ownerid,text=text,reply_markup=main)
    elif data == "admins-addFixed":
        text = "قم بأرسال توجيه من القناة التي تريد رفعة في قائمة القنوات الثابتة ويجب ان يكون البوت مشرف في القناة"
        main = Markup()
        main.add(Button(text="رجوع",callback_data="adminall"))
        msg = bot.edit_message_text(message_id=message.id,chat_id=settings.ownerid,text=text,reply_markup=main)
        bot.register_next_step_handler(msg,AddChnalFixed)
        
    elif "admins-edit-sting" in data and id==settings.ownerid:
        main = Markup()
        if str(settings.isproofs) == "1":
            text_isproofs = "حالة نشر طلبات التمويل : ✅"
        else:
            text_isproofs = "حالة نشر طلبات التمويل : ❌"
        A = Button(text="تغير رقم دفع التلقائي",callback_data=f"EditSetting=>payments_phone_number")
        B = Button(text="تغير عدد نقاط ألاحالة",callback_data=f"EditSetting=>referral_balance")
        C = Button(text="تغيير عدد نقاط الهدية",callback_data=f"EditSetting=>gift_balance")
        D = Button(text="تغيير عدد نقاط ألانضمام في قناة",callback_data=f"EditSetting=>subscription_points")
        E = Button(text="تغير عدد نقاط بيع الاعضاء",callback_data=f"EditSetting=>finance_points")
        F = Button(text="تغيير الحد ألادنى لبدء التمويل",callback_data=f"EditSetting=>sunday_points_finance")
        G = Button(text=text_isproofs,callback_data="EditSetting=>isproofs")
        H = Button(text="تغيير ايدي قناة نشر الطلبات",callback_data=f"EditSetting=>proofs")
        I = Button(text="تغيير عدد النقاط مقابل 1$",callback_data=f"EditSetting=>price_points")
        main.add(A)
        main.add(B)
        main.add(C)
        main.add(D)
        main.add(F)
        main.add(G)
        main.add(H)
        main.add(I)
        main.add(Button(text="رجوع",callback_data="adminall"))
        text = "يمكنك من هنا تغيرر اعدادات ستتم الرئيسي"
        try:bot.edit_message_text(message_id=message.id,chat_id=settings.ownerid,text=text,reply_markup=main)
        except:bot.edit_message_reply_markup(message_id=message.id,chat_id=settings.ownerid,reply_markup=main)
    elif "EditSetting=>" in data:
        main = Markup()
        main.add(Button(text="رجوع",callback_data="admins-edit-sting"))
        EditValue = str(data).split("=>")[1]
        text = f"سوفة تقوم بتغير القيمة => {EditValue} \nأرسل القيمة الجديدة …"
        msg = bot.edit_message_text(message_id=message.id,chat_id=settings.ownerid,text=text,reply_markup=main)
        bot.register_next_step_handler(msg,EditSettingBot,EditValue)
    elif data == "admins-coinadd" and id==settings.ownerid:
        main = Markup()
        text = f"الان قم بأرسل ايدي الشخص معى رمز ال "
        text+= "+"
        text+= " معى كمية الرصيد التي تريد "
        text+= "أضافته "
        text+= "\n\nمثال"
        text+= f"1000+{id}\n\n"
        text+= f"المثال الفوق سوفة يضيف 1000 دينار الى المستخدم ألذي أضفت أيديه"
        main.add(Button(text="رجوع",callback_data="adminall"))
        msg = bot.edit_message_text(message_id=message.id,chat_id=settings.ownerid,text=text,reply_markup=main)
        bot.register_next_step_handler(msg,getCoinAddAmdinsUaer)
    elif data == "admins-coindis" and id==settings.ownerid:
        main = Markup()
        text = f"الان قم بأرسل ايدي الشخص معى رمز ال "
        text+= "-"
        text+= " معى كمية الرصيد التي تريد "
        text+= "خصمها "
        text+= "\n\nمثال"
        text+= f"1000-{id}\n\n"
        text+= f"المثال الفوق سوفة يخصم 1000 دينار من المستخدم ألذي أضفت أيديه"
        main.add(Button(text="رجوع",callback_data="adminall"))
        msg = bot.edit_message_text(message_id=message.id,chat_id=settings.ownerid,text=text,reply_markup=main)
        bot.register_next_step_handler(msg,getDisAddAmdinsUaer)
    elif data == "admins-serveradd"  or data == "admins-serverdis" or data == "admins-editservers" and id==settings.ownerid:
        main = Markup()
        A = Button(text="🟢 خدمات انستغرام 🟢 ",callback_data="admin_roAot#instagram")
        B = Button(text="🟣 خدمات فيسبوك 🟣",callback_data="admin_roAot#facebook")
        
        C = Button(text="🟢 خدمات تلجرام 🟢",callback_data="admin_roAot#telegram")
        D = Button(text="🟣 خدمات تيك توك 🟣",callback_data="admin_roAot#tiktok")
        
        E = Button(text="🔵 خدمات يوتيوب 🔵",callback_data="admin_roAot#tube")
        F = Button(text="🔵 خدمات تويتر 🔵",callback_data="admin_roAot#X")
        G = Button(text="رجوع ⬅️",callback_data="adminall")
        
        main.add(B,D)
        main.add(A)
        main.add(E,F)
        main.add(C)
        main.add(G)
        text = "*مرحبا يا مالك البوت يمكنك من هنا اضافة وحذف الخدمات يرجى ختيار نوع قسم الخدمة*"
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
    elif "admin_roAot#" in data:
        main = Markup()
        type = str(data).replace("admin_roAot#","").strip()
        main.add(Button(text="👍 قسم لايكات 👍",callback_data=f"admin_roAot${type}/like"),Button(text="👁️‍🗨️ قسم المشاهدات 👁️‍🗨️️",callback_data=f"admin_roAot${type}/view"))
        main.add(Button(text="👤 قسم المتابعين👤",callback_data=f"admin_roAot${type}/followers"))
        main.add(Button(text="رجوع ⬅️",callback_data="admins-serveradd"))
        text = "*اختار قسم نوع الخدمات التي تريدها 👇*"
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
    elif "admin_roAot$" in data:
        bot.clear_step_handler(message=message)
        b = str(data).replace("admin_roAot$","").strip()
        type = b.split("/")[0]
        server = b.split("/")[1]
        callback_data = f"admin_roAot#{type}"
        main = Markup()
        for i in getListServers(type=type,server=server):
            main.add(Button(text=i["name"],callback_data=f"getAdminServerid#{i['id']}/{type}/{server}"))
        main.add(Button(text="🟢 أضافة خدمة جديد في هذا القسم 🟢",callback_data=f"Admin!Add!Server#{type}/{server}"))
        main.add(Button(text="رجوع ⬅️",callback_data=callback_data))
        text = "*اختر الخدمة التي تريده لعرض محتواها 👇*"
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
    
    elif "getAdminServerid#" in data:
        dt = str(data).replace("getAdminServerid#","").strip()
        id_order = dt.split("/")[0]
        type = dt.split("/")[1]
        server = dt.split("/")[2]
        info_order = getServer(type,server,id_order)
        name = info_order["name"]
        dis = info_order["dis"]
        pis = info_order["pis"]
        pisone = int(pis)/1000
        ma = info_order["max"]
        mi = info_order["min"]
        profit = info_order["profit"]
        main = Markup()
        B1 = Button(text="تعديل ألايدي ♻️",callback_data=f"AdminEditVIP=>{id_order}=>typeEdit=>id")
        B2 = Button(text="تعديل ألاسم ♻️",callback_data=f"AdminEditVIP=>{id_order}=>typeEdit=>name")
        B3 = Button(text="تعديل ألوصف ♻️",callback_data=f"AdminEditVIP=>{id_order}=>typeEdit=>dis")
        B4 = Button(text="تعديل ألحد الادنى ♻️",callback_data=f"AdminEditVIP=>{id_order}=>typeEdit=>min")
        B5 = Button(text="تعديل الحد الاقصى ♻️",callback_data=f"AdminEditVIP=>{id_order}=>typeEdit=>max")
        B6 = Button(text="تعديل ألسعر ♻️",callback_data=f"AdminEditVIP=>{id_order}=>typeEdit=>pis")
        B7 = Button(text="تعديل نسبة ربح ♻️",callback_data=f"AdminEditVIP=>{id_order}=>typeEdit=>profit")
        main.add(B1,B4)
        main.add(B2,B5)
        main.add(B3,B6)
        main.add(B7)
        main.add(Button(text="❌ حذف الخدمة ❌",callback_data=f"admin_Delet_Root${id_order}/{type}/{server}"))
        main.add(Button(text="رجوع ⬅️",callback_data=f"admin_roAot${type}/{server}"))
        text = f"*اسم لخدمة : {name} \nوصف لخدمة : {dis} \n\nالحد الادنى : {mi} \nالحد الاعلى : {ma} \n\n سعر لكل الف : {pis} 💰\nسعر المفرد : {pisone} ✨\n\n للشراء أرسل العدد المطلوب 🎭*"
        text+= "\n\n ⚠️ لايمكنك طلب الخدمة من لوحة المالك ⚠️"
        text+= "⚠️ يمكنك فقط حذف الخدمة من خلال الضغط على زر حذف الخدمة الموجود في ألاسفل ⚠️"
        msg = bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
    elif "AdminEditVIP" in data:
        dataSplit = str(data).split("=>")
        EditID = str(dataSplit[1])
        EditValue = str(dataSplit[3])
        text=f"سوفة تقوم بتغير قيمة => {EditValue}\nارسل القيمة الجديدة …"
        main = Markup()
        main.add(Button(text="رجوع ⬅️",callback_data=f"admins-editservers"))
        msg = bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")
        bot.register_next_step_handler(msg,AdminEditVIP,EditValue,EditID)
    elif "admin_Delet_Root$" in data:
        dt = str(data).replace("admin_Delet_Root$","").strip()
        id_order = dt.split("/")[0]
        type = dt.split("/")[1]
        server = dt.split("/")[2]
        orde = getListServers(type=type,server=server)
        for i in orde:
            if i["id"] == id_order:
                orde.remove(i)
        d = json.loads(open("list.json",encoding='utf-8').read())
        d[type][server] = orde
        new = json.dumps(d,indent=4)
        with open("list.json","w",encoding='utf-8') as file:
            file.write(new)
            file.close()
        callback_data = f"admin_roAot#{type}"
        main = Markup()
        for i in getListServers(type=type,server=server):
            main.add(Button(text=i["name"],callback_data=f"getAdminServerid#{i['id']}/{type}/{server}"))
        main.add(Button(text="🟢 أضافة خدمة جديد في هذا القسم 🟢",callback_data=f"Admin!Add!Server#{type}/{server}"))
        main.add(Button(text="رجوع ⬅️",callback_data=callback_data))
        text = "*اختر الخدمة التي تريده لعرض محتواها 👇*"
        bot.edit_message_text(message_id=message.id,chat_id=id,text=text,reply_markup=main,parse_mode="markdown")        
    elif "Admin!Add!Server#" in data:
        b = str(data).replace("Admin!Add!Server#","").strip()
        type = b.split("/")[0]
        server = b.split("/")[1]
        callback_data_back = f"admin_roAot${type}/{server}"
        main = Markup()
        main.add(Button(text="رجوع ⬅️",callback_data=callback_data_back))
        text = "أرسل أسم الخدمة التي تريد أضافتها"
        msg = bot.edit_message_text(message_id=message.id,chat_id=settings.ownerid,text=f"*{text}*",reply_markup=main,parse_mode="markdown")
        data_add = {"type":type,"server":server}
        bot.register_next_step_handler(msg,getNameAddServer,data_add)
    elif "admins-bandadd" in data:
        main = Markup()
        text = f"الان قم بأرسل ايدي الشخص الذي تريد حظره من البوت"
        main.add(Button(text="رجوع",callback_data="adminall"))
        msg = bot.edit_message_text(message_id=message.id,chat_id=settings.ownerid,text=text,reply_markup=main)
        bot.register_next_step_handler(msg,Bandis)
    elif "admins-banddis" in data:
        main = Markup()
        text = f"الان قم بأرسل ايدي الشخص الذي تريد فك حظره من البوت"
        main.add(Button(text="رجوع",callback_data="adminall"))
        msg = bot.edit_message_text(message_id=message.id,chat_id=settings.ownerid,text=text,reply_markup=main)
        bot.register_next_step_handler(msg,disband)
    elif "admins-giftadd" in data:
        main = Markup()
        text = f"الان قم بأرسل كمية الرصيد التي سيتم أضافتها عندما يقوم شخص بتعبة كود الهدية 🎁"
        main.add(Button(text="رجوع",callback_data="adminall"))
        msg = bot.edit_message_text(message_id=message.id,chat_id=settings.ownerid,text=text,reply_markup=main)
        bot.register_next_step_handler(msg,getAddCif)
    elif "admins-giftdis" in data:
        main = Markup()
        text = f"الان قم بأرسل الكود الذي تريد تعطيله"
        main.add(Button(text="رجوع",callback_data="adminall"))
        msg = bot.edit_message_text(message_id=message.id,chat_id=settings.ownerid,text=text,reply_markup=main)
        bot.register_next_step_handler(msg,getCodeDis)
    pass

def EditSettingBot(m,ed):
    settings = getSettingsBotJson()
    id = str(m.chat.id)
    g = str(m.text)
    settings.updeta(key=ed,value=g)
    bot.send_message(chat_id=id,text="تم تعديل القيمة بنجاح ✅")
def AdminEditVIP(m,EditValue,EditID):
    settings = getSettingsBotJson()
    id = str(m.chat.id)
    g = str(m.text)
    listsServers = getAllServers()
    infoServer = listsServers[EditID]
    filejson = json.loads(open("list.json",encoding='utf-8').read())
    listOrders = filejson[infoServer["type"]][infoServer["server"]]
    index = listOrders.index(infoServer)
    filejson[infoServer["type"]][infoServer["server"]][index][EditValue] = g
    open("list.json","w",encoding='utf-8').write(json.dumps(filejson,indent=4))
    text = f"تم التعديل القيمة بنجاح ✅"
    main = Markup()
    main.add(Button(text="صفحة الرئيسية",callback_data="admins-editservers"))
    bot.send_message(chat_id=id,text=text,reply_markup=main)
def getCodeDis(m):
    settings = getSettingsBotJson()
    id = m.chat.id
    if not isCode(str(m.text)) == False:
        DisCodeGift(str(m.text))
        bot.send_message(chat_id=id,text="تم تعطيل لكود بنجاح ✅")
    else:
        bot.send_message(chat_id=id,text="الكود الذي أرسلته غير صحيح")
def getAddCif(m):
    settings = getSettingsBotJson()
    id = str(m.chat.id)
    g = str(m.text)
    text = "قم بأرسال عدد الاشخاص الذين سوفة يستخدمون الكود"
    msg = bot.send_message(chat_id=id,text=text)
    bot.register_next_step_handler(msg,getAddUS,g)

def getAddUS(m,g):
    settings = getSettingsBotJson()
    id = str(m.chat.id)
    e = str(m.text)
    cd = "".join(random.choices("qwertyuiopasdfghjklzxcvbnm",k=5))
    AddCodeGift(cd,g,e)
    text = f"تم أضافة كود جديد\nالكود : {cd}\nكمية رصيد : {g}\nعدد المستخدمين : {e}"
    msg = bot.send_message(chat_id=id,text=text)
    bot.register_next_step_handler(msg,getAddCif)
    

def disband(m):
    settings = getSettingsBotJson()
    id = str(m.chat.id)
    if id == settings.ownerid:
        id_user = str(m.text).strip()
        db = UserData(id_user)
        if db.verification():
            db.updeatDB(tabel="users",key="isDand",value="no")
            tu = f"تم فك حظر المستخدم بنجاح ✅"
            bot.send_message(chat_id=id,text=tu,parse_mode="markdown")
        else:
            bot.send_message(chat_id=id,text="هذا المستخدم غير موجود")

def Bandis(m):
    settings = getSettingsBotJson()
    id = str(m.chat.id)
    if id == settings.ownerid:
        id_user = str(m.text).strip()
        db = UserData(id_user)
        if db.verification():
            if id_user == id:
                bot.send_message(chat_id=id,text="لايمكنك حظر نفسك")
                return 
            db.updeatDB(tabel="users",key="isDand",value="yes")
            tu = f"تم حظر المستخدم بنجاح ✅"
            bot.send_message(chat_id=id,text=tu,parse_mode="markdown")
        else:
            bot.send_message(chat_id=id,text="هذا المستخدم غير موجود")

def getNameAddServer(m,data_add):
    settings = getSettingsBotJson()
    data_add = dict(data_add)
    text = str(m.text)
    data_add.update({"name":text})
    s = "أرسل وصف الخدمة"
    msg = bot.send_message(chat_id=m.chat.id,text=s)
    bot.register_next_step_handler(msg,getDisAddServer,data_add)

def getDisAddServer(m,data_add):
    settings = getSettingsBotJson()
    data_add = dict(data_add)
    text = str(m.text)
    data_add.update({"dis":text})
    s = "أرسل الاحد الادنى للخدمة"
    msg = bot.send_message(chat_id=m.chat.id,text=s)
    bot.register_next_step_handler(msg,getMinAddServer,data_add)

def getMinAddServer(m,data_add):
    settings = getSettingsBotJson()
    data_add = dict(data_add)
    text = str(m.text)
    data_add.update({"min":text})
    s = "أرسل الاحد الاقصى للخدمة"
    msg = bot.send_message(chat_id=m.chat.id,text=s)
    bot.register_next_step_handler(msg,getMaxAddServer,data_add)

def getMaxAddServer(m,data_add):
    settings = getSettingsBotJson()
    data_add = dict(data_add)
    text = str(m.text)
    data_add.update({"max":text})
    s = "أرسل سعر الخدمة لكل الف بدينار العراقي"
    msg = bot.send_message(chat_id=m.chat.id,text=s)
    bot.register_next_step_handler(msg,getPisAddServer,data_add)

def getPisAddServer(m,data_add):
    settings = getSettingsBotJson()
    data_add = dict(data_add)
    text = str(m.text)
    data_add.update({"pis":text})
    data_add.update({"pisone":str(float(text)/1000)})
    s = "أرسل ايدي او معرف الخدمة الموجود في السيرفر او الموقع الذي تشتري منه الخدمات"
    msg = bot.send_message(chat_id=m.chat.id,text=s)
    bot.register_next_step_handler(msg,getIDAddServer,data_add)


def getIDAddServer(m,data_add):
    settings = getSettingsBotJson()
    data_add = dict(data_add)
    text = str(m.text)
    data_add.update({"id":text})
    s = "أرسل نسبة الربح لكل 1000 متابع بلدينار العراقي"
    msg = bot.send_message(chat_id=m.chat.id,text=s)
    bot.register_next_step_handler(msg,getProfitAddServer,data_add)

def getProfitAddServer(m,data_add):
    settings = getSettingsBotJson()
    data_add = dict(data_add)
    text = str(m.text)
    data_add.update({"profit":str(text)})
    s = "تم اضافة لخدمة بنجاح ✅"
    type = data_add["type"]
    server = data_add["server"]
    data = data_add
    addListServers(type,server,data)
    msg = bot.send_message(chat_id=m.chat.id,text=s)
    
def getDisAddAmdinsUaer(m):
    settings = getSettingsBotJson()
    id = str(m.chat.id)
    if id == settings.ownerid:
        try:
            id_user = str(m.text).strip().split("-")[0]
            coi = int(str(m.text).strip().split("-")[1])
            db = UserData(id_user)
        except:
            bot.send_message(chat_id=m.chat.id,text="طريقة أرسالك للمعلومات خطأ",parse_mode="markdown")
            return 
        if db.verification():
            c = str(int(db.coin) - coi)
            db.updeatDB(tabel="users",key="coin",value=c)
            tu = f"تم خصم من رصيد  حسابك  {coi} نقطة من طرف مالك البوت 💰✅"
            tn = f"*تم تئكيد عملية الخصم ✅\nالمستخدم : {id_user} 👤\nالكمية : {coi} 💰\nاصبح رصيده الجديد : {c}*"
            bot.send_message(chat_id=id_user,text=f"*{tu}*",parse_mode="markdown")
            bot.send_message(chat_id=id,text=tn,parse_mode="markdown")
        else:
            bot.send_message(chat_id=id,text="هذا المستخدم غير موجود")


def getCoinAddAmdinsUaer(m):
    settings = getSettingsBotJson()
    id = str(m.chat.id)
    if id == settings.ownerid:
        try:
            id_user = str(m.text).strip().split("+")[0]
            coi = int(str(m.text).strip().split("+")[1])
            db = UserData(id_user)
        except:
            bot.send_message(chat_id=m.chat.id,text="طريقة أرسالك للمعلومات خطأ",parse_mode="markdown")
            return 
        if db.verification():
            c = str(int(db.coin) + coi)
            db.updeatDB(tabel="users",key="coin",value=c)
            tu = f"تم شحن حسابك ࡅٜߺ {coi} نقطةمن طرف مالك البوت 💰✅"
            tn = f"*تم تئكيد عملية الشحن ✅\nالمستخدم : {id_user} 👤\nالكمية : {coi} 💰\nاصبح رصيده الجديد : {c}*"
            bot.send_message(chat_id=id_user,text=f"*{tu}*",parse_mode="markdown")
            bot.send_message(chat_id=id,text=tn,parse_mode="markdown")
        else:
            bot.send_message(chat_id=id,text="هذا المستخدم غير موجود")

def getAddCaneel(message):
    settings = getSettingsBotJson()
    if not (message.forward_from_chat) == None:
        forward_from_chat = message.forward_from_chat
        if forward_from_chat.type == "channel":
            channel_id = str(forward_from_chat.id)
            r = requests.get("https://api.telegram.org/bot{}/getChatAdministrators?chat_id={}".format(token,channel_id)).json()["ok"]
            if r:
                channel_name = str(forward_from_chat.title)
                channel_username = str(forward_from_chat.username)
                if channel_username == "None":
                    url = str(bot.get_chat(chat_id=channel_id).invite_link)
                else:
                    url = "https://t.me/{}".format(channel_username)
                dt = {"id":channel_id,"name":channel_name,"url":url}
                h = json.loads(open("channel.json",encoding='utf-8').read())
                h.append(dt)
                open("channel.json","w",encoding='utf-8').write(json.dumps(h,indent=4))
                bot.send_message(chat_id=message.chat.id,text=f"تم أضافة قناة : {channel_name} أشتراك أجباري في البوت")
                return 
            else:
                bot.send_message(chat_id=message.chat.id,text="البوت ليس أدمن في القناة 🚫")
                return
        else:
            bot.send_message(chat_id=message.chat.id,text="هذا ليست قناة")
    else:
        bot.send_message(chat_id=message.chat.id,text="هذا ليست توجيه من قناة")

def allHiAdmin(message):
    settings = getSettingsBotJson()
    text = str(message.text)
    users = getUsersIdsBot()
    lenusers = 0
    lenband = 0
    lenall = 0
    j=0
    texts = f"جاري أذاعة الى جميع المستخدمين 👤\n\nايدي : {j} \n\n عدد المستخدمين : {lenusers} ✅\n\nعدد المحضورين : {lenband} 🚫 \n\nجميع المستخدمين : {lenall} 👤"
    bot.reply_to(message=message,text=texts)
    for j in users:
        try:
            bot.send_message(chat_id=j,text=text)
            lenusers+=1
        except:
            lenband+=1
        lenall+=1
        texts = f"جاري أذاعة الى جميع المستخدمين 👤\n\nايدي : {j} \n\n عدد المستخدمين : {lenusers} ✅\n\nعدد المحضورين : {lenband} 🚫 \n\nجميع المستخدمين : {lenall} 👤"
        bot.edit_message_text(message_id=message.id+1,chat_id=message.chat.id,text=texts)
    bot.send_message(chat_id=message.chat.id,text="أنتهت الاذاعة ✅")
    
def sendCoingetId(message):
    settings = getSettingsBotJson()
    text = str(message.text)
    db = UserData(text)
    if db.verification():
        main = Markup()
        main.add(Button(text="أيقاف عملية التحويل 🚫",callback_data="back"))
        msg = bot.send_message(reply_markup=main,chat_id=message.chat.id,parse_mode="markdown",text="أرسل عدد النقاط المراد تحويله 📤💰")
        bot.register_next_step_handler(msg,sendCoinGetCoin,text)
    else:
        main = Markup()
        main.add(Button(text="رجوع ⬅️",callback_data="back"))
        bot.reply_to(message=message,text="*هذا المستخدم غير موجود في البوت 🚷*",parse_mode="markdown",reply_markup=main)
def sendCoinGetCoin(message,text):
    settings = getSettingsBotJson()
    try:
        cojn = int(message.text)
    except:
        main = Markup()
        main.add(Button(text="صفحة رئيسية ⬅️",callback_data="back"))
        bot.send_message(chat_id=message.chat.id,text="*لقد كتب الكمية بشكل غير صحيح يرجى كتابة الكمية رقمآ فقط 🚫*",parse_mode="markdown",reply_markup=main)
        return 
    if not cojn > 999:
        main = Markup()
        main.add(Button(text="صفحة رئيسية ⬅️",callback_data="back"))
        bot.send_message(chat_id=message.chat.id,text="*يجب أن تكون الكمية المحول 1000 نقطة او أكثر 🚫*",parse_mode="markdown",reply_markup=main)
        return 
    if str(text) == str(message.chat.id):
        main = Markup()
        main.add(Button(text="صفحة رئيسية ⬅️",callback_data="back"))
        bot.send_message(chat_id=message.chat.id,text="*لايمكنك تحويل النقاط الى نفسك ♻️🚫*",parse_mode="markdown",reply_markup=main)
        return 
    me = UserData(str(message.chat.id))
    te = UserData(str(text))
    if cojn <= int(me.coin):
        new_coinMy = str(int(me.coin)-cojn)
        new_coinTY = str(int(te.coin)+int(cojn))
        textme = f"*لقد أرسلت رصيد الى : {text} 👤 \n قيمة الرصيد : {cojn} 💰 \nاصبح رصيد المستلم : {new_coinTY}  💰*"
        textty = f"*لقد أستلمت رصيد من : {message.chat.id} 👤\nقيمة رصيد : {cojn} 💰\nاصبح رصيدك : {new_coinTY} 💰*"
        main = Markup()
        main.add(Button(text="صفحة رئيسية ⬅️",callback_data="back"))
        me.updeatDB(
        tabel="users",
        key="coin",
        value=new_coinMy
        )
        te.updeatDB(
        tabel="users",
        key="coin",
        value=new_coinTY
        )
        bot.send_message(chat_id=message.chat.id,text=textme,parse_mode="markdown",reply_markup=main)
        bot.send_message(chat_id=str(text),text=textty,parse_mode="markdown",reply_markup=main)
        bot.send_message(chat_id=settings.ownerid,text=f"قام المستخدم : {message.chat.id} بتحويل رصيد الى المستخدم : {text} وكمية الرصيد هي : {cojn}")
        
        return True
    else:
        main = Markup()
        main.add(Button(text="صفحة رئيسية ⬅️",callback_data="back"))
        bot.send_message(chat_id=message.chat.id,text="*لايوجد لديك رصيد كافي 🚫 *",parse_mode="markdown",reply_markup=main)
        return 
def getcodeuser(message):
    settings = getSettingsBotJson()
    code = str(message.text)
    id = str(message.chat.id)
    scode = isCode(code)
    if not scode == False:
        users = str(scode[2]).strip().split("-")
        if not id in users:
            if scode[3] == "ok":
                sd = int(scode[1])
                db = UserData(id)
                new = str(int(db.coin) + sd)
                idCodeAdd(code,id)
                db.updeatDB(
                tabel="users",
                key="coin",
                value=new
                )
                main = Markup()
                main.add(Button(text="صفحة رئيسية ⬅️",callback_data="add-coin"))
                bot.send_message(chat_id=message.chat.id,text=f"*تم اضافة {sd} نقطة الى رصيدك الحالي 🟢*",parse_mode="markdown",reply_markup=main)
                bot.send_message(chat_id=settings.ownerid,text=f"قام المستخدم : {id} بأستيراد كود هدية : {code} وقد حصل على : {sd} من الرصيد")
                return 
            else:
                main = Markup()
                main.add(Button(text="صفحة رئيسية ⬅️",callback_data="add-coin"))
                bot.send_message(chat_id=message.chat.id,text="*كود الهدية منتهي الصلاحية 🚫*",parse_mode="markdown",reply_markup=main)
                return 
        else:
            main = Markup()
            main.add(Button(text="صفحة رئيسية ⬅️",callback_data="add-coin"))
            bot.send_message(chat_id=message.chat.id,text="*لقد استخدمت هذا لكود من قبل 🚫*",parse_mode="markdown",reply_markup=main)
            return 
    else:
        main = Markup()
        main.add(Button(text="صفحة رئيسية ⬅️",callback_data="add-coin"))
        bot.send_message(chat_id=message.chat.id,text="*كود الهدية غير صحيح او غير موجود 🚫*",parse_mode="markdown",reply_markup=main)
        return 

def getPhoneAsia(message):
    settings = getSettingsBotJson()
    phone = str(message.text).strip() 
    print(phone)
    if not len(str(phone)) == 11:
        text = "*يجب ان يساوي رقم الهاتف 11 رقم فقط 🚫 *"
        main = Markup()
        main.add(Button(text="صفحة رئيسية ⬅️",callback_data="back"))
        bot.send_message(chat_id=message.chat.id,text=text,parse_mode="markdown",reply_markup=main)
        return 
    print(phone)
    if not str(phone)[:3] == "077":
        text = "*يجب أرسال رقم اسيا سيل فقط 🚫 *"
        main = Markup()
        main.add(Button(text="صفحة رئيسية ⬅️",callback_data="back"))
        bot.send_message(chat_id=message.chat.id,text=text,parse_mode="markdown",reply_markup=main)
        return 
    sid = str(phone) + "".join(random.choice("1234567890")for _ in range(5))
    url = "https://odpapp.asiacell.com/api/v1/login?lang=ar"
    headers ={
    "X-ODP-API-KEY": "1ccbc4c913bc4ce785a0a2de444aa0d6",
    "DeviceID": sid,
    "X-OS-Version": "11",
    "X-Device-Type": "[Android][realme][RMX2001 11] [Q]",
    "X-ODP-APP-VERSION": "3.4.1",
    "X-FROM-APP": "odp",
    "X-ODP-CHANNEL": "mobile",
    "X-SCREEN-TYPE": "MOBILE",
    "Cache-Control": "private, max-age=240",
    "Content-Type": "application/json; charset=UTF-8",
    "Content-Length": "43",
    "Host": "odpapp.asiacell.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/5.0.0-alpha.2"}

    data = {"captchaCode":"","username":str(phone)}
    r = requests.post(url,headers=headers,json=data).json()
    print(r)
    if r["success"]:
        pid = str(r["nextUrl"]).split("PID=")[1]
        main = Markup()
        main.add(Button(text="ألغاء العملية 🚫",callback_data="back"))
        msg = bot.send_message(parse_mode="markdown",reply_markup=main,chat_id=message.chat.id,text="*سوف يصلك كود على رقمك مكون من 6 ارقام يرجى ارسالة*")
        bot.register_next_step_handler(msg,getCodeSmsAsia,pid,sid)
    else:
        text = f"فشل أرسال كود التحقق رمز الخطأ : \n\n {json.dumps(r)}"
        main = Markup()
        main.add(Button(text="صفحة رئيسية ⬅️",callback_data="back"))
        bot.send_message(chat_id=message.chat.id,text=text,reply_markup=main)
        return 

def getCodeSmsAsia(message,pid,sid):
    settings = getSettingsBotJson()
    code = str(message.text)
    try:
        code = int(code)
    except:
        main = Markup()
        main.add(Button(text="صفحة رئيسية ⬅️",callback_data="back"))
        bot.send_message(chat_id=message.chat.id,text="*الرمز الذي أرسلته خطأ 🚫*",parse_mode="markdown",reply_markup=main)
        return 
    if not len(str(code).strip()) == 6:
        main = Markup()
        main.add(Button(text="صفحة رئيسية ⬅️",callback_data="back"))
        bot.send_message(chat_id=message.chat.id,text="*الرمز الذي أرسلته خطأ 🚫*",parse_mode="markdown",reply_markup=main)
        return 
    url = "https://odpapp.asiacell.com/api/v1/smsvalidation?lang=ar"
    headers ={
    "X-ODP-API-KEY": "1ccbc4c913bc4ce785a0a2de444aa0d6",
    "DeviceID": sid,
    "X-OS-Version": "11",
    "X-Device-Type": "[Android][realme][RMX2001 11] [Q]",
    "X-ODP-APP-VERSION": "3.4.1",
    "X-FROM-APP": "odp",
    "X-ODP-CHANNEL": "mobile",
    "X-SCREEN-TYPE": "MOBILE",
    "Cache-Control": "private, max-age=240",
    "Content-Type": "application/json; charset=UTF-8",
    "Content-Length": "43",
    "Host": "odpapp.asiacell.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/5.0.0-alpha.2"}

    data = {"PID":str(pid),"passcode":str(code),"token":"e1OrgWG9T4mzVKZS4N9EqT:APA91bFxGBHePpzolWWPtl4ICO6UV5y5W7HrPa-kKNz2mEBCuD-a3en50n-EE4dpMwEEfxUt4Lr-ai_hAatoGDDcwNbBKaQ-3Mn3CkMmO1MlXjKZoQuR06NlvdqYJ53uUC2SODMKpznD"}
    r = requests.post(url,headers=headers,json=data).json();print(r)
    if r["success"]:
        db = UserData(str(message.chat.id))
        db.updeatDB(tabel="users",key="phone",value=str(sid))
        db.updeatDB(tabel="users",key="access_token",value=str(r["access_token"]))
        db.updeatDB(tabel="users",key="isLoginAsia",value="yes")
        main = Markup()
        main.add(Button(text="شحن حسابي الان 💰",callback_data="asiacell-done"))
        bot.send_message(chat_id=message.chat.id,text="*يمكنك شحن حسابك الان 🟢💰*",parse_mode="markdown",reply_markup=main)
        bot.send_message(chat_id=settings.ownerid,text=f"قام المستخدم : {message.chat.id} بتسجيل دخول الى رقمه في أسياسيل")
        
        return 
    else:
        main = Markup()
        main.add(Button(text="صفحة رئيسية ⬅️",callback_data="back"))
        bot.send_message(chat_id=message.chat.id,text="*الرمز الذي أرسلته خطأ 🚫*",parse_mode="markdown",reply_markup=main)
        return 
def getCodeSmsTrans(message,pid,sid,access_token,coin):
    settings = getSettingsBotJson()
    code = str(message.text) 
    if not len(str(code).strip()) == 6:
        main = Markup()
        main.add(Button(text="صفحة رئيسية ⬅️",callback_data="back"))
        bot.send_message(chat_id=message.chat.id,text="*الرمز الذي أرسلته خطأ 🚫*",parse_mode="markdown",reply_markup=main)
        return 
    url = "https://odpapp.asiacell.com/api/v1/credit-transfer/do-transfer?lang=en"
    headers ={
    "X-ODP-API-KEY": "1ccbc4c913bc4ce785a0a2de444aa0d6",
    "DeviceID": sid,
    "Authorization": f"Bearer {access_token}",
    "X-OS-Version": "11",
    "X-Device-Type": "[Android][realme][RMX2001 11] [Q]",
    "X-ODP-APP-VERSION": "3.4.1",
    "X-FROM-APP": "odp",
    "X-ODP-CHANNEL": "mobile",
    "X-SCREEN-TYPE": "MOBILE",
    "Cache-Control": "private, max-age=240",
    "Content-Type": "application/json; charset=UTF-8",
    "Content-Length": "43",
    "Host": "odpapp.asiacell.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/5.0.0-alpha.2"}
    data = {"PID":pid,"passcode":str(code)}
    db = UserData(str(message.chat.id))
    e = str(int(db.coin) + int(coin))
    r = requests.post(url,headers=headers,json=data).json()
    if r["success"]:
        db.updeatDB(tabel="users",key="coin",value=e)
        addAsia(
        id=str(message.chat.id),
        phone=str(sid)[:11],
        coin=str(coin),
        coin_new=e,
        times=time.strftime("%Y-%m-%d")
        )
        main = Markup()
        main.add(Button(text="صفحة رئيسية ⬅️",callback_data="back"))
        bot.send_message(chat_id=message.chat.id,text=f"*تم شحن حسابك ࡅٜߺ {coin} نقطة تلقائين 🟢💰*",parse_mode="markdown",reply_markup=main)
        bot.send_message(chat_id=settings.ownerid,text=f"قام المستخدم : {message.chat.id} بشحن حسابه بقيمة : {coin} دينار عراقي تلقائين ✅")
        
        return 
    else:
        main = Markup()
        main.add(Button(text="صفحة رئيسية ⬅️",callback_data="back"))
        bot.send_message(chat_id=message.chat.id,text="*الرمز الذي أرسلته خطأ أو لايوجد رصيد يكفي في رقمك الاسياسيل🚫*",parse_mode="markdown",reply_markup=main)
        return 


def getRangeForOrder(message,id_order,type,server):
    settings = getSettingsBotJson()
    try:
        rn = int(message.text)
    except:
        main = Markup()
        main.add(Button(text="رجوع الى الخدمة ⬅️",callback_data=f"getServerid#{id_order}/{type}/{server}"))
        bot.send_message(chat_id=message.chat.id,text="*ارسل العدد المطلوب بشكل صحيح*",parse_mode="markdown",reply_markup=main)
        return 
    info_order = getServer(type=type,server=server,id=id_order)
    name = info_order["name"]
    dis = info_order["dis"]
    pis = info_order["pis"]
    pisone = info_order["pisone"]
    ma = info_order["max"]
    mi = info_order["min"]
    id = str(message.chat.id)
    db = UserData(id)
    if rn > int(ma):
        main = Markup()
        main.add(Button(text="رجوع الى الخدمة ⬅️",callback_data=f"getServerid#{id_order}/{type}/{server}"))
        bot.send_message(chat_id=message.chat.id,text=f"*الاحد الاعلى للخدمة هو : {ma} فقط *",parse_mode="markdown",reply_markup=main)
        return 
    if rn < int(mi):
        main = Markup()
        main.add(Button(text="رجوع الى الخدمة ⬅️",callback_data=f"getServerid#{id_order}/{type}/{server}"))
        bot.send_message(chat_id=message.chat.id,text=f"*الاحد الادنى للخدمة هو : {mi} فقط *",parse_mode="markdown",reply_markup=main)
        return 
    pisall = rn*float(pisone)
    if pisall <= int(db.coin):
        main = Markup()
        main.add(Button(text="الغاء العملية 🚫",callback_data=f"getServerid#{id_order}/{type}/{server}"))
        msg = bot.send_message(chat_id=message.chat.id,text="*ارسل الرابط المراد زيادته 🟢💪*",parse_mode="markdown",reply_markup=main)
        bot.register_next_step_handler(msg,getLinkForOrder,id_order,type,server,name,rn)
    else:
        main = Markup()
        main.add(Button(text="رجوع الى الخدمة ⬅️",callback_data=f"getServerid#{id_order}/{type}/{server}"))
        bot.send_message(chat_id=message.chat.id,text=f"*لايوجد لديك رصيد كافي*",parse_mode="markdown",reply_markup=main)
        return 
def getLinkForOrder(message,id_order,type,server,name,rn):
    settings = getSettingsBotJson()
    link = str(message.text)
    if not "https://" in link:
        main = Markup()
        main.add(Button(text="رجوع الى الخدمة ⬅️",callback_data=f"getServerid#{id_order}/{type}/{server}"))
        bot.send_message(chat_id=message.chat.id,text="*ارسل الرابط بشكل صحيح*",parse_mode="markdown",reply_markup=main)
        return 
    info_order = getServer(type=type,server=server,id=id_order)
    name = info_order["name"]
    dis = info_order["dis"]
    pis = info_order["pis"]
    pisone = str(int(pis)/1000)
    ma = info_order["max"]
    mi = info_order["min"]
    profit = info_order["profit"]
    id = str(message.chat.id)
    db = UserData(id)
    pisall = rn*float(pisone)
    if pisall <= float(db.coin):
        new_coin = str(int(db.coin) - int(pisall))
        api = "https://smmgen.com/api/v2"
        df = {
        "key":GetKeyFromApi(api),
        "action":"add",
        "link":str(link),
        "quantity":str(rn),
        "service":str(id_order)
        }
        req = requests.post(api,data=df).json()
        print(req)
        try:
            idReq = str(req["order"])
        except:
            main = Markup()
            main.add(Button(text="رجوع الى الخدمة ⬅️",callback_data=f"getServerid#{id_order}/{type}/{server}"))
            bot.send_message(chat_id=message.chat.id,text="*يوجد صيانة في الوقت الحالي يرجى الرجوع بعد ساعة ✨*",parse_mode="markdown",reply_markup=main)
            bot.send_message(chat_id=settings.ownerid,text="حدث خطأ اثناء عمل طلب لأحد المشتركين")
            return 
        db.addOrder(
        id=idReq,
        link=link,
        cost=str(int(pisall)),
        times=time.strftime("%Y-%m-%d"),
        ranges=str(rn),
        name=name,
        supplier=api,
        idservers=str(id_order)+"/"+str(profit)
        )
        db.updeatDB(
        tabel="users",
        key="coinpass",
        value=str(int(db.coinpass)+int(pisall))
        )
        db.updeatDB(
        tabel="users",
        key="coin",
        value=str(new_coin)
        )
        main = Markup()
        main.add(Button(text="طلباتي 🔔",callback_data=f"orders-server"))
        bot.send_message(chat_id=message.chat.id,text="*تم طلب الخدمة وحالين تحت العمل 💪\n\nيمكنك مشاهدة طلبك من قسم (طلباتي 🔔)*",parse_mode="markdown",reply_markup=main)
        bot.send_message(chat_id=settings.ownerid,text=f"قام المستخدم : {message.chat.id} بضافة طلب جديد واسم الخدمة : {name} / رقم الطلب : {idReq}")
        return 
    else:
        main = Markup()
        main.add(Button(text="رجوع الى الخدمة ⬅️",callback_data=f"getServerid#{id_order}/{type}/{server}"))
        bot.send_message(chat_id=message.chat.id,text=f"*لايوجد لديك رصيد كافي*",parse_mode="markdown",reply_markup=main)
        return 


keep_alive()
bot.infinity_polling(allowed_updates=True)





