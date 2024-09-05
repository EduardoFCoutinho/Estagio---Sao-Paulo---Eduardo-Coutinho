def fibonacci(n):
    if n <= 0:
        return "Número inválido"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Digite um número: "))
resultado = fibonacci(num)
print(f"O número {num} pertence à sequência de Fibonacci: {num in fibonacci_sequence}")
