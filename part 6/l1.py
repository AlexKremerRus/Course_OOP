class Logger:
    def __init__(self):
        # Инициализируем счетчик позиции сообщения в журнале
        self.position = 1
        # Инициализируем пустой список для хранения журнала событий
        self.storage = []

#Звездочка `*` в определении метода `text_print` разделяет обязательные позиционные аргументы и необязательные ключевые аргументы. Это гарантирует, что аргументы будут переданы правильно, избегая ошибок при вызове метода. Аргументы после звездочки должны передаваться как ключевые аргументы в виде пар "имя = значение".

    def text_print(self, *, text, LEVEL = "DEBUG"):
        logger_text = f"[{self.position}][{LEVEL}] -  {text}"
        self.storage.append(logger_text)
        self.position  +=  1
        print(logger_text)


# class сохранения журнала лога
class LoggerManager:
    @staticmethod
    def save_joutnal(logger_obj: Logger, file_name: str):
        with open(file_name, "w", encoding = 'UTF-8') as f:
            f.write("\n".join(logger_obj.storage))


if __name__ == "__main__":
    debug_1 =  Logger()
    debug_1.text_print(text="Hello World!", LEVEL="DEBUG")
    debug_1.text_print(text="Test", LEVEL="INFO")
    LoggerManager.save_joutnal(logger_obj=debug_1, file_name="test.log")