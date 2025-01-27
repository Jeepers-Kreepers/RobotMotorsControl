# Отчет по учебному проекту.

Это скрипт на Python для управления двигателями робота. Цель проекта - получение навыков работы с распределенной системой контроля версий. Правильность кода и его практическая ценность не является основополагающей. Важно ознакомиться с основными принципами GIT: отслеживанием, сохранением истории, возможности отмены изменений в коде и возможность ведения совместных проектов в составе команды разработчиков.

В данном README ниже представлены два скрипта управления движением роботом - с мгновенным и плавным изменением скорости вращения двигателей (моторов).

Также приведены последовательности команд для добавления кода в отслеживание GIT, коммиты и дальнейшей отправки кода в удаленный репозиторий.

Для написания скриптов я буду использовать общую абстракцию, чтобы сделать его применимым к разным типам роботов и моторов. В дальнейшем, возможно, потребуется адаптировать его под конкретную аппаратную платформу и библиотеки.

**Структура скрипта:**

1. **Интерфейс** ** `Motor` **   **:**  Абстрактный класс, определяющий общие методы управления мотором (включение, выключение, установка скорости, изменение направления).
2. **Реализации класса** `Motor`   **:**  Классы, которые конкретизируют управление для определенного типа мотора (например, ШИМ-управление для DC моторов, управление через драйвер мотора).
3. **Класс** `Robot`   **:**  Управляет набором моторов, представляя собой интерфейс управления роботом.
4. **Пример использования:**  Демонстрирует, как создать робота и управлять его движением.

 

### Модуль `abstract.py` 

Модуль `abstract.py`  определяет **абстрактный базовый класс (ABC)**  под названием `Motor`  , который служит шаблоном для создания классов, управляющих моторами. Абстрактный класс не может быть инстанцирован (создан как объект) напрямую, но он задает обязательные методы, которые должны быть реализованы в любом классе-наследнике.

### Что делает этот код:

1. **Определяет абстрактный класс** `Motor`  :

    * Класс наследуется от `ABC`  (Abstract Base Class), что делает его абстрактным.
    * Абстрактный класс используется для создания общего интерфейса, который должны реализовать все классы-наследники.
2. **Определяет абстрактные методы**:

    * Абстрактные методы — это методы, которые не имеют реализации в абстрактном классе, но должны быть реализованы в любом классе-наследнике.
    * В данном случае определены четыре абстрактных метода:

      *  `enable()`  : Включает мотор.
      *  `disable()`  : Выключает мотор.
      *  `set_speed(speed)`  : Устанавливает скорость мотора (значение должно быть в диапазоне от -1 до 1).
      *  `set_direction(direction)`  : Устанавливает направление вращения мотора (допустимые значения: 1 — вперед, -1 — назад, 0 — стоп).
      *  `set_speed_smooth(target_speed, step=0.01, interval=0.1)`  : Метод для плавного изменения скорости мотора. Принимает:
      *  `set_speed_smooth(target_speed, step=0.01, interval=0.1)` : Метод для плавного изменения скорости мотора. Принимает:

        *  `target_speed`  — целевая скорость (тип `float` ),
        *  `step`  — шаг изменения скорости (тип `float` , по умолчанию 0.01),
        *  `interval`  — интервал времени между шагами в секундах (тип `float` , по умолчанию 0.1).
3. **Зачем это нужно**:

    * Этот класс задает **интерфейс** для управления мотором. Любой класс, который наследует `Motor`  , должен реализовать все эти методы.
    * Это обеспечивает единообразие в работе с моторами, даже если их реализация отличается (например, для разных типов моторов или оборудования).

### Пример использования (что хотим получить):

В коде класс `DummyMotor`  наследует `Motor`  и реализует все абстрактные методы. Это позволяет использовать `DummyMotor`  как конкретную реализацию моторов для тестирования.

```python
class DummyMotor(Motor):
    def enable(self):
        print("Мотор включен.")

    def disable(self):
        print("Мотор выключен.")

    def set_speed(self, speed):
        print(f"Скорость установлена: {speed}")

    def set_direction(self, direction):
        print(f"Направление установлено: {direction}")

	def set_speed_smooth(self, target_speed, step=0.01, interval=0.1):
        	current_speed = 0.0
        	while current_speed != target_speed:
            	current_speed += step if target_speed > current_speed else -step
            	self.set_speed(current_speed)
            	time.sleep(interval)

# Теперь можно создать объект DummyMotor и управлять им
motor = DummyMotor()
motor.enable()
motor.set_speed(0.5)
motor.set_direction(1)
motor.set_speed_smooth(1.0)
motor.disable()
```

### Итог:

Этот код определяет **интерфейс** для управления мотором, который должен быть реализован в любом классе, управляющем мотором. Это полезно для обеспечения единообразия и упрощения работы с разными типами моторов.

---

### Скрипт `motor_control.py` 

Скрипт `motor_control.py`  представляет собой простую симуляцию управления роботом с двумя моторами. Он использует классы для управления моторами и роботом, но вместо реальных моторов используются "заглушки" (DummyMotor), которые имитируют поведение моторов, выводя информацию в консоль.

### Основные компоненты кода:

1. **Класс** `DummyMotor`  :

    * Это класс, который имитирует поведение мотора. Он наследуется от абстрактного класса `Motor`  (который определяет интерфейс для моторов).
    * Методы:

      *  `enable()`  : Включает мотор (устанавливает флаг `is_enabled`  в `True` ).
      *  `disable()`  : Выключает мотор (устанавливает флаг `is_enabled`  в `False` )..
      *  `set_speed(speed)`  : Устанавливает скорость мотора (значение должно быть в диапазоне от -1 до 1). Если направление некорректно, выводится сообщение об ошибке.
      *  `set_direction(direction)`  : Устанавливает направление вращения мотора (допустимые значения: -1, 0, 1).
      *  `set_speed_smooth(target_speed, step, interval)` : Плавно изменяет скорость мотора до целевого значения с заданным шагом и интервалом.
2. **Класс** `Robot`  :

    * Этот класс управляет роботом, который имеет два мотора (левый и правый).
    * Методы:

      *  `move_forward(speed, duration)` : Движение вперед с заданной скоростью. Если указана длительность (`duration` ), робот остановится после завершения движения.
      *  `move_forward_smooth(target_speed, duration, step, interval)` : Плавное движение вперед с постепенным увеличением скорости.
      *  `move_backward(speed, duration)` : Движение назад с заданной скоростью.
      *  `move_backward_smooth(target_speed, duration, step, interval)` : Плавное движение назад.
      *  `turn_left(speed, duration)` : Поворот налево (левый мотор вращается назад, правый — вперед).
      *  `turn_left_smooth(target_speed, duration, step, interval)` : Плавный поворот налево.
      *  `turn_right(speed, duration)` : Поворот направо (левый мотор вращается вперед, правый — назад).
      *  `turn_right_smooth(target_speed, duration, step, interval)` : Плавный поворот направо.
      *  `stop()` : Останавливает робота (устанавливает скорость и направление обоих моторов в 0).
3. **Пример использования**:

    В блоке `if __name__ == "__main__":`  создаются два объекта `DummyMotor`  (левый и правый моторы) и объект `Robot` , который управляет этими моторами.

    * Робот выполняет следующие действия:

      1. Плавно движется вперед с целевой скоростью 0.8 в течение 2 секунд.
      2. Плавно поворачивает налево в течение 2 секунд.
      3. Плавно движется назад в течение 2 секунд.
      4. Плавно поворачивает направо в течение 2 секунд.
      5. Выключает оба мотора.

---

### Что делает этот код:

1. **Имитирует управление моторами**:

    * Класс `DummyMotor`  не управляет реальными устройствами, а только выводит информацию в консоль. Это полезно для тестирования и отладки.
2. **Реализует управление роботом**:

    * Класс `Robot`  использует два мотора для выполнения различных действий, таких как движение вперед, назад, повороты и остановка.
3. **Демонстрирует плавное управление**:

    * Методы с суффиксом `_smooth`  позволяют плавно изменять скорость моторов, что делает движение робота более естественным.
4. **Пример использования**:

    * В блоке `if __name__ == "__main__":`  показано, как можно использовать классы `DummyMotor`  и `Robot`  для управления роботом.

---

### Пример вывода в консоль:

```plaintext
Мотор Left Motor включен.
Мотор Right Motor включен.
Робот плавно движется вперед
Мотор Left Motor скорость: 0.01
Мотор Right Motor скорость: 0.01
Мотор Left Motor скорость: 0.02
Мотор Right Motor скорость: 0.02
...
Мотор Left Motor скорость: 0.8
Мотор Right Motor скорость: 0.8
Робот плавно поворачивает на лево
Мотор Left Motor направление: -1
Мотор Right Motor направление: 1
Мотор Left Motor скорость: 0.01
Мотор Right Motor скорость: 0.01
...
Остановка
Мотор Left Motor выключен.
Мотор Right Motor выключен.
```

---

### Зачем это нужно:

* Этот код может быть использован для тестирования логики управления роботом без необходимости подключения реальных устройств.
* Код может быть расширен для управления реальными моторами, заменив `DummyMotor`  на класс, который взаимодействует с аппаратным обеспечением.

 

## Работа с Github

* Описание работы с Git:

  * Создание и клонирование репозитория: опишите, как был создан и склонирован репозиторий.

  ||||
  | -----------------------------------------------------------------------------------------------------------------------------------------| --------------------------| ------------------------------------------------------------------------------------------------------|
  |Создал репозиторий RobotMotorsControl|[https://github.com/Jeepers-Kreepers/RobotMotorsControl.git](https://github.com/Jeepers-Kreepers/RobotMotorsControl.git)|Public / Token для доступа|
  |Локально:|||
  |Создал конфигурацию GIT| `git config --global user.name "Alexandr"` <br />`git config --global user.email k_____v@y______.ru` <br />`git config --global core.editor nano` <br />|имя пользователя<br />email пользователя<br />текстовый редактор|
  |Инициировал git репозиторий| `git init` <br />|Создается папка `.git`   |
  |Проверил статус| `git status`  >>> No commits yet|Файлы в отслеживание пока не добавлены|
  |Добавление файлов в отслеживание| `git add .gitignore` <br />`git add README.md` <br />----<br />`git add abstract.py` <br />`git add motor_control.py` <br />||
  |Commit файлов| `git commit -m "add .gitignore / файл .gitignore"` <br />`git commit -m "Modifies README.md / правка ошибок в README.md"` <br />----<br />`git commit -m "first commit abstract.py & motor_control.py"` <br />||
  |Установил связь между локальным репозиторием Git и удаленным репозиторием| `git remote add origin https://github.com/Jeepers-Kreepers/RobotMotorsControl.git` ||
  |Проверил, что связь установлена| `git remote show origin` |Авторизация через созданный ранее Token|
  |Отправил локальные комиты в ветку `master`  удаленного репозитория| `git push -u origin master` |Все файлы появились в ветке `master ` удаленного репозитория|

  * Взаимодействие с ветками:

  ||||
  | ------------------------------------------------------------------------------------------------------------------------------------| --------------| -----------------------------------------------------------------------------------------------------|
  |Создал вторую ветку в локальном репозитории| `git branch feature_branch_name` |<br />|
  |Проверил, что ветка создана| `git branch` | `master*` <br />`feature_branch_name` |
  |Перешел на вновь созданную ветку| `git checkout feature_branch_name` | `master` <br />`feature_branch_name*` |
  |Произвел изменение в коде модуля `abstract.py`  / добавление в отслеживание и коммит| `git add abstract.py` <br />`git commit -m "set_Speed_smooth method"` ||
  |Произвел изменение в коде модуля `motor_control.py`  / добавление в отслеживание и коммит| `git add motor_control.py` <br />`git commit -m "Implementation of smooth increase in speed of motors"` <br /><br />||
  |Отправил локальные комиты  в ветку `feature_branch_name` удаленного репозитория| `git push -u origin feature_branch_name` | `master` <br />`feature_branch_name*` <br />|
  |Внес новое описание кода в `README.md`  с учетом произведенных правок. <br />Далее `add -> commit -> push` | `commit -am "new README.md"` <br />`git push` ||
  |Все готово к `merge`  / `pull reaquest` ||Изменения появились в удаленном дипозитории в ветке `feature_branch_name` |

  * Работа с Пул-реквест:   пул-реквест,  ревью, изменения.

  ||||
  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ------------| ------------------------|
  |Создан `pull request ` для внесения изменений связанных с реализацией функции плавной регулировки скорости вращения двигателя| `base: master`  <- `compare: feature_branch_name` ||
  |Осуществлен ревью кода||Опционально|
  |Произведено слияние веток `master`  и `feature_branch_name` |||

  * Основные изменения в коде: Первоначально код описывал мгновенное изменение скорости при поступлении управляющей команды. Далее был добавлен метод `set_speed_smooth()`  - плавного,  линейного, изменения скорости (описание выше).

 

 

---

Здесь приведен полностью код из двух реализации управления движением робота. 

1. Мгновенное управление скоростью вращения двигателей робота

```bash
from abc import ABC, abstractmethod
import time

class Motor(ABC):
    """
    Абстрактный класс для управления мотором.
    """
    @abstractmethod
    def enable(self):
        """Включить мотор."""
        pass

    @abstractmethod
    def disable(self):
        """Выключить мотор."""
        pass

    @abstractmethod
    def set_speed(self, speed):
        """Установить скорость мотора.
  
        Args:
            speed (float): Скорость в диапазоне от -1 (полная назад) до 1 (полная вперед).
        """
        pass
  
    @abstractmethod
    def set_direction(self, direction):
        """Установить направление мотора.
   
         Args:
             direction (int): 1 - вперед, -1 - назад, 0 - стоп
        """
        pass

    @abstractmethod
    def set_speed_smooth(self, target_speed, step=0.01, interval=0.1):
         """
        Плавное изменение скорости мотора.

        Args:
             target_speed (float): Целевая скорость в диапазоне от -1 до 1.
             step (float): Шаг изменения скорости.
             interval (float): Интервал времени между шагами в секундах.
         """
         pass


class DummyMotor(Motor):
    """
    Пример реализации для тестирования (не управляет реальным мотором).
    """
    def __init__(self, name):
        self.name = name
        self.is_enabled = False
        self.speed = 0
        self.direction = 0

    def enable(self):
        self.is_enabled = True
        print(f"Мотор {self.name} включен.")

    def disable(self):
        self.is_enabled = False
        print(f"Мотор {self.name} выключен.")

    def set_speed(self, speed):
  
       if -1 <= speed <= 1:
            self.speed = speed
            print(f"Мотор {self.name} скорость: {speed}")
       else:
            print(f"Некорректная скорость для мотора {self.name}. Скорость должна быть в диапазоне от -1 до 1")

    def set_direction(self, direction):
        if direction in [-1, 0, 1]:
            self.direction = direction
            print(f"Мотор {self.name} направление: {direction}")
        else:
            print(f"Некорректное направление для мотора {self.name}. Допустимые значения: -1, 0, 1.")

    def set_speed_smooth(self, target_speed, step=0.01, interval=0.1):
        """
        Плавное изменение скорости мотора.

        Args:
            target_speed (float): Целевая скорость в диапазоне от -1 до 1.
            step (float): Шаг изменения скорости.
            interval (float): Интервал времени между шагами в секундах.
        """
        current_speed = self.speed
        while abs(current_speed - target_speed) > step:
            if current_speed < target_speed:
                current_speed = min(current_speed + step, target_speed)
            else:
                current_speed = max(current_speed - step, target_speed)
            self.set_speed(current_speed)
            time.sleep(interval)
        self.set_speed(target_speed)  # Устанавливаем окончательную скорость

class Robot:
    """
    Класс для управления роботом.
    """
    def __init__(self, left_motor, right_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor
  
    def move_forward(self, speed=0.5, duration=None):
        """Движение вперед."""
        self.left_motor.set_direction(1)
        self.right_motor.set_direction(1)
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed)
  
        if duration:
            time.sleep(duration)
            self.stop()
      
    def move_forward_smooth(self, target_speed=0.5, duration=None, step=0.01, interval=0.1):
        """Плавное движение вперед"""
        self.left_motor.set_direction(1)
        self.right_motor.set_direction(1)
        self.left_motor.set_speed_smooth(target_speed, step, interval)
        self.right_motor.set_speed_smooth(target_speed, step, interval)
        if duration:
            time.sleep(duration)
            self.stop()

    def move_backward(self, speed=0.5, duration=None):
        """Движение назад."""
        self.left_motor.set_direction(-1)
        self.right_motor.set_direction(-1)
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed)

        if duration:
            time.sleep(duration)
            self.stop()

    def move_backward_smooth(self, target_speed=0.5, duration=None, step=0.01, interval=0.1):
        """Плавное движение назад."""
        self.left_motor.set_direction(-1)
        self.right_motor.set_direction(-1)
        self.left_motor.set_speed_smooth(target_speed, step, interval)
        self.right_motor.set_speed_smooth(target_speed, step, interval)

        if duration:
            time.sleep(duration)
            self.stop()

    def turn_left(self, speed=0.5, duration=None):
        """Поворот налево."""
        self.left_motor.set_direction(-1)
        self.right_motor.set_direction(1)
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed)

        if duration:
            time.sleep(duration)
            self.stop()

    def turn_left_smooth(self, target_speed=0.5, duration=None, step=0.01, interval=0.1):
        """Плавный поворот налево."""
        self.left_motor.set_direction(-1)
        self.right_motor.set_direction(1)
        self.left_motor.set_speed_smooth(target_speed, step, interval)
        self.right_motor.set_speed_smooth(target_speed, step, interval)

        if duration:
            time.sleep(duration)
            self.stop()

    def turn_right(self, speed=0.5, duration=None):
        """Поворот направо."""
        self.left_motor.set_direction(1)
        self.right_motor.set_direction(-1)
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed)
  
        if duration:
            time.sleep(duration)
            self.stop()

    def turn_right_smooth(self, target_speed=0.5, duration=None, step=0.01, interval=0.1):
        """Плавный поворот направо."""
        self.left_motor.set_direction(1)
        self.right_motor.set_direction(-1)
        self.left_motor.set_speed_smooth(target_speed, step, interval)
        self.right_motor.set_speed_smooth(target_speed, step, interval)

        if duration:
            time.sleep(duration)
            self.stop()

    def stop(self):
        """Остановить робота."""
        self.left_motor.set_speed(0)
        self.right_motor.set_speed(0)
        self.left_motor.set_direction(0)
        self.right_motor.set_direction(0)
        print("Остановка")

# Пример использования
if __name__ == "__main__":
    left_motor = DummyMotor("Left Motor")
    right_motor = DummyMotor("Right Motor")
  
    robot = Robot(left_motor, right_motor)

    left_motor.enable()
    right_motor.enable()
  
    print("Робот плавно движется вперед")
    robot.move_forward_smooth(target_speed=0.8, duration=2)
  
    print("Робот плавно поворачивает на лево")
    robot.turn_left_smooth(duration=2)
  
    print("Робот плавно движется назад")
    robot.move_backward_smooth(duration=2)
  
    print("Робот плавно поворачивает на право")
    robot.turn_right_smooth(duration=2)
  
    left_motor.disable()
    right_motor.disable()
```

 

2. Плавное управление скоростью вращения двигателей робота

```bash
from abc import ABC, abstractmethod
import time

class Motor(ABC):
    """
    Абстрактный класс для управления мотором.
    """
    @abstractmethod
    def enable(self):
        """Включить мотор."""
        pass

    @abstractmethod
    def disable(self):
        """Выключить мотор."""
        pass

    @abstractmethod
    def set_speed(self, speed):
        """Установить скорость мотора.
  
        Args:
            speed (float): Скорость в диапазоне от -1 (полная назад) до 1 (полная вперед).
        """
        pass
  
    @abstractmethod
    def set_direction(self, direction):
        """Установить направление мотора.
   
         Args:
             direction (int): 1 - вперед, -1 - назад, 0 - стоп
        """
        pass

    @abstractmethod
    def set_speed_smooth(self, target_speed, step=0.01, interval=0.1):
         """
        Плавное изменение скорости мотора.

        Args:
             target_speed (float): Целевая скорость в диапазоне от -1 до 1.
             step (float): Шаг изменения скорости.
             interval (float): Интервал времени между шагами в секундах.
         """
         pass


class DummyMotor(Motor):
    """
    Пример реализации для тестирования (не управляет реальным мотором).
    """
    def __init__(self, name):
        self.name = name
        self.is_enabled = False
        self.speed = 0
        self.direction = 0

    def enable(self):
        self.is_enabled = True
        print(f"Мотор {self.name} включен.")

    def disable(self):
        self.is_enabled = False
        print(f"Мотор {self.name} выключен.")

    def set_speed(self, speed):
  
       if -1 <= speed <= 1:
            self.speed = speed
            print(f"Мотор {self.name} скорость: {speed}")
       else:
            print(f"Некорректная скорость для мотора {self.name}. Скорость должна быть в диапазоне от -1 до 1")

    def set_direction(self, direction):
        if direction in [-1, 0, 1]:
            self.direction = direction
            print(f"Мотор {self.name} направление: {direction}")
        else:
            print(f"Некорректное направление для мотора {self.name}. Допустимые значения: -1, 0, 1.")

    def set_speed_smooth(self, target_speed, step=0.01, interval=0.1):
        """
        Плавное изменение скорости мотора.

        Args:
            target_speed (float): Целевая скорость в диапазоне от -1 до 1.
            step (float): Шаг изменения скорости.
            interval (float): Интервал времени между шагами в секундах.
        """
        current_speed = self.speed
        while abs(current_speed - target_speed) > step:
            if current_speed < target_speed:
                current_speed = min(current_speed + step, target_speed)
            else:
                current_speed = max(current_speed - step, target_speed)
            self.set_speed(current_speed)
            time.sleep(interval)
        self.set_speed(target_speed)  # Устанавливаем окончательную скорость

class Robot:
    """
    Класс для управления роботом.
    """
    def __init__(self, left_motor, right_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor
  
    def move_forward(self, speed=0.5, duration=None):
        """Движение вперед."""
        self.left_motor.set_direction(1)
        self.right_motor.set_direction(1)
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed)
  
        if duration:
            time.sleep(duration)
            self.stop()
      
    def move_forward_smooth(self, target_speed=0.5, duration=None, step=0.01, interval=0.1):
        """Плавное движение вперед"""
        self.left_motor.set_direction(1)
        self.right_motor.set_direction(1)
        self.left_motor.set_speed_smooth(target_speed, step, interval)
        self.right_motor.set_speed_smooth(target_speed, step, interval)
        if duration:
            time.sleep(duration)
            self.stop()

    def move_backward(self, speed=0.5, duration=None):
        """Движение назад."""
        self.left_motor.set_direction(-1)
        self.right_motor.set_direction(-1)
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed)

        if duration:
            time.sleep(duration)
            self.stop()

    def move_backward_smooth(self, target_speed=0.5, duration=None, step=0.01, interval=0.1):
        """Плавное движение назад."""
        self.left_motor.set_direction(-1)
        self.right_motor.set_direction(-1)
        self.left_motor.set_speed_smooth(target_speed, step, interval)
        self.right_motor.set_speed_smooth(target_speed, step, interval)

        if duration:
            time.sleep(duration)
            self.stop()

    def turn_left(self, speed=0.5, duration=None):
        """Поворот налево."""
        self.left_motor.set_direction(-1)
        self.right_motor.set_direction(1)
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed)

        if duration:
            time.sleep(duration)
            self.stop()

    def turn_left_smooth(self, target_speed=0.5, duration=None, step=0.01, interval=0.1):
        """Плавный поворот налево."""
        self.left_motor.set_direction(-1)
        self.right_motor.set_direction(1)
        self.left_motor.set_speed_smooth(target_speed, step, interval)
        self.right_motor.set_speed_smooth(target_speed, step, interval)

        if duration:
            time.sleep(duration)
            self.stop()

    def turn_right(self, speed=0.5, duration=None):
        """Поворот направо."""
        self.left_motor.set_direction(1)
        self.right_motor.set_direction(-1)
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed)
  
        if duration:
            time.sleep(duration)
            self.stop()

    def turn_right_smooth(self, target_speed=0.5, duration=None, step=0.01, interval=0.1):
        """Плавный поворот направо."""
        self.left_motor.set_direction(1)
        self.right_motor.set_direction(-1)
        self.left_motor.set_speed_smooth(target_speed, step, interval)
        self.right_motor.set_speed_smooth(target_speed, step, interval)

        if duration:
            time.sleep(duration)
            self.stop()

    def stop(self):
        """Остановить робота."""
        self.left_motor.set_speed(0)
        self.right_motor.set_speed(0)
        self.left_motor.set_direction(0)
        self.right_motor.set_direction(0)
        print("Остановка")

# Пример использования
if __name__ == "__main__":
    left_motor = DummyMotor("Left Motor")
    right_motor = DummyMotor("Right Motor")
  
    robot = Robot(left_motor, right_motor)

    left_motor.enable()
    right_motor.enable()
  
    print("Робот плавно движется вперед")
    robot.move_forward_smooth(target_speed=0.8, duration=2)
  
    print("Робот плавно поворачивает на лево")
    robot.turn_left_smooth(duration=2)
  
    print("Робот плавно движется назад")
    robot.move_backward_smooth(duration=2)
  
    print("Робот плавно поворачивает на право")
    robot.turn_right_smooth(duration=2)
  
    left_motor.disable()
    right_motor.disable()
```