# RobotMotorsControl
Linux operating system training on the Skillbox platform

# Пояснения

Это скрипт на Python для управления двигателями робота. Я буду использовать общую абстракцию, чтобы сделать его применимым к разным типам роботов и моторов. В дальнейшем, возможно, потребуется адаптировать его под конкретную аппаратную платформу и библиотеки.

**Структура скрипта:**

1. **Интерфейс** **`Motor`** **:** Абстрактный класс, определяющий общие методы управления мотором (включение, выключение, установка скорости, изменение направления).
2. **Реализации** ** `Motor` **  **:** Классы, которые конкретизируют управление для определенного типа мотора (например, ШИМ-управление для DC моторов, управление через драйвер мотора).
3. **Класс** ** `Robot` **  **:** Управляет набором моторов, представляя собой интерфейс управления роботом.
4. **Пример использования:** Демонстрирует, как создать робота и управлять его движением.

### Модуль `abstract.py`


Модуль `abstract.py`  определяет **абстрактный базовый класс (ABC)** под названием `Motor` , который служит шаблоном для создания классов, управляющих моторами. Абстрактный класс не может быть инстанцирован (создан как объект) напрямую, но он задает обязательные методы, которые должны быть реализованы в любом классе-наследнике.

### Что делает этот код:

1. **Определяет абстрактный класс** ** `Motor` ** :

    * Класс наследуется от `ABC`  (Abstract Base Class), что делает его абстрактным.
    * Абстрактный класс используется для создания общего интерфейса, который должны реализовать все классы-наследники.
2. **Определяет абстрактные методы**:

    * Абстрактные методы — это методы, которые не имеют реализации в абстрактном классе, но должны быть реализованы в любом классе-наследнике.
    * В данном случае определены четыре абстрактных метода:

      *  `enable()` : Включает мотор.
      *  `disable()` : Выключает мотор.
      *  `set_speed(speed)` : Устанавливает скорость мотора (значение должно быть в диапазоне от -1 до 1).
      *  `set_direction(direction)` : Устанавливает направление вращения мотора (допустимые значения: 1 — вперед, -1 — назад, 0 — стоп).
3. **Зачем это нужно**:

    * Этот класс задает **интерфейс** для управления мотором. Любой класс, который наследует `Motor` , должен реализовать все эти методы.
    * Это обеспечивает единообразие в работе с моторами, даже если их реализация отличается (например, для разных типов моторов или оборудования).

### Пример использования:

В вашем коде класс `DummyMotor`  наследует `Motor`  и реализует все абстрактные методы. Это позволяет использовать `DummyMotor`  как конкретную реализацию моторов для тестирования.

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
```

### Итог:

Этот код определяет **интерфейс** для управления мотором, который должен быть реализован в любом классе, управляющем мотором. Это полезно для обеспечения единообразия и упрощения работы с разными типами моторов.

---

### Скрипт `motor_control.py` 

‍

Скрипт `motor_control.py`  представляет собой простую симуляцию управления роботом с двумя моторами. Он использует классы для управления моторами и роботом, но вместо реальных моторов используются "заглушки" (DummyMotor), которые имитируют поведение моторов, выводя информацию в консоль.

### Основные компоненты кода:

1. **Класс** ** `DummyMotor` ** :

    * Это класс, который имитирует поведение мотора. Он наследуется от абстрактного класса `Motor`  (который не показан в коде, но, вероятно, определяет интерфейс для моторов).
    * Методы:

      *  `enable()` : Включает мотор.
      *  `disable()` : Выключает мотор.
      *  `set_speed(speed)` : Устанавливает скорость мотора (значение должно быть в диапазоне от -1 до 1).
      *  `set_direction(direction)` : Устанавливает направление вращения мотора (допустимые значения: -1, 0, 1).
2. **Класс** ** `Robot` ** :

    * Этот класс управляет роботом, который имеет два мотора (левый и правый).
    * Методы:

      *  `move_forward(speed, duration)` : Двигает робота вперед с заданной скоростью и продолжительностью.
      *  `move_backward(speed, duration)` : Двигает робота назад с заданной скоростью и продолжительностью.
      *  `turn_left(speed, duration)` : Поворачивает робота налево с заданной скоростью и продолжительностью.
      *  `turn_right(speed, duration)` : Поворачивает робота направо с заданной скоростью и продолжительностью.
      *  `stop()` : Останавливает робота, устанавливая скорость и направление моторов в 0.
3. **Пример использования**:

    * В блоке `if __name__ == "__main__":`  создаются два "заглушечных" мотора (`left_motor`  и `right_motor` ).
    * Создается объект `Robot` , который использует эти моторы.
    * Моторы включаются, и робот выполняет последовательность команд: движение вперед, поворот налево, движение назад, поворот направо.
    * После выполнения всех команд моторы выключаются.

### Что делает код:

* Код симулирует управление роботом с двумя моторами, выводя в консоль информацию о состоянии моторов и действиях робота.
* Это может быть полезно для тестирования логики управления роботом без необходимости использования реального оборудования.

### Пример вывода в консоль:

```
Мотор Left Motor включен.
Мотор Right Motor включен.
Робот движется вперед
Мотор Left Motor направление: 1
Мотор Right Motor направление: 1
Мотор Left Motor скорость: 0.8
Мотор Right Motor скорость: 0.8
Остановка
Робот поворачивает на лево
Мотор Left Motor направление: -1
Мотор Right Motor направление: 1
Мотор Left Motor скорость: 0.5
Мотор Right Motor скорость: 0.5
Остановка
Робот движется назад
Мотор Left Motor направление: -1
Мотор Right Motor направление: -1
Мотор Left Motor скорость: 0.5
Мотор Right Motor скорость: 0.5
Остановка
Робот поворачивает на право
Мотор Left Motor направление: 1
Мотор Right Motor направление: -1
Мотор Left Motor скорость: 0.5
Мотор Right Motor скорость: 0.5
Остановка
Мотор Left Motor выключен.
Мотор Right Motor выключен.
```

Этот код может быть расширен для управления реальными моторами, если заменить `DummyMotor`  на классы, которые взаимодействуют с реальным оборудованием.
