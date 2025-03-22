# python-project-49

[![Actions Status](https://github.com/barbadjhar/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/barbadjhar/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/ede06b4c8cf98a569db2/maintainability)](https://codeclimate.com/github/barbadjhar/python-project-49/maintainability)

# ИГРЫ РАЗУМА

"Игры разума" - это коллекция игр, предназначенных для тренировки математического мышления и логики.

## Как играть

Выберите игру из списка, он представлен ниже. Запустите игру командой, к примеру:

   ```bash
   brain-even
   ```

Далее следуйте инструкциям в консоли.
После каждой попытки вы получите приавильный ответ решения. Если ответ неверный, игра завершиться. В каждой игре три раунда.

## Установка с использованием UV

Проект собирался с использованием пакета *UV*. Это современный инструмент управления пакетами Python, который обеспечивает быструю и надежную установку зависимостей. 
Для установки проекта выполните следующие шаги:

1. Установите UV:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/barbadjhar/python-project-49.git
    cd python-project-49
    ```

3. Создайте виртуальное окружение и установите зависимости:

    ```bash
    uv venv
    uv pip install -r requirements.txt
    ```

4. Активируйте виртуальное окружение:

    ```bash
    source .venv/bin/activate
    ```

Более подробную информацию об использовании UV можно найти в [официальной документации](https://docs.astral.sh/uv/?spm=a2ty_o01.29997173.0.0.4041c921lJYVk4).



### Игры

```brain-even``` - проверка на чётность. ([example](#игра-проверка-на-чётность))\
```brain-calc``` - калькулятор. Проверь себя на простые алгебраичесике вычисления. ([example](#игра-калькулятор))\
```brain-gcd``` - НОД (Наибольший общий делитель). ([example](#игра-нод))\
```brain-progression``` - арифметическая прогрессия. ([example](#игра-арифметическая-прогрессия))\
```brain-prime``` - простое ли число? ([example](#игра-простое-ли-число))\

---

#### Игра "Проверка на чётность".

> _Вам показывается случайное число. Нужно ответить 'yes', если число чётное, или 'no' — если нечётное._

[![asciicast](https://asciinema.org/a/ThnJq8N68Kb5wVqxad71bgglw.png)](https://asciinema.org/a/ThnJq8N68Kb5wVqxad71bgglw)


#### Игра "Калькулятор".

> _Вам показывается случайное математическое выражение, например 35 + 16, которое нужно вычислить и записать правильный ответ._

[![asciicast](https://asciinema.org/a/3A7CedZw4ekVvCTIBSazyuxc9.png)](https://asciinema.org/a/3A7CedZw4ekVvCTIBSazyuxc9)

#### Игра "НОД".

> _Вам показывается два случайных числа, например, 25 50. Пользователь должен вычислить и ввести наибольший общий делитель этих чисел._

[![asciicast](https://asciinema.org/a/TpgG28sHKYF83AxkPrs0ZprwP.png)](https://asciinema.org/a/TpgG28sHKYF83AxkPrs0ZprwP)

#### Игра "Арифметическая прогрессия".

> _Вам показывается ряд чисел, образующий арифметическую прогрессию, одно число скрыто. Вам нужно определить это число._

[![asciicast](https://asciinema.org/a/O8i7SJ4vM7tgXpVpKlLb9j7Kl.png)](https://asciinema.org/a/O8i7SJ4vM7tgXpVpKlLb9j7Kl)

#### Игра "Простое ли число".

> _Вам показывается случайное число. Нужно ответить 'yes', если число чётное, или 'no' — если нечётное._

[![asciicast](https://asciinema.org/a/aezFAQ9l9bichqq2zhe6j9kXn.png)](https://asciinema.org/a/aezFAQ9l9bichqq2zhe6j9kXn)