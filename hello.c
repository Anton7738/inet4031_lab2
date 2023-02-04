#include <stdio.h>

int main() {

	int a = 2;
	int b = 2;
	int c = a + b;

	printf("C says: Hello, World!\n");
	printf("%d + %d = %d\n", a, b, c);
	printf("\n");
	char * userArray[] = {"User1", "User2", "User3"};

	printf("Part 2 Starts:\n");
	for (int i = 0; i <= 2; i++) {
		printf("%s\n", userArray[i]);
	}

	return 0;

}
