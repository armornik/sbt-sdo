from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
NAME_ORGANIZATION = 'СБТ'


# Create your views here.
@login_required
def topics(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/topics.html', context=context)


@login_required
def study_start(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/topics_a.html', context=context)


@login_required
def topics_b(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/topics_b.html', context=context)


@login_required
def topics_c(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/topics_c.html', context=context)


@login_required
def topics_d(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/topics_d.html', context=context)


@login_required
def topics_e(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/topics_e.html', context=context)


@login_required
def topic_1_1(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_a_1.html', context=context)


@login_required
def topic_1_2(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_a_2.html', context=context)


@login_required
def topic_1_3(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_a_3.html', context=context)


@login_required
def topic_1_4(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_a_4.html', context=context)


@login_required
def topic_1_5(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_a_5.html', context=context)


@login_required
def topic_2_1(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_b_1.html', context=context)


@login_required
def topic_2_2(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_b_2.html', context=context)


@login_required
def topic_2_3(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_b_3.html', context=context)


@login_required
def topic_2_4(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_b_4.html', context=context)


@login_required
def topic_3_1(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_c_1.html', context=context)


@login_required
def topic_3_2(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_c_2.html', context=context)


@login_required
def topic_3_3(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_c_3.html', context=context)


@login_required
def topic_3_4(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_c_4.html', context=context)


@login_required
def topic_3_5(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_c_5.html', context=context)


@login_required
def topic_3_6(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_c_6.html', context=context)


# @login_required
# def topic_3_7(request):
#     context = {
#         'title': f'СДО {NAME_ORGANIZATION}',
#         'name': NAME_ORGANIZATION,
#     }
#     if request.method == 'POST':
#         pass
#     return render(request, 'studyapp/studying_c_7.html', context=context)
#
#
# @login_required
# def topic_3_8(request):
#     context = {
#         'title': f'СДО {NAME_ORGANIZATION}',
#         'name': NAME_ORGANIZATION,
#     }
#     if request.method == 'POST':
#         pass
#     return render(request, 'studyapp/studying_c_8.html', context=context)


@login_required
def topic_4_1(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_d_1.html', context=context)


@login_required
def topic_4_2(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_d_2.html', context=context)


@login_required
def topic_4_3(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_d_3.html', context=context)


@login_required
def topic_4_4(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_d_4.html', context=context)


@login_required
def topic_4_5(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_d_5.html', context=context)


@login_required
def topic_4_6(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_d_6.html', context=context)


@login_required
def topic_4_7(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_d_7.html', context=context)


@login_required
def topic_4_8(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_d_8.html', context=context)


@login_required
def topic_4_9(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_d_9.html', context=context)


@login_required
def topic_5_0(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_e_0.html', context=context)


@login_required
def topic_5_1(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_e_1.html', context=context)


@login_required
def topic_5_2(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_e_2.html', context=context)


@login_required
def topic_5_3(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_e_3.html', context=context)


@login_required
def topic_5_4(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_e_4.html', context=context)


@login_required
def topic_5_5(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_e_5.html', context=context)


@login_required
def topic_5_6(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_e_6.html', context=context)


@login_required
def topic_5_7(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_e_7.html', context=context)


@login_required
def topic_5_8(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_e_8.html', context=context)


@login_required
def topic_5_9(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_e_9.html', context=context)


@login_required
def topic_5_10(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_e_10.html', context=context)


@login_required
def topic_5_11(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_e_11.html', context=context)


@login_required
def topic_5_12(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_e_12.html', context=context)


@login_required
def topic_5_13(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_e_13.html', context=context)


@login_required
def topic_5_14(request):
    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'studyapp/studying_e_14.html', context=context)

# @login_required
# def test_a(request):
#     print(request)
#     student = AppUser.objects.filter(username=request.user).first()
#     context = {
#         'title': f'СДО {NAME_ORGANIZATION}',
#         'name': NAME_ORGANIZATION,
#         'questions': QUESTIONS_A,
#         'student': student,
#     }
#     if request.method == 'POST':
#         pass
#     return render(request, 'studyapp/test_a.html', context=context)
