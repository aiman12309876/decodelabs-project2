import java.util.Scanner;

public class StudentGradeCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("============================================");
        System.out.println("     STUDENT GRADE CALCULATOR");
        System.out.println("============================================");

        System.out.print("Enter student name: ");
        String name = scanner.nextLine();

        System.out.print("Enter number of subjects: ");
        int numSubjects = scanner.nextInt();

        double totalMarks = 0;
        double[] marks = new double[numSubjects];

        System.out.println("\nEnter marks for each subject (out of 100):");
        for (int i = 0; i < numSubjects; i++) {
            System.out.print("Subject " + (i + 1) + ": ");
            marks[i] = scanner.nextDouble();

            while (marks[i] < 0 || marks[i] > 100) {
                System.out.print("Invalid! Enter marks between 0 and 100: ");
                marks[i] = scanner.nextDouble();
            }

            totalMarks += marks[i];
        }

        double average = totalMarks / numSubjects;

        char grade;
        String status;

        if (average >= 90) {
            grade = 'A';
            status = "Excellent";
        } else if (average >= 80) {
            grade = 'B';
            status = "Very Good";
        } else if (average >= 70) {
            grade = 'C';
            status = "Good";
        } else if (average >= 60) {
            grade = 'D';
            status = "Satisfactory";
        } else if (average >= 50) {
            grade = 'E';
            status = "Pass";
        } else {
            grade = 'F';
            status = "Fail";
        }

        System.out.println("\n============================================");
        System.out.println("              RESULTS");
        System.out.println("============================================");
        System.out.println("Student Name: " + name);
        System.out.println("Total Subjects: " + numSubjects);
        System.out.println("Total Marks: " + totalMarks + " / " + (numSubjects * 100));
        System.out.printf("Average Percentage: %.2f%%\n", average);
        System.out.println("Grade: " + grade);
        System.out.println("Status: " + status);
        System.out.println("============================================");

        scanner.close();
    }
}