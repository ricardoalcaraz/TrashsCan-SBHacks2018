all:
	swig -python -c++ -o _display_module.cc wrapper.i
	python setup.py build_ext --inplace
