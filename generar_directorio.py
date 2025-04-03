from pathlib import Path
import os

# prefix components:
space =  '    '
branch = '    '
# pointers:
tee =    '  * '
last =   '  * '


# Extracted from https://stackoverflow.com/a/59109706/13132076 
# with some modifications to generate a markdown index.
def tree(dir_path: Path, prefix: str='', is_dir:bool=False):
    """Generar un directorio markdown

    Args:
        dir_path (Path): dirección de la carpeta actual
        prefix (str, optional): Lo que poner antes del nombre. Defaults to ''.
        is_dir (bool, optional): ¿Es carpeta?. Defaults to False.

    Yields:
        string: Nombre de carpeta o archivo en formato markdown
    """
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
        ]):
            if '.git' in path.parts or '.dist' in path.parts:
                continue
            if path.is_dir():
                folder_name = ' '.join(path.name.split('-')).title()
                yield f'* {folder_name}'
            else:
                corrected_path = f'{path.relative_to(dir_path.parent)}'
                corrected_path = '/'.join(corrected_path.split('\\'))
                file_name = ' '.join(path.name.split('-')).split('.')[0].title()
                yield pointer + f'[{file_name}](./{corrected_path})'
            if path.is_dir():
                extension = branch if pointer == tee else space 
                yield from tree(path, prefix=prefix+extension, is_dir=True)
            

with open('_sidebar.md', 'w') as directorio_md:
    directorio_md.write('* Home\n\n')
    for line in tree(Path('.')):
        directorio_md.write(line + '\n')