from copy import deepcopy

from classes.Range import Range
from constants.table_constants import ID_ROW_INDEX, ID_ROW_HEADER, PRICE_ROW_INDEX


class SheetRangeService:
    sheet = None

    def __init__(self, sheet):
        self.sheet = sheet

    def generate_range(self, range_start):
        range_end = range_start + 1
        while self.sheet[range_end][ID_ROW_INDEX].value is not None:
            range_end += 1
        return Range(range_start + 1, range_end - 1)

    def find_ranges_to_sort(self):
        row_count = self.sheet.max_row
        start_range_creating = False
        ranges = []
        for row_index in range(1, row_count):
            first_cell_value = self.sheet[row_index][ID_ROW_INDEX].value
            if first_cell_value == ID_ROW_HEADER:
                start_range_creating = True
            if start_range_creating:
                next_cell_value = self.sheet[row_index + 1][ID_ROW_INDEX].value
                if first_cell_value is None and next_cell_value is not None:
                    ranges.append(self.generate_range(row_index))
        print("generated ranges: " + str(ranges))
        return ranges

    def sort_by_range(self, min_row, max_row):
        rows_to_sort = []
        for row in self.sheet.iter_rows(min_row, max_row):
            rows_to_sort.append(row)

        sorted_rows = sorted(deepcopy(rows_to_sort), key=lambda r: r[PRICE_ROW_INDEX].value)

        for row_index in range(len(rows_to_sort)):
            row = rows_to_sort[row_index]
            for cell_index in range(len(row)):
                rows_to_sort[row_index][cell_index].value = sorted_rows[row_index][cell_index].value
            print(f"sorted: {row}")
