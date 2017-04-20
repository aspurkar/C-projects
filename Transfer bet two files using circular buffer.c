#include<stdio.h>
#include<conio.h>
int r;		//read head
int p;		//write head
char A[10];		//buffer of size 10
FILE *fp1, *fp2;
int smphr;
void P()
{
	smphr--;
}

void V()
{
	smphr++;
}

void swait()
{
}

int nextptr(int u)
	{
		u++;
		if(u==10)
			u=0;
		return u;
	}

int transfer()
{	
	while(smphr!=0)
	{
		swait();
	};
	P();
	char ch;
	fp1 = fopen("A.txt", "r");
   if (fp1 == NULL) {
      puts("cannot open this file");
	  V();
      return 9;
   }
   fp2 = fopen("B.txt", "w");
   if (fp1 == NULL) {
      puts("cannot open this file");
      V();
	  return 9;
   }
	   do
	   {
		   ch=fgetc(fp1);
		   A[r]=ch;
		   r=nextptr(r);
				

			fputc(A[p],fp2);
			p=nextptr(p);
	   }while(ch!=EOF);
   
   fclose(fp1);
   fclose(fp2);
   printf("Data has been transfered sucessfully");
   V();
   return 6;
}


int writetoA()
	{ char h[100];
	while(smphr!=0)
	{
		swait();
	};
	P();
		
	fp1 = fopen("A.txt", "a");
   if (fp1 == NULL) {
      puts("cannot open this file");
      V();
	  return 9;
   }

 printf("Enter data\n");
 scanf("%s",&h);
 if(fp1 != NULL)
	 fputs(h, fp1);
 fclose(fp1);

 printf("data has been written sucessfully ");
 V();
 return 9;
}

int readA()
{	char h;
		
	fp1 = fopen("A.txt", "r");
   if (fp1 == NULL) {
      puts("cannot open this file");
	  return 9;
   }
	do
	{
		h=fgetc(fp1);
		putchar(h);
	}while(h!=EOF);
	fclose(fp1);
	return 0;
}
int readB()
{	char h;
	fp2 = fopen("B.txt", "r");
   if (fp2 == NULL) {
      puts("cannot open this file");
      return 9;
   }
	do
	{
		h=fgetc(fp1);
		putchar(h);
	}while(h!=EOF);
	fclose(fp2);
	return 4;
}


void main()
{	smphr=0;
	r=0;
	p=0;
	int z=0;
	for(int i=0;i<10;i++)
		A[i]=0;
   do
   {
   printf("\nPlease Select one from following options\n");
   printf("1.write data in file A\n");
   printf("2.Transfer from A to B\n");
   printf("3.Print file A\n");
   printf("4.print file B\n");
   printf("5.Exit\n");
   scanf("%d",&z);

   if(z==1)
		{
			writetoA();
			goto GH;
		}
   else if(z==2)
		{
			transfer();
			goto GH;
		}
   else if(z==3)
		{
			readA();
			goto GH;
		}
   else if(z==4)
		{
			readB();
			goto GH;
		}
   else if(z==5)
		{
			break;
		}
   else 
	   {printf("Please select proper option");
   }
GH:	;
}while(z!=5);

END:	;
}