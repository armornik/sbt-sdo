from django.urls import path

from .views import study_start, topic_1_1, topic_1_2, topic_1_3, topic_1_4, topic_1_5, topics, topic_2_1, topic_2_2, \
    topic_2_3, topic_2_4, topic_3_1, topic_3_2, topic_3_3, topic_3_4, topic_3_5, topic_3_6, topic_4_1, topic_4_2, \
    topic_4_3, topic_4_4, topic_4_5, topic_4_6, topic_4_7, topic_4_8, topic_4_9, topic_5_0, topic_5_1, topic_5_2, \
    topic_5_3, topic_5_4, topic_5_5, topic_5_6, topic_5_7, topic_5_8, topic_5_9, topic_5_10, topic_5_11, topic_5_12, \
    topic_5_13, topic_5_14, topics_b, topics_c, topics_d, topics_e

app_name = 'studyapp'

urlpatterns = [
    path('', study_start, name='study_start'),
    # path('test-a', test_a, name='test_a'),
    path('topics', topics, name='topics'),
    path('topics-b', topics_b, name='topics_b'),
    path('topics-c', topics_c, name='topics_c'),
    path('topics-d', topics_d, name='topics_d'),
    path('topics-e', topics_e, name='topics_e'),
    path('topic-1-1', topic_1_1, name='topic_1_1'),
    path('topic-1-2', topic_1_2, name='topic_1_2'),
    path('topic-1-3', topic_1_3, name='topic_1_3'),
    path('topic-1-4', topic_1_4, name='topic_1_4'),
    path('topic-1-5', topic_1_5, name='topic_1_5'),
    path('topic-2-1', topic_2_1, name='topic_2_1'),
    path('topic-2-2', topic_2_2, name='topic_2_2'),
    path('topic-2-3', topic_2_3, name='topic_2_3'),
    path('topic-2-4', topic_2_4, name='topic_2_4'),
    path('topic-3-1', topic_3_1, name='topic_3_1'),
    path('topic-3-2', topic_3_2, name='topic_3_2'),
    path('topic-3-3', topic_3_3, name='topic_3_3'),
    path('topic-3-4', topic_3_4, name='topic_3_4'),
    path('topic-3-5', topic_3_5, name='topic_3_5'),
    path('topic-3-6', topic_3_6, name='topic_3_6'),
    # path('topic-3-7', topic_3_7, name='topic_3_7'),
    # path('topic-3-8', topic_3_8, name='topic_3_8'),
    path('topic-4-1', topic_4_1, name='topic_4_1'),
    path('topic-4-2', topic_4_2, name='topic_4_2'),
    path('topic-4-3', topic_4_3, name='topic_4_3'),
    path('topic-4-4', topic_4_4, name='topic_4_4'),
    path('topic-4-5', topic_4_5, name='topic_4_5'),
    path('topic-4-6', topic_4_6, name='topic_4_6'),
    path('topic-4-7', topic_4_7, name='topic_4_7'),
    path('topic-4-8', topic_4_8, name='topic_4_8'),
    path('topic-4-9', topic_4_9, name='topic_4_9'),
    path('topic-5-0', topic_5_0, name='topic_5_0'),
    path('topic-5-1', topic_5_1, name='topic_5_1'),
    path('topic-5-2', topic_5_2, name='topic_5_2'),
    path('topic-5-3', topic_5_3, name='topic_5_3'),
    path('topic-5-4', topic_5_4, name='topic_5_4'),
    path('topic-5-5', topic_5_5, name='topic_5_5'),
    path('topic-5-6', topic_5_6, name='topic_5_6'),
    path('topic-5-7', topic_5_7, name='topic_5_7'),
    path('topic-5-8', topic_5_8, name='topic_5_8'),
    path('topic-5-9', topic_5_9, name='topic_5_9'),
    path('topic-5-10', topic_5_10, name='topic_5_10'),
    path('topic-5-11', topic_5_11, name='topic_5_11'),
    path('topic-5-12', topic_5_12, name='topic_5_12'),
    path('topic-5-13', topic_5_13, name='topic_5_13'),
    path('topic-5-14', topic_5_14, name='topic_5_14'),
]
