import os
import time

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            print(f"Gap={gap}: {arr}")
        gap //= 2
    print("Shell Sort:", arr)


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Paso index={i}: {arr}")
    print("Selection Sort:", arr)


def counting_sort(arr):
    if not arr:
        print("Counting Sort:", arr)
        return
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)
    for num in arr:
        count[num - min_val] += 1
    print(f"Conteo: {count}")
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    print(f"Conteo acumulado: {count}")
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]
    print("Counting Sort:", arr)


def radix_sort(arr):
    if not arr:
        print("Radix Sort:", arr)
        return
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        print(f"Ordenando por digito (exp={exp})")
        counting_sort_radix(arr, exp)
        print(f"Después de exp={exp}: {arr}")
        exp *= 10
    print("Radix Sort:", arr)


def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in arr:
        index = (i // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in reversed(arr):
        index = (i // exp) % 10
        output[count[index] - 1] = i
        count[index] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]


def bucket_sort(arr):
    if len(arr) == 0:
        print("Bucket Sort:", arr)
        return
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val + 1
    for num in arr:
        i = (num - min_val) * (bucket_count - 1) // range_val
        buckets[i].append(num)
    print(f"Buckets: {buckets}")
    result = []
    for idx, bucket in enumerate(buckets):
        sorted_bucket = sorted(bucket)
        print(f"Bucket {idx} ordenado: {sorted_bucket}")
        result.extend(sorted_bucket)
    for i in range(len(arr)):
        arr[i] = result[i]
    print("Bucket Sort:", arr)


class PriorityQueue:
    def _init_(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2 if i > 0 else None

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, key):
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, i):
        while i > 0:
            p = self.parent(i)
            if self.heap[p] > self.heap[i]:
                self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
                i = p
            else:
                break

    def extract_min(self):
        if not self.heap:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify(0)
        return min_val

    def _heapify(self, i):
        n = len(self.heap)
        smallest = i
        l = self.left(i)
        r = self.right(i)
        if l < n and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < n and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify(smallest)


def heapsort(arr):
    pq = PriorityQueue()
    for s in arr:
        pq.insert(s)
        print(f"Insertado {s}: {pq.heap}")
    for i in range(len(arr)):
        arr[i] = pq.extract_min()
        print(f"Después de extraer min: {arr[:i+1]} + heap: {pq.heap}")
    print("Heap Sort (PriorityQueue):", arr)


def insert_young(Y, m, n, valor):
    i, j = m - 1, n - 1
    Y[i][j] = valor
    while True:
        up = Y[i - 1][j] if i > 0 else float('-inf')
        left = Y[i][j - 1] if j > 0 else float('-inf')
        best_i, best_j = i, j
        if i > 0 and Y[i][j] < up:
            best_i, best_j = i - 1, j
        if j > 0 and Y[best_i][best_j] < left:
            best_i, best_j = i, j - 1
        if (best_i, best_j) == (i, j):
            break
        Y[i][j], Y[best_i][best_j] = Y[best_i][best_j], Y[i][j]
        i, j = best_i, best_j


def extract_min_young(Y, m, n):
    val_min = Y[0][0]
    Y[0][0] = float('inf')
    restaurar_young(Y, 0, 0, m, n)
    return val_min


def restaurar_young(Y, i, j, m, n):
    min_i, min_j = i, j
    if i + 1 < m and Y[i + 1][j] < Y[min_i][min_j]:
        min_i, min_j = i + 1, j
    if j + 1 < n and Y[i][j + 1] < Y[min_i][min_j]:
        min_i, min_j = i, j + 1
    if (min_i, min_j) != (i, j):
        Y[i][j], Y[min_i][min_j] = Y[min_i][min_j], Y[i][j]
        restaurar_young(Y, min_i, min_j, m, n)


def young_sort(arr):
    n = int(len(arr) ** 0.5) + 1
    Y = [[float('inf')] * n for _ in range(n)]
    m = n
    for num in arr:
        insert_young(Y, m, n, num)
        print("Insertado:", num, "->")
        for fila in Y:
            print(fila)
    for i in range(len(arr)):
        arr[i] = extract_min_young(Y, m, n)
        print(f"Extraído mínimo {arr[i]}:")
        for fila in Y:
            print(fila)
    print("Young Tableaux Sort:", arr)


def menu():
    arr = [19, 6, 73, 27, 35, 52, 18, 42, 25]
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        #Lo agregue simplemente por limpieza y especificamente ese si se lo pedi a 
        #chatgpt por q no me acordaba bien como era (limpiar terminal)
        print("\nArreglo original:", arr)
        print("1. Shell Sort")
        print("2. Selection Sort")
        print("3. Counting Sort")
        print("4. Radix Sort")
        print("5. Bucket Sort")
        print("6. Heap Sort (PriorityQueue)")
        print("7. Young Tableaux Sort")
        print("8. Salir")
        opcion = input("\nSelecciona un algoritmo (1-8): ")

        temp_arr = arr[:]

        if opcion == '1':
            shell_sort(temp_arr)
        elif opcion == '2':
            selection_sort(temp_arr)
        elif opcion == '3':
            counting_sort(temp_arr)
        elif opcion == '4':
            radix_sort(temp_arr)
        elif opcion == '5':
            bucket_sort(temp_arr)
        elif opcion == '6':
            heapsort(temp_arr)
        elif opcion == '7':
            young_sort(temp_arr)
        elif opcion == '8':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Saliendo del menú.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

        input("\nPresiona Enter para continuar...")


if __name__ == '_main_':
    menu()