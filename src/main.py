from processor import calculation_processor

EXIT_VALUE = 4

while True:
    exit_value = calculation_processor()

    if exit_value == EXIT_VALUE:
        break
