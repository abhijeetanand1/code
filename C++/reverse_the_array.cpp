#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;

int main()
{
    char arr[30];
    char str[20];
    int n;
    cout<<"Enter the size of array:";
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    for(int i=n;i<=0;i--)
    {
        cout<<arr[i];
    }
    return 0;
}