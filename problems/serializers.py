from rest_framework import serializers

from .models import Problem


# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = '__all__'


# class TestCaseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TestCase
#         fields = '__all__'


class ProblemSerializer(serializers.ModelSerializer):
    # tags = TagSerializer(many=True)
    # test_cases = serializers.SerializerMethodField()

    class Meta:
        model = Problem
        # fields = ('id', 'judge', 'title', 'statement', 'input_constraints', 'output_constraints', 'time_limit',
        #           'memory_limit', 'problem_link', 'source') #, 'tags', 'test_cases')
        fields = '__all__'

    # def get_test_cases(self, obj: Problem):
    #     return TestCaseSerializer(TestCase.objects.filter(problem=obj), many=True).data
