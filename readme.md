# PDF Merger

PDF를 병합하는 Python 프로그램입니다. Tkinter를 사용하여 GUI를 제공하며, PyPDF2를 사용하여 PDF 파일을 병합합니다.
그렇다면 왜 PDF 병합 프로그램을 로컬에서 사용해야 할까요? 웹 상에 존재하는 무료 PDF 병합 프로그램들은 모두 파일을 업로드 시 그 파일이Host 서버로 전송되기 때문에 파일 유출의 가능성이 존재합니다.
따라서 정보 유출을 막기 위해서라도 로컬에서 사용하는 것이 보안에 좋을 것입니다. 


## 주요 기능

- 여러 개의 PDF 파일을 하나의 PDF로 병합
- 출력 파일 위치를 선택할 수 있는 간편한 GUI 제공
- 병합 성공 또는 오류에 대한 상태 업데이트

## 요구 사항

- `Python` 3.9 이상
- `tkinter` (GUI 용) **tkinter가 없으면 코드 자체가 실행이 안될 수 있습니다.**
- `PyPDF2` (PDF 병합 용)
</br>
따라서 tkinter가 있는지 먼저 확인을 해봅시다. (tkinter 뭐 이상한거 아니고, python에서 제공되는 GUI Interface임.

```bash
python -m tkinter
```

Tkinter 창이 열려야 합니다. 창이 열리지 않는다면, Python에 tkinter가 포함되지 않은 것이기 때문에 다시 재 설치를 해줘야 합니다. 

**mac의 경우**
```bash
brew install tcl-tk
```
python 재설치를 진행해줍니다.
```bash
brew reinstall python
```

그 다음 다시 tkinter의 설치 여부를 확인해보고 잘 설치 되었다면 아래 가이드를 계속 진행합니다. 


**window의 경우**
tkinter 설치 여부를 확인한 후 
```bash
python -m tkinter
```
python 재설치를 진행해줍니다.
https://docs.python.org/3.12/

    1. "Add Python to PATH" 선택: 설치 화면에서 "Add Python to PATH" 옵션을 체크합니다. 이 옵션을 선택하면, 명령 프롬프트에서 Python을 쉽게 실행할 수 있습니다.
   
    2. "Customize installation" 선택: 기본 설정 대신 "Customize installation"을 선택합니다.

    3. Optional Features 선택: "Optional Features" 화면에서 "tcl/tk and IDLE" 항목이 체크되어 있는지 확인합니다. 이 항목이 Tkinter를 설치하게 됩니다.


다시 확인해본 다음에 아래 가상환경을 실행하고, 가이드 대로 실행합니다.
## 설치 방법

1. **github Clone 하기**:

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


---
프로그램이 실행되었을 때, 아래와 같은 화면이 뜨게 됩니다.</br>
![image](https://github.com/user-attachments/assets/885a3fb2-e236-4d6e-b651-05c8187c3818)

위 화면에서 pdf 파일 추가 버튼을 클릭하고 병합하고 싶은 순서대로 파일을 넣어서 아래 초록색 병합하기 버튼을 클릭해주시면 됩니다. 버튼을 클릭하면 병합할 파일의 저장 경로를 지정해주고 진행해주시면 됩니다. 
</br> 
(아마 맥 환경에서 병합하기 버튼이 색깔 때문에 잘 안보일 수도 있음.)
병합이 성공하게 되면 초록색 글자로 병합이 성공되었다고 뜹니다. 

---
프로그램이 실행이 안될 시 아래 Instagram으로 DM 또는 이메일 주세요. </br>
<a href="https://www.instagram.com/dev.choi28/"><img src="https://img.shields.io/badge/Instagram-E4405F?style=flat&logo=instagram&logoColor=white"></a>
