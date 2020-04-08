from pygal_maps_world.i18n import COUNTRIES
import json
import pygal.maps.world

def get_country_code(country_name):
	for code, name in COUNTRIES.items():
		if name ==country_name:
			return code
	return None

with open("population_data.json") as f:
	pop_data=json.load(f)
cc_populations= {}
for pop_dict in pop_data:
	if pop_dict["Year"]== "2010":
		country=pop_dict["Country Name"]
		population =int(float(pop_dict["Value"]))
		code = get_country_code(country)
		if code:
			cc_populations[code]= population

cc_pops_1, cc_pops_2, cc_pops_3= {},{},{}
for cc, pop in cc_populations.items():
	if pop < 10000000:
		cc_pops_1[cc] =pop
	elif pop < 1000000000:
		cc_pops_2[cc] =pop
	else:
		cc_pops_3[cc] =pop
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))
wm_style = pygal.style.RotateStyle('#3399AA',base_style=pygal.style.LightColorizedStyle)
wm = pygal.maps.world.World(style= wm_style)
wm.title = "world population in 2010"
wm.add("0-10m",cc_pops_1)
wm.add("10-1bn",cc_pops_2)
wm.add(">1bn",cc_pops_3)
wm.render_to_file("americas.svg")
