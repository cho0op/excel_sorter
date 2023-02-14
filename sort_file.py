import time

from openpyxl.reader.excel import load_workbook

from classes.SheetRangeService import SheetRangeService
from constants.files import get_ready_file_name


def sort_file(file_name):
    workbook = load_workbook(filename=file_name)
    sheet = workbook.active
    sheet_range_service = SheetRangeService(sheet)

    ranges = sheet_range_service.find_ranges_to_sort()
    try:
        start_time = time.time()
        for range in ranges:
            sheet_range_service.sort_by_range(range.start, range.end)
        print("--- %s sorting time ---" % (time.time() - start_time))
    finally:
        workbook.save(get_ready_file_name(file_name))
