install-deps:
	pip3 install -r requirements.txt

test:
	export PYTHONPATH=.; \
	python -m unittest tests/edempresence_test.py

run:
	export PYTHONPATH=.; \
	python3 bin/edempresence-gui.py
