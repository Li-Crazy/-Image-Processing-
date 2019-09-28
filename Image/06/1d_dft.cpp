#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#define M 256
#define Maxgray 255

double Pi;
struct Complex
{
	double real;
	double img;
};

void  setimage(int data[M])
{
	srand((int)time(0));
	for(int i=0;i<M;i++)
		data[i]=rand()%Maxgray;
	
}
void fft(int data[M],Complex dst[M],int imagefft[M])
{
	clock_t start,end;
	start=clock();
	int m,n,x,y;
	double t1cos,t1sin,t2cos,t2sin;	
	double uxvy;
	for(m=0;m<M;m++)
		{	t2cos=0.0;
			t2sin=0.0;
			for(x=0;x<M;x++)
			{	uxvy=m*x;
				uxvy=2.0*Pi*uxvy;
				t1cos=cos(uxvy/M);
				t1sin=-sin(uxvy/M);
				t2cos=t2cos+double(data[x])*t1cos;
				t2sin=t2sin+double(data[x])*t1sin;
			}			
			dst[m].real=t2cos;
			dst[m].img=t2sin;
		}
	for(int m=0;m<M;m++)
		imagefft[m]=sqrt(dst[m].real*dst[m].real+dst[m].img*dst[m].img)/sqrt(M);
	end=clock();
	printf("\nDFT use time:%lf second\n ",double(end-start)/CLOCKS_PER_SEC);
}	

int main()
{
	struct Complex dst[M];
	int image[M];
	int imagefft[M];
	system("clear");
	Pi=atan(1)*4.0;
	printf("Set line image......\n");
	setimage(image);
	for(int i=0;i<M;i++)
		if(i % int(sqrt(M))==0)
			printf("\n");
		else
			printf("%6d",image[i]);
	printf("\n");
	printf("\nWaiting for foriour tansformation......\n");
	fft(image,dst,imagefft);
	for(int i=0;i<M;i++)
		if(i % int(sqrt(M))==0)
			printf("\n");
		else
			printf("%6d",imagefft[i]);
	printf("\n");

}




