import re

def read_current_languages():
    with open('languages.txt', 'r') as file:
        return file.read().splitlines()


def generate_markdown(languages):
    markdown = ""
    for lang in languages:
        # Replace with actual URL to the language icon
        markdown += f"![{lang}](https://img.shields.io/badge/{lang}-blue.svg) "
    return markdown

def update_readme(markdown):
    with open('README.md', 'r+') as file:
        content = file.read()
        content = re.sub(r'<!--langs_start-->.*<!--langs_end-->', f'<!--langs_start-->{markdown}<!--langs_end-->', content, flags=re.DOTALL)
        file.seek(0)
        file.write(content)
        file.truncate()

languages = read_current_languages()
markdown = generate_markdown(languages)
update_readme(markdown)
