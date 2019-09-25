# Hello-Codes
Just another repository\
In this repository, I write codes by 4 languages, Javascript, C#, C++, Python.\
I wrote...
1. How to find GCD
2. How to make and solve Encryption (only Python...)
3. How to find sqrt
4. How to find LCM
```python: index.py
def greet(x):
    return("Hello, " + str(x) + "!")
print(greet("Python"))
```
```cs: index.cs
using System;
using System.Console;
class Greeting{
    public static string greet(string x){
        return "Hello, " + x + "!";
    }
    public static void Main(){
        WriteLine(greet("C#"));
    }
}
```
```cpp: index.cpp
#include <iostream>
#include <string>
using namespace std;
string greeting(string x){
    return "Hello, " + x + "!";
}
int main(){
    std::cout << greeting("C++") << std::endl;
}
```
```javascript: index.js
function greet(x){
    return "Hello, " + x + "!";
}
console.log(greet("Javascript"));
```
