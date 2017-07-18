from os import mkdir, chdir, listdir

class creat_folder(object):

	def __init__(self, ep_name):
		self.ep_name = ep_name
	
	def creat_ep_folder(self):
		
		if 'EP' in (listdir(".")):
			pass
		else:
			mkdir('./EP/')

		if self.ep_name in (listdir('./EP/')):
			pass
		else:
			mkdir('./EP/'+str(self.ep_name))
			chdir('./EP/'+str(self.ep_name))