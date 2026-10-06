class Solution(object):
    def minimizeResult(self, expression):
        plus = expression.index('+')
        left = expression[:plus]
        right = expression[plus + 1:]
        best_value = float('inf')
        best_expression = ""
        for i in range(len(left)):
            for j in range(1, len(right) + 1):
                left_before = left[:i]
                left_inside = left[i:]
                right_inside = right[:j]
                right_after = right[j:]
                a = int(left_before) if left_before else 1
                b = int(left_inside)
                c = int(right_inside)
                d = int(right_after) if right_after else 1
                value = a * (b + c) * d
                if value < best_value:
                    best_value = value
                    best_expression = (
                        left_before + "(" +
                        left_inside + "+" +
                        right_inside + ")" +
                        right_after
                    )
        return best_expression