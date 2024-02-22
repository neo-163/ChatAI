# config/modules.py

SYSTEM_PLUGINS = {
    # 'System.Demo': 'System.Demo.route.setup',
}

EXTENSION_PLUGINS = {
    'Extension.Demo': 'Extension.Demo.route.setup',
    # 'Extension.OpenAI': 'Extension.OpenAI.route.setup',
    # 'Extension.ERNIEBot': 'Extension.ERNIEBot.route.setup',
    # 'Extension.Qwen': 'Extension.Qwen.route.setup',
    # 'Extension.Classify': 'Extension.Classify.route.setup',
}

# These are mandatory modules that must be loaded, and some modules can be selectively loaded
ENABLED_PLUGINS = {**SYSTEM_PLUGINS, **EXTENSION_PLUGINS}
