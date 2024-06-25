# calculator/calculations.py
"""Provee diferentes metodos de calcular el valor de ecuaciones diferenciales ordinarias.

Este modulo permite al usuario hacer calculos matematicos.

El modulo contiene las siguientes funciones:

- `ecu(x,t)` - Devuelve el valor de una funcion especifica.
- `euler(ecu, x0, t)` - Devuelve una lista con los valores dx/dt calculandolos mediante el metodo de euler.
- `rk2(ecu, x0, t)` - Devuelve una lista con los valores dx/dt calculandolos mediante el metodo de runge-kutta de orden 2.
- `rk4(ecu, x0, t)` - Devuelve una lista con los valores dx/dt calculandolos mediante el metodo de runge-kutta de orden 4.
"""

from scipy.special import legendre
import numpy as np

t1 = np.linspace(1, 2, 4)


def ecu(x,t):
	"""Ecuación utilizada para los ejemplos. Devuelve un valor.
	
	Examples:
	
	>>> ecu(1,3)
	
	-0.8588799919401328
	
	Args:
	      x (double): valor para calcular x' de la ecuacion diferencial ordinaria
	      t (double): valor para calcular x' de la ecuacion diferencial ordinaria
	Return:
		double: valor de dx/dt según los x y t que se suministrarón a la función.
	"""
	return (-x)**3 + np.sin(t)

def euler(ecu, x0, t):
	"""Devuelve una lista con los valores de la ecuación diferencial utilizando el método numérico de Euler.
	
	Examples:
	
	>>> euler(ecu,0, t1)
	array([0.        , 0.28049033, 0.59711379, 0.85795049])
	
	

    Args:
        ecu (callable): Función que representa la ecuación diferencial dx/dt.
            Debe aceptar dos argumentos: x (valor actual de la variable) y t (tiempo actual).
        x0 (double): Valor inicial de la variable x.
        t (array-like): Arreglo de tiempos en los cuales se evalúa la ecuación diferencial.

    Returns:
        np.ndarray: Arreglo con los valores de la variable x calculados por el método de Euler.
    """
	h = t[1]-t[0]
	x = np.zeros(t.size)
	x[0] = x0
	for i in range(1, t.size):
		x[i] = x[i-1] + h*ecu(x[i-1],t[i-1])
	return x
    
def rk2(ecu, x0, t):
	"""Devuelve una lista con los valores de la ecuación diferencial utilizando Método de Runge-Kutta 2do orden.

	Examples:
	>>> rk2(ecu,0, t1 )
	array([0.        , 0.30556218, 0.60501975, 0.79511031])
	
    Args:
        ecu (callable): Función que representa la ecuación diferencial dx/dt.
            Debe aceptar dos argumentos: x (valor actual de la variable) y t (tiempo actual).
        x0 (double): Valor inicial de la variable x.
        t (array-like): Arreglo de tiempos en los cuales se evalúa la ecuación diferencial.

    Returns:
        np.ndarray: Arreglo con los valores de la variable x calculados por el Método de Runge-Kutta 2do Orden.
    """
	h = t[1]-t[0]
	x = np.zeros(t.size)
	x[0] = x0
	for i in range(1, t.size):
		k1 = h*ecu(x[i-1],t[i-1])
		k2 = h*ecu(x[i-1] + 0.5*k1,t[i-1] + h*0.5)
		x[i]= x[i-1] + k2
	return x
    
def rk4(ecu, x0, t):
	"""Devuelve una lista con los valores de la ecuación diferencial utilizando Método de Runge-Kutta 4to orden.


	Examples:
	
	>>> rk4(ecu,0, t1)
	array([0.        , 0.3027825 , 0.5988007 , 0.79754751])
	
    Args:
        ecu (callable): Función que representa la ecuación diferencial dx/dt.
            Debe aceptar dos argumentos: x (valor actual de la variable) y t (tiempo actual).
        x0 (double): Valor inicial de la variable x.
        t (array-like): Arreglo de tiempos en los cuales se evalúa la ecuación diferencial.

    Returns:
        np.ndarray: Arreglo con los valores de la variable x calculados por el Método de Runge-Kutta 4to Orden.
    """
	h = t[1]-t[0]
	x = np.zeros(t.size)
	x[0] = x0
	for i in range(1, t.size):
		k1 = h*ecu(x[i-1],t[i-1])
		k2 = h*ecu(x[i-1] + 0.5*k1,t[i-1] + h*0.5)
		k3 = h*ecu(x[i-1] + 0.5*k2,t[i-1] + h*0.5)
		k4 = h*ecu(x[i-1] + k3,t[i-1] + h)
		x[i]= x[i-1] + (k1 + 2*k2+2*k3+k4)/6
	return x

