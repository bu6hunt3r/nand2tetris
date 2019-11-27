#!/usr/bin/env python2
import os

COMMENT = '//'

class Parser(object):
    def __init__(self, vm_filename):
        self.vm_filename = vm_filename
        self.vm = open(vm_filename, 'r')
        self.commands = self.commands_dict()
        self.curr_instruction = None
        self.initialize_file()

    def advance(self):
        self.curr_instruction = self.next_instruction
        self.load_next_instruction()
    
    @property
    def has_more_commands(self):
        return bool(self.next_instruction)

    @property
    def command_type(self):
        return self.commands.get(self.curr_instruction)
 
    def load_next_instruction(self, line=None):
        line = line if line is not None else self.vm.readline().strip()
        self.next_instruction = line.split(COMMENT)[0].strip().split()

    def commands_dict(self):
        return {
            'add'       : 'C_ARITHMETIC',
            'sub'       : 'C_ARITHMETIC',
            'neg'       : 'C_ARITHMETIC',
            'eq'        : 'C_ARITHMETIC',
            'gt'        : 'C_ARITHMETIC',            
            'lt'        : 'C_ARITHMETIC',                        
            'and'       : 'C_ARITHMETIC',                        
            'or'        : 'C_ARITHMETIC',                        
            'not'       : 'C_ARITHMETIC', 
            'push'      : 'C_PUSH',                                                           
            'pop'       : 'C_POP',                                                                       
            'label'     : 'C_LABEL',
            'goto'      : 'C_GOTO',                                                                                   
            'if_goto'   : 'C_IF',                                                                                               
            'function'  : 'C_FUNCTION',
            'return'    : 'C_RETURN',
            'call'      : 'C_CALL',
        }

class CodeWriter(object):
    def __init__(self, asm_filename):
        return None
    
    def set_filename(self, asm_filename):
        self.asm = open(asm_filename, 'w')
        self.curr_file = None
        self.bool_count = 0 # Number of boolean comparisons so far
        self.addresses = self.address_dict()

class Main(object):
    def __init__(self, file_path):
        self.parse_files(file_path)
        self.cw = CodeWriter(self.asm_file)
        for vm_file in vm_files:
            self.translate(vm_file)
    
    def parse_files(self, file_path):
        if '.vm' in file_path:
            self.asm_file = file_path.replace('.vm', '.asm')
            self.vm_files = [file_path]
        else:
            file_path = file_path[:-1] if file_path[-1] == '/' else file_path
            path_elements = file_path.split('/')
            path = '/'.join(path_elements)
            self.asm_file = path + '/' + path_elements[-1] + '.asm' 
            dirpath, dirnames, filenames = next(os.walk(file_path), [[], [], []])
            vm_files = filter(lambda x: '.vm' in x, filenames)
            self.vm_files = [path + '/' + vm_file for vm_file in vm_files]
    
    def translate(self, vm_file):
        parser = Parser(vm_file)

if __name__ == "__main__":
    import sys

    file_path=sys.argv[1]
    Main(file_path)