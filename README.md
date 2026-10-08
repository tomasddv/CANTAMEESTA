# ¡Cantá esa palabra! — Streamlit

App móvil para jugar a cantar una canción que contenga una palabra aleatoria. Incluye niveles, cronómetro, palabras personalizadas y juego sin repetir hasta agotar el mazo.

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
