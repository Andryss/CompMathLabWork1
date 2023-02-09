import pandas as pd
from modified_gauss import *


# func to beautify the result
def print_result(result: ResultContainer):
    print("\nCOMPUTATION COMPLETE\n")
    print("Original matrix:")
    print(format_matrix(result.original_matrix), end="\n\n")

    print("Solution count:", result.solution_count, end="\n\n")

    if result.solution_count != SolutionCount.ONE:
        return

    print("Triangle matrix:")
    print(format_matrix(result.triangle_matrix), end="\n\n")

    print("Determinant:", format_number(result.determinant), end="\n\n")

    print("Answer:")
    print(format_matrix(result.answer), end="\n\n")

    print("Residual:")
    print(format_matrix(result.answer_residual))


def format_matrix(matrix: np.ndarray) -> np.ndarray:
    return matrix.round(5)


def format_number(number: float) -> float:
    return round(number, 5)


def read_n() -> int:
    line = input("Enter n:\n").strip()
    n: int
    try:
        n = int(line)
        if n < 1:
            raise Exception("n must be positive")
    except Exception:
        n = read_n_from_file(line)
    return n


def read_n_from_file(filename: str) -> int:
    frame: pd.DataFrame
    try:
        frame = pd.read_csv(filename, header=None)
        validate_file_n(frame)
    except Exception as e:
        raise Exception("file \"" + filename + "\" can't be opened: " + e.__str__())
    return frame[0][0]


def validate_file_n(frame: pd.DataFrame):
    if len(frame) != 1 or len(frame[0]) != 1 or not isinstance(frame[0][0], np.integer) or frame[0][0] < 1:
        raise Exception("must contains only one number (positive integer)")


def read_matrix(n: int) -> np.ndarray:
    line = input("Enter matrix:\n").strip()
    args = line.split()
    result: np.ndarray
    if len(args) != n + 1:
        result = read_matrix_from_file(line)
        if len(result) != n:
            raise Exception("wrong elements count in file")
    else:
        matrix = [[float(x) for x in args]]
        for i in range(1, n):
            args = input().strip().split()
            if len(args) != n + 1:
                raise Exception("wrong elements count")
            matrix.append([float(x) for x in args])
        result = np.array(matrix)
    return result


def read_matrix_from_file(filename: str) -> np.ndarray:
    frame: pd.DataFrame
    try:
        frame = pd.read_csv(filename, header=None)
        validate_file_matrix(frame)
    except Exception as e:
        raise Exception("file \"" + filename + "\" can't be opened: " + e.__str__())
    return frame.values


def validate_file_matrix(frame: pd.DataFrame):
    for row in frame.values:
        for val in row:
            if not isinstance(val, np.number):
                raise Exception("Must contains only numbers (integer or real)")


def run():
    try:
        print_result(calculate_gauss_from_parameters(read_matrix(read_n())))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    run()
