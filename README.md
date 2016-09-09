# PythonClient

## Prepare

- Clone this repository
- Checkout 2 branches `swagger-builder` & `conda-build-template` and pull from those 2 branches

## Generate Swagger Client

- Checkout branch `swagger-builder`
- Open `swagger_package_builder` project with `Pycharm`
- Edit `main.py` with your package's information:


	```python
	    name = 'package-name'
	    version = '0.0.0'
	    service = 'http://swagger-service/'
	```

- Run `main.py`
- A `package-name` folder will appear in project
- Create `MANIFEST.in` file in that `package-name` folder (Change `package-name` in last line to your package name):


	```
	include AUTHORS.rst
	include CONTRIBUTING.rst
	include HISTORY.rst
	include LICENSE
	include README.rst

	recursive-include tests *
	recursive-exclude * __pycache__
	recursive-exclude * *.py[co]

	recursive-include docs *.rst conf.py Makefile make.bat *.jpg *.png *.gif
	recursive-include package-name *
	```

- Copy `package-name` folder to somewhere else (Optional)

# Build Conda Package

- Checkout branch `conda-build-template`
- Edit `../conda-build/meta.yaml` file:


	```
	package:
	# 1.Change to your package name & version
	  name:  your_package_name
	    version: "1.0.0"

	    source:
	# 2. Change `/source/path` to your package directory
	      path: /source/path

	      requirements:
	        build:
		    - python
		        - setuptools

			  run:
			      - python
	```

- Change directory out of `conda-build` folder and run:

	```
	conda build conda-build/
	```

- If build successful, a package will appear in `$CONDA_HOME/conda-bld/linux-64/`
- Make a diretory `channel` in anywhere you want and run:
	
	```
	cd channel/
	conda convert --platform all /$CONDA_HOME/conda-bld/linux-64/package_name-verson.tar.bz2
	conda index linux-64 osx-64 win-64 win-32 linux-32
	cd ..
	conda index channel
	```

- Your local channel is ready
