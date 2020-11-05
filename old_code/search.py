def ser(dz):
	for i in os.listdir(dz):
		local=dz+'\\'+i
		if osp.isdir(local):
			print(dz)
			ser(local)
		else:
			print('    ',i)
