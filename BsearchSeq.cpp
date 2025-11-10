#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>
using namespace std;

int binarySearch(const vector<int> &arr, int target)
{
    int low = 0, high = arr.size() - 1;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

int linearSearch(const vector<int> &arr, int target)
{
    for (int i = 0; i < arr.size(); ++i)
        if (arr[i] == target)
            return i;
    return -1;
}

int main()
{
    int n, target;
    bool ordered;
    cout << "Ingrese tamaño del arreglo: ";
    cin >> n;
    cout << "Buscar valor: ";
    cin >> target;
    cout << "¿Está ordenado el arreglo? (1=Sí, 0=No): ";
    cin >> ordered;

    vector<int> arr(n);
    srand(static_cast<unsigned>(time(0)));
    for (int i = 0; i < n; ++i)
        arr[i] = rand() % 100;

    if (ordered)
        sort(arr.begin(), arr.end());

    int result = ordered ? binarySearch(arr, target) : linearSearch(arr, target);
    if (result != -1)
        cout << "Elemento encontrado en índice " << result << endl;
    else
        cout << "Elemento no encontrado." << endl;

    return 0;
}
