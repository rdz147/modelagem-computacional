# calculo/bissecao_logic.py

def metodo_bissecao(func, a, b, tolerancia=1e-7, max_iteracoes=100):
    """
    Encontra a raiz de uma função usando o método da Bisseção.

    Parâmetros:
    func (callable): A função para a qual a raiz está sendo procurada.
    a (float): O limite inferior do intervalo inicial.
    b (float): O limite superior do intervalo inicial.
    tolerancia (float): A tolerância para a convergência (largura do intervalo ou |f(m)|).
    max_iteracoes (int): O número máximo de iterações permitidas.

    Retorna:
    tuple: (raiz, iteracoes, mensagem_status)
           raiz (float | None): A raiz aproximada ou None se não convergir/erro.
           iteracoes (int): Número de iterações realizadas.
           mensagem_status (str): Mensagem descrevendo o resultado.
    """
    fa = func(a)
    fb = func(b)

    if fa * fb >= 0:
        return None, 0, "Erro: f(a) e f(b) devem ter sinais opostos para garantir uma raiz no intervalo."

    if abs(fa) < tolerancia: #caso 'a' já seja a raiz
        return a, 0, "O ponto 'a' já é uma raiz dentro da tolerância."
    if abs(fb) < tolerancia: #caso 'b' já seja a raiz
        return b, 0, "O ponto 'b' já é uma raiz dentro da tolerância."

    iter_count = 0
    for i in range(max_iteracoes):
        iter_count = i + 1
        m = (a + b) / 2.0  #ponto medio
        fm = func(m)

        #critério de parada: |f(m)| < tol OU largura do intervalo < tol
        if abs(fm) < tolerancia or (b - a) / 2.0 < tolerancia:
            return m, iter_count, f"Solução encontrada após {iter_count} iterações."

        if fa * fm < 0: #a raiz tá no intervalo [a, m]
            b = m
            # fb = fm #opcional, mas pode economizar uma chamada de func se não reavaliar fb
        else: #a raiz tá no intervalo [m, b]
            a = m
            fa = fm #atualiza fa para a próxima iteração

    #se chegou aqui, o máximo de iterações foi atingido sem satisfazer a tolerância principal
    m_final = (a + b) / 2.0
    return m_final, max_iteracoes, f"Máximo de {max_iteracoes} iterações atingido. Última aproximação: {m_final:.10f} (f(m)={func(m_final):.2e}, intervalo_final=[{a:.5f}, {b:.5f}])."

#exemplo de uso
if __name__ == "__main__":
    def minha_funcao_exemplo(x):
        return x**3 - x - 2 #raiz próxima de 1.52

    #teste 1: sucesso
    a1, b1 = 1.0, 2.0
    raiz, iters, msg = metodo_bissecao(minha_funcao_exemplo, a1, b1, tolerancia=1e-5)
    print(f"Teste 1 - Intervalo [{a1}, {b1}]")
    print(f"Raiz: {raiz}, Iterações: {iters}, Mensagem: {msg}\n")

    #teste 2: f(a) e f(b) com mesmo sinal
    a2, b2 = -1.0, 0.0
    raiz, iters, msg = metodo_bissecao(minha_funcao_exemplo, a2, b2)
    print(f"Teste 2 - Intervalo [{a2}, {b2}]")
    print(f"Raiz: {raiz}, Iterações: {iters}, Mensagem: {msg}\n")
    
    #teste 3: número máximo de iterações
    a3, b3 = 1.0, 2.0
    raiz, iters, msg = metodo_bissecao(minha_funcao_exemplo, a3, b3, tolerancia=1e-15, max_iteracoes=20)
    print(f"Teste 3 - Intervalo [{a3}, {b3}], max_iter=20")
    print(f"Raiz: {raiz}, Iterações: {iters}, Mensagem: {msg}\n")

    #teste 4: limite 'a' já é a raiz
    def funcao_b_raiz(x): return x - 1
    raiz, iters, msg = metodo_bissecao(funcao_b_raiz, 0, 1, tolerancia=1e-5)
    print(f"Teste 4 - Limite 'b' é raiz")
    print(f"Raiz: {raiz}, Iterações: {iters}, Mensagem: {msg}\n")