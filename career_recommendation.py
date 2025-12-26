def recommend_career(gpa, grades):
    total_score = 0

    # LOOP: calculate total score based on grades
    for grade in grades:
        if grade >= 80:
            total_score += 3
        elif grade >= 60:
            total_score += 2
        else:
            total_score += 1

    average_score = total_score / len(grades)

    # IF-ELSE: final recommendation decision
    if gpa >= 3.5 and average_score >= 2.5:
        return ["AI Engineer", "Data Scientist", "ML Engineer"]
    else:
        return ["IT Support", "QA Tester", "Business Analyst"]


# Example test run (optional)
if __name__ == "__main__":
    print(recommend_career(3.8, [85, 90, 80]))
