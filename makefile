resultado.png : 17.py solucion.txt
	python 17.py

solucion.txt : 17.x
	./17.x
	rm 17.x

17.x : 17.cpp solar.png
	c++ 17.cpp -o 17.x

solar.png : 16.py 
	python 16.py

sigma.png : 15.py
	python 15.py

clear :
	rm sigma.png sola.png