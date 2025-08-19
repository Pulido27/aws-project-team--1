# 📚 BookSearcher

&#x20;

Una aplicación para buscar palabras o frases en una colección de libros, mostrando en qué títulos aparecen y en qué posición. Ideal para investigadores, lectores curiosos y cualquier persona que necesite rastrear términos específicos en textos.

---

## 📑 Tabla de contenidos

- [Características](#características)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Uso](#uso)
  - [Generación de índices (](#generación-de-índices-genfiles)[`genfiles`](#generación-de-índices-genfiles)[)](#generación-de-índices-genfiles)
  - [Búsqueda local (](#búsqueda-local-booksearcher)[`bookSearcher`](#búsqueda-local-booksearcher)[)](#búsqueda-local-booksearcher)
  - [Peticiones web (FastAPI)](#peticiones-web-fastapi)
- [Pruebas](#pruebas)

---

## ✨ Características

- Búsqueda exacta y por conjunto de palabras
- Índices binarios precomputados para alta velocidad
- Soporte de búsqueda tanto en consola como vía API HTTP
- Estructura modular que separa generación de índices y motor de búsqueda

---

## 🗂️ Estructura del proyecto

```
booksearcher/
├── genfiles/            # Scripts para generar índices binarios
│   ├── gen_titles.py    # Genera Titulos.txt con los títulos de los libros
    ├── gen_dic.py       # Dependencia interna de gen_index.py
│   ├── gen_index.py     # Crea archivos .bin con índices de palabras
│   ├── gen_posBin.py    # Genera pos.bin con offsets de línea en Titulos.txt
│   └── test/            # Pruebas unitarias (pytest)
│
├── bookSearcher/        # Lógica del motor de búsqueda
│   ├─── recurPar.py     # Búsqueda recursiva en índices
│   └─── test/           # Pruebas unitarias (pytest)
│
├── cliente.py           # Cliente HTTP para FastAPI
├── app.py               # Servidor FastAPI (endpoint `/search`)
├── requirements.txt     # Dependencias del proyecto
└── README.md
```

---

## ⚙️ Instalación

1. Clona el repositorio
   ```bash
   git clone https://github.com/Pulido27/aws-project-team--1
   cd booksearcher
   ```
2. Crea y activa un entorno virtual
   ```bash
   python -m venv venv
   source venv/bin/activate    # Windows: .\venv\Scripts\activate
   ```
3. Instala las dependencias
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Uso

### Generación de índices (`genfiles`)

1. Genera el listado de títulos
   ```bash
   python genfiles/gen_titles.py
   ```
2. Crea los índices binarios
   ```bash
   python genfiles/gen_index.py
   ```
3. Calcula posiciones de línea
   ```bash
   python genfiles/gen_posBin.py
   ```

> **Nota:** `gen_dic.py` es utilizado internamente por `gen_index.py`.

---

### Búsqueda local (`bookSearcher`)

Ejecuta la búsqueda desde consola:

```bash
python bookSearcher/main.py --query "término de búsqueda"
```

O con el script principal:

```bash
python bookSearcher/recurPar.py --query "término"
```

---

### Peticiones web (FastAPI)

1. Activa el entorno virtual (si no está activo).
2. Inicia el servidor:
   ```bash
   uvicorn app:app --host 127.0.0.1 --port 8000
   ```
3. En otra terminal, ejecuta el cliente interactivo:
   ```bash
   python bookSearcher/cliente.py
   ```

---

## ✅ Pruebas

Con Pytest:

```bash
pytest --maxfail=1 --disable-warnings -q
```

- **bookSearcher\_test**: pruebas para el script de búsqueda con rutas de test.
- **genFiles\_test**: pruebas unitarias de la lógica del motor.

