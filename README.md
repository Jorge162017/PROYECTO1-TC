# Proyecto 1 – Teoría de la Computación

Este proyecto implementa un **simulador de autómatas** a partir de expresiones regulares, como parte del curso de **Teoría de la Computación**.

## 🚀 Funcionalidad

El programa permite:

1. **Ingresar una expresión regular en notación infix**.
2. Convertir la expresión a **notación postfix** (usando el algoritmo de Shunting Yard).
3. Construir un **AFN** (Autómata Finito No Determinista).
4. Convertir el AFN a **AFD** (Autómata Finito Determinista).
5. Minimizar el AFD.
6. Generar visualizaciones gráficas (`.png`) de los autómatas en la carpeta `automaton_graphs/`.
7. Probar cadenas de entrada y verificar si son **aceptadas o rechazadas**.

---

## 📂 Estructura del proyecto

```
PROYECTO1-TC/
│
├── modules/
│   ├── AFNToAFD.py              # Conversión de AFN a AFD
│   ├── minimizeAFD.py           # Minimización de AFD
│   ├── regexpToAFN.py           # Construcción de AFN desde regex
│   ├── shunYard.py              # Conversión de infix a postfix
│   ├── simulate.py              # Script principal para correr la simulación
│   └── automaton_graphs/        # Carpeta donde se generan los .gv y .png
│
├── tests.py                     # Casos de prueba
└── README.md                    # Este archivo
```

---

## ⚙️ Instalación

1. **Clonar este repositorio:**
   ```bash
   git clone <URL_DEL_REPO>
   cd PROYECTO1-TC
   ```

2. **Crear un entorno virtual:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate      # Windows
   ```

3. **Instalar dependencias:**
   ```bash
   pip install graphviz colorama
   ```

4. **Instalar Graphviz en el sistema** (necesario para renderizar .png):
   - **macOS (Homebrew):** `brew install graphviz`
   - **Ubuntu/Debian:** `sudo apt-get install graphviz`
   - **Windows:** instalar desde [Graphviz.org](https://graphviz.org/download/)

---

## ▶️ Uso

Ejecuta el simulador con:

```bash
cd modules
python3 simulate.py
```

**Ejemplo de entrada:**
```
Ingrese la expresión regular en infix: (a+b)*abb
Ingrese la cadena a probar: aabb
```

**El programa mostrará:**
- La expresión en postfix.
- La construcción del AFN.
- El AFD y el AFD minimizado.
- Si la cadena es aceptada o rechazada.
- Archivos `.gv` y `.png` generados en `automaton_graphs/`.

---

## 📸 Ejemplo de salida

- `automaton_graphs/_a_b__abb/AFN.gv.png` → gráfico del AFN.
- `automaton_graphs/_a_b__abb/AFD.gv.png` → gráfico del AFD.
- `automaton_graphs/_a_b__abb/Minimized_AFD.gv.png` → gráfico del AFD minimizado.

---

## ✅ Ejemplos de expresiones regulares

- `(a+b)*abb` → Cadenas sobre {a,b} que terminan en **abb**.
- `(0+1)*01` → Cadenas binarias que terminan en **01**.
- `(a+b)(a+b)` → Cadenas de longitud **2**.

---

## 👨‍💻 Autores
Jorge Luis Lopez 221038

Proyecto desarrollado como parte del curso de **Teoría de la Computación**.

**Universidad del Valle de Guatemala – 2024.**