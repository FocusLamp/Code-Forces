#include <iostream>
#include <vector>

using namespace std;


int main() {
    int number_of_participants, minimum_score;

    cin >> number_of_participants >> minimum_score;


    vector<int> participants(number_of_participants);
    for (int i = 0; i < number_of_participants; i++) {
        cin >> participants[i];
    } 

    int score_limit_position = participants[minimum_score - 1];
    int advancers = 0;

    for (int i = 0; i < number_of_participants; i++) {
        if (participants[i] > 0 && participants[i] >= score_limit_position) {
            advancers++;
        }
    }

    cout << advancers << endl;

    return 0;

}