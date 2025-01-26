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