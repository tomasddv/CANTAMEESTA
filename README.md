# ¡Cantá esa palabra! — Streamlit

App móvil para jugar a cantar una canción que contenga una palabra aleatoria. Incluye ruleta animada con sonido, niveles, cronómetro, hasta 10 jugadores con botones alrededor de la palabra, puntos individuales y palabras personalizadas. Los puntos y las palabras usadas se guardan en el navegador.

## Publicar gratis en Streamlit Community Cloud

1. Crear un repositorio en GitHub y subir `app.py`, `cancion_con_la_palabra.html`, `requirements.txt` y la carpeta `.streamlit`.
2. Abrir https://share.streamlit.io/ e iniciar sesión con GitHub.
3. Elegir **Create app**, seleccionar repositorio, rama `main` y archivo principal `app.py`.
4. Pulsar **Deploy** y compartir el enlace que genere Streamlit.

## Ejecución local

```bash
pip install -r requirements.txt
streamlit run app.py
```

> Las palabras personalizadas se almacenan en el navegador de cada jugador (no se sincronizan entre dispositivos). La app necesita conexión para abrirse desde Streamlit, pero el juego en sí no hace peticiones a servidores.

## Jugadores y puntuación

Ingresar entre 1 y 10 nombres (uno por línea) y pulsar **Guardar jugadores**. Los íconos se ubican alrededor de la palabra. Al tocar el ícono de quien acertó, se suma un punto y gira la ruleta para el siguiente turno. Los nombres y puntos se conservan en el almacenamiento local del navegador utilizado. No se sincronizan entre distintos celulares.
