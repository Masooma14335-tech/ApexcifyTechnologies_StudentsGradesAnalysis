import pandas as pd

# CSV file load karein
df = pd.read_csv("Student_grades.csv.csv")

# Top 5 rows
print(df.head())

score_columns = [
    "Maths_Score", "English_Score", "Science_Score",
    "Computer_Score", "GK_Score", "Statistics_Score"
]

df["Average_Score"] = df[score_columns].mean(axis=1)

print("\n✔ Average Scores Added!\n")
print(df[["Student_ID", "Name", "Average_Score"]].head())

# ---------------------------------------------------
# 3. Find Student With the Highest Average
# ---------------------------------------------------

top_student = df.loc[df["Average_Score"].idxmax()]

print("\n🎉 STUDENT WITH HIGHEST AVERAGE 🎉")
print("-------------------------------------")
print(f"Student ID: {top_student['Student_ID']}")
print(f"Name: {top_student['Name']}")
print(f"Average Score: {top_student['Average_Score']:.2f}")
print("-------------------------------------")

# ---------------------------------------------------
# 4. Save Updated CSV (Optional)
# ---------------------------------------------------

output_path = r"C:\Users\YourFolder\students_with_average.csv"
df.to_csv(output_path, index=False)

print("\n✔ New CSV saved with averages added!")
print("File:", output_path)
