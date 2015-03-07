class Singleton (object):
    instance = None       
    def __new__(cls, *args, **kargs): 
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kargs)
        return cls.instance

"""definimos el objecto"""

MySingletonUno = Singleton()
MySingletonDos = Singleton()

MySingletonUno.nuevo = "hola"
print MySingletonDos.nuevo


"""Creamos otra instancia del mismo objecto, que almacena la variable nuevo"""


NuevoSingleton = Singleton()
print NuevoSingleton.nuevo

