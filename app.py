from dash import Dash
import dash_bootstrap_components as dbc
from components.layout import layout
from components.callbacks import register_callbacks

# Initialisation de l'application Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Visualisation Cours Bitcoin"

# Définition du layout
theme_class = "light-mode"  # Par défaut en mode clair
app.layout = layout(theme_class)

# Enregistrement des callbacks
register_callbacks(app)

# Lancer le serveur
if __name__ == "__main__":
    app.run_server(debug=True)