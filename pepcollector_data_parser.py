from parser_functions import *

FOLDER_PATH = "logs"

BUS_ORDER = [
    3035, 3213, 3895, 3783, 10063, 3699, 10055, 10059, 13024, 11283,
    13021, 13071, 13023, 11282, 13063, 13059, 13055, 13057, 13056,
    13022, 13422, 13421, 11164, 10428, 11190, 10817, 3890, 3779,
    4041, 13058
]

def main():
    cell_tests, speed_tests, cliusage_tests, internet_tests = load_csv_files(FOLDER_PATH)
    summary_data, bearer_columns = prepare_summary_data(cell_tests, speed_tests, cliusage_tests, internet_tests)

    for column in bearer_columns:
        if column not in summary_data:
            summary_data[column] = None

    save_to_csv(summary_data, 'resultados_buses_ordenados_comas.csv', BUS_ORDER)


if __name__ == "__main__":
    main()


