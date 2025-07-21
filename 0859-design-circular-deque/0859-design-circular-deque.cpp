class MyCircularDeque {
private:
    vector<int> deq;
    int front, rear, count, capacity;
public:
    MyCircularDeque(int k) : deq(k), front(0), rear(k - 1), count(0), capacity(k) { }

     bool insertFront(int value) {
        if(isFull()) {
            return false;
        }

        front = (front - 1 + capacity) % capacity;
        deq[front] = value;
        count++;
        return true;
    }
    
    bool insertLast(int value) {
        if(isFull()) {
            return false;
        }

        rear = (rear + 1) % capacity;
        deq[rear] = value;
        count++;
        return true;
    }
    
    bool deleteFront() {
        if(isEmpty()) {
            return false;
        }
        front = (front + 1) % capacity;
        count--;
        return true;
    }
    
    bool deleteLast() {
        if(isEmpty()) {
            return false;
        }

        rear = (rear - 1 + capacity) % capacity;
        count--;
        return true;
    }
    
    int getFront() {
        if(isEmpty()) {
            return -1;
        }        

        return deq[front];
    }
    
    int getRear() {
        if(isEmpty()) {
            return -1;
        }
        return deq[rear];
    }
    
    bool isEmpty() {
        return count == 0;
    }
    
    bool isFull() {
        return count == capacity;
    }
};

