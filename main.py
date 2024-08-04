import PySimpleGUI as sg
import img2pdf
from tkinter import filedialog
import tkinter as tk
import os

# Function to select images
def select_images():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_paths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff")]
    )
    return file_paths

# Function to convert images to PDF
def convert_images(file_paths, output_pdf):
    if not file_paths:
        sg.popup_error("Nenhuma imagem selecionada")
        return

    if not output_pdf:
        sg.popup_error("Nenhum arquivo de saída selecionado.")
        return

    if os.path.splitext(output_pdf)[1].lower() != '.pdf':
        sg.popup_error("O arquivo de saída deve ser um pdf.")
        return

    if os.path.exists(output_pdf):
        overwrite = sg.popup_yes_no("Arquivo já existe, deseja substituí-lo?")
        if overwrite == "No":
            return

    try:
        with open(output_pdf, "wb") as f:
            f.write(img2pdf.convert(file_paths))
        sg.popup(f"PDF salvo como: {output_pdf}")
    except Exception as e:
        sg.popup_error(f"An error occurred: {e}")

# Layout for the PySimpleGUI window

button_select_image = b'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'
button_convert_image = b'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'

layout = [
    #
    [sg.Text("Selecione as imagens para converter para PDF", font=("Helvetica", 12, 'bold'), )],
    [sg.Button(image_data=button_select_image, key="select_images", border_width=0)],
    [sg.Text("", size=(40, 1), key="status_text", font=("Helvetica", 12, 'bold'))],
    [sg.Text("", size=(40, 5), key="file_list", font=("Helvetica", 8, 'bold'))],
    [sg.Button(image_data=button_convert_image, key="convert_button", border_width=0, disabled=True)]
]

# Create the window
window = sg.Window("Conversor para PDF", layout, resizable=True, size=(600, 400), finalize=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "select_images":
        file_paths = select_images()
        if file_paths:
            window["file_list"].update("\n".join(file_paths))
            num_files = len(file_paths)
            status_message = f"{num_files} image{'ns' if num_files > 1 else 'm'} selecionada{'s' if num_files > 1 else ''}."
            window["status_text"].update(status_message)
            window["convert_button"].update(disabled=False)  # Enable button if files exist
            
    elif event == "convert_button":
            
        output_pdf = sg.popup_get_file(
            'Selecionar pasta', 
            save_as=True, 
            file_types=(("PDF Files", "*.pdf"),),
            default_extension="pdf"
            )
        
        if output_pdf:
            if not output_pdf.lower().endswith('.pdf'):
                output_pdf += '.pdf'
                
            convert_images(file_paths, output_pdf)
            
        else:
           sg.popup_error("Nenhum arquivo de saída selecionado, tente de novo.") 

window.close()
