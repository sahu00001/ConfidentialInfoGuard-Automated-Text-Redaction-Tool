setup(
	name='project1',
	version='1.0',
	author='Sujata Sahu',
	authour_email='sujata.sahu-1@ou.edu',
	packages=find_packages(exclude=('tests', 'docs')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']	
)
