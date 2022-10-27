import numpy as np

def loocking_number(number: int = 25) -> int:
    
    """ Сначала устанавливаем random число, а потом уменьшаем
        или увеличиваем его в половину дельты границ проверок взависимости 
        от того, больше оно или меньше нужного.
        
    Args:
        number (int, optional): Загаданное число. Defaults to 25.
    Returns:
        int: Число попыток
    """
    
    predict_current = np.random.randint (1, 101)
    
    predict_max = 101
    predict_min = 0
    
    count = 1 #не ноль, что-бы при угадывании с первой попытки функция вернула 1
        
    while True:
        if predict_current == number:
            break
        elif predict_current > number:
            predict_max = predict_current
            predict_current -= int((predict_max - predict_min) // 2)
        else:
            predict_min = predict_current
            predict_current += int((predict_max - predict_min) // 2)
        count += 1   
    
    return count
    

def count_attempt(loocking_number):
    """ Функция для сбора статистики расчетов нашего когда.
        Принимает функцию, выдает сообщение о максимальном, минимальном и среднем
        количестве результатов выполнения нашего кода за 1000 запусков
    """
    
    count_lst = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:   
        count_lst.append(loocking_number(number))
    
    print(f'Среднее число попыток {int(np.mean(count_lst))}') # Ожидаемо 6
    print(f'Максимальное количество попыток {max(count_lst)}') # Ожидаемо 8
    print(f'Минимальное количество попыток {min(count_lst)}') # Ожидаемо 1