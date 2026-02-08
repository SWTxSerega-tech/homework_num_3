from typing import Callable

text = '''
        Загальний дохід працівника складається з декількох частин: 1000.01 
        як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 
        доларів.
        '''

'''
За допомогою генератора generator_numbers розділяємо 
текст та виводимо числа з крапкою
'''
    
def generator_numbers(text: str):
    for word in text.split():
        word = word.replace(',', '.')
        if word.count('.') <= 1:
            if word.replace('.', '').isdigit():
                yield float(word)
  

'''
Функція sum_profit виводить
суму всіх доходів працівника
'''
     
def sum_profit(text: str, func: Callable):
    return sum(func(text))
        
total_income = sum_profit(text, generator_numbers)
print(f'Загальний дохід: {total_income}')