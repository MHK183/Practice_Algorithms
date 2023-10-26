#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int pizza = n / 7;
    if (n % 7 == 0) {
        return pizza;
    } else {
        return pizza + 1;
    }
}