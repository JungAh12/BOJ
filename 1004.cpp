#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

class pos {
public: 
	int x, y;
};
class circle {
public: 
	int cx, cy, r;
};

bool checkpoint(pos s, pos e, circle p) {
	bool check = false;
	int cnt = 0;
	if (pow((s.x - p.cx), 2) + pow((s.y - p.cy), 2) < pow(p.r, 2)) {
		cnt++;
	}
	if (pow((e.x - p.cx), 2) + pow((e.y - p.cy), 2) < pow(p.r, 2)) {
		cnt++;
	}
	if (cnt == 1) {
		check = true;
	}
	return check;
}
int main() {
	
	pos start = pos();
	pos end = pos();
	vector<int> cnt;
	int T, n;
	
	cin >> T;

	for (int i = 0; i < T; ++i) {
		cin >> start.x >> start.y >> end.x >> end.y;
		cin >> n;
		cnt.push_back(0);
		circle planet = circle();
		for (int j = 0; j < n; ++j) {
			cin >> planet.cx >> planet.cy >> planet.r;
			if (checkpoint(start, end, planet) == true) {
				++cnt[i];
			}
		}
	}

	for (int i = 0; i < T; ++i) {
		cout << cnt[i] << endl;
	}

	return 0;
}