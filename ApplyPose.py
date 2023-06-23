import maya.cmds as cmds 
import json


def apply_pose(json_path):
    with open(json_path, 'r') as f:
        pose = json.load(f)

    for control_name, attributes in pose.items():
        print(control_name)
        for attribute_name, value in attributes.items():
            if value is not None:
                cmds.setAttr(control_name + '.' + attribute_name, value[0])
                


apply_pose("D:/Dev/DataPose.json")        



     