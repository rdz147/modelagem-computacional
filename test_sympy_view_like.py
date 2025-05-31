# test_sympy_view_like.py
import sys
import sympy
from sympy.core.expr import Expr

print(f"Versão do Python: {sys.version}")
print(f"Versão do SymPy: {sympy.__version__}")
print("-" * 30)

funcao_str_usuario = "(x**2)" # A função que estava dando erro no Django
# funcao_str_usuario = "x**2" # Teste também sem os parênteses
# funcao_str_usuario = "sin(x)" # Teste com uma função do local_scope

print(f"Testando com a função: '{funcao_str_usuario}'")
print("-" * 30)

try:
    x_sym = sympy.symbols('x')

    allowed_functions = {
        "sin": sympy.sin, "cos": sympy.cos, "tan": sympy.tan,
        "exp": sympy.exp, "ln": sympy.log, "log": sympy.log,
        "log10": lambda arg: sympy.log(arg, 10),
        "sqrt": sympy.sqrt, "abs": sympy.Abs, "fabs": sympy.Abs,
        "pi": sympy.pi, "e": sympy.E,
        "asin": sympy.asin, "acos": sympy.acos, "atan": sympy.atan,
        "sinh": sympy.sinh, "cosh": sympy.cosh, "tanh": sympy.tanh,
    }
    local_scope = allowed_functions.copy()
    local_scope['x'] = x_sym

    print("1. Preparando para sympify...")
    func_sympy = sympy.sympify(funcao_str_usuario, locals=local_scope)
    print(f"   Resultado do sympify: {func_sympy} (Tipo: {type(func_sympy)})")

    print("2. Verificando se é Expr...")
    if not isinstance(func_sympy, Expr):
        raise ValueError(f"A função '{funcao_str_usuario}' não foi interpretada como uma expressão matemática escalar válida.")
    print("   É uma Expr válida.")

    print("3. Verificando se é um número...")
    if func_sympy.is_number:
        if sympy.Eq(func_sympy, 0):
            raise ValueError("A função fornecida é '0'.")
        else:
            raise ValueError(f"A função fornecida é uma constante '{func_sympy}'.")
    print("   Não é um número (contém 'x' ou é uma expressão simbólica).")

    print("4. Calculando a derivada...")
    derivada_sympy = sympy.diff(func_sympy, x_sym)
    print(f"   Derivada: {derivada_sympy} (Tipo: {type(derivada_sympy)})")

    print("5. Criando função chamável (lambdify) para f(x)...")
    func_callable = sympy.lambdify(x_sym, func_sympy, modules=['math'])
    print("   func_callable criada.")
    print(f"   Teste func_callable(2): {func_callable(2)}")


    print("6. Criando função chamável (lambdify) para f'(x)...")
    derivada_callable = sympy.lambdify(x_sym, derivada_sympy, modules=['math'])
    print("   derivada_callable criada.")
    print(f"   Teste derivada_callable(2): {derivada_callable(2)}")

    print("-" * 30)
    print(">>> Teste 'view-like' do SymPy CONCLUÍDO SEM O ERRO ESPERADO <<<")

except TypeError as e:
    if 'cannot unpack non-iterable float object' in str(e):
        print("-" * 30)
        print(f">>> ERRO REPRODUZIDO (TypeError): {e} <<<")
    else:
        print("-" * 30)
        print(f">>> Outro TypeError ocorreu: {e} <<<")
except ValueError as e:
    print("-" * 30)
    print(f">>> ERRO (ValueError): {e} <<<") # Captura os ValueErrors que adicionamos
except Exception as e:
    print("-" * 30)
    print(f">>> Outra exceção ocorreu: {e} <<<")