import os
import sys
import pkgutil
import importlib

if "bpy" in locals():

	importlib.reload(operator_anim_export)
	

else:
	import bpy

	from . import (
		operator_anim_export
	)


def register(bl_info):


	# for mod_num in sorted(list(modules)):
	# 	mod = locals()[modules[mod_num]['name']]
	# 	if hasattr(mod, "register"):
	# 		getattr(mod, "register")()
	# 	else:
	# 		print("Error, {} does not have a register function".format(
	# 			modules[mod_num]['name']))

	operator_anim_export.register()



def unregister(bl_info):

	operator_anim_export.unregister()