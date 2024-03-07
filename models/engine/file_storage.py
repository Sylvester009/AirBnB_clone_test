#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
      return FileStorage.__objects

    def new(self, obj):
      obj_class_name = obj.__class__.__name__
      obj_key = "{}.{}".format(obj_class_name, obj.id)

      FileStorage.__objects[obj_key] = obj

    def save(self):
      all_obj = FileStorage.__objects

      obj_dict = {}

    for obj in all_obj.keys():
      obj_dict[obj] = all_obj[obj].to_dict()

      with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
        json.dump(obj_dict, file)

  def reload(self):
    if os.path.isfile(FileStorage.__file_path):
      with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
        try:
          obj_dict = json.load(file)
          for key, value in obj_dict.items():
            class_name, obj_id = key.split('.')
            clas = eval(class_name)
            inst = clas(**value)
            FileStorage.__objects[key] = inst
        except Exception:
          pass
