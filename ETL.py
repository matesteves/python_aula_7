import csv

def read_csv(file_path: str) -> list[dict]:
    lista = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        #print(file)
        reader = csv.DictReader(file) # just an iterator
        #print(reader)
        for i in csv.DictReader(file):
            lista.append(i)
    return lista