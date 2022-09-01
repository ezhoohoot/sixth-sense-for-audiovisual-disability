# sixth-sense-for-audiovisual-disability
AI device for audiovisual disability to provide information by haptic stimulation

# requirements
준비물 : 아두이노 나노, 라즈베리파이, 점퍼선 및 진동(EMS) 모듈

# 회로 구성
회로 구성은 첨부파일의 '회로 구성 및 설명.ppt' 파일을 확인해주세요.

# 라즈베리 파이 준비
https://velog.io/@yoonj1n/%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%ED%8C%8C%EC%9D%B4-%EC%9A%B0%EB%B6%84%ED%88%AC-%EB%AF%B8%EB%8B%88%EC%BD%98%EB%8B%A4-%EC%84%A4%EC%B9%98
https://pinkwink.kr/1352
위 블로그들을 참고하여 라즈베리 파이의 기본 셋팅을 진행해줍니다.

# 아래의 깃허브를 통해 라즈베리 파이에 필요한 파일들을 받아주세요.
https://github.com/ezhoohoot/sixth-sense-for-audiovisual-disability.git
원하는 디렉토리로 이동 후 
git clone https://github.com/ezhoohoot/sixth-sense-for-audiovisual-disability.git
커멘드를 통해 다운받으실 수 있습니다.

# 라즈베리 파이의 터미널을 열고, 아래 커멘드를 통해 필요한 파이썬 라이브러리를 다운받아주세요.
# 아나콘다 가상환경 이용을 권장드립니다.

conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
pip install opencv-python
pip install mediapipe
pip install easyocr
pip install jamo

# 오류가 발생하는 경우, 아래 커맨드를 실행해주세요.
pip uninstall opencv-python
pip uninstall opencv-python-headless
pip install opencv-python
pip install opencv-python-headless

# 라즈베리파이의 블루투스 통신은 아래 링크를 참고해주세요.
https://popcorn16.tistory.com/196

# 데모 실행
깃허브의 sensing 폴더 안에
demo_raspberrypi.py 파일을 실행하면 데모를 실행할 수 있습니다.
라즈베리 파이가 아닌 컴퓨터 환경에서 테스트 해보시려면 demo_test.py 파일을 실행해주세요.


# 기타 참고 자료 링크
https://github.com/kth920517/Delphi-Hangul-Parser