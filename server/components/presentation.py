
from public.server.components.modules.person import Person

class Module_PresentationBoard:
    def __init__(self, props):
        self.db = props["db"]

    @staticmethod
    def actionGetUrlByNum(self, data):
        result = {}
        result["status"] = "ok"
        result["count_slides"] = 6
        result["curent_url"] = "./static/src/images/presentation/" +  str(data["id_presentation"]) + "/"+  str(data["id_presentation"]) + "_" +  str(data["num_slide"]) + ".jpg"
        return result

    def returnAction(self, action, data):
        print(data)
        return getattr(self, "action" + action)(self, data)
