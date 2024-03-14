from artifacts.test_data.test_table import TEST_TABLE
from latex_generator.latex_kelonmyosa import add_table, create_latex_document, end_document, save_document


def table_to_latex(table: list[list], path: str = "table.tex"):
    doc = create_latex_document()
    doc = add_table(doc, table)
    doc = end_document(doc)
    save_document(doc, path)


if __name__ == "__main__":
    table_to_latex(TEST_TABLE, "artifacts/table.tex")
