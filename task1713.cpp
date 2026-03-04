#include <iostream>
#include <cmath>

using namespace std;
int main() {
    int number;
    cin >> number;
    int arr[100000];
    for (int i = 0; i < number; i++) {
        int value;
        cin >> value;
        arr[i] = value;
    }

    for (int i = 0; i < number; i++) {
        int num_divisors = 0;
        double square_root = sqrt(arr[i]);
        for (int j = 1; j <= square_root; j++) {
            if (arr[i] % j == 0) {
                num_divisors += 2; // j and arr[i]/j are both divisors
            }
        }
        if (square_root == (int)square_root) {
            num_divisors--; // If perfect square, subtract one to avoid double counting the square root
        }
        cout << num_divisors << endl;
    }
    return 0;

}
