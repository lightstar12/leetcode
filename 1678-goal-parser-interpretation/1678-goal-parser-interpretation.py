class Solution:
    def interpret(self, command: str) -> str:
        interpret = ''
        interpret_part = ''
        for i in range(len(command)):
            if command[i] == 'G':
                interpret = interpret + command[i]
            elif command[i] == '(':
                interpret_part = interpret_part + command[i]
            elif command[i] == ')':
                interpret_part = interpret_part + command[i]
                if interpret_part == '()':
                    interpret = interpret + 'o'
                    interpret_part = ''
                else:
                    interpret = interpret + 'al'
                    interpret_part = ''
            else:
                interpret_part = interpret + command[i]
        return(interpret)