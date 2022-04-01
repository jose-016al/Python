def string_mas_larga(texto = []):
    for n in texto:
        mas_larga = texto[n]
        tamano = len(mas_larga)
        if tamano < len(texto):
            mas_larga = texto[n]
    return mas_larga

def main():
    print(string_mas_larga(["hola", "como", "estas"]))

if __name__ == "__main__":
    main()