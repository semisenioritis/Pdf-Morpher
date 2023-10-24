from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
import re

# Function to replace "I" with "X" in the text
def replace_I_with_X(input_text):
    return re.sub(r' ', ' ....... ', input_text)


# Path to the text file
text_file_path = "input.txt"  # Change this to the path of your text file

# Read the text from the file
with open(text_file_path, 'r') as file:
    input_text = file.read()

# Replace "I" with "X"
modified_text = replace_I_with_X(input_text)

counter_file_path="counter.txt"

with open(counter_file_path, 'r') as file:
    counterr = file.read()

with open(counter_file_path, 'w') as file:
    counterr = (int(counterr) + 1)
    file.write(str(counterr))


# Create a PDF document
pdf_filename = "output"+str(counterr)+".pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

# Define styles for the PDF content
styles = getSampleStyleSheet()
centered = Paragraph(modified_text, styles["Normal"])
centered.alignment = TA_CENTER

# Build the PDF content
content = [centered]

# Generate the PDF
doc.build(content)

print(f"PDF generated as {pdf_filename}")
