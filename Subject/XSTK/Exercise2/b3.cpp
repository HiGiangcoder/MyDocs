#include<bits/stdc++.h>
using namespace std;
using ll = long long;

mt19937_64 rngll(chrono :: steady_clock :: now().time_since_epoch().count());
ll random(ll l, ll r) {
    return uniform_int_distribution<ll>(l, r)(rngll);
}

double Randfloat() {
    double num = random(-1e18, 1e18);
    num /= 1e18;
    return num;
}

int main() {
    int cntin(0), cntall(0);

    for (int i = 1; i <= 1e9; i ++) {
        double u = Randfloat();
        double v = Randfloat();

        double d = sqrt(abs(u * u) + abs(v * v));

        cntall ++;
        if (d <= 1.0) cntin ++;
    }
    cout << setprecision(10) << fixed << double(cntin) / double(cntall) * 4.0 << '\n';
}