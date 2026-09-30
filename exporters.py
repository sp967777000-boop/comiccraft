from fpdf import FPDF
import os


def save_pdf(panel_paths, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=False)

    for panel_path in panel_paths:
        pdf.add_page()

        pdf.image(
            panel_path,
            x=0,
            y=0,
            w=210,
            h=297
        )

    pdf.output(output_path)

    return output_path