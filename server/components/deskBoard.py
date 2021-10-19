
from public.server.components.modules.person import Person
import time
class Module_DeskBoard:
    def __init__(self, props):
        self.db = props["db"]
        # self.pers = Person(name)

    @staticmethod
    def actionAddRecord(self, data):
        print("\n\n\n")
        print(data)
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO desk_board (owner,title,description) VALUES ( ?,?,? ) ", (data["owner"],data["title"],data["description"]))
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
        # desk_board
        
    def actionGetRecord(self,tmp, data):
        print("\n\n\n")
        print(data)
        cursor = self.db.cursor()
     
        
        query = """SELECT * FROM desk_board"""
        cursor.execute( query )
        tasks = cursor.fetchall()
        result = {}
        self.db.commit()
        self.db.close()
        result["status"] = "ok"
        result["tasks"] = tasks
        return result
        # desk_board

    def returnAction(self, action, data):
        print(data)
        return getattr(self, "action" + action)(self, data)

    def actionDeleteRecord(self,tmp, data):
        print("\n\n\n")
        print(data)
        cursor = self.db.cursor()
     
        
        query = """DELETE  FROM desk_board WHERE id_record =  %s""" % (data["id_record_delete"])

        print (query)
        print ("\n\n\n")
        cursor.execute( query )
        self.db.commit()
        self.db.close()
        result = {}
        result["status"] = "ok"
    
        return result
        # desk_board