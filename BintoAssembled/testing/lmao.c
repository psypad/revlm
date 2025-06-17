#include <stdio.h>

// Function declarations (prototypes)
int calculateArea(int length, int width);
int calculatePerimeter(int length, int width);
void displayResults(int area, int perimeter);

int main() {
    int length = 10;
    int width = 5;

    // Function calls
    int area = calculateArea(length, width);
    int perimeter = calculatePerimeter(length, width);

    // Display the results
    displayResults(area, perimeter);

    return 0;
}

// Function definitions

// Calculates and returns the area of a rectangle
int calculateArea(int length, int width) {
    return length * width;
}

// Calculates and returns the perimeter of a rectangle
int calculatePerimeter(int length, int width) {
    return 2 * (length + width);
}

// Displays the area and perimeter
void displayResults(int area, int perimeter) {
    printf("Area: %d\n", area);
    printf("Perimeter: %d\n", perimeter);
}
