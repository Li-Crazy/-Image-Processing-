#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#define M 128
#define N 128
#define Maxgray 255

double Pi;
struct Complex
{
	double real;
	double img;
};

void  setimage(int data[M][N])
{
	srand((int)time(0));
	for(int i=0;i<M;i++)
		for(int j=0;j<N;j++)
			data[i][j]=rand()%Maxgray;
}
void fft(int data[M][N],Complex dst[M][N])
{
	clock_t start,end;
	start=clock();
	int m,n,x,y;
	double t1cos,t1sin,t2cos,t2sin;	
	double uxvy;
	for(m=0;m<M;m++)
		for(n=0;n<N;n++)
		{	t2cos=0.0;
			t2sin=0.0;
			for(x=0;x<M;x++)
			{
				for(y=0;y<N;y++)
				{	uxvy=m*x+n*y;
					uxvy=2.0*Pi*uxvy;
					t1cos=cos(uxvy/M);
					t1sin=-sin(uxvy/M);
					t2cos=t2cos+data[x][y]*t1cos;
					t2sin=t2sin+data[x][y]*t1sin;
				}
				dst[m][n].real=t2cos;
				dst[m][n].img=t2sin;
			}
		}
	end=clock();
	printf("DFT use time:%lf second\n ",double(end-start)/CLOCKS_PER_SEC);
}	
void ffttrans(Complex dst[M][N],int imagefft[M][N])
{
	for(int m=0;m<M;m++)
		for(int n=0;n<N;n++)
			imagefft[m][n]=sqrt(dst[m][n].real*dst[m][n].real+dst[m][n].img*dst[m][n].img)/M;
}

int main()
{
	struct Complex dst[M][N];
	int image[M][N];
	int imagefft[M][N];
	system("clear");
	Pi=atan(1)*4.0;
	printf("SET image......\n");
	setimage(image);
	printf("waiting for foriour tansformation......\n");
	fft(image,dst);
	ffttrans(dst,imagefft);

	
}




