from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfMerger

root = Tk()
root.title("PDF Merger")

def merge_pdfs():
    # 병합할 파일 리스트 (1.pdf ~ 7.pdf)
    pdfs = ['1.pdf', '2.pdf', '3.pdf', '4.pdf', '5.pdf', '6.pdf', '7.pdf'] # pdf 파일 경로를 지정해서 입력해주면 된다. 
    
    # PdfMerger 객체 생성
    merger = PdfMerger()
    
    # 모든 PDF 파일 병합
    for pdf in pdfs:
        merger.append(pdf)
    
    # 병합된 파일을 저장할 경로 지정
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Save Merged PDF As")
    if output_path:
        merger.write(output_path)
        merger.close()
        status_label.config(text="PDF 파일이 성공적으로 병합됨", fg="green")
    else:
        status_label.config(text="저장할 파일이 선택되지 않았음", fg="red")

# 병합 시작 버튼
select_button = Button(root, text="PDF 병합하기", command=merge_pdfs)
select_button.pack(pady=10)

# 상태 표시 레이블
status_label = Label(root, text="", font=("Arial", 10))
status_label.pack(pady=5)

root.mainloop()
