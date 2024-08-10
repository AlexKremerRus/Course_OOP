
class MyClassException(Exception):
    def __init__(self, message):
        self.message = message




while True:
    argument_1 = int(input("Введите первое число: "))
    argument_2 = int(input("Введите второе число: "))
    action = input("Выберите действие: ")

    # создание своего исключения - можно обработку с try-except
    if action == "exit":
        raise MyClassException("Вы вышли из программы")
        break

    statement = f"print({argument_1}{action}{argument_2})"

    try:
        eval(statement)
    except ZeroDivisionError as e:
        print(" Вы пытаетесь делить на ноль - не надо так =( ")
        print(f'error is {e}')
    except NameError:
        print("Вы ввели неверное действие")
    except ValueError:
        print("Вы ввели неверное число")
    except SyntaxError:
        print("Вы ввели неверное число")
    except TypeError:
        print("Проблема с приведением типов")
    # чтобы понять что за ошибка можем ее печатать в консоль
    except Exception as e:
        print("Что-то пошло не так - не обработанная ошибка")
        print(f'error is {e}')

    else:
        print("Вы ввели правильные данные")
    finally:
        print("Завершение работы программы")
