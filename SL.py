class sp: #armamos un class para cada una de las tareas por hacer y asi comprimirlo
    def __init__(self):
        self.super_list =[] #definimos que es una lista
  
    def add_product(self): #para añadir el producto
        product = input (" text the name of the product that u want to add> ")
        self.super_list.append(product) #append funciona para agregar un producto a lo ultimo de la lista
        print (" The product {product} has been added") #las corcheas hacen que puedas llamar a una variable dentro de un mensaje 
        
    def list_products(self): #para listar los productos
       if len(self.super_list)  == 0: #el len funciona para validar si hay algo almacenado dentro de una lista
           print (" there are no products saved")
       else: 
           for product in self.super_list: #usamos el for para buscar especificamente lo que buscamos dentro de la lista 
               print(f"This are the products saveds:  {product}")
    
    def remove_products(self): #para borar una variable
        product = input (" enter the name off the producto to d3l3t3>  ")
        for product in self.super_list: #con el for buscamos especificamente la variable nombrada 
            self.super_list.remove(product) # el remove, funciona para borrar una variable
            print ("the product {product} has been removed  ")
    
        
           