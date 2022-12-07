from utils import read_text_file

commands = read_text_file('day07input.txt').splitlines()

# $ - commands
#     cd
#        dirname - go into dir
#        .. - go up one dir
#        / - go to root
#     ls
#        starts with "dir" - directory
#        starts with number - filesize, filename

# build a tree of directories
# each node has a name, a parent, and a list of children
# each node also has a list of files
# each file has a name and a size


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f'File({self.name}, {self.size})'


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []

    def __repr__(self):
        return f'Dir({self.name}, {self.parent})'

    def add_child(self, child):
        self.children.append(child)

    def add_file(self, file):
        self.files.append(file)

    def get_path(self):
        if self.parent is None:
            return self.name
        else:
            return self.parent.get_path() + '/' + self.name

    def get_size(self):
        size = 0
        for file in self.files:
            size += file.size
        for child in self.children:
            size += child.get_size()
        return size


def process_command(command, directory):
    if command.startswith('$ ls'):
        return directory

    if command.startswith('$ cd'):
        dirname = command[5:]
        if dirname == '..':
            directory = directory.parent
        elif dirname == '/':
            directory = root
        else:
            for child in directory.children:
                if child.name == dirname:
                    directory = child
                    break
            else:
                new_dir = Directory(dirname, directory)
                directory.add_child(new_dir)
                directory = new_dir
        return directory

    if command.startswith('dir'):
        name = command[4:]
        new_dir = Directory(name, directory)
        directory.add_child(new_dir)
    else:
        size, name = command.split(' ', 1)
        size = int(size)
        new_file = File(name, size)
        directory.add_file(new_file)

    return directory


root = Directory('root')
current = root
for c in commands:
    current = process_command(c, current)
    # print(current.get_path(), current.get_size())


def get_directory_sizes(root):
    sizes = []
    # sizes.append((root.get_path(), root.get_size()))
    for child in root.children:
        sizes.append((child.get_path(), child.get_size()))
        sizes.extend(get_directory_sizes(child))
    return sizes


# Part A
dir_list = get_directory_sizes(root)
sizes_at_most_100000 = [s for s in dir_list if s[1] <= 100000]
total_size = sum([s[1] for s in sizes_at_most_100000])
print("Part A:", total_size)

# Part B
TOTAL_SPACE = 70000000
SPACE_NEEDED = 30000000
used = root.get_size()
free = TOTAL_SPACE - used
needed = SPACE_NEEDED - free
delete_candidates = [d for d in dir_list if d[1] >= needed]
name, size = min(delete_candidates, key=lambda x: x[1])
print("Part B:", size)
