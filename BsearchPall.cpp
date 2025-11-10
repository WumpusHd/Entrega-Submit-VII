#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <omp.h>
using namespace std;

int parallelBinarySearch(vector<int> &arr, int target, int threads)
{
    int n = arr.size();
    int low = 0, high = n - 1;
    int found = -1;

    omp_set_num_threads(threads);
    while (low <= high && found == -1)
    {
        int len = high - low + 1;
        int step = len / threads;
        if (step < 1)
            step = 1;

#pragma omp parallel for shared(found)
        for (int i = 0; i < threads; ++i)
        {
            int start = low + i * step;
            int end = (i == threads - 1) ? high : (start + step - 1);
            if (start > high || found != -1)
                continue;
            if (arr[start] == target)
                found = start;
            else if (arr[end] == target)
                found = end;
            else if (arr[start] < target && target < arr[end])
            {
#pragma omp critical
                {
                    low = start;
                    high = end;
                }
            }
        }
        if (step == 1)
            break;
    }
    return found;
}

// Búsqueda lineal paralela
int parallelLinearSearch(vector<int> &arr, int target, int threads)
{
    int found = -1;
    omp_set_num_threads(threads);
#pragma omp parallel for shared(found)
    for (int i = 0; i < arr.size(); ++i)
    {
        if (arr[i] == target)
        {
#pragma omp critical
            {
                if (found == -1)
                    found = i;
            }
        }
    }
    return found;
}

int main()
{
    int n, target, threads;
    bool ordered;
    cout << "Tamaño del arreglo: ";
    cin >> n;
    cout << "Valor a buscar: ";
    cin >> target;
    cout << "Número de hilos: ";
    cin >> threads;
    cout << "¿Arreglo ordenado? (1=Sí, 0=No): ";
    cin >> ordered;

    vector<int> arr(n);
    srand(static_cast<unsigned>(time(0)));
    for (int i = 0; i < n; ++i)
        arr[i] = rand() % 1000;

    if (ordered)
        sort(arr.begin(), arr.end());

    int pos = ordered ? parallelBinarySearch(arr, target, threads) : parallelLinearSearch(arr, target, threads);

    if (pos != -1)
        cout << "Elemento encontrado en índice " << pos << endl;
    else
        cout << "Elemento no encontrado." << endl;

    return 0;
}
