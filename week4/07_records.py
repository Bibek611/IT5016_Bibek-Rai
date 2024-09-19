def average_grade(records):
    total_grade= sum(record[2] for record in records)
    return total_grade/len(records)

students=(
    ('James', 20, 85),
    ('Bibek', 28, 90),
    ('Krishna', 19, 79),

)
def main():
    avg_grade=average_grade(students)
    print("Average grade:", avg_grade)
main()


