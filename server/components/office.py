import time
import json
class Module_office:
    def __init__(self,props):
        self.db = props["db"]
   
    def actionSave(self,data):
        try:
            cursor = self.db.cursor()
            result = {}
            query = """ SELECT COUNT(*) FROM office  WHERE id_office = %s """ % (data["id_office"])
            cursor.execute(query)
            office = cursor.fetchall()
            if(office[0][0] == 0):
                users_data = [(data['id_office'], json.dumps(data['design']))]
                cursor.executemany("INSERT INTO office (id_office, design) VALUES ( ?,? ) ", users_data)
            else:
                query = """
                UPDATE office 
                SET design = '%s'
                WHERE id_office = %d 
                """ % ( json.dumps(data['design']), data['id_office'])  
                cursor.execute(query)
           
            self.db.commit()
            self.db.close()
            result["status"] = "ok"
            return result
        except:
            result = {}
            result["status"] = "fail"
            result["message"] = "Ошибка сохранении дизайна оффиса."
            return result
    def actionGet(self, data):
        try:
            cursor = self.db.cursor()
            query = """ SELECT design FROM office  WHERE id_office = %s """ % (data["id_office"])
            cursor.execute(query)
            design = cursor.fetchall()
            self.db.commit()
            self.db.close()
            result = {};
            result["status"] = "ok"
            result["design"] = design[0][0]
            return result
        except:
            result = {}
            result["status"] = "fail"
            result["message"] = "Ошибка при загрузке дизайна оффиса."
            return result

    def actionGetAnimationConfig(self, data):
        try:
            with open("public/server/files/json/animation.json", "r") as read_file:
                config_skins = json.load(read_file)
            result = {};
            result["status"] = "ok"
            result["config_skins"] = config_skins
            return result
        except:
            result = {}
            result["status"] = "fail"
            result["message"] = "Ошибка при загрузке данных анимации."
            return result
    def actionGetLevelEditorCategories(self, data):
        try:
            with open("public/server/files/json/level_editor_categories.json", encoding='utf-8') as read_file:
                categories = json.load(read_file)
            result = {};
            result["status"] = "ok"
            result["categories"] = categories
            return result
        except:
            result = {}
            result["status"] = "fail"
            result["message"] = "Ошибка при загрузке данных редактора офиса."
            return result

    def returnAction(self ,action, data):
        return getattr(self, "action" + action)( data)