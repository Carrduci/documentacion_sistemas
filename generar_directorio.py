from pathlib import Path

# prefix components:
space =  '    '
branch = '    '
# pointers:
tee =    '  - '
last =   '  - '

# Extracted from https://stackoverflow.com/a/59109706/13132076 
# with some modifications to generate a markdown index.
def tree(dir_path: Path, prefix: str='', is_dir:bool=False):
    """
    A recursive generator, given a directory Path object
    will yield a visual tree structure line by line
    with each line prefixed by the same characters
    """
    contents = sorted(dir_path.iterdir(), key=lambda x: x.name)
    # contents each get pointers that are ├── with a final └── :
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        if (path.name != 'assets'):
            if '.git' in path.parts or '.dist' in path.parts:
                continue
            if path.is_dir():
                yield  prefix + pointer + f'[{path.name}/]({path.relative_to(dir_path.parent)})'
            else:
                yield  prefix + pointer + f'[{path.name}]({path.relative_to(dir_path.parent)})'
            if path.is_dir(): # extend the prefix and recurse:
                extension = branch if pointer == tee else space 
                # i.e. space because last, └── , above so no more |
                yield from tree(path, prefix=prefix+extension, is_dir=True)
            

with open('directorio.md', 'w') as directorio_md:
    directorio_md.write('# Directorio De Manuales De Sistemas\n\n')
    for line in tree(Path('.')):
        directorio_md.write(line + '\n')