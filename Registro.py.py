import os
import sys

if(len(sys.argv) == 1):
    print("No se han introducido argumentos!!")
    sys.exit()

if (os.path.exists(sys.argv[1]) == False):
    with open(sys.argv[1], "w+") as creator:
        creator.write("Cédula;Nombres;Apellidos;Edad\n")

def CedExist(x):
    with open(sys.argv[1], "r") as reader:
        if x + ";" in reader.read():
            return True

def Search():
    searchCed = input("\nIntroduzca la cédula a buscar: ")
    finded = ""
    
    if(searchCed == ""):
        print("No se han ingresado datos!!")    
    elif(CedExist(searchCed)):
        with open(sys.argv[1], "r") as reader:
            data = reader.readlines()
            for i in data:
                valor = i[0:i.index(';') + 1]
                if (valor == searchCed + ";" and searchCed != "Cédula"):
                    finded = i
        
    if finded == "":
        print("\nLa cédula introducida no existe...")
    
    return finded, searchCed

while (True):
    menu = input("\n1. Capturar\n2. Listar\n3. Búsqueda\n4. Editar\n5. Eliminar\n6. Salir\n")
    
    if(menu == "1"):
        while(True):
            ced = input("\nCédula: ")
            name = input("Nombre: ")
            ape = input("Apellidos: ")
            age = input("Edad: ")
            
            if(ced == "" and name == "" and ape == "" and age == ""):
                break
            
            if(CedExist(ced)):
                print("\nLa cédula ya existe, favor escribir la correcta!!")
            else:
                while (True):
                    opt = input("\nGuardar(G), Rehacer(R), Salir(S)\n")
                    
                    if (opt == "G"):
                        with open(sys.argv[1], "a") as writer:
                            writer.write(ced + ";" + name + ";" + ape + ";" + age + "\n")
                        break
                    elif(opt == "R"):
                        break
                    elif(opt == "S"):
                        sys.exit()
                    else:
                        continue
    elif (menu == "2"):
        print()
        with open(sys.argv[1], "r") as reader:
            data = reader.read().split("\n")
            for i in data:
                print(i)
    elif (menu == "3"):
        finded, searchCed = Search()
        
        print(finded)
    elif (menu == "4"):
        finded, searchCed = Search()
        
        
        
        if(finded == "" and searchCed == ""):
            continue
            
        print(finded)
        
        while (True):
            newCed = input("Para cambiar los datos, escriba los nuevos valores\nCédula: ")
            newName = input("Nombre: ")
            newApe = input("Apellidos: ")
            newAge = input("Edad: ")
            newInfo = newCed + ";" + newName + ";" + newApe + ";" + newAge + "\n"
            
            if (newCed == "" and newName == "" and newApe == "" and newAge == ""):
                break
                
            if(searchCed == newCed):
                with open(sys.argv[1], "r+") as reader, open(sys.argv[1], "a") as writer:
                    data = reader.readlines()
                    reader.truncate(0)
                    for line in data:
                        if finded in line:
                            line = line.replace(finded, newInfo)
                        writer.write(line)
                break
            elif(CedExist(newCed)):
                print("\nLa cédula ya existe, favor escribir otra...\n")
            else:
                with open(sys.argv[1], "r+") as reader, open(sys.argv[1], "a") as writer:
                    data = reader.readlines()
                    reader.truncate(0)
                    for line in data:
                        if finded in line:
                            line = line.replace(finded, newInfo)
                        writer.write(line)
                break
    elif (menu == "5"):
        finded, searchCed = Search()
        
        if(finded == "" and searchCed == ""):
            continue
        
        print(finded)
        
        while(True):
            confirm = input("¿Deseas eliminar este usuario? (Y/N)\n")
            
            if(confirm == "Y"):
                with open(sys.argv[1], "r+") as reader:
                    data = reader.readlines()
                    
                os.remove(sys.argv[1])
                    
                with open(sys.argv[1], "w+") as creator:
                    for line in data:
                        if finded in line:
                            line = ""
                        creator.write(line)
                break
            elif(confirm == "N"):
                break
            else:
                print("La opción elegida no es válida!!\n")
    elif (menu == "6"):
        sys.exit()
    else:
        print("La opción introducida no es válida!!")