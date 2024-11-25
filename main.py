def check_category(line):
    parts = line.strip().split(',')
    return bool(parts[2]) if len(parts) > 2 else False


def process_line(line, result_file_handler):
    if check_category(line):
        result_file_handler.write(line)


if __name__ == '__main__':
    with open('visits_log.csv', 'r') as log_file:
        with open('funnel.csv', 'w', encoding='utf-8') as results_file:
            for line in log_file:
                process_line(line, results_file)

    with open('funnel.csv', 'r') as file:
        counter = 0
        for line in file:
            print(line, end='')
            counter += 1
            if counter == 3: break

