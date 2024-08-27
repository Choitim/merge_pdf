# PDF Merger

이 프로젝트는 여러 개의 PDF 파일을 하나의 PDF로 병합할 수 있는 간단한 Python 프로그램입니다. Tkinter를 사용하여 GUI를 제공하며, PyPDF2를 사용하여 PDF 파일을 병합합니다.

## 주요 기능

- 여러 개의 PDF 파일을 하나의 PDF로 병합
- 출력 파일 위치를 선택할 수 있는 간편한 GUI 제공
- 병합 성공 또는 오류에 대한 상태 업데이트

## 요구 사항

- Python 3.x
- `tkinter` (GUI 용)
- `PyPDF2` (PDF 병합 용)

## 설치 방법

1. **저장소 클론하기**:

   ```bash
   git clone https://github.com/your-username/pdf-merger.git
   cd pdf-merger
   ```

2. **가상환경 생성하기**:
    ```bash
    python -m venv env
    ```

    가상환경 활성화:
    </br>
    </br>
    (window)
    ```bash
    .\env\Scripts\activate
    ```
     (macOS/Linux)
    </br>
     ```bash
    source env/bin/activate
    ```

3. **package** 설치하기

    ```bash
    pip install -r requirements.txt
    ```


4. **실행하기**
    ```bash
    python pdf_merger.py
    ```