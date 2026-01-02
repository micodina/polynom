package : src/polynom/*.py
	python3 -m build
	
clean :
	rm dist/*

publish : 
	python3 -m twine upload --repository testpypi dist/*
