# 250717 Offline

Git 이란? **분산 저장 관리**
    : 버전 기록을 통한 효과적인 협업 가능 

`git status` : 현재 상태 확인
    - 현재 브랜치에서 수정된 파일과 커밋되지 않은 변경사항 확인

`git add` : 변경사항 스테이징
    - 변경된 파일을 커밋할 준비 상태로 올림 (가상의 스테이징 에어리어에 추가)
    `git add file_name` 특정 파일만 추가
    `git add .` 현재 티렉토리의 전체 변경사항 추가
    `git add -p` 부분적으로 선택해 추가

`git commit` : 커밋 생성 명령어
    `git commit -m "description message"` - 커밋 생성
    cf) 깃커밋 단독 입력 시 vim 진입: vim 인서트(입력) 명령어 i , 저장 후 나가기 wq
`git log`
`git log oneline`
`git log -p`