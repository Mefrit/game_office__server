
from public.server.components.modules.person import Person
import time
class Module_PresentationBoard:
    def __init__(self, props):
        self.db = props["db"]
        # self.pers = Person(name)

    @staticmethod
    def actionGetUrlByNum(self, data):
   
        # cursor = self.db.cursor()
        # cursor.execute("INSERT INTO desk_board (owner,title,description) VALUES ( ?,?,? ) ", (data["owner"],data["title"],data["description"]))
        # self.db.commit()
        

        result = {}

        result["status"] = "ok"
        result["count_slides"] = 6
        result["curent_url"] = "./static/src/images/presentation/" +  str(data["id_presentation"]) + "/"+  str(data["id_presentation"]) + "_" +  str(data["num_slide"]) + ".jpg"
        return result
        
  

    def returnAction(self, action, data):
        print(data)
        return getattr(self, "action" + action)(self, data)

  
        # desk_board