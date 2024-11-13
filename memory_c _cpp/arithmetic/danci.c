#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char matrix[5][5] = {
        {'A', 'B', 'C', 'D', 'E'},
        {'F', 'G', 'H', 'I', 'J'},
        {'K', 'L', 'M', 'N', 'O'},
        {'P', 'Q', 'R', 'S', 'T'},
        {'U', 'V', 'W', 'X', 'Y'}
    };
    char ch[3][3] = {
        {'B', 'C', 'D'},
        {'M', 'N', 'O'},
        {'G', 'H', 'I'}
    };
    int ch_0 = 0, ch_1 = 0;
    while (ch_0 <= 2) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                char target[4] = ""; // 目标字符串
                char current[4] = ""; // 当前方向的字符串
                strncpy(target, ch[ch_0], 3);
                target[3] = '\0'; // 确保字符串以空字符结尾

                // 向右
                if (i + 2 < 5) {
                    for (int k = 0; k < 3; k++) {
                        current[k] = matrix[i + k][j];
                    }
                    current[3] = '\0';
                    if (strcmp(current, target) == 0) {
                        printf("%s found at %d,%d, direction: right\n", target, i, j);
                        ch_1++;
                        continue;
                    }
                }

                // 向下
                if (j + 2 < 5) {
                    for (int k = 0; k < 3; k++) {
                        current[k] = matrix[i][j + k];
                    }
                    current[3] = '\0';
                    if (strcmp(current, target) == 0) {
                        printf("%s found at %d,%d, direction: down\n", target, i, j);
                        ch_1++;
                        continue;
                    }
                }

                // 向右下
                if (i + 2 < 5 && j + 2 < 5) {
                    for (int k = 0; k < 3; k++) {
                        current[k] = matrix[i + k][j + k];
                    }
                    current[3] = '\0';
                    if (strcmp(current, target) == 0) {
                        printf("%s found at %d,%d, direction: down-right\n", target, i, j);
                        ch_1++;
                        continue;
                    }
                }

                // 向左
                if (i - 2 >= 0) {
                    for (int k = 0; k < 3; k++) {
                        current[k] = matrix[i - k][j];
                    }
                    current[3] = '\0';
                    if (strcmp(current, target) == 0) {
                        printf("%s found at %d,%d, direction: left\n", target, i, j);
                        ch_1++;
                        continue;
                    }
                }

                // 向上
                if (j - 2 >= 0) {
                    for (int k = 0; k < 3; k++) {
                        current[k] = matrix[i][j - k];
                    }
                    current[3] = '\0';
                    if (strcmp(current, target) == 0) {
                        printf("%s found at %d,%d, direction: up\n", target, i, j);
                        ch_1++;
                        continue;
                    }
                }

                // 向左上
                if (i - 2 >= 0 && j - 2 >= 0) {
                    for (int k = 0; k < 3; k++) {
                        current[k] = matrix[i - k][j - k];
                    }
                    current[3] = '\0';
                    if (strcmp(current, target) == 0) {
                        printf("%s found at %d,%d, direction: up-left\n", target, i, j);
                        ch_1++;
                        continue;
                    }
                }

                // 向右上
                if (i + 2 < 5 && j - 2 >= 0) {
                    for (int k = 0; k < 3; k++) {
                        current[k] = matrix[i + k][j - k];
                    }
                    current[3] = '\0';
                    if (strcmp(current, target) == 0) {
                        printf("%s found at %d,%d, direction: up-right\n", target, i, j);
                        ch_1++;
                        continue;
                    }
                }

                // 向左下
                if (i - 2 >= 0 && j + 2 < 5) {
                    for (int k = 0; k < 3; k++) {
                        current[k] = matrix[i - k][j + k];
                    }
                    current[3] = '\0';
                    if (strcmp(current, target) == 0) {
                        printf("%s found at %d,%d, direction: down-left\n", target, i, j);
                        ch_1++;
                        continue;
                    }
                }
            }
        }
        ch_0++;
    }
    system("pause");
    return 0;
}
