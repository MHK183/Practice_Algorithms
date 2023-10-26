#include <string>
#include <vector>

using namespace std;

double solution(vector<int> numbers) {
    int arrSize = numbers.size();
    float sum = 0;
    for(int i = 0; i < arrSize; i++){
        sum += numbers[i];
    }
    return sum / arrSize;
}