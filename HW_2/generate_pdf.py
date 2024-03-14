import os
import subprocess

from artifacts.test_data.test_table import TEST_TABLE
from latex_kelonmyosa import (
    add_empty_line,
    add_image,
    add_table,
    create_latex_document,
    end_document,
    save_document,
)


def table_and_img_to_latex(table: list[list], img_path: str, path: str = "for_pdf.tex"):
    doc = create_latex_document()
    doc = add_table(doc, table)
    doc = add_empty_line(doc)
    doc = add_image(doc, img_path, "8cm")
    doc = end_document(doc)
    save_document(doc, path)


if __name__ == "__main__":
    output_dir = "./artifacts/pdf"
    latex_file = f"{output_dir}/latex.tex"

    os.makedirs(output_dir, exist_ok=True)

    table_and_img_to_latex(TEST_TABLE, "../test_data/test.jpg", latex_file)

    command = ["pdflatex", "-output-directory", output_dir, latex_file, "-interaction=nonstopmode"]
    subprocess.run(command, check=True)
