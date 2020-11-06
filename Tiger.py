from collections import defaultdict
# from mailcap import show
#
# salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
#                         (48000, 0.7), (76000, 6),
#                         (69000, 6.5), (76000, 7.5),
#                         (60000, 2.5), (83000, 10),
#                         (48000, 1.9), (63000, 4.2)]
#
# # def make_chart_salaries_by_tenure():
# #     tenures = [tenure for salary, tenure in salaries_and_tenures]
# #     salaries = [salary for salary, tenure in salaries_and_tenures]
# #     scatter(tenures, salaries)
# #     xlabel("Years Experience")
# #     ylabel("Salary")
# #     show()
#
# salary_by_tenure = defaultdict(list)
# for salary, tenure in salaries_and_tenures:
#     salary_by_tenure[tenure].append(salary)
#
# print(salary_by_tenure)
#
# average_salary_by_tenure = {
#     tenure : sum(salaries) / len(salaries)
#     for tenure, salaries in salary_by_tenure.items()
# }
# print(average_salary_by_tenure)
#
# def tenure_bucket(tenure):
#     if tenure < 2: return "less than two"
#     elif tenure < 5: return "between two and five"
#     else: return "more than five"
#
# salary_by_tenure_bucket = defaultdict(list)
#
# for salary, tenure in salaries_and_tenures:
#     bucket = tenure_bucket(tenure)
#     salary_by_tenure_bucket[bucket].append(salary)
#
# print(salary_by_tenure_bucket)
#
# average_salary_by_bucket = {
#   tenure_bucket : sum(salaries) / len(salaries)
#   for tenure_bucket, salaries in salary_by_tenure_bucket.iteritems()
# }
# print(average_salary_by_bucket)

# a = defaultdict(list)

# a[1].append(10)
# a[2].append(20)
# a[3].append(30)
# print(a)
#
# b = {
#     i: sum(j) / len(j)
#     for i, j in a.items()
# }
# print(b)

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]
from collections import Counter
words_and_counts = Counter(
    word
    for user, interest in interests
    for word in interest.lower().split()
)

print(words_and_counts)
for word, count in words_and_counts.items():
    if count > 2:
        print(word, count)

a = "무궁화 꽃"
b = "무궁화\t꽃"
print(a, b)

x, y = 1, 2
_, y = [3, 2]
print(x, y)
a = [3 for _ in range(5)]
print(3)


def f():
    return 1 + 2, 1 - 2, 1 * 2

print(f())

a = {10, 20, 30}
a.add(40)
print("len = ", len(a))
print(a)
a.add(30)
print("len = ", len(a))
print(a)
print(type(a))

assert 1 + 1 == 2
# assert 1 + 2 == 2


def f(a):
    return min(a)


b = f([1, 2, 3, 4])
print(b == 5)
assert b == 5

print(b)

