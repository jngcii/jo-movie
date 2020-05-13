from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import ReviewForm, CommentForm
from .models import Review, Comment
from movies.models import Movie

# Create your views here.

# 리뷰 생성
@login_required
@require_POST
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.reviewer = request.user
        review.movie = movie
        review.save()
        return redirect('detail', movie_pk)
    else:
        messages.error(request, '리뷰를 다시 입력해주세요.')
    return redirect('detail', movie_pk)

# 리뷰 수정
@login_required
@require_POST
def update_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    movie_pk = review.movie.id
    form = ReviewForm(request.POST, instace=review)

    if form.is_valid():
        form.save()
        return redirect('detail', movie_pk)
    else:
        messages.error(request, '리뷰를 다시 입력해주세요.')
    return redirect('detail', movie_pk)

# 리뷰 삭제
@login_required
def delete_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    movie_pk = review.movie.id
    if review.reviewer == request.user:
        review.delete()
    else:
        message.error(request, '삭제 권한이 없습니다.')
    return redirect('detail', movie_pk)

# 리뷰 디테일
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm()
    context = {
        'form':form,
        'review':review,
    }
    return render(request, 'review/detail.html', context)

# 코멘트 생성
@login_required
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.commenter = request.user
        comment.review = review
        comment.save()
        return redirect('reviews:detail', review_pk)
    else:
        messages.error(request, '댓글을 다시 입력해주세요.')
    return redirect('reviews:detail', movie_pk)

# 코멘트 수정
@login_required
@require_POST
def update_comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    review_pk = comment.review.id
    form = commentForm(request.POST, instace=comment)

    if form.is_valid():
        form.save()
        return redirect('reviews:detail', review_pk)
    else:
        messages.error(request, '댓글을 다시 입력해주세요.')
    return redirect('reviews:detail', review_pk)

# 코멘트 삭제
@login_required
def delete_comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    review_pk = comment.review.id
    if comment.commenter == request.user:
        comment.delete()
    else:
        message.error(request, '삭제 권한이 없습니다.')
    return redirect('reviews:detail', review_pk)