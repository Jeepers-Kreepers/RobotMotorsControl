from abc import ABC, abstractmethod


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
            speed (float): Скорость в диапазоне от -1 (полный назад) до 1 (полный вперед).
        """
        pass

    @abstractmethod
    def set_direction(self, direction):
        """Установить направление вращения/движения.

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