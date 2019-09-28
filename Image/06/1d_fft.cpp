#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#define M 128*128 
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
int fft_map(int *image,int Msize)
{
	if (Msize==1)
		return 0;
	int *temp=(int *)malloc(sizeof(int)*Msize);
	for (int i=0;i<Msize;i++)
		if(i%2==0)
			temp[i/2]=image[i];
		else
			temp[(Msize+i)/2]=image[i];
	for (int i=0;i<Msize;i++)
		image[i]=temp[i];
	free(temp);
	fft_map(image,Msize/2);
	fft_map(image+Msize/2,Msize/2);
	return 1;
}
void Getwn(int z,int Msize,Complex *dst) 
{
	double x=2.0*Pi*z/Msize;
	dst->img=-sin(x);
	dst->real=cos(x);
}
void MultComplex(Complex *s1,Complex *s2,Complex *dst)
{
	double r1=0.0,r2=0.0;
	double i1=0.0,i2=0.0;
	r1=s1->real;
	r2=s2->real;
	i1=s1->img;
	i2=s2->img;
	dst->img=r1*i2+r2*i1;
	dst->real=r1*r2-i1*i2;
}
void AddComplex(Complex *s1,Complex *s2,Complex *dst)
{
	dst->img=s1->img+s2->img;
	dst->real=s1->real+s2->real;
	
}
void SubComplex(Complex *s1,Complex *s2,Complex *dst)
{
	dst->real=s1->real-s2->real;
	dst->img=s1->img-s2->img;

}
void fft(int src[M],Complex dst[M],int Msize)
{
	clock_t start,end;
	start=clock();
	/*fft_map(data,M);*/
	int k=Msize;
	int z=0;
	while(k/=2)
	{
		z++;
	}
	k=z;
	if (Msize!=(1<<k))
		exit(0);
	Complex *srcom=(Complex *)malloc(sizeof(Complex)*Msize);
	if (srcom==NULL)
		exit(0);
	for(int i=0;i<Msize;i++)  //initial 
	{
		srcom[i].real=src[i];
		srcom[i].img=0;
	}
	for(int i=0;i<k;i++)
	{
		z=0;
		for(int j=0;j<Msize;j++)
		{
			if(j/(1<<i)%2==1)
			{
				Complex wn;
				Getwn(z,Msize,&wn);
				MultComplex(&srcom[j],&wn,&srcom[j]);
				z+=1<<(k-i-1);	
				Complex temp;
				int neighbour=j-(1<<(i));
				temp.real=srcom[neighbour].real;
				temp.img=srcom[neighbour].img;
				AddComplex(&temp,&srcom[j],&srcom[neighbour]);
				SubComplex(&temp,&srcom[j],&srcom[j]);
			}
			else
				z=0;
				
		}
				
	}
	for(int i=0;i<k;i++)
	{
		dst[i].img=srcom[i].img;
		dst[i].real=srcom[i].real;	
	}
	end=clock();
	printf("DFT use time:%lf second\n ",double(end-start)/CLOCKS_PER_SEC);
}	


int main()
{
	struct Complex dst[M];
	int image[M];
	int imagefft[M];
	system("clear");
	Pi=atan(1)*4.0;
	printf("SET image......\n");
	setimage(image);
	printf("\nwaiting for foriour tansformation......\n");
	fft(image,dst,M);
	/*for (int i =0;i<M;i++)
		printf("%lf,%lf\n",dst[i].real,dst[i].img);
	*/
}




