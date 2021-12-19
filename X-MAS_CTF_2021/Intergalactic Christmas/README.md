# Intergalactic Christmas 

## Description

The year is 3021, humans have finally managed to populate the entire galaxy. This is a problem for Santa Claus though. He now has to deliver gifts not only to Earth in one night but to the entire Milky Way Galaxy!!!

Because of that his elves developed an advanced neutrio-based space-sleigh. This space-sleigh uses a special type of fuel called Christmasium, a combination of two chemical elements that have been discovered in the 29-th century -- Nicenium and Naughtynium.

Theese elements have some interesting properties:

- Both elements have positive integer atomic weights that can vary vastly between isotopes
- Nicenium has an atomic weight that is always a prime number
- Naughtynium on the other hand has an atomic weight that is never a prime number

Combining one isotope of Nicenium and one of Naughtynium collapses them both in Christmasium that has an atomic weight equal to the sum of the atomic weights of the two elements.

Now, Santa still has some free time until Christmas and he has a list of N chemical elements (Nicenium or Naughtynium), and he wonders what is the K-th lightest Christmasium that he can obtain by combining any two Nicenium and Naughtynium from the list of chemical elements.

Note: for each test you will have to answer multiple questions (Q) that Santa asks you!

Restrictions and Clarifications:

- The atomic weight of any element is <= 5 * 10^6
- N <= 10^5
- Q <= 15
- 1 <= K <= the numbers of valid obtainable distinct Christmasium fuels

Example:

N = 8

Q = 3

elements = [3, 7, 2, 1, 11, 8, 10, 4]

queries = [15, 7, 11]

desired_response = [19, 11, 13]

Explanation:

- The Nicenium elements have weights: [2, 3, 7, 11]

- The Naughtynium elements have weights: [1, 4, 8, 10]

- The possible Christmasium fuels, sorted by weights have the weights: [3, 4, 6, 7, 8, 10, 11, 11, 12, 12, 13, 15, 15, 17, 19, 21]

- The 15-th Christmasium fuel has weight 19

- The 7-th Christmasium fuel has weight 11

- The 11-th Christmasium fuel has weight 13

`nc challs.xmas.htsp.ro 5006`

## Solution 

```c++
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef complex<double> cpx;

static int base = 1;
static vector<cpx> roots = {{0, 0}, {1, 0}};
static vector<int> rev = {0, 1};
static const double PI = acosl(-1.0);

void ensure_base(int nbase) {
    if (nbase <= base) {
        return;
    }
    rev.resize(1 << nbase);
    for (int i = 0; i < (1 << nbase); i++) {
        rev[i] = (rev[i >> 1] >> 1) + ((i & 1) << (nbase - 1));
    }
    roots.resize(1 << nbase);
    while (base < nbase) {
        double angle = 2 * PI / (1 << (base + 1));
        for (int i = 1 << (base - 1); i < (1 << base); i++) {
            roots[i << 1] = roots[i];
            roots[(i<<1)+1] = polar(1.0, angle*(2*i+1-(1<<base)));
        }
        base++;
    }
}

void fft(vector<cpx> &a) {
    int n = a.size();
    int zeros = __builtin_ctz(n);
    ensure_base(zeros);
    int shift = base - zeros;
    for (int i = 0; i < n; i++) {
        if (i < (rev[i] >> shift)) {
            swap(a[i], a[rev[i] >> shift]);
        }
    }
    for (int k = 1; k < n; k <<= 1) {
        for (int i = 0; i < n; i += 2 * k) {
            for (int j = 0; j < k; j++) {
                cpx z = a[i + j + k] * roots[j + k];
                a[i + j + k] = a[i + j] - z;
                a[i + j] = a[i + j] + z;
            }
        }
    }
}

static vector<cpx> fa, fb;

vector<int> multiply(vector<int> &a, vector<int> &b) {
    int need = a.size() + b.size() - 1;
    int nbase = 0;
    while ((1 << nbase) < need) nbase++;
    ensure_base(nbase);
    int sz = 1 << nbase;
    if (sz > (int) fa.size()) {
        fa.resize(sz);
    }
    for (int i = 0; i < sz; i++) {
        double x = (i < (int) a.size() ? a[i] : 0);
        double y = (i < (int) b.size() ? b[i] : 0);
        fa[i] = {x, y};
    }
    fft(fa);
    cpx r(0, -0.25 / sz);
    for (int i = 0; i <= (sz >> 1); i++) {
        int j = (sz - i) & (sz - 1);
        cpx z = (fa[j] * fa[j] - conj(fa[i] * fa[i])) * r;
        if (i != j) {
            fa[j] = (fa[i] * fa[i] - conj(fa[j] * fa[j])) * r;
        }
        fa[i] = z;
    }
    fft(fa);
    vector<int> res(need);
    for (int i = 0; i < need; i++) {
        res[i] = real(fa[i]) + 0.5;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);

    int N;
    cin >> N;

    vector<int> elements(N);
    for (int& e : elements) {
        cin >> e;
    }

    int Q;
    cin >> Q;

    vector<ll> queries(Q);
    for (ll& q : queries) {
        cin >> q;
    }

    int max_el = *max_element(elements.begin(), elements.end()) + 1;

    vector<char> is_prime(max_el, 1);
    is_prime[0] = is_prime[1] = false;

    for (int i = 2; i < max_el; i++) {
        if (!is_prime[i]) continue;
        for (int j = 2 * i; j < max_el; j += i) {
            is_prime[j] = false;
        }
    }

    vector<int> nice(max_el);
    vector<int> naughty(max_el);

    for (int e : elements) {
        if (is_prime[e]) {
            nice[e]++;
        } else {
            naughty[e]++;
        }
    }

    vector<int> xmas = multiply(nice, naughty);

    for (ll q : queries) {
        ll cnt = 0;
        for (size_t i = 0; i < xmas.size(); i++) {
            cnt += xmas[i];
            if (cnt >= q) {
                cout << i << ' ';
                break;
            }
        }
    }
    cout << endl;
        
    return 0;
}

// g++ -std=c++17 -Wall -Wextra -Wshadow -O3 -o intergalactic_christmas intergalactic_christmas.cpp
```

#### **FLAG >>** `X-MAS{Gr33dy_4nd_B1n4ry_53arch_G0_H4nd_1n_Hand_h8129fhwe}`