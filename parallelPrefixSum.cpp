#include <iostream>
#include <vector>
#include <thread>

void upsweep(std::vector<int>& v, int step, int offset) {
    int n = v.size();
    for (int i = offset - 1; i < n; i += step) {
        v[i] += v[i - offset / 2];
    }
}

void downsweep(std::vector<int>& v, int step, int offset) {
    int n = v.size();
    for (int i = offset - 1; i < n; i += step) {
        int temp = v[i - offset / 2];
        v[i - offset / 2] = v[i];
        v[i] += temp;
    }
}

int main() {
    std::vector<int> v = {1, 2, 1, 7, 3, 0, 4, 3}; 
    int n = v.size();

    // ------------------------------
    // Upsweep
    // ------------------------------
    for (int d = 1; d < n; d *= 2) {
        int step = d * 2;
        std::thread t(upsweep, std::ref(v), step, d);
        t.join();
    }

    v[n - 1] = 0; // root a cero

    // ------------------------------
    // Downsweep
    // ------------------------------
    for (int d = n / 2; d >= 1; d /= 2) {
        int step = d * 2;
        std::thread t(downsweep, std::ref(v), step, d);
        t.join();
    }

    for (int x : v) std::cout << x << " ";
    std::cout << "\n";

    return 0;
}