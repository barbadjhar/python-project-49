install:  			# Клонирование репозитория или удаление зависимостей
	uv sync

brain-games: 		# Запуск игры
	uv run brain-games

build:				# сборка как пакет для PyPi
	uv build

package-install:	# установка как пакета из PyPi
	uv tool install dist/*.whl

lint:				# запуск lint (проверка на синтаксис) 
	uv run ruff check brain_games