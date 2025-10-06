import os
from pathlib import Path

# pointers:
tee = '- '
last = '- '


def tree(dir_path: Path):
    contents = sorted(dir_path.iterdir(), key=lambda x: x.name)
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        if (path.name not in [
            'assets',
            'generar_directorio.py',
            '.obsidian',
            'subir_cambios.ps1',
            'subir_cambios.sh',
            'package.json',
            '.vscode',
            '.nojekyll',
            '_coverpage.md',
            '_sidebar.md',
            'index.html',
            '.git',
            '.dist',
            'tags',
            'propuesta-nueva-estructura-api.md'
        ]):
            print(path.name)
            if path.name == 'docs':
                yield ''
            if path.is_dir():
                folder_name = ' '.join(path.name.split('-')).title()
                folder_indent_size = len(f'{path}'.split(os.sep)) - 2
                folder_indent = '  ' * folder_indent_size
                if folder_name != 'Docs':
                    yield f'{folder_indent}- <b class="title-badge">{folder_name}</b>'
            else:
                corrected_path = path
                file_indent_size = len(f'{corrected_path}'.split(os.sep)) - 2
                file_indent = '  ' * file_indent_size
                file_name = ' '.join(path.name.split('-')).split('.')[0].title()
                yield file_indent + pointer + f'[{file_name}](./{corrected_path})'
            if path.is_dir():
                yield from tree(path)


with open('_sidebar.md', 'w') as directorio_md:
    directorio_md.write('- <b class="title-badge">Home</b>\n')
    for line in tree(Path('.')):
        directorio_md.write(line + '\n')
