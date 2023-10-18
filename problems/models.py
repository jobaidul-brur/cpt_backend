from django.db import models


# class Tag(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name


class Problem(models.Model):
    JUDGE_CODEFORCES = "CF"
    JUDGE_CHOICES = (
        (JUDGE_CODEFORCES, "Codeforces"),
    )
    judge = models.CharField(max_length=5, choices=JUDGE_CHOICES, default=JUDGE_CODEFORCES)
    title = models.CharField(max_length=255)
    problem_statement = models.TextField(default='<div>Problem statement not available<div>')
    input_specification = models.TextField(default='<div>Input specification not available<div>')
    output_specification = models.TextField(default='<div>Output specification not available<div>')

    time_limit = models.TextField(default='1 seconds')
    memory_limit = models.TextField(default='256 megabytes')
    problem_link = models.URLField(default='-1')
    source = models.TextField(blank=True, null=True)
    contest_id = models.IntegerField(blank=True, null=True)
    index = models.CharField(max_length=5, blank=True, null=True)
    # tags = models.ManyToManyField(Tag, null=True, blank=True)


# class TestCase(models.Model):
#     problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
#     input_text = models.TextField()
#     output_text = models.TextField()
