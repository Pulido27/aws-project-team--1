import requests

def buscar_libros():
    url = "http://localhost:5000/search"

    texto = input("¿Qué deseas buscar?: ").strip()

    if not texto:
        print("No se puede buscar una cadena vacía.")
        return

    payload = {
        "query": texto
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()

        data = response.json()
        print("\n Resultados:")
        print(f"Query: {data['query']}")
        print(f"Total libros encontrados: {data['count']}")
        for i, libro in enumerate(data['books'], 1):
            print(f"{i}. {libro}")

    except requests.exceptions.HTTPError as errh:
        print("Error en la respuesta del servidor:", errh)
        print("Detalle:", response.text)
    except requests.exceptions.RequestException as err:
        print("Error en la conexión:", err)

if __name__ == "__main__":
    buscar_libros()
