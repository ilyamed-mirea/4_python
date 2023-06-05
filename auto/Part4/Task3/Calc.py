class Num:
    def __init__(self, value):
        self.value = value


class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class PrintVisitor:
    def visit(self, node):
        method_name = f"visit_{node.__class__.__name__}"
        method = getattr(self, method_name)
        return method(node)

    def visit_Num(self, node):
        return str(node.value)

    def visit_Add(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return f"({left} + {right})"

    def visit_Mul(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return f"({left} * {right})"


class CalcVisitor:
    def visit(self, node):
        method_name = f"visit_{node.__class__.__name__}"
        method = getattr(self, method_name)
        return method(node)

    def visit_Num(self, node):
        return node.value

    def visit_Add(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return left + right

    def visit_Mul(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return left * right


class StackVisitor:
    def visit(self, node):
        method_name = f"visit_{node.__class__.__name__}"
        method = getattr(self, method_name)
        return method(node)

    def visit_Num(self, node):
        return f"PUSH {node.value}"

    def visit_Add(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return f"{left}\n{right}\nADD"

    def visit_Mul(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return f"{left}\n{right}\nMUL"


ast = Add(Num(2), Mul(Num(140), Num(213)))

pv = PrintVisitor()
print(pv.visit(ast))

cv = CalcVisitor()
print(cv.visit(ast))

sv = StackVisitor()
print(sv.visit(ast))