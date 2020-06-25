def dict_combine():
	"""结合两个字典"""
	code_dict = dict([(43236678, 98000000), (76776678, 98000001), (33356678, 98000002)])
	device_dict = dict([(98000000, 'dee-sss-333'), (98000001, 'srr-koo-118')])
	for c in code_dict:
		code_dict[c] = device_dict.get(code_dict[c], '')
	return code_dict


print(dict_combine())