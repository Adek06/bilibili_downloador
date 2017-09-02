from os import mkdir, chdir, listdir

class creat_folder(object):

	def __init__(self, Ep_name):
		self.Ep_name = Ep_name

	def creat_ep_folder(self):
		try:
			if 'EP' in (listdir(".")):
				chdir('./EP')
				if self.Ep_name in (listdir('.')):
					chdir(str(self.Ep_name))
				else:
					mkdir(str(self.Ep_name))
					chdir(str(self.Ep_name))
			else:
				mkdir('./EP/')
				chdir('./EP')
				mkdir(str(self.Ep_name))
				chdir(str(self.Ep_name))

		except:
			print("在创建文件夹时出了问题")
