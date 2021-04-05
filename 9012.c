#include <stdio.h>
#include <string.h>
#define _CRT_SECURE_NO_WARNINGS
//헷
char stack[51]={0};
int top = -1;
int sum = 0;

void push(int data) {
  stack[++top] = data;
}

int pop() {
  return stack[top--];
}

void show() {
  if (top==-1) {
   printf("YES\n");
   top=-1;
  }
  else {
   printf("NO\n");
   top=-1;
  }
  for (int i = top; i >= 0; i--) {
    sum+=stack[i];
  }
}

int main(void) {
  int i=0, t=0, q=0, lcount=0, rcount=0;
  scanf("%d", &t);
  for (int i = 0; i < t ; i++) {
    char a[51]={0};
    lcount=0, rcount=0;
    scanf("%s", a);
    
    for (int q = 0; q<strlen(a); q++){
      if(a[q]=='('){
        push(1);
        lcount++;
      }
      else if (a[q]==')'){
        pop();
        rcount++;
      }
      if(lcount<rcount){
        break;
      }
    }
    show();
  }
  return 0;
}