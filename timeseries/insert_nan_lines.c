#include <stdio.h>
#include <time.h>

#define MAX_LINE_SIZE 1000

int main() {
	char line[MAX_LINE_SIZE];
	if (fgets(line, MAX_LINE_SIZE, stdin) == NULL) return 0; // Skip the header
	while (fgets(line, MAX_LINE_SIZE, stdin) != NULL) {
		struct tm current;
		sscanf(line, "%d-%d-%dT%d:%d ", &current.tm_year, &current.tm_mon, &current.tm_mday, &current.tm_hour, &current.tm_min);
		current.tm_mon--; // from [1,12] to [0,11]
		current.tm_sec = 0;
		
		mktime(&current);
		printf("%d\n", current.tm_year);
		printf("%s", asctime(&current));
		//printf("%s", line);
	}
}
