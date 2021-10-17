# THE PUZZLE

## Description

Thanks to the ex-con, R-boy and IronCode discover that Zer0 has hidden an encrypted file in the Forbidden Forest, which contains the coordinates of his secret lair. The file is protected by a giant dragon. Help R-Boy and IronCode defeat the dragon and take the file.

[coding200](coding200.zip)

## Solution

```c++
#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>
#include <cassert>
#include <set>
#include <map>

using namespace std;

constexpr int H = 200;
constexpr int W = 200;
constexpr int L = H * W;

int grid[H][W];
char val[L];
int neighbor_down[L];
int neighbor_right[L];
bool not_corner[L];

map<int, int> up_val;
map<int, int> left_val;
int val_down[L];
int val_right[L];

int main() {
    memset(val, ' ', sizeof val);
    memset(neighbor_down, -1, sizeof neighbor_down);
    memset(neighbor_right, -1, sizeof neighbor_right);

    ifstream fin("puzzle.txt");
    ofstream fout("grid.txt");

    string line;
    for (int i = 0; getline(fin, line); i++) {
        istringstream iss(line);
        int u, d, l, r;
        char c;
        if (iss >> u >> d >> l >> r >> c) {
            val[i] = c;
        }
        up_val[u] = i;
        left_val[l] = i;

        val_down[i] = d;
        val_right[i] = r;
    }

    for (int i = 0; i < L; i++) {
        neighbor_down[i] = up_val[val_down[i]];
        neighbor_right[i] = left_val[val_right[i]];
        not_corner[neighbor_down[i]] = true;
        not_corner[neighbor_right[i]] = true;
    }

    for (int i = 0; i < L; i++) {
        if (!not_corner[i]) {
            grid[0][0] = i;
            break;
        }
    }

    for (int i = 0; i < H - 1; i++) {
        for (int j = 0; j < W - 1; j++) {
            grid[i + 1][j] = neighbor_right[grid[i][j]];
            grid[i][j + 1] = neighbor_down[grid[i][j]];
        }
    }

    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (val[grid[j][i]] != ' ') cout << val[grid[j][i]];
        }
    }

    return 0;
}
```

```console
$ ./a.out 
RPZwJYegNTPHjNQEALlFigcYxqhDBWVP
```

Now we can use this string as password for the `secret_room.zip`

#### **FLAG >>** `{FLG:++---N0t_4_H4mM3r---||}`