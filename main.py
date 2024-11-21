import random
import time
import sys

# Base class for plugins
class Plugin:
    def perform_operation(self, *args):
        raise NotImplementedError("This method should be overridden by subclasses.")

# Idea Maker Plugin
class IdeaMakerPlugin(Plugin):
    def __init__(self):
        self.idea_templates = [
            "Write a story about a [adjective] [noun] who [verb].",
            "Create a business plan for a [adjective] [noun] that helps people [verb].",
            "Design an app that combines [concept] and [concept] to solve [problem].",
            "Develop a project focusing on [topic] with [focus].",
            "Compare [currency1] and [currency2] for the best exchange rate."
        ]
        self.words = {
            "adjective": ["brave", "mysterious", "ancient", "futuristic", "innovative", "creative"],
            "noun": ["explorer", "robot", "wizard", "detective", "startup", "community"],
            "verb": ["discovers", "invents", "travels", "solves", "creates", "analyzes"],
            "concept": ["AI", "blockchain", "sustainability", "wellness", "education", "technology"],
            "problem": ["climate change", "mental health", "education", "urban living", "poverty", "inequality"],
            "topic": ["technology", "health", "finance", "entertainment", "art", "environment"],
            "focus": ["efficiency", "appeal", "functionality", "usability"],
            "currency1": ["USD", "EUR", "GBP", "AUD"],
            "currency2": ["INR", "JPY", "CNY", "CAD"]
        }

    def perform_operation(self, *args):
        if args:
            added_items = ", ".join(args)
            return f"✨ Successfully added {added_items} to the algorithm!"
        else:
            template = random.choice(self.idea_templates)
            for word_type, word_list in self.words.items():
                word = random.choice(word_list)
                template = template.replace(f"[{word_type}]", word, 1)
            return f"💡 Generated Idea: {template}"

# Plugin Manager
class PluginManager:
    def __init__(self):
        self.plugins = {
            'idea_maker': IdeaMakerPlugin()
        }

    def execute_plugin(self, name, *args):
        plugin = self.plugins.get(name)
        if plugin:
            result = plugin.perform_operation(*args)
            return f"✅ Executed plugin '{name}' with result: {result}\n" + self.get_suggested_apps()
        else:
            return f"❌ No plugin found with the name '{name}'."

    def get_suggested_apps(self):
        apps = [
            "1. **Termux** (F-Droid): A powerful terminal emulator for Android to run Python. [Download](https://f-droid.org/packages/com.termux/)\n   - **Usage**: Install Python and run the script.",
            "2. **Pydroid 3** (Google Play Store): A Python IDE for Android. [Download](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3)\n   - **Usage**: Create a new file, paste your script, and run it.",
            "3. **QPython 3L** (Google Play Store): A script engine for Android. [Download](https://play.google.com/store/apps/details?id=org.qpython.qpy3)\n   - **Usage**: Create a new script, paste the code, and execute it.",
            "4. **AIDE** (Android IDE): IDE that supports Python. [Download](https://play.google.com/store/apps/details?id=com.aide.ui)\n   - **Usage**: Create a new project, add your Python script, and run it.",
            "5. **GitHub**: Use the GitHub mobile app to manage your repositories. [Android](https://play.google.com/store/apps/details?id=com.github.android) | [iOS](https://apps.apple.com/us/app/github/id1477376905)"
        ]
        return "📲 Suggested Apps:\n" + "\n".join(apps)

def typing_animation(text, delay=0.05):
    """Simulates typing animation in the console."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    manager = PluginManager()
    typing_animation("🌟 Welcome to the Idea Generator by Not Insane! 🌟")
    typing_animation("Type 'exit' to quit the program.")

    while True:
        typing_animation("\nAvailable plugins: idea_maker")
        plugin_name = input("🔍 Enter the plugin name to execute: ").strip()
        
        if plugin_name.lower() == 'exit':
            typing_animation("🚪 Exiting the program. Goodbye!")
            break
        
        if plugin_name in manager.plugins:
            args = input("✍️ Enter arguments (comma-separated, leave empty for random idea): ").strip()
            args = args.split(",") if args else []
            result = manager.execute_plugin(plugin_name, *args)
            typing_animation(result)
        else:
            typing_animation("⚠️ Invalid plugin name. Please try again.")

if __name__ == '__main__':
    main()