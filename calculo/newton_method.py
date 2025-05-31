# calculo/newton_method.py

def newton_raphson(func, func_derivada, x0, tolerancia=1e-7, max_iteracoes=100):
    """
    Encontra a raiz de uma função usando o método de Newton-Raphson.
    Retorna uma tupla: (raiz, iteracoes, mensagem)
    """
    xn = x0
    for n in range(max_iteracoes):
        fxn = func(xn)
        if abs(fxn) < tolerancia:
            # Retorna os 3 valores esperados pela view
            return xn, n + 1, f"Solução encontrada após {n + 1} iterações."

        Dfxn = func_derivada(xn)
        if abs(Dfxn) < 1e-12: # Para evitar divisão por um número muito próximo de zero
            # Se a derivada é próxima de zero, mas f(x) já satisfaz a tolerância, consideramos uma solução
            if abs(fxn) < tolerancia:
                 return xn, n + 1, f"Solução encontrada (derivada próxima de zero, mas f(x) dentro da tolerância) após {n + 1} iterações."
            # Caso contrário, não podemos prosseguir
            return None, n + 1, f"Derivada próxima de zero (Dfxn={Dfxn:.2e}) encontrada na iteração {n + 1} em xn={xn:.4f} e f(xn)={fxn:.2e}. O método não pode continuar com segurança."
        
        xn_novo = xn - fxn / Dfxn
        xn = xn_novo

    # Após o loop, verifica uma última vez se a condição de tolerância para f(xn) foi atingida
    fxn_final = func(xn)
    if abs(fxn_final) < tolerancia:
        return xn, max_iteracoes, f"Solução encontrada na última iteração ({max_iteracoes}) permitida."

    # Se não convergiu após o máximo de iterações
    return None, max_iteracoes, f"Excedido o número máximo de {max_iteracoes} iterações. Não convergiu (f(x_final) = {fxn_final:.2e}, x_final = {xn:.4f})."

# O bloco if __name__ == "__main__": abaixo é para teste e pode ser mantido ou removido.
# Ele não afeta a execução quando o Django importa esta função.
if __name__ == "__main__":
    def minha_funcao(x):
        return x**2 - 4
    def minha_funcao_derivada(x):
        return 2*x

    raiz, iters, msg = newton_raphson(minha_funcao, minha_funcao_derivada, 1.0)
    print(f"Raiz: {raiz}, Iterações: {iters}, Mensagem: {msg}")

    raiz, iters, msg = newton_raphson(minha_funcao, minha_funcao_derivada, 3.0)
    print(f"Raiz: {raiz}, Iterações: {iters}, Mensagem: {msg}")

    def f_sem_raiz_real_perto(x): return x**2 + 4
    def df_sem_raiz_real_perto(x): return 2*x
    raiz, iters, msg = newton_raphson(f_sem_raiz_real_perto, df_sem_raiz_real_perto, 1.0)
    print(f"Raiz: {raiz}, Iterações: {iters}, Mensagem: {msg}")