
from public.server.components.modules.person import Person
import time

class Module_GeoPosition:
    def __init__(self, props):
        self.db = props["db"]

    @staticmethod
    def actionGetInfo(self, data):
        try:
            result = {
                "users": self.pers.GetId(),
                "posX": self.pers.GetPosX(),
                "posY": self.pers.GetPosY()
            }
            return result
        except:
            result = {}
            result["status"] = "fail"
            result["message"] = "Ошибка при получении  информации о пользователе"
            return result

    def returnAction(self, action, data):
        return getattr(self, "action" + action)(self, data)

    def deleteOflineUsers(self):
        cursor = self.db.cursor()
        time_to_kik = time.time() - 1000000
        query = """ SELECT id_user FROM users WHERE time_start_session < %d OR  time_start_session IS NULL   """ % (time_to_kik)
        cursor.execute(query)
        kik_users = cursor.fetchall()
        cache_id = []

        for row in kik_users:
            cache_id.append(row[0])
        query = """
                UPDATE users 
                SET online = %d 
                WHERE id_user IN (%s) 
                """ % (0, ",".join(str(x) for x in cache_id) )
        cursor.execute(query)
        self.db.commit()

    def getCoordOnlineUsers(self):
        cursor = self.db.cursor()
        query = """ SELECT id_user,x, y, skin, nick FROM users WHERE online = 1   """ 
        cursor.execute(query)
        online_users = cursor.fetchall()
    
        return online_users
    def actionGetAllUsers(self, obj, data):
    
        cursor = self.db.cursor()
        
        query = """
                UPDATE users 
                SET time_start_session = %d , online = %d
                WHERE id_user = %s 
                """ % (time.time(),1, data['data']["id_curent_user"] )

        cursor.execute(query)
        self.db.commit()
        result = {}
        self.deleteOflineUsers()
       
  
        online_users = self.getCoordOnlineUsers() 
        result = {}
        result["status"] = "ok"
        result["online_users"] = online_users
        return result

    def actionSetUserCoord(self,obj,data):
        result = {}
        result["status"] = "ok"
        result["message"] = 'wait'
        cursor = self.db.cursor()
        
        query = """
                UPDATE users 
                SET x = %s , y = %s
                WHERE id_user = %s 
                """ % (data["x"], data["y"] , data["id_curent_user"] )

        cursor.execute(query)
        self.db.commit()
        return result