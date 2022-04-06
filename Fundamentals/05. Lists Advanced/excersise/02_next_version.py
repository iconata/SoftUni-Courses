version = [int(x) for x in input().split(".")]
if version[2] == 9 and version[1] == 9:
	version[0] = version[0] + 1
	version[1] = 0
	version[2] = 0
elif 0 <= version[2] < 9:
	version[2] = version[2] + 1
elif version[2] == 9:
	version[2] = 0
	if version[2] == 0:
		if version[1] < 9:
			version[1] = version[1] + 1
		else:
			version[1] = 0

print(*version, sep=".")
