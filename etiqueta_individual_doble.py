import os
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128
# The following imports are necessary for reportlab to work properly
from reportlab.graphics.barcode import code93
from reportlab.graphics.barcode import code39
from reportlab.graphics.barcode import usps
from reportlab.graphics.barcode import usps4s
from reportlab.graphics.barcode import ecc200datamatrix

def create_individual_label_pdf(label_data):
    page_size = (104 * mm, 25 * mm)

    directory = "Etiquetas Generadas"
    filename = "Etiqueta Individual doble.pdf"
    full_path = os.path.join(directory, filename)

    # Create a new PDF file
    c = canvas.Canvas(full_path, pagesize=page_size)

    # Set the font and font size
    c.setFont("Helvetica", 10)

    # Calculate the label dimensions
    label_width = 50 * mm
    label_height = 25 * mm
    space_between_labels = 4 * mm

    # Variable for horizontal displacement of the second label
    x = 0

    # Draw the label border
    #c.rect(0, 0, label_width, label_height)

    for i in range(2):
        # Text1
        # Draw the barcode number
        c.setFont("Helvetica-Bold", 8)
        text = label_data[0]
        text_width = c.stringWidth(format(text))
        c.drawString(x + (label_width - text_width) / 2, 21 * mm, format(text))

        # Draw the barcode
        barcode_number = label_data[0]
        barcode = code128.Code128(barcode_number, barHeight=8 * mm, barWidth=1.0)
        barcode.drawOn(c, x + (label_width - barcode.width) / 2, 12 * mm)

        # Text2
        c.setFont("Helvetica", 7)
        text = label_data[1]
        text_width = c.stringWidth(format(text))
        c.drawString(x + (label_width - text_width) / 2, 9 * mm, format(text))

        # Text3 and Text4
        c.setFont("Helvetica", 7)
        text = label_data[2] + "      " + label_data[3]
        text_width = c.stringWidth(format(text))
        c.drawString(x + (label_width - text_width) / 2, 5.5 * mm, format(text))

        # Text5 and Text6
        c.setFont("Helvetica", 7)
        text = label_data[4] + "  " + label_data[5]
        text_width = c.stringWidth(format(text))
        c.drawString(x + (label_width - text_width) / 2, 2 * mm, format(text))

        # Add the space between labels + the size of a label to the displacement
        x = x + label_width + space_between_labels

    # Save the PDF and close the canvas
    c.save()