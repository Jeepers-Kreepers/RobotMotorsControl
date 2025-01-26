from abstract import Motor
import time


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


class Robot:
    """
    Класс для управления роботом.
    """

    def __init__(self, l_motor, r_motor):
        self.left_motor = l_motor
        self.right_motor = r_motor

    def move_forward(self, speed=0.5, duration=None):
        """Движение вперед."""
        self.left_motor.set_direction(1)
        self.right_motor.set_direction(1)
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed)

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

    def turn_left(self, speed=0.5, duration=None):
        """Поворот налево."""
        self.left_motor.set_direction(-1)
        self.right_motor.set_direction(1)
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed)

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

    print("Робот движется вперед")
    robot.move_forward(speed=0.8, duration=2)

    print("Робот поворачивает на лево")
    robot.turn_left(duration=2)

    print("Робот движется назад")
    robot.move_backward(duration=2)

    print("Робот поворачивает на право")
    robot.turn_right(duration=2)

    left_motor.disable()
    right_motor.disable()
