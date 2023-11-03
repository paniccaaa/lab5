import statistics

class BatchCalculatorContextManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def read_lines(self):
        for line in self.file:
            yield line.strip()

def calculate(action, tolerance=1e-6, *args):
  """
    Функция вычисляет результат заданного действия над числами.

    :param action: тип арифметического действия ('+', '-', '*', '/', 'mean', 'variance', 'std_deviation', 'median', 'q2')
    :param tolerance: точность вычислений (по умолчанию 1e-6)
    :param args: неименованные аргументы (числа)
    :return: результат вычисления
    """

  def convert_precision(value):
    """
        Функция извлекает порядок значения.

        :param value: значение
        :return: порядок значения
        """
    return len(str(value).split("e")[-1].lstrip("0"))

  def round_result(result, precision):
    """
        Функция округляет результат с заданной точностью.

        :param result: результат вычисления
        :param precision: точность округления (порядок значения)
        :return: округленный результат
        """
    return round(result, precision)

  if action == "+":
    result = sum(args)
  elif action == "-":
    result = args[0] - sum(args[1:])
  elif action == "*":
    result = 1
    for num in args:
      result *= num
  elif action == "/":
    result = args[0]
    for num in args[1:]:
      if num == 0:
        return "деление на ноль невозможно"
      result /= num
  elif action == "mean":
    result = statistics.mean(args)
  elif action == "variance":
    result = statistics.variance(args)
  elif action == "std_deviation":
    result = statistics.stdev(args)
  elif action == "median" or action == "q2":
    result = statistics.median(args)
  elif action == "q3 - q1":
    q3 = statistics.quantiles(args, n=4)[3]
    q1 = statistics.quantiles(args, n=4)[0]
    result = q3 - q1
  else:
    return "неподдерживаемое действие"

  precision = convert_precision(tolerance)
  return round_result(result, precision)
    
    # Ваш код калькулятора здесь
    # Оставьте без изменений

# Пример использования

filename = 'expressions.txt'  # Замените на имя вашего текстового файла

with BatchCalculatorContextManager(filename) as batch_calculator:
    for line in batch_calculator.read_lines():
        # Разбиваем строку на операцию и числа
        expression = line.split(' ')
        action = expression[1]
      
        
        numbers = [float(num) for num in expression if (num != '+' and num != '-' and num != '*' and num != '/')]
        result = calculate(action, 1e-6, *numbers)
        print(result)