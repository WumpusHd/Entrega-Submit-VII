#include <iostream>
#include <vector>
#include <thread>

void localMinMax(const std::vector<int>& v, int start, int end, int& localMin, int& localMax) {
    localMin = v[start];
    localMax = v[start];
    for (int i = start + 1; i < end; i++) {
        if (v[i] < localMin) localMin = v[i];
        if (v[i] > localMax) localMax = v[i];
    }
}

int main() {
    std::vector<int> v = {3, 5, 1, 7, 9, 2, 8, 4};
    int n = v.size();
    int numThreads = 4;
    int blockSize = n / numThreads;

    std::vector<int> mins(numThreads), maxs(numThreads);
    std::vector<std::thread> threads;

    for (int i = 0; i < numThreads; i++) {
        int start = i * blockSize;
        int end = (i == numThreads - 1) ? n : start + blockSize;
        threads.emplace_back(localMinMax, std::ref(v), start, end,
                             std::ref(mins[i]), std::ref(maxs[i]));
    }

    for (auto& t : threads) t.join();

    int globalMin = mins[0];
    int globalMax = maxs[0];

    for (int i = 1; i < numThreads; i++) {
        if (mins[i] < globalMin) globalMin = mins[i];
        if (maxs[i] > globalMax) globalMax = maxs[i];
    }

    std::cout << "Min: " << globalMin << "\n";
    std::cout << "Max: " << globalMax << "\n";

    return 0;
}

