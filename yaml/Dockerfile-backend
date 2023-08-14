# 베이스 이미지 설정
FROM ubuntu:20.04

# 포트 열기
EXPOSE 8000

# 기본 패키지 및 도구 설치
RUN apt-get update && apt-get install -y vim curl git python3 python3-venv python3-pip libmysqlclient-dev libpq-dev

# 작업 디렉토리 설정
WORKDIR /home

# Python 가상 환경 생성
RUN python3 -m venv venv

# 가상 환경 활성화 및 프로젝트 코드 클론
RUN . venv/bin/activate && \
    git clone https://github.com/kakao-cloud-school/3-tier-back-hisoonni.git

# 작업 디렉토리 변경
WORKDIR /home/3-tier-back-hisoonni

# 프로젝트 의존성 설치
RUN pip install -r requirements.txt

# 데이터베이스 마이그레이션
CMD python3 manage.py makemigrations && \
    python3 manage.py migrate

# 컨테이너 실행 시 서버 시작
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
