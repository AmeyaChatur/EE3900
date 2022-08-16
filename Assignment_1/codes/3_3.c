#include <stdlib.h>
#include <stdio.h>
#define k 20

int main(){
    double x[6]={1,2,3,4,2,1};
    double y[k]={0};
    y[0]=x[0];
    y[1]=x[1]- 0.5*y[0];
    for(int i=2;i<k;i++){
        if (i<6)
            y[i]=-0.5*y[i-1] + x[i]+x[i-2];
        else if(i<8)
            y[i]=-0.5*y[i-1] +x[i-2];
        else
            y[i]=-0.5*y[i-1];
    }
    int axes_x[sizeof(x)/sizeof(int)]={0};
    int axes_y[k]={0};

    FILE* fpy;
    fpy=fopen("3_3_data_y.dat","w");
    for(int i=0;i<k;i++){
        fprintf(fpy,"%f\n",y[i]);
    }
    fclose(fpy);
    FILE* fpx;
    fpx=fopen("3_3_data_x.dat","w");
    for(int i=0;i<6;i++){
        fprintf(fpx,"%f\n",x[i]);
    }
    fclose(fpx);
    return 0;
}