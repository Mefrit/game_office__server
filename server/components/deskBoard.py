
from public.server.components.modules.person import Person
import time
class Module_DeskBoard:
    def __init__(self, props):
        self.db = props["db"]

    @staticmethod
    def actionAddRecord(self, data):
        cursor = self.db.cursor()
        print("\n\n",data)
        cursor.execute("INSERT INTO desk_board (id_owner,title,description,id_customer,time_end,price) VALUES ( ?,?,?,?,?,?) ", 
        (data["id_owner"],data["title"],data["description"],data["id_customer"], data["time_end"], data["price"]))
        self.db.commit()
        
        query = """SELECT MAX(`id_record`) FROM desk_board"""
        cursor.execute( query )
        max_id = cursor.fetchall()
        result = {}
        self.db.commit()
        self.db.close()
        result["status"] = "ok"
        result["id_record"] = max_id[0][0]
        return result
        
    def actionGetInfo(self,tmp, data):
        cursor = self.db.cursor()
        query = """ SELECT id_user, nick FROM users """
        cursor.execute( query )
        users = cursor.fetchall()
        
        self.db.commit()
    
        
        query = """SELECT * FROM desk_board"""
        cursor.execute( query )
        tasks = cursor.fetchall()
      
        self.db.commit()
        self.db.close()
        result = {}
        result["status"] = "ok"
        result["users"] = users
        result["tasks"] = tasks
        return result
    def actionDeleteRecord(self,tmp, data):
        cursor = self.db.cursor()

        query = """DELETE  FROM desk_board WHERE id_record =  %s""" % (data["id_record_delete"])
        cursor.execute( query )
        self.db.commit()
        self.db.close()
        result = {}
        result["status"] = "ok"
    
        return result
    def returnAction(self, action, data):
        return getattr(self, "action" + action)(self, data)