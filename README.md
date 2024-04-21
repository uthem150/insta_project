# 인스타그램 프로젝트  
<br>

| 실행화면 |
|:------------------------------------------------------:|
|![ezgif-2-f0fce298c6](https://github.com/uthem150/insta_project/assets/142042011/a95d34f1-8a3f-4240-88c8-c923d54f922b)|

<br>

## 📍개발 스택
front : HTML, CSS, JS  
back : MariaDB, Nginx, Django, Docker  
  
장고만으로는 배포용으로 만들어진 소프트웨어가 아니기 때문에,  
웹서버에 해당하는 소프트웨어를 넣어주기 위해 nginx선택  


## 📍주요 기능
게시물 작성, 수정, 삭제
게시글 좋아요 기능, 댓글 기능
Pinterest 카드형 레이아웃 구현(MagicGrid)
Pagination


## 📌 구현 분류

### Accounts App 
    - 회원가입 
    - MyPage                 (paginate_by = 5)
    - 비밀번호 변경           (login_required, account_ownership_required)
    - 회원탈퇴               (login_required, account_ownership_required)
    - 로그인, 로그아웃

### Article App
    - 게시글 생성            (login_required)
    - 게시글 뷰
    - 게시글 변경            (article_ownership_required)
    - 게시글 삭제            (article_ownership_required)
    - 모든 게시글의 목록 뷰   (paginate_by = 5)

### Project App
    - 프로젝트 생성           (login_required ) 
    - 프로젝트 상세 뷰        (paginate_by = 25) 
    - 프로젝트 리스트 뷰      (paginate_by = 25)  

### Comment App
    - 댓글 생성
    - 댓글 삭제               (comment_ownership_required)
    
### Profile App
    - 프로필 생성
    - 프로필 변경             (profile_ownership_required)

### Subscribe App
    * 구독 기능 구현          (login_required)
    * 구독한 프로젝트의 모든 게시글을 보여주는 기능 구현 (login_required) (paginate_by = 5)






