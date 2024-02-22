from flask import Flask
# Import ENABLED from configuration file_ PLUGINS Dictionary
from Config.modules import ENABLED_PLUGINS
import importlib  # Import the importlib module for dynamically loading modules and classes

app = Flask(__name__)  # Create Flask application instance

# Browser cookie key configuration (a key string should be provided when needed)
# app.config['SECRET_KEY'] = 'your_secret_key'

# Dynamically loading and registering plugins
for plugin_name, plugin_path in ENABLED_PLUGINS.items():
    # Splitting the plugin path to obtain module and class names
    # module_name: Extension.Demo.route, class_name: setup
    module_name, class_name = plugin_path.rsplit('.', 1)
    module = importlib.import_module(module_name)  # Dynamic import module
    PluginClass = getattr(module, class_name)  # Get classes from modules
    plugin_instance = PluginClass()  # Create an instance of a class
    # Registering Flask Blueprint Objects
    app.register_blueprint(plugin_instance.blueprint)


@app.route('/')
def index():
    return "ChatAI"


# Program entry
if __name__ == '__main__':
    app.run(debug=True)
