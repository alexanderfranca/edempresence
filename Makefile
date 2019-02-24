install-deps:
	yaml

test:
	export PYTHONPATH=.; \
	python -m unittest tests/edempresence_test.py

run:
	export PYTHONPATH=.; \
	python3 bin/edempresence-gui.py
