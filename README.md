# Proyecto FastAPI

API básica desarrollada con [FastAPI](https://fastapi.tiangolo.com/) y [Uvicorn](https://www.uvicorn.org/).

---

## Requisitos previos

- **Python 3.9** o superior instalado en tu sistema.
- **Git** instalado.

---

## Instrucciones para levantar el proyecto

### 1. Clonar el repositorio (si aún no lo tienes localmente)

```bash
git clone https://github.com/Juanito-Diaz/FASTAPI.git
cd FASTAPI
```

---

### 2. Crear y activar el entorno virtual

#### En macOS / Linux:

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate
```

#### En Windows:

- **Usando PowerShell:**
  ```powershell
  # Crear entorno virtual
  python -m venv venv

  # Activar entorno virtual
  venv\Scripts\Activate.ps1
  ```
  > *Nota: Si PowerShell arroja un error de ejecución de scripts, ejecuta primero en tu terminal: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`*

- **Usando Símbolo del sistema (CMD):**
  ```cmd
  # Crear entorno virtual
  python -m venv venv

  # Activar entorno virtual
  venv\Scripts\activate.bat
  ```

---

### 3. Instalar dependencias

Una vez activado el entorno virtual, instala las librerías necesarias con:

```bash
pip install -r requirements.txt
```

---

### 4. Ejecutar el servidor de desarrollo

Inicia el servidor local con recarga automática:

```bash
uvicorn main:app --reload
```

El servidor estará corriendo en: **`http://127.0.0.1:8000`**

---

## Documentación interactiva de la API

FastAPI genera documentación interactiva automáticamente. Con el servidor corriendo, puedes acceder a:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
