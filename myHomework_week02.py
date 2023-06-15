import maya.cmds as cmds
from random import uniform

#function
def create_planet(planet_name, radius_planet, moons, radius_moon):

	if radius_moon * 2 > radius_planet:		
		cmds.error("ponyatnoe soobshenie")	
		return

	#create planet
	planet = cmds.polySphere(r=radius_planet, n=planet_name)
	
	#create moons
	min_distance = radius_planet + radius_moon
	for i in range(moons): 
		moon_name = "Moon_{}".format(i+1)
		moon = cmds.polySphere(r=radius_moon,n=moon_name)
		group_name = moon_name + "_grp"
		moon_group = cmds.group(empty=1, n=group_name)
		cmds.parent(moon, moon_group)

		distance = uniform(0, 10) + min_distance
		cmds.xform(moon, worldSpace=1, t=[distance,0,0])
		min_distance = distance + 2 * radius_moon

		orbit_angle = uniform(-45, 45)
		rotation_angle = uniform(0, 360)
		cmds.xform(moon_group, ro=[0,rotation_angle,orbit_angle])
		
		

create_planet("Earth",4,5,2)