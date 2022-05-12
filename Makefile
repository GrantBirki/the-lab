run:
	@echo "\033[0;34m[#] Killing old docker processes\033[0m"
	docker-compose down -v -t 1

	@echo "\033[0;34m[#] Building\033[0m"
	docker-compose up --build -d

	@echo "\e[32m[#] Running!\e[0m"

attached-run:
	@echo "\033[0;34m[#] Killing old docker processes\033[0m"
	docker-compose down -v -t 1

	@echo "\033[0;34m[#] Building\033[0m"
	docker-compose up --build

	@echo "\e[32m[#] Running!\e[0m"
