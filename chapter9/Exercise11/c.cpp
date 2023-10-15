#include <iostream>
#include <cstdio>
#include <unordered_map>
using namespace std;

int main()
{
    unordered_map<int, int> m;
    m.insert({10, 20});
    for (auto &x : m)
    {
        cout << x.first << " " << x.second << endl;
    }
    if(m.find(11)==m.end()){
        cout<<"Not found";
    }
    cout << m.at(10);
    return 0;
}

// int size,count;
//     LRUCache(int capacity) {
//         this->size=capacity;
//         this->count=0;
//     }

//     int get(int key) {
//         if(this->m.find(key)==this->m.end()){
//             return -1;
//         }
//         return this->m.at(key);
//     }

//     void put(int key, int value) {
//         this->count+=1;
//         if(this->count >= this->size) return;
//         if(this->m.find(key)!=this->m.end()){
//             this->m.erase(key);
//         }
//         else{
//             this->m.insert({key,value});
//         }

//     }
// };