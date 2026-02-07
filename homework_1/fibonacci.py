"""
Функція caching_fibonacci() створює замикання, всередені
якої знаходиться рекурсивна функція fibonacci() для розв'язання 
ряду Фібоначчі
"""
def caching_fibonacci():
    cache = {} #Кешування чисел
        
    def fibonacci(n): #Рекурсивна функція, для визначення ряду Фібоначчі
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

fib = caching_fibonacci() #Отримання фунцкції fibonacci()

#Використання фукції fibonacci() для обчислення чисел Фібоначчі

print(fib(10))
print(fib(15))
print(fib(1))
print(fib(0))
print(fib(10))