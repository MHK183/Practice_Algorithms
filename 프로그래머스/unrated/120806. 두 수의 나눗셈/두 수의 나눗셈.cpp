#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    float answer = static_cast<float>(num1) / num2 * 1000;
        
    return answer;
}