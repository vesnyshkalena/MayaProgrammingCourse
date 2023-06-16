import maya.cmds as cmds
from random import uniform

autoKFstate=cmds.autoKeyframe(q=1,state=1)
cmds.autoKeyframe(state=False)
minTime= cmds.playbackOptions(q=1, minTime=1)
maxTime= cmds.playbackOptions(q=1, maxTime=1)

#function create planet with moons
def create_planet(planet_name, planet_radius, moons, moon_radius):

    if moon_radius * 2 > planet_radius:     
        cmds.error("you need to enter the radius of the moon less")  
        return

    #create planet
    planet = cmds.polySphere(r=planet_radius, n=planet_name)
    planet_group_name = planet_name + "_grp"
    planet_group = cmds.group(empty=1, n=planet_group_name)
    cmds.parent(planet, planet_group_name)

    #create moons
    min_distance = planet_radius + moon_radius
    for i in range(moons): 
        moon_name = "Moon_{}".format(i+1)
        moon = cmds.polySphere(r=moon_radius,n=moon_name)

        #create moon_grp
        moon_group_name = moon_name + "_grp"
        moon_group = cmds.group(empty=1, n=moon_group_name)
        cmds.parent(moon, moon_group)

        #create moon_anim_grp
        moon_anim_group_name = moon_name + "_anim_grp"
        moon_anim_group = cmds.group(empty=1, n=moon_anim_group_name)
        cmds.parent(moon_group, moon_anim_group)

        cmds.parent(moon_anim_group, planet_group)

        distance = uniform(0, 10) + min_distance

        #create orbit
        orbit = cmds.circle(n=moon_name + "_orbit",nr=[0,1,0], r=distance)
        cmds.parent(orbit, planet_group)


        cmds.xform(moon, worldSpace=1, t=[distance,0,0])
        min_distance = distance + 2 * moon_radius

        orbit_angle = uniform(-45, 45)
        rotation_angle = uniform(0, 360)
        cmds.xform(moon_group, ro=[0,rotation_angle,0])
        cmds.xform(orbit, ro=[0,0,orbit_angle])
        cmds.xform(moon_anim_group, ro=[0,0,orbit_angle])

        #animation moons
        cmds.setKeyframe(moon_anim_group, at='rotateY', ott='linear', t=minTime)
        cmds.setKeyframe(moon_anim_group, v=3600, at='rotateY', itt='linear', t=maxTime)

    #animation planet
    cmds.setKeyframe(planet, at='rotateY', ott='linear', t=minTime)
    cmds.setKeyframe(planet, v=360, at='rotateY', itt='linear', t=maxTime)


cmds.autoKeyframe(state=autoKFstate)

create_planet("Earth",4,5,1)