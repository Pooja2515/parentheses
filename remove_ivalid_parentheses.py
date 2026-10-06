class Solution(object):
    def removeInvalidParentheses(self, s):
        def isValid(string):
            count = 0
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        queue = [s]
        visited = set([s])
        while queue:
            next_level = []
            for string in queue:
                if isValid(string):
                    return [
                        x for x in queue
                        if isValid(x)
                    ]
            for string in queue:
                for i in range(len(string)):
                    if string[i] not in '()':
                        continue
                    new_string = string[:i] + string[i + 1:]
                    if new_string not in visited:
                        visited.add(new_string)
                        next_level.append(new_string)
            queue = next_level
        return [""]