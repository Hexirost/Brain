OBJECT_PATH = "Objects/"
OBJECT_LIST_PATH = OBJECT_PATH + "ObjectList.txt"

class Object:
    def __init__(self, name, value = "", obj_type = ""):
        self.name = name
        self.obj_type = obj_type.strip().lower()
        self.value = value 

        str_text = ""
        if not obj_type or obj_type == "str":
            str_text = name + " = \"\""
            obj_type = "str"
        
        elif obj_type == "int":
            str_text = name + " = " + str(value)

        new_obj_file = open(OBJECT_PATH+name,"x")
        new_obj_file.write(str_text)
        new_obj_file.close()

        obj_list_file = open(OBJECT_LIST_PATH,"a")
        obj_list_file.write((obj_type + " " + name + " " + value + "\n"))
        obj_list_file.close()
    
    def __repr__(self):
        return self.value

    def __str__(self):
        return self.obj_type + " " + self.name + " " + self.value


        
