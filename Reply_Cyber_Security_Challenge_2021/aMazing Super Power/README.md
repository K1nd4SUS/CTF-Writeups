# aMazing Super Power

## Description

After an open battle, and thanks to the super strength of IronCode, R-Boy manages to get hold of the file. But it’s a trap. IronCode and R-boy are stuck into the file and the only way to get out is through a labyrinth of codes! Solve the problems in the maze and help the two heroes escape!

[coding300](coding300.zip)

## Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

pair<int, int> operator+(const pair<int, int>& a, const pair<int, int>& b) {
    return make_pair(a.first + b.first, a.second + b.second);
}

pair<int, int> operator-(const pair<int, int>& a, const pair<int, int>& b) {
    return make_pair(a.first - b.first, a.second - b.second);
}

constexpr int N = 14;
constexpr int L = 1 << N;

pair<int, int> graph[N][N];
pair<int, int> dp[N][L];
int pv[N][L];

int main() {
    ifstream fin("file_pretty.txt");

    vector<string> cities(N);
    for (auto& c : cities) {
        fin >> c;
    }

    memset(graph, 0x3f, sizeof(graph));
    for (auto& l : graph) {
        for (auto& e : l) {
            fin >> e.first >> e.second;
        }
    }

    for (int s = 0; s < N - 1; s++) {
        memset(dp, 0x3f, sizeof(dp));
        dp[s][0] = make_pair(0, 0);
        for (int m = 0; m < L; m++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (m & (1 << j)) continue;
                    auto p = dp[i][m] + graph[i][j];
                    if (!(135 <= p.first && p.first <= 135 + 515) && j == 13) continue;
                    if (p.second > 58000) continue;
                    if (p < dp[j][m | 1 << j]) {
                        dp[j][m | 1 << j] = p;
                        pv[j][m | 1 << j] = i;
                    }
                }
            }
        }
        cout << setw(12) << left << cities[s] << ' ' << dp[s][L - 1].first << ' ' << dp[s][L - 1].second << endl;

        string cat = cities[s].substr(0, 2);
        int c = s, m = L - 1;
        for (int i = 0; i < N; i++) {
            int c1 = pv[c][m];
            m ^= 1 << c;
            c = c1;
            cat = cities[c].substr(0, 2) + cat;
        }

        cout << dp[s][L - 1].first << '-' << cat << '-' << dp[s][L - 1].second << endl;
    }
    

    return 0;
}
```

```console

```

Now we can use this string as password for the `power.zip`

#### **FLAG >>** ``