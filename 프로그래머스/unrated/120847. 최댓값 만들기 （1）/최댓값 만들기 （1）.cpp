#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers) {
    int largest = 0;
    int secondLargest = 0;
    
    for(int num : numbers) {
        if (num >=largest) {
            secondLargest = largest;
            largest = num;
        } else if (num > secondLargest) {
            secondLargest = num;
        }
    }
    return largest * secondLargest;
}