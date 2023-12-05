"""
Tests
"""
from run import import_data, rename_columns, random_row, concat_dataset, column_totalsepal, column_totalpetal

def test_import_data():
    """
    Test la fonction import_data
    """
    data = import_data()
    assert data.shape[0] > 0

def test_rename_columns():
    """
    Test la fonction rename_columns
    """
    data = import_data()
    data_renamed = rename_columns(data)
    assert "sepal_length" in data_renamed.columns

def test_random_row():
    """
    Test la fonction random_row
    """
    data = import_data()
    random_lines = random_row(data, 50)
    assert len(random_lines) == 50

def test_concat_dataset():
    """
    Test la fonction concat_dataset
    """
    data = import_data()
    concatenated_data = concat_dataset(data)
    assert concatenated_data.shape[0] == 3 * 50  # Trois fois le nombre initial de lignes

def test_column_totalsepal():
    """
    Test la fonction column_totalsepal
    """
    data = import_data()
    data_renamed = rename_columns(data)
    data_with_totals = column_totalsepal(data_renamed)
    assert "total_sepal" in data_with_totals.columns

def test_column_totalpetal():
    """
    Test la fonction column_totalpetal
    """
    data = import_data()
    data_renamed = rename_columns(data)
    data_with_totals = column_totalpetal(data_renamed)
    assert "total_petal" in data_with_totals.columns



# """
# Tests
# """
# from run import import_data, rename_columns,random_rows,concat_dataset,column_totalsepal,column_totalpetal


# def test_import_data():
#     """
#     Test
#     """
#     data = import_data()
#     assert data.shape[0] > 0


# def test_rename_columns():
#     """
#     Doc
#     """
#     data = import_data()
#     data_renamed = rename_columns(data)
#     assert "sepal_length" in data_renamed.columns

# def test_random_rows():
#     """"
#     Doc
#     """
#     data = import_data()
#     few_line = random_rows(data,50)
#     assert len(few_line) == 50

# # def test_concact_dataset():
# #     """
# #     Doc
# #     """

