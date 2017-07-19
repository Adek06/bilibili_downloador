from os import mkdir, chdir, listdir

class creat_folder(object):

	def __init__(self, Ep_name):
		self.Ep_name = Ep_name
	
	def creat_ep_folder(self):
		
		if 'EP' in (listdir(".")):
			pass
		else:
			mkdir('./EP/')

		if self.Ep_name in (listdir('./EP/')):
			pass
		else:
			mkdir('./EP/'+str(self.Ep_name))
		
