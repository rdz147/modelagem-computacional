# test_sympy_minimal.py
import sys
import sympy

print(f"Versão do Python: {sys.version}")
print(f"Versão do SymPy: {sympy.__version__}")
print("-" * 30)

try:
    print("Iniciando teste mínimo do SymPy...")

    x = sympy.symbols('x')
    print(f"1. sympy.symbols('x'): {x} (Tipo: {type(x)})")

    expr_str = "x**2 + x" # Uma expressão simples
    expr = sympy.sympify(expr_str)
    print(f"2. sympy.sympify('{expr_str}'): {expr} (Tipo: {type(expr)})")

    deriv = sympy.diff(expr, x)
    print(f"3. sympy.diff(expr, x): {deriv} (Tipo: {type(deriv)})")

    f_lamb = sympy.lambdify(x, expr, modules=['math'])
    print(f"4. sympy.lambdify(x, expr) criada.")

    val_test = 2
    resultado_lambdify = f_lamb(val_test)
    print(f"5. Teste f_lamb({val_test}): {resultado_lambdify}")

    print("-" * 30)
    print(">>> Teste mínimo do SymPy CONCLUÍDO SEM O ERRO ESPERADO <<<")

except TypeError as e:
    if 'cannot unpack non-iterable float object' in str(e):
        print("-" * 30)
        print(f">>> ERRO REPRODUZIDO (TypeError): {e} <<<")
    else:
        print("-" * 30)
        print(f">>> Outro TypeError ocorreu: {e} <<<")
except Exception as e:
    print("-" * 30)
    print(f">>> Outra exceção ocorreu: {e} <<<")