from django.http import HttpResponseForbidden

from commentapp.models import Comment #Comment 모델을 가져옴

# 다른 사용자가 해당 댓글 삭제 URL을 알고 있어도 삭제를 시도할 수 없도록 함
def comment_ownership_required(func): #다른 함수를 매개변수로 받고, 데코레이터로 감싸진 함수를 반환
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk']) #Comment 모델에서 주어진 pk 값을 가진 댓글을 가져옴
        if not comment.writer == request.user: #가져온 댓글의 작성자(comment.writer)와 요청한 사용자(request.user)를 비교하여 소유권을 확인
            return HttpResponseForbidden()
        return func(request, *args, **kwargs) #소유권이 확인되면 원래의 함수(func)를 호출하여 요청을 처리하고, 그 결과를 반
    return decorated