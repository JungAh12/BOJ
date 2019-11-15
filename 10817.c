#include <stdio.h>

void tmp (int x){
    
    int max2;
    max2 = x;
    printf("%d",max2);
}

int main(){
    
    int x, y, z;
    scanf("%d %d %d",&x,&y,&z);
    
    if(x>=y&&x>=z){
        if(y>=z){
            tmp(y);
        }
        else{
            tmp(z);
        }
           }
    else if(y>=x&&y>=z){
        if(x>=z){
            tmp(x);
        }
        else{
            tmp(z);
        }
    }
    
    else if(z>=x&&z>=y){
        if(x>=y){
            tmp(x);
        }
        else{
            tmp(y);
        }
    }
  
    
    return 0;
}