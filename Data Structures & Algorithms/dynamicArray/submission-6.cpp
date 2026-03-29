class DynamicArray {
private:
    int* arr;
    int* arr2;
    int cap;
    int size;
public:

    DynamicArray(int capacity) {
        arr = new int[capacity];
        cap = capacity;
        size = 0;
    }

    int get(int i) {
        return arr[i-1];
    }

    void set(int i, int n) {
        arr[i-1] = n;
    }

    void pushback(int n) {
        if (size == cap){
            resize();
        }
        arr[size-1] = n;
        size++;
    }

    int popback() {
        if (size>0){
            size-=1;
        }
        
        return arr[size-1];

    }

    void resize() {
        cap*=2;
        arr2 = new int[cap];
        for (int i = 0; i<size;i++){
            arr2[i-1] = arr[i-1];
        }
        arr = arr2;
    }

    int getSize() {
        return size;

    }

    int getCapacity() {
        return cap;

    }
};
