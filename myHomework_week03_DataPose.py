import maya.cmds as cmds 
import json


def get_all_controls():
    """
    Get all controls 

    """
    controls = cmds.listRelatives(cmds.ls(type="nurbsCurve"), p=1)
    result = {}

    for control_name in controls:
        attributes = {}
        control_attrs = cmds.listAttr(control_name, k=1)
        for attribute_name in control_attrs:
            values = cmds.keyframe(control_name, q=1, attribute=attribute_name,
                time=(1,),valueChange=1) 

            attributes[attribute_name] = values

        result[control_name] = attributes

    return result

       
def save_pose(json_path):
    result = get_all_controls()
    with open(json_path,'w') as f:
        f.write(json.dumps(result, indent=4))

    print("Success!")


save_pose("D:/Dev/DataPose.json")


