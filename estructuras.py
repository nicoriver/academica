lista = ["apple", "samsung"]
print("lista original", lista)
lista.append("nokia")
print("lista alterada", lista)
lista.remove("apple")
print("lista removida", lista)
lista[0]="huawei"
print("lista modificada", lista)
print("lista modificada", len(lista))

tupla = ("aplle", "xiamo")
print("tupla", tupla)


diccionario1={
    "marca":"aplle",
    "modelo":"iphone3" ,
    "precio":999   

}
print("diccionario", diccionario1)
print("diccionario", diccionario1["marca"])
diccionario1["marca"] = "apple"
print("diccionario", diccionario1)
diccionario1["color"] = "gris"
print("diccionario", diccionario1)
diccionario1.pop("color")
print("diccionario", diccionario1)