class Node:
    def __init__(self, path, name, type, size=0):
        self.path = path
        self.name = name
        self.type = type
        self.size = size
        self.children = []
        self.dir_sizes = []

    def add_child(self, path, name, type, size = 0):
        self.children.append(Node(path, name, type, size))

    def find_node(self, path):
        if self.path == path: 
            return self
        for node in self.children:
            n = node.find_node(path)
            if n: return n
        return None

    def print_tree(self):
        print(self.path + ' ' + self.name + ' ' + self.type + ' ' + str(self.size))
        for child in self.children:
            child.print_tree()

    # each dir has a size field that should be the sum of all 
    # child files and dirs
    # need to recurse through tree and update all sizes starting at the 
    # lowest level first
    def update_dir_sizes(self, node):
        sum = 0
        if node:
            for child in node.children:
                if child.type == 'dir':
                    child.size = self.update_dir_sizes(child)
                    self.dir_sizes.append(child.size)
                sum += child.size
        return sum

    # for some reason the update_dir_sizes function doesn't sum up the root level
    # and I don't feel like figuring out why
    # so, this function does that instead
    # it's not pretty but it works
    def add_top_level_dir_sizes(self):
        sum = 0
        for child in self.children:
            sum += child.size
        self.dir_sizes.append(sum)



# Given file with a stream of commands, parse the commands to build
# a data tree consisting of directories and files
# Uses the filepath as a kind of key to find correct nodes
def generate_tree(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')

    tree = None
    current_path = ""

    for i, line in enumerate(lines):
        parts = line.split(' ')

        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "/":
                    # update the current path
                    current_path = "/"
                    # create root node
                    tree = Node(current_path, parts[2], 'dir')
                elif parts[2] == "..":
                    # going up a level
                    current_path = current_path[:current_path.rfind('/')]
                else:
                    # going into a new dir
                    #
                    # first level already has the forward slash, so don't add 
                    # if we're already in the top directory
                    if current_path != '/':
                        current_path += '/' + parts[2]
                    else:
                        current_path += parts[2]
            elif parts[1] == "ls":
                continue
        # else, must be a file or directory
        else:
            if parts[0] == 'dir':
                # this conditional gets around the issue of the root level current_path already having '/'
                # finds the node of the current path and adds the appropriate dir as a child
                if current_path != '/':
                    tree.find_node(current_path).add_child(current_path + '/' + parts[1], parts[1], 'dir')
                else:
                    tree.find_node(current_path).add_child(current_path + parts[1], parts[1], 'dir')
                
            else:
                # this conditional gets around the issue of the root level current_path already having '/'
                # finds the node of the current path and adds the appropriate file as a child
                if current_path != '/':
                    tree.find_node(current_path).add_child(current_path + '/' + parts[1], parts[1], 'file', int(parts[0]))
                else:
                    tree.find_node(current_path).add_child(current_path + parts[1], parts[1], 'file', int(parts[0]))

    return tree

def main_part1(filename):
    # generate the tree from input
    tree = generate_tree(filename)

    # update the dir sizes once all the commands are parsed
    tree.update_dir_sizes(tree)

    # get the list of dir sizes and order smallest to largest
    sizes = tree.dir_sizes
    sizes.sort()

    sum = 0
    # iterate through the list and sum values <= 100000
    for elem in sizes:
        if elem > 100000:
            break
        sum += elem

    return sum

def main_part2(filename):
    # generate the tree from input
    tree = generate_tree(filename)

    # update the dir sizes once all the commands are parsed
    tree.update_dir_sizes(tree)

    # realized that it the dir sizes for the top level weren't calculated
    # it didn't matter in part 1, so here is a patch to get that value in here
    tree.add_top_level_dir_sizes()

    # get the list of dir sizes and order largest to smallest
    sizes = tree.dir_sizes
    sizes.sort(reverse=True)

    total_disk_space = 70000000
    minimum_unused_space = 30000000
    used_disk_space = sizes[0]     # largest, thus full size

    # calculate the space needed to free 
    needed_disk_space = minimum_unused_space - (total_disk_space - used_disk_space)
    # iterate through the list and return smallest value of any value > needed_disk_space
    # do this by finding the first element which is < needed_disk_space, then backing up 1 element
    for i, elem in enumerate(sizes):
        if elem < needed_disk_space:
            return sizes[i-1]

print("Day 07-1 Output: ", main_part1('input.txt'))
print("Day 07-2 Output: ", main_part2('input.txt'))