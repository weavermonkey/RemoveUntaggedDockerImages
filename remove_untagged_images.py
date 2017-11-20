import subprocess

x = subprocess.check_output( [ "docker", "images", "-q" ] ).split('\n')

for curr_image in x:
	docker_ls = subprocess.Popen( ["docker","images"], stdout=subprocess.PIPE)
	untagged_image = subprocess.Popen( ["grep", curr_image], stdin=docker_ls.stdout,stdout=subprocess.PIPE)
	result = untagged_image.communicate()[0]
	if "<none>" in result:
		print "removing image with id : ",untagged_image
		subprocess.call( ["docker", "rmi", curr_image, "-f"])
