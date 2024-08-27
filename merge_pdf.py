from tkinter import *
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

root = Tk()
root.title("PDF Merger")
root.geometry("400x400")  # 창 크기를 더 크게 조정

selected_pdfs = []

def add_pdfs():
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if files:
        for file in files:
            selected_pdfs.append(file)
            pdf_listbox.insert(END, file)
        status_label.config(text="PDF 파일이 선택되었습니다.", fg="blue")

def merge_pdfs():
    if not selected_pdfs:
        messagebox.showwarning("경고", "PDF 파일을 선택하세요.")
        return
    
    merger = PdfMerger()
    
    for pdf in selected_pdfs:
        merger.append(pdf)
    
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Save Merged PDF As")
    if output_path:
        merger.write(output_path)
        merger.close()
        status_label.config(text="PDF 파일이 성공적으로 병합되었습니다.", fg="green")
    else:
        status_label.config(text="저장할 파일이 선택되지 않았습니다.", fg="red")

def clear_list():
    pdf_listbox.delete(0, END)
    selected_pdfs.clear()
    status_label.config(text="파일 목록이 초기화되었습니다.", fg="orange")

# PDF 파일 추가 버튼
add_button = Button(root, text="PDF 파일 추가", command=add_pdfs)
add_button.pack(pady=10)

# 선택된 PDF 파일 목록 표시
pdf_listbox = Listbox(root, width=50, height=10)
pdf_listbox.pack(pady=10)

# 파일 목록 초기화 버튼
clear_button = Button(root, text="파일 목록 초기화", command=clear_list)
clear_button.pack(pady=5)

# 병합 시작 버튼 스타일 정의
def on_enter(e):
    merge_button['background'] = '#4CAF50'  # 마우스 오버 시 배경색 변경
    merge_button['foreground'] = 'white'

def on_leave(e):
    merge_button['background'] = '#3E8E41'  # 기본 배경색으로 복원
    merge_button['foreground'] = 'white'

merge_button = Button(root, text="PDF 병합하기", command=merge_pdfs, font=("Arial", 12),
                      background='#3E8E41', foreground='white', width=20, height=2, bd=3, relief=RAISED)

merge_button.bind("<Enter>", on_enter)  # 마우스가 버튼 위로 올라갔을 때
merge_button.bind("<Leave>", on_leave)  # 마우스가 버튼을 떠났을 때

merge_button.pack(pady=20)

# 상태 표시 레이블
status_label = Label(root, text="", font=("Arial", 10))
status_label.pack(pady=5)

root.mainloop()
