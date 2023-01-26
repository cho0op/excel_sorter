import time

from openpyxl.reader.excel import load_workbook

from classes.SheetRangeService import SheetRangeService


def main():
    workbook = load_workbook(filename="excel_file_to_sort.xlsx")
    sheet = workbook.active
    sheet_range_service = SheetRangeService(sheet)

    ranges = sheet_range_service.find_ranges_to_sort()
    try:
        start_time = time.time()
        for range in ranges:
            sheet_range_service.sort_by_range(range.start, range.end)
        print("--- %s sorting time ---" % (time.time() - start_time))
    finally:
        workbook.save("excel_file_to_sort_ready.xlsx")


if __name__ == "__main__":
    main()
